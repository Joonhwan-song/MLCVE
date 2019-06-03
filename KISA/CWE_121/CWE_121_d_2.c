//gcc -z execstack -o ./CB ./CWE_121_d.c -fno-pie -fno-stack-protector -mpreferred-stack-boundary=2 -m32
#include <stdio.h>
#include <math.h>

void shell(){
	system("/bin/sh");
}

void func(){
	char buf[128]={0,};

	printf("secret vuln: ");
	read(0, buf, 512);
}

int add(int x, int y){

	return x+y;
}

int minus(int x, int y){
	return abs(x-y);
	
}

int main(){

	setbuf(stdin , 0LL);
	setbuf(stdout, 0LL);
	setbuf(stderr, 0LL);
	
	char buffer[512]={0,};
	char choice[10]={0,};
	int retn=0;
	int x,y=0;
	int count=0;

	int secret_number=5959;

	for(;;){
		printf("Loop count: ");
		scanf("%d",&count);

		if(count != 0){
			break;
		}
	}
			
	for(int i=0; i<count; i++){
		printf(">");
		scanf("%s",choice);

		if(!strcmp(choice,"add")){
			printf("Input x: ");
			scanf("%d",&x);
			printf("Input y: ");
			scanf("%d",&y);

			retn+=add(x,y);

			printf("result: %d\n",retn);
		}

		else if(!strcmp(choice,"minus")){
                	printf("Input x: ");
                	scanf("%d",&x);
                	printf("Input y: ");
               		scanf("%d",&y);

       	         	retn+=minus(x,y);
	
			printf("result: %d\n",retn);
		}
		
		else{
			i--;
		}
		
	}

	if(retn>secret_number){
	
		func();
		puts("attach fail");
	}
}
	
