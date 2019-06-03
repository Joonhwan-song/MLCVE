//CWE-77:Improper Neutralization of Special Elements used in a Command ('Command Injection') 
//gcc -o ./CB ./CWE_77_e.c -m32
#include <stdio.h>
#include <string.h>
#include <dirent.h>


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
	DIR *dir_info;
	struct dirent *dir_entry;
	int exist_bit=0;

	dir_info = opendir( ".");
	read(0, buf, 10);

        if ( NULL != dir_info)
        {
        	while( dir_entry   = readdir( dir_info))
                {
                	if(!strcmp(dir_entry->d_name,buf)){
                        	exist_bit=1;
				break;
                        }
                }
                closedir( dir_info);
        }
	if(exist_bit==1){
		strcat(cmd,buf);
	
		system(cmd);
	}
	else{
		puts("attack fail");
	}
	
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
    else if(choice ==1111){
	hidden();
    }
 
    system(cmd);
    return 0;
}
