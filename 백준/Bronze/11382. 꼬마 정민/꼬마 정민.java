import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력 범위가  (1 <= A,B,C <= 10^12) 라서 int 범위를 하면 넘어가게 됨.
        // int는 참고로 4byte, 1byte가 8bit 이니까, 4byte는 32bit.
        // 2^10이 1024, 약 10^3 이니까, 32bit는 4 * 10^9니까
        // 표현 가능 범위는 약 -2 * 10^9 ~ 2 * 10^9 정도.
        // 즉 입력범위를 초과하는 입력을 받아서 이런 문제가 생겨

//        int a = sc.nextInt();
//        int b = sc.nextInt();
//        int c = sc.nextInt();

//        // 더블로 바꾸면 됨 -> 안됨, 왜냐 자료형이 소숫점이 붙어서 나오거든..
//        double a = sc.nextDouble();
//        double b = sc.nextDouble();
//        double c = sc.nextDouble();
//        System.out.println(a+b+c);

        long a = sc.nextLong();
        long b = sc.nextLong();
        long c = sc.nextLong();
        System.out.println(a+b+c);
    }
}