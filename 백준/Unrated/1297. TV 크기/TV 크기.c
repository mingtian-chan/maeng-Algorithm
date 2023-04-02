#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
  double d;
  double w;
  double h;
  double ans;
  scanf("%lf %lf %lf", &d, &w, &h);

  ans = pow((pow(d,2)) / (pow(w,2) + pow(h,2)),0.5);
  int answ = ans * w;
  int ansh = ans * h;

  printf("%d %d\n", answ, ansh);
  return 0;
}