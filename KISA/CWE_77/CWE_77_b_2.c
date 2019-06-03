//gcc -o ./CB ./CWE_77_b -m32

#include <stdio.h>

void bof(){
	char buf[128]={0,};

	printf("Possible exploit from bof ? \n");
	read(0,buf,132);
}

void cmd(){
        char command[0x10];

        read(0,command,0x10);

        system(command);
}

int main(){
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);

    int choice=0;

    printf("> ");
    scanf("%d",&choice);

    if(choice == 1){
	bof();
    }

    else if(choice == 2){
 	cmd();
    }

    else{
	puts("attack fail");
    }

    return 0;
}
