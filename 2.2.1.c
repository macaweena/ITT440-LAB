
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char**argv){
int pid;
switch (pid = fork()){
case 0:
printf("I am the child process: pid=%d\n", getpid());
break;
default:
printf("i am the parent process: pid=%d, child pid=%\n", getpid() pid);
break;
case -1:
perror("fork");
exit(1);
}
exit(0);
}

