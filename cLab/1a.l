%{
#include<stdio.h>
int c = 0 , line = 0, s = 0, w = 0;
char filename[50];
%}

%%
[ ] c++,s++;
\n line++;
\t c += 5, s += 5;
[^\n\t ]+ {w++; c += yyleng;}
%%

int main()
{
     printf("enter the file name");
     scanf("%s",filename);
     
     yyin = fopen(filename, "r");
     yylex();

     printf("c = %d , w = %d , line = %d , sp = %d\n", c, w, line, s); 
     return 0;
}
