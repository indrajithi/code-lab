// Lex Program to check the entered arithmetic operation is valid or not
// Programmer: Indrajith Indraprastham 
// Date : 19 AUG 2015 ; 1:34
// Note: 
        // Final expr with (a+b)*(a-b):  ^({op1})({op1}?{op2}{op1}{op1}?)*{op2}?{op1}$ 
        // Final expr with (a+b)(a-b) :  ^({op1})({op1}*{op2}{op1}{op1}*)*{op2}?{op1}$
        // ^({op1}                    :  starts with op1; 
        // ({op1}*{op2}{op1}{op1}*)*  :  matches a+b+c+d
        // {op2}?{op1}$               :  ends expr with op1


%{
#include<stdio.h>
char a[10];
%}

op1 [ a-zA-Z/(/)0-9] 
op2 [+/*-]
%%

^({op1})({op1}*{op2}{op1}{op1}*)*{op2}?{op1}$ {printf("vaid expr\n"); strcpy(a,yytext); count(); exit(0);}

%%
count()
{
	int i;
	for(i=0; i<strlen(a); i++){

	 if(a[i] == '+' | a[i] == '-' | a[i] == '*' | a[i] == '/')
		printf("operator = %c \n" , a[i]);

	else if (a[i] == '(' | a[i] == ')')
		printf("Par= %c \n", a[i]);
	
	else printf("operant = %c \n", a[i]);
	}
}

main()
{
	printf("enter an exper\n");
	yylex();
	printf("invalid expr\n");
	
// Final expr with (a+b)*(a-b):  ^({op1})({op1}?{op2}{op1}{op1}?)*{op2}?{op1}$ 
// Final expr with (a+b)(a-b) :  ^({op1})({op1}*{op2}{op1}{op1}*)*{op2}?{op1}$
}