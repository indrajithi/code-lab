%{
#include<stdio.h>
%}
%token id num
%left '+' '-'
%left '*' '/'
%%
s:s expr '\n' {printf("valid");}
|
;
expr: expr '+' expr
|expr '-' expr
|expr '*' expr
|expr '/' expr
|id
|num
;
%%
int main()
{
    printf("enter an expression\n");
    yyparse();
    return 1;
}

yyerror()
{
    printf("invalid expression\n");
  
}
