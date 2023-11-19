import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 1; i <= T; i++) {
            int num = sc.nextInt();
            int cnt = 0;
            for (int j = -num; j <= num; j++) {
                for (int k = -num; k <= num; k++) {
                    if (j * j + k * k <= num * num) {
                        cnt++;
                    }
                }
            }
            System.out.printf("#%d %d\n",i,cnt);
        }
    }
}
