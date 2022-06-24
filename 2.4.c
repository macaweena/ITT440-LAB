#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){
  pid_t wpid;
  int status = 0;

  for(int i = 0; i < 4; i++){
    pid_t pid = fork();

    if(pid == 0){
      char name[30];

      printf("What is your name? > ");
      scanf("%s", name);
      printf("Your name is %s\n", name);
      exit(0);
    }

    else if(pid == -1){
      perror("fork");
      exit(1);
    }

    else{
      wait(NULL);
      printf("Job is done\n\n");
    }
  }
  return EXIT_SUCCESS;
}
