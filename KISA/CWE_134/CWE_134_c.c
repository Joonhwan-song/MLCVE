//CWE-134: Use of Externally-Controlled Format String
//gcc -z execstack -o ./CB ./CWE_134_c.c -m32

#include <stdio.h>

char shellcode[] = "\x31\xc0\x50\x68\x2f\x2f\x73"
                   "\x68\x68\x2f\x62\x69\x6e\x89"
                   "\xe3\x89\xc1\x89\xc2\xb0\x0b"
                   "\xcd\x80\x31\xc0\x40\xcd\x80";

void func(){

	char buf[1024]={0,};

	puts("Hello ~~~");
	puts("Input: ");

	fgets(buf,1024, stdin);

	printf(buf);

	return 0;
}

int main(){
	setbuf(stdin, 0LL);
	setbuf(stdout, 0LL);
	setbuf(stderr, 0LL);
	func();
	puts("attack fail");

	return 0;
}
