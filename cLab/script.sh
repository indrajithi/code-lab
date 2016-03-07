#!/bin/bash
lex 4a.l
yacc -d 4a.y
cc lex.yy.c y.tab.c -ll

