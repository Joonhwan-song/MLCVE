//gcc -z execstack -o ./CB ./CWE_121_b.c -fno-pie -mpreferred-stack-boundary=2 -m32

#include <stdio.h>

void shell(){
    system("/bin/sh");
}

void func(){
    char buf[128]={0,};

    read(0,buf,133);
    printf("buf: %s\n",buf);

    read(0,buf,1024);
}

int main(){
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);
    func();
    puts("attack fail");
    return 0;
}
