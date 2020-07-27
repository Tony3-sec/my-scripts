#include <stdio.h>
#include <string.h>

int passwdCheck(void)
{
	char secret[15];
	FILE *fp;
	fp = fopen("secret.txt", "r"); //secretpassword
	fgets(secret, 15, fp);

	char passwd[15];
	gets(passwd);

	if(strcmp(passwd, secret) == 0) {
		return 1;
	}
	else {
		return 0;
	}
	fclose(fp);
}

int main(void)
{
	//int passwdCheck = passwdCheck();

	if (passwdCheck() != 1) {
		puts("Incorrect password");
	}
	else {
		puts("Authorized!");
		char secret[15];
		FILE *fp;
		fp = fopen("secret.txt", "r");
		fgets(secret, 15, fp);
		printf("Password is %s\n", secret);
		
		fclose(fp);
	}

	return 0;
}
