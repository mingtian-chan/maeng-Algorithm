class Solution {
    public int[] solution(long n) {
            String s = Long.toString(n);
            int l = s.length();
            int[] answer = new int[l];
            for (int i = 0; i < l; i++) {
                long a = n % 10;
                answer[i] = (int) a;
                n = n / 10;
            }

            return answer;
        }
}