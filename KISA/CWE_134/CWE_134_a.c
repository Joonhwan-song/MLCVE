//CWE-134: Use of Externally-Controlled Format String
//gcc -o ./CB ./CWE_134_a.c -m32

#include <stdio.h>

void func(){

	FILE *fd = fopen("flag","r");	
	char flag[32]={0,};
	int len=0;

	fread(flag,1,32,fd);
	fclose(fd);

	puts("Input len: ");
	scanf("%d",&len);

	getchar();
	fgets(flag ,len, stdin);

	printf(flag);
}
int main(){
	setbuf(stdin, 0LL);
	setbuf(stdout, 0LL);
	setbuf(stderr, 0LL);
	func();

	return 0;
}
