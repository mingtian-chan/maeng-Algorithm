#include <stdio.h>
#include <stdlib.h>
int main(){
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        int a; 
        int b;
        scanf("%d %d", &a, &b);
        printf("%d\n",(a/b)*(a/b));
    }
        return 0;
}