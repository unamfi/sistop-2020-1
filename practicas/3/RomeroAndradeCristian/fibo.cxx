#include <cstdio>
#include <cstdlib>
#include <vector>

int fibo(int n);

int main(int argc, char** argv){
  int i;
  i = fibo(atoi(argv[1]));
  printf("%i", i);
  return 0;
}

int fibo(int n)
{
  int fibv[n+2];

  fibv[0] = 0;
  fibv[1] = 1;
  if (n == 0){
    return 0;
  }else if (n == 1){
    return 1;
  }
  else{
    return (fibo(n - 1) + fibo(n - 2));
  }
}
