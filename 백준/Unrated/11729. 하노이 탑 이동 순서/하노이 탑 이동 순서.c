#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int hanoi(int n, int from, int tmp, int to){
    if (n == 1){
        printf("%d %d\n", from, to);
    }
    else{
        hanoi(n-1, from, to, tmp);
        printf("%d %d\n",from, to);
        hanoi(n-1, tmp, from, to);
    }
}

int main(){
    int T;
    int n;
    scanf("%d", &T);
    n = pow(2, T) - 1;
    printf("%d\n", n);
    hanoi(T, 1, 2, 3);

    return 0;
}