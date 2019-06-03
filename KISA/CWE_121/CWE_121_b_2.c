//gcc -z execstack -o ./CB ./CWE_121_b.c -fno-pie -fno-stack-protector -mpreferred-stack-boundary=2 -m32
#include <stdio.h>

void shell(){
	system("/bin/sh");
}
void func(){

        char buf1[128];
        char buf2[128];
        char buf3[128];
        char buf4[128];

        printf("1 input: ");
        read(0,buf4,sizeof(buf4));
        printf("2 input: ");
        read(0,buf3,strlen(buf4));
        printf("3 input: ");
        read(0,buf2,strlen(buf4));
        printf("4 input: ");
        read(0,buf1,strlen(buf4));
}	
int main(){

	setbuf(stdin,0LL);
	setbuf(stdout,0LL);
	setbuf(stderr,0LL);

	func();

	return 0;
}
