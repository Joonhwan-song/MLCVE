//gcc -z execstack -o ./CB ./CWE_121_a.c -fno-pie -fno-stack-protector -mpreferred-stack-boundary=2 -m32
#include <stdio.h>

void shell(){
	system("/bin/sh");
}

void func(){
	char buf[512]={0,};
	
	read(0,buf,1024);
}

int main(int argc, char *argv[]){

	setbuf(stdin,0LL);
	setbuf(stdout,0LL);
	setbuf(stderr,0LL);
	
	int secret_number=0;

	printf("Secret number: ");
	scanf("%d",&secret_number);

	if(secret_number == 20181130){
		func();
	}
	puts("attack fail");
}
