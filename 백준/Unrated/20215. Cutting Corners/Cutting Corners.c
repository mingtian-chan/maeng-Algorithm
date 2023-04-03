#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    float w;
    float h;
    float ans;
    // double의 형식지정자는 %f , long double의 형식 지정자는 %lf
    scanf("%f %f", &w, &h);
    
    ans = w+h-pow((pow(w, 2) + pow(h, 2)),0.5);
    printf("%f\n", ans);

    return 0;
}