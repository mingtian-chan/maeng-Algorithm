 class Solution {
        public int solution(int n) {
            int answer = 0;
            long tmp = (long) n;

            while (tmp != 1) {
                if (answer >= 500) {
                    return -1;
                }
                answer += 1;
                if (tmp % 2 == 0) {
                    tmp = tmp / 2;
                } else {
                    tmp = tmp * 3 + 1;
                }
            }
            return answer;
        }
    }