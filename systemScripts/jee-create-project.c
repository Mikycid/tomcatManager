#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

int main(int argc, char* argv[]){
    if(argc == 2){
        char *cmd = argv[1];
        struct stat st;

        if(stat(cmd, &st) == 0){
            printf("Directory %s already exists.\n", cmd);
            return 0;
        }


        char exe_path[200];
        memset(exe_path, 0, sizeof(exe_path));

        strncpy(exe_path, argv[0], strlen(argv[0]) - 18);


        char webXmlPath[200];
        char testClassPath[200];
        char indexHtmlPath[200];
        char path[50];

        strcpy(webXmlPath, exe_path);
        strcat(webXmlPath, (char *)("web.xml"));

        strcpy(testClassPath, exe_path);
        strcat(testClassPath, (char *)("Test.java"));

        strcpy(indexHtmlPath, exe_path);
        strcat(indexHtmlPath, (char *)("index.html"));
        
        strcpy(path, cmd);
        
        mkdir(cmd, 0777);

        mkdir(strcat(cmd, (char *)("/src")), 0777);

        strcpy(cmd, path);
        mkdir(strcat(cmd, (char *)("/WEB-INF")), 0777);

        strcpy(cmd, path);
        mkdir(strcat(cmd, (char *)("/WEB-INF/lib")), 0777);

        strcpy(cmd, path);
        mkdir(strcat(cmd, (char *)("/WEB-INF/classes")), 0777);

        strcpy(cmd, path);
        
        char destXmlPath[400];
        sprintf(destXmlPath, "cp %s %s/WEB-INF/web.xml", webXmlPath, cmd);
        system(destXmlPath);

        char destClassPath[400];
        sprintf(destClassPath, "cp %s %s/src/Test.java", testClassPath, cmd);
        system(destClassPath);

        char destIndexPath[400];
        sprintf(destIndexPath, "cp %s %s/index.jsp", indexHtmlPath, cmd);
        system(destIndexPath);

        printf("Project %s has been created !\n", argv[1]);

    } else {
        printf("Missing argument : directory\n");
    }
    
    return 0;

}