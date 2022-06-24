#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <errno.h>
#include <signal.h>

bool primecheck(int input){

	if(input == 2 || input == 3 || input == 5){
		return 1;
	}
	else if((input % 2) == 0 || (input % 3) == 0 || (input % 5) == 0){
		return 0;
	}

	return 1;
}

int main(){
	int fd[2];
	pipe(fd);
	printf("\n");
	pid_t pid = fork();
	void sigint_handler(int sig);
	void sigtstp_handler(int sig);
	void sigquit_handler(int sig);

	if(pid == 0){
		close(fd[0]);
		int num;

		if(signal(SIGINT, sigint_handler) == SIG_ERR){
               		perror("signal");
               		exit(1);
       		}

		printf("Enter a number: ");
		scanf("%d", &num);
		write(fd[1], &num, sizeof(num));

		exit(EXIT_SUCCESS);
	}
	if(pid > 0){
		wait(NULL);
		close(fd[1]);

		int input;
		bool prime;
		read(fd[0], &input, sizeof(input));
		prime = primecheck(input);

		if(signal(SIGINT, sigint_handler) == SIG_ERR){
                        perror("signal");
                        exit(1);
                }

		printf("Reading from pipe...\n");
		sleep(5);
		printf("The number is: %d\n", input);
		prime ? printf("It is a prime number.\n\n") : printf("It is not a prime number.\n\n");
	}
	return EXIT_SUCCESS;
}

void sigint_handler(int sig){
	printf("Process terminated.\n");
}
