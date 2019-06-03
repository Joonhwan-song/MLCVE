//CWE-77:Improper Neutralization of Special Elements used in a Command ('Command Injection') 
//gcc -o ./CB ./CWE_77_c.c -m32
#include <stdio.h>
#include <string.h>

char cmd[20]={0,};

void menu(){
	printf("1. 'ls'\n");
	printf("2. 'pwd'\n");
	printf("3. 'id'\n");
	printf("4. 'time'\n");
	printf("> ");
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
	read(0,cmd,20);
    }
 
    system(cmd);
    return 0;
}
