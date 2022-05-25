#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    if(argc >= 2){
        char *dir = argv[1];
        printf("Generating a war file...\n");

        char cmdWarFile[300];

        sprintf(cmdWarFile, "cd %s; jar -cvf project.war * 2>&1 >/dev/null;mv project.war ../tmp", dir);
        system(cmdWarFile);
    } else {
        printf("No directory specified");
    }
    return 0;
}