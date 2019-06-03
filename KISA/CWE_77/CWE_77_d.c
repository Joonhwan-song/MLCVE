//CWE-77:Improper Neutralization of Special Elements used in a Command ('Command Injection') 
//gcc -o ./CB ./CWE_77_d.c -m32
#include <stdio.h>
#include <string.h>

char cmd[20]="cat ";

void menu(){
	printf("1. 'ls'\n");
	printf("2. 'pwd'\n");
	printf("3. 'id'\n");
	printf("4. 'time'\n");
	printf("> ");
} 

void hidden(){
	char buf[10]={0,};

	read(0, buf, 10);

	strcat(cmd,buf);
	
	system(cmd);
}	
int main(int argc, char* argv[], char** envp){
 
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);

    int choice=0; 

    menu();
    scanf("%d",&choice);

    if(choice == 1){
	strcpy(cmd,"ls");
    }
    else if (choice ==2){
	strcpy(cmd,"pwd");
    }
    else if(choice ==3){
	strcpy(cmd,"id");
    }
    else if(choice ==4){
 	strcpy(cmd,"time");
    }
    else{
	hidden();
    }
 
    system(cmd);
    return 0;
}
