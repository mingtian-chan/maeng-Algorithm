import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int answer = 0;
        String[] arr = s.split("-");
        for (int i = 0; i < arr.length; i++) {
            String[] arr2 = arr[i].split("\\+");
            int sum = 0;
            for (int j = 0; j < arr2.length; j++) {
                sum += Integer.parseInt(arr2[j]);
            }
            if (i == 0) {
                answer += sum;
            } else {
                answer -= sum;
            }
        }
        System.out.println(answer);
    }
}
