import java.util.Scanner;

public class Main {

    static Integer[][] dp = new Integer[41][2];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numTestCases = sc.nextInt();

        dp[0][0] = 1; // n == 0 일때 0의 호출 횟수
        dp[0][1] = 0; // n == 0 일때 1의 호출 횟수
        dp[1][0] = 0; // n == 1 일때 0의 호출 횟수
        dp[1][1] = 1; // n == 1 일때 1의 호출 횟수


        for (int i = 0; i < numTestCases; i++) {
            int n = sc.nextInt();
            fibonacci(n);
            System.out.println(dp[n][0] + " " + dp[n][1]);
        }
    }

    private static Integer[] fibonacci(int n) {
        if (dp[n][0] == null || dp[n][1] == null) {
            dp[n][0] = fibonacci(n - 1)[0] + fibonacci(n - 2)[0];
            dp[n][1] = fibonacci(n - 1)[1] + fibonacci(n - 2)[1];
        }
        return dp[n];
    }
}