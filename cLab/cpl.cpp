#include <iostream>
#include<unistd.h>
using namespace std;

int main()
{
 for(int i = 1; i <= 10; i++)
 {
  std::cout << i*10 << '%';
  std::cout.flush(); // see wintermute's comment
  sleep(10);
  std::cout << '\r';
 }
}
