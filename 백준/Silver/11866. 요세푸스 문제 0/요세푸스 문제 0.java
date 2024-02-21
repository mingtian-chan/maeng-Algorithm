import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i < n + 1; i++) {
            deque.addLast(i);
        }

        Deque<Integer> ans = new ArrayDeque<>();
        while (!deque.isEmpty()) {
            for (int i = 0; i < k-1; i++) {
                deque.addLast(deque.removeFirst());
            }
            ans.addLast(deque.removeFirst());
        }
        System.out.print("<");

        for (int i = 0; i < n-1; i++) {
            System.out.print(ans.removeFirst() + ", ");
        }
        System.out.print(ans.removeFirst() + ">");
    }
}
