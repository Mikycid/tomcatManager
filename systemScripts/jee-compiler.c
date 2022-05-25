#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>


char *cSystem(char *cmd, size_t size){
    char finalCmd[size + sizeof(" 2>&1 >/dev/null")];
    memset(finalCmd, 0, sizeof(finalCmd));
    strcat(finalCmd, cmd);
    strcat(finalCmd, " 2>&1 >/dev/null");

    FILE *fp;
    fp = popen(finalCmd, "r");
    char *output = (char*) calloc(500, sizeof(char));
    fgets(output, 500, fp);
    pclose(fp);
    return output;
}

void replaceAll(char *str, char *oldChar, char *newChar)
{
    int i = 0;

    /* Run till end of string */
    while(str[i] != '\0')
    {
        /* If occurrence of character is found */
        if(str[i] == oldChar[0])
        {
            str[i] = newChar[0];
        }

        i++;
    }
}

char *getEndPath(char *dir, char *file){
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    char file_path[200];
    sprintf(file_path, "%s/src/%s", dir, file);

    fp = fopen(file_path, "r");
    read = getline(&line, &len, fp);
    fclose(fp);
    replaceAll(line, ".", "/");

    char *ret = strstr(line, (char*)("package"));

    if(ret){
        line[strcspn(line, "\n")] = 0;
        line[strcspn(line, ";")] = 0;
        memmove(line, line+8, strlen(line));
        strcat(line, (char*)("/"));

        return line;
    } else {
        return "";
    }
}

void createSubdirectories(char *basePath, char *path){
    
    char path_copy[200];
    strcpy(path_copy, path);
    char *token = strtok(path_copy, "/");


    while(token != NULL){
        strcat(basePath, (char *)("/"));
        strcat(basePath, token);
        mkdir(basePath, 0777);
        token = strtok(NULL, "/");
    }
}

char *compile(char* dir, char* file, char* api)
{
    printf("Compiling file %s...\n", file);

    char *endPath = getEndPath(dir, file);

    if(endPath[0] == '\0'){
        printf("Failed to compile file %s. To make it work, the first line of your java code must be the package declaration.\n", file);
        return file;
    }

    char cmd[500];

    sprintf(cmd, "javac -cp %s %s/src/%s", api, dir, file);
    
    char *error = cSystem(cmd, sizeof(cmd));

    char cmdMove[800];
    char compiledFile[200];
    

    char baseDir[200];

    strcpy(baseDir, dir);
    strcat(baseDir, (char *)("/WEB-INF/classes"));


    createSubdirectories(baseDir, endPath);

    memset(compiledFile, 0, sizeof(compiledFile));
    strncpy(compiledFile, file, strlen(file) - 4);
    strcat(compiledFile, (char *)("class"));

    sprintf(cmdMove, "mv -f %s/src/%s %s/WEB-INF/classes/%s%s", dir, compiledFile, dir, endPath, compiledFile);

    strcat(error, cSystem(cmdMove, sizeof(cmdMove)));

    return error;
}

char *createWarFile(char *dir, size_t size)
{
    printf("Generating a war file...\n");

    char cmdWarFile[size+sizeof("cd ; jar -cvf project.war * 2>&1 >/dev/null;mv project.war ../tmp")];

    sprintf(cmdWarFile, "cd %s; jar -cvf project.war * 2>&1 >/dev/null;mv -f project.war ../tmp", dir);
    char *error = cSystem(cmdWarFile, sizeof(cmdWarFile));

    return error;
}

int endsWith(const char *str, const char *suffix)
{
    if (!str || !suffix)
        return 0;
    size_t lenstr = strlen(str);
    size_t lensuffix = strlen(suffix);
    if (lensuffix >  lenstr)
        return 0;
    return strncmp(str + lenstr - lensuffix, suffix, lensuffix) == 0;
}

void help(){
    printf("This tool is used to compile a java project ready for deployment on a tomcat server.\n");
    printf("Use it as so : jee-compiler dir_path tomcat_api_path [(file1, file2, file3,...) || all]\n");
    printf("Use all instead of files to compile to compile every file in the src subdirectory.\n");
}

int main(int argc, char* argv[])
{
    
    char errors[1000];
    memset(errors, 0, 1000);

    if(argc > 3){
        char *dir = argv[1];
        char *api = argv[2];

        if(strcmp(argv[3], (char*)("all")) == 0){
            char *srcdir = (char *) calloc(sizeof(argv[1]) + sizeof("/src"), sizeof(char));
            strcpy(srcdir, dir);
            strcat(srcdir, (char *)("/src"));

            DIR *d;
            struct dirent *directory;
            d = opendir(srcdir);
            free(srcdir);

            if (d){
                while((directory = readdir(d)) != NULL){
                    char *file = directory->d_name;
                    if(endsWith(file, (char*)(".java"))){
                        strcat(errors, compile(dir, file, api));
                    }
                    
                }
                closedir(d);
            }
            if(errors[0] == '\0'){
                strcat(errors, createWarFile(dir, sizeof(argv[1])));
                printf("The compilation went successful.");
            }
            
        } else {
            
            for(int i=3;i<argc;i++){
                if(endsWith(argv[i], (char*)(".java"))){
                    strcat(errors, compile(dir, argv[i], api));
                } else {
                    printf("The file %s is not a java file.\n", argv[i]);
                    strcat(errors, argv[i]);
                    strcat(errors, (char *)(","));
                }

            }
            if(errors[0] == '\0'){
                strcat(errors, createWarFile(dir, sizeof(argv[1])));
                printf("The compilation went successful.");
            }
        }
    } else {
        help();
    } 

    printf("%s", errors);
    return 0;
}