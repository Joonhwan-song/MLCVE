//gcc -z execstack -o CWE_126_e CWE_126_e.c -fno-stack-protector -mpreferred-stack-boundary=2 -m32
//No stack dummy, PIE, No NX, No canary

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
	
void application(){
	char motive_[1024];
	char name_[10];
	int app_num_=0;
	int age_=0;
	int sex_=0;

	puts("Hello manager");
	puts("You have to answer the question!!!");

	printf("Applicant number: ");
	scanf("%d",&app_num_);
	printf("Applicant age: ");
	scanf("%d",&age_);
	printf("Applicant sex(0:woman, 1:man): "); //0: woman , 1: man
	scanf("%d",&sex_);
	
	if(sex_!=0 && sex_!=1){
		printf("You have to choice 0(woman) or 1(man)\n");
		exit(0);
	}
	
	printf("Applicant name: ");
	scanf("%10s",name_);
	
	puts("Applicant motivation: ");
	read(0,motive_,0x4000); //buffer overflow!!!! 0x400=1024 , 0x4000 X
		

	puts("*********************Application Form*************************");
	printf("*Applicant number : %d\n",app_num_);
	printf("*Applicant name: %s\n",name_);
	printf("*Applicant age: %d\n",age_);
	printf("*Applicant sex: %d\n",sex_);
	printf("*Applicant motivation: %s\n",motive_);
	puts("**************************************************************");
	
}

int main(int argc, char* argv[]){

	char ans=0;

	for(;;){
		ans=0;
		printf("Do you want to enter applicant information?(1(Yes) or 0(No)): ");
		scanf("%d",&ans);

		if(ans==1 || ans== 0){
			if(ans==1){
				application();
			}

			else{
				puts("attack fail");
				exit(0);
			}

		}
		else{
			puts("attack fail");
			exit(0);
		}
	}
	return 0;
}
	

		
	
	

