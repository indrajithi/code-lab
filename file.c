#define _POSIX_SOURCE
#define _POSIX_C_SOURCE 200809L
#include<stdio.h>
#include<iostream>
#include<unistd.h>
using namespace std;
int main()
{
    int res;
    #ifdef _POSIX_VERSION
        cout<<"system confirms to POSX "
            <<"version is:"<<_POSIX_VERSION<<endl;
    #endif

    if((res=sysconf(_SC_OPEN_MAX))==-1)
        perror("sysconf");
    else cout << "OPEN_MAX:"<<res<<endl;
    
    if ((res=pathconf("/",_PC_PATH_MAX))==-1)
        perror("pathconf");
    else cout<<"Max path name:"<<(res+1)<<endl;

    if((res=sysconf(_SC_CLK_TCK))==-1)
        perror("sysconf:");
    else cout << "CLK:"<<res<<endl;
    
    return 0;
}
