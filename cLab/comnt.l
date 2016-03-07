%{
#include<stdio.h>
int c;
%}
begin "/*"
end "*/"
begin1 "//"
text[a-zA-Z]
%%
{begin1}{end} {c++;}
{begin}{text}{end} {c++;}
%%
int main(int argc,char *argv[])
{
     if(argc != 3)
     {
          printf("usage: ./a.out <input-file> <output-file>");
          exit(0);
     }
yyin = fopen(argv[1],"r");
yyout = fopen(argv[2],"w");
yylex();
printf("c+%d",c);
printf("conmment free files =%s", argv[2]);
return 0;
}
