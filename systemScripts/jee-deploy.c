#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
    if(argc > 2){
        char *deployPath = argv[1];
        char *title = argv[2];

        char cmd[200];
        sprintf(cmd, "mv tmp/project.war %s/%s.war", deployPath, title);
        
        system(cmd);

        printf("The project %s has been deployed ! Go to http://localhost:8080/%s to see it.\n", title, title);
    } else {
        printf("Missing argument : directory or path.\n");
        printf("This tool is used as so : \n");
        printf("jee-deploy deploy_path project_title");
    }
    

    return 0;
}