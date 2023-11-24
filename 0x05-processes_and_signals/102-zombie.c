#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - function
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			printf("Zombie process created, PID: %u\n", getpid());
	}
	infinite_while();
	return (0);
}
