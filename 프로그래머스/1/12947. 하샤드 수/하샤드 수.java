 class Solution {
        public boolean solution(int n) {
            int tmp = n;
            int s = 0;

            while (n > 0) {
                s += n % 10;
                n = n / 10;
            }
            boolean answer = tmp % s == 0;

            return answer;
        }
    }