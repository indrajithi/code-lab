 #include <stdio.h>

   int main (){
       int i = 0;
     
     printf("........progress bar.............");
       for (i = 0; i < 10000; i++){
           printf("\rIn progress %d", i/100);
           fflush(stdout);
       }
       printf("\n");
   }
