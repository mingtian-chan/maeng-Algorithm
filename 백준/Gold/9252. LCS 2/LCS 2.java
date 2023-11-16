import java.util.Scanner;

public class Main {
    public static int MAX_LENGTH = 1001;
    public static int[][] L = new int[MAX_LENGTH][MAX_LENGTH];
    public static int[][] S = new int[MAX_LENGTH][MAX_LENGTH];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        String s1 = sc.next();
        String s2 = sc.next();
        char[] s = s1.toCharArray();
        char[] t = s2.toCharArray();
        System.out.printf("%d", lengthLCS(s, t, s.length, t.length));
        printLCS(s,t, s.length, t.length);
    }


    private static void printLCS(char[] s, char[] t, int m, int n) {
        if (m == 0 || n == 0) {
            return;
        }
        if (S[m][n] == 0) {
            printLCS(s, t, m-1, n-1);
            System.out.printf("%c", s[m - 1]);
        } else if (S[m][n] == 1) {
            printLCS(s, t, m, n - 1);
        } else if (S[m][n] == 2) {
            printLCS(s, t, m - 1, n);
        }
    }

    private static int lengthLCS(char[] s, char[] t, int m, int n) {
        // base case
        for (int i = 0; i < m; i++) {
            L[i][0] = 0;
        }
        for (int i = 0; i < n; i++) {
            L[0][i] = 0;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    L[i][j] = L[i - 1][j - 1] + 1;
                    S[i][j] = 0;
                } else {
                    L[i][j] = Math.max(L[i][j - 1], L[i - 1][j]);
                    if (L[i][j] == L[i][j - 1]) {
                        S[i][j] = 1;
                    } else {
                        S[i][j] = 2;
                    }
                }
            }
        }
        return L[m][n];
    }
}