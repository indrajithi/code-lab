#include<stdio.h>

int fib(int n)
{
    if ( n == 0){
        printf("0, ");
        return 0;
    if (n == 1) {
        print("1");
        return 1;
    else
    {
        return fib(n-1) + fib (n-2);
    }

}




int main()
{
int i , n;
printf("enter a range:");
scanf("%d",&n);
for( i= 0; i<n; i++)
    printf("%d, ",fib(i));

}

