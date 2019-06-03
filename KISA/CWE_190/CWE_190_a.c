//CWE-190: Integer Overflow or Wraparound
//Not ASLR
//Not NX bit
//gcc -fno-stack-protector -z execstack -o ./CB ./CWE_190_a.c -m32
 
#include <stdio.h>
 
#include <stdio.h>
 
char flag[128]={0,};
 
void file(){
        FILE *fp=fopen("./flag","r");
        fgets(flag,128,fp);
}
 
void func(){
        char file_buf[128];
    int num;
 
        strcpy(file_buf,flag);
 
    printf("How many read..?");
    scanf("%d",&num);
 
    if(num >=1){
        printf("Can`t access..");
        exit(-1);
    }
     
    write(1,file_buf,num);
}
int main(){
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);
        file();
        func();
        return 0;
}
