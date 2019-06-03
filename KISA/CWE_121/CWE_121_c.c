//gcc -o ./CB ./CWE_121_c.c -fno-pie -fno-stack-protector -mpreferred-stack-boundary=2 -m32 

#include <stdio.h>

void shell(){
    system("/bin/sh");
}


void func(){
    char buf[128]={0,};
 
    read(0,buf,1024);
}
 
int main(){
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);
    printf("Hard Buffer OverFLow World!!!\n");
    func();
    puts("attack fail");
    return 0;
}
