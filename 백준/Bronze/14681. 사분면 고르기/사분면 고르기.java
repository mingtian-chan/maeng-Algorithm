//  사분면 고르기

import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        if (x > 0 && y > 0) {
            System.out.println(1);
        }        if (x > 0 && y < 0) {
            System.out.println(4);
        }        if (x < 0 && y > 0) {
            System.out.println(2);
        }        if (x < 0 && y < 0) {
            System.out.println(3);
        }
    }
}