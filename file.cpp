#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 199309L
#include<stdio.h>
#include<iostream>
#include<unistd.h>
using namespace std;
int main()
{
    int res;

    if((res=sysconf(_SC_OPEN_MAX))==-1)
        perror("sysconf");
    else cout << "OPEN_MAX:"<<res<<endl;
    
    perror("test error!\n");
    
    return 0;
}
