//gcc -o ./CB ./CWE_121_d.c -fno-pie -fno-stack-protector -mpreferred-stack-boundary=2 -m32 
 
#include <stdio.h>
#include <string.h>
 
void func(){
    char buf[128]={0,};
  
    read(0,buf,1024);
}
  
int main(){
    char introduce[1024]="Very Hard Buffer OverFLow World!!!\n";

    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL); 
    write(1,introduce,strlen(introduce));
    func();
     
    puts("attack fail");
    return 0;
}
