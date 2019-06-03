//CWE-77:Improper Neutralization of Special Elements used in a Command ('Command Injection') 
//gcc -o ./CB ./CWE_77_c.c -m32
#include <stdio.h>
#include <string.h>
 
int check(char* cmd){
    int str=0;
 
    str += strstr(cmd, "flag")!=0;
    str += strstr(cmd, "sh")!=0;
    str += strstr(cmd, "cat")!=0;
    return str;
}
int main(int argc, char* argv[], char** envp){
 
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);
    if(check(argv[1])) 
    {
        printf("No hack\n");
        return 0;
    }
 
    system( argv[1] );
    return 0;
}
