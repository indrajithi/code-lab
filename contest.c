//Sunday 06 September 2015 10:56:37 PM IST 
//Programmer: Indrajith indraprastham
// Other link: http://hostcode.sourceforge.net/view/3332
/*............... Question ...................
Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
Relational Operators are operators which check relatioship between two values. Given two numerical values A and B you need to help chef in finding the relationship between them that is,
First one is greater than second or,
First one is less than second or,
First and second one are equal.
 
Input
First line contains an integer T, which denotes the number of testcases. Each of the T lines contain two integers A and B.
Output
For each line of input produce one line of output. This line contains any one of the relational operators
'≺' , '≻' , '='.
Constraints
1 ≤ T ≤ 10000
1 ≤ A, B ≤ 1000000001
Example
Input:
3
10 20
20 10
10 10
Output:
≺
≻
=
 
Explanation
Example case 1. In this example 1 as 10 is lesser than 20.
*/

#include<stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int isNumeric (const char * s)  // to chk if string is number. (Not used now)
{
    if (s == NULL || *s == '\0' || isspace(*s))
      return 0;
    char * p;
    strtod (s, &p);
    return *p == '\0';
}

void freeStr( char *str , int n) // set string to NULLL
{
     while(n >= 0)
          str[n--] = '\0';
}


int main()
{    
     char  c, s[100];
     int  c1 , c2, ip_buff = 0, i = 0;
     // printf("-1:Iam here!\n");
     while((c=getchar()) != EOF){
       //   if( c != ' ' && c != '\n'){
            if(isdigit(c)){
               s[i++] = c;
               continue;          
               }
              //  printf("01:Iam here!");
    if((ip_buff == 0 ) && (c == '\n')){  // why this works here? ip_buff = 0 when null input, it warks for one i/p !
    // printf("success");
     freeStr(s , i);
     i=0;
     ip_buff = 0;
     }
  else   if(ip_buff < 2 ){ 
//printf("0:Iam here!");

               if(ip_buff == 0){
                    c1 = atoi(s);
                    ip_buff++;
                    printf("c1 = %d \n", c1);
                    freeStr(s , i);
                    i=0;
                     
                     }
            
               else if(ip_buff == 1){
                    c2 = atoi(s); 
                    printf("c2 = %d \n", c2);
                    ip_buff++;  
                    freeStr(s , i); 
                    i=0;
                     
                    }
                    
          }       
     
               if(ip_buff == 2)  // compares
               {
                    if(c1<c2)
                         printf("<\n");
                    else if (c1 > c2)
                         printf(">\n");
                    else printf("=\n");
                    
                    ip_buff = 0;
               }
                
     }
}