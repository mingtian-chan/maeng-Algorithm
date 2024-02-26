import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] dp = new int[n+1][m+1];
            for (int j = 1; j <= n; j++) {
                for (int k = 1; k <= m; k++) {
                    if (j == 1) {
                        dp[j][k] = k;
                    } else if (j == k) {
                        dp[j][k] = 1;
                    } else {
                        dp[j][k] = dp[j][k-1] + dp[j-1][k-1];
                    }
                }
            }
            System.out.println(dp[n][m]);
        }
    }
}
