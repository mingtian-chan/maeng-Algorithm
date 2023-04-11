#include <stdio.h>
#include <stdlib.h>
int main(){
  int denum = 1;
  int num = 1;
  int idx = 1;
  int flag = -1;

  int T;
  scanf("%d", &T);

  while (idx < T){
    if ((num == 1) && (flag == -1)){
      denum++;
      flag = 1;
    }
    else if ((denum ==1) && (flag == 1)){
      num++;
      flag = -1;
    }
    else {
      num += flag;
      denum -= flag;
    }
    idx++;
  }

  printf("%d/%d",num, denum);
  return 0;
}