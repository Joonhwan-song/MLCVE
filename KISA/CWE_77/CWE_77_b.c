//CWE-77:Improper Neutralization of Special Elements used in a Command ('Command Injection') 
//gcc -o ./CB ./CWE_77_b.c -m32
#include <stdio.h>
#include <string.h>
 
int main(int argc, char* argv[], char** envp){

    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL); 
    system( argv[1] );
    return 0;
}
