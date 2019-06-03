//CWE-77:Improper Neutralization of Special Elements used in a Command ('Command Injection') 
//gcc -o ./CB ./CWE_77_a.c -m32
#include <stdio.h>

void func(){
	char command[0x10];

	read(0,command,0x10);

	system(command);
}

int main(){
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);
	func();
	return 0;
}
