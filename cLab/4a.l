%{
    #include "y.tab.h"
    extern yylval
%}
%%
[a-zA-Z]+ {return id;}
[0-9]+ {yylval=atoi(yytext);return num;}
.|\n return yytext[0];
%%

