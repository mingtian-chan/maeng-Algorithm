import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int divisor) {
            int[] ans = {};
            ArrayList<Integer> list = new ArrayList<>();
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] % divisor == 0) {
                    list.add(arr[i]);
                }
            }

            if (list.size() == 0) {
                ans = new int[]{-1};
            } else {
                ans = new int[list.size()];
                for (int j = 0; j < list.size(); j++) {
                    ans[j] = list.get(j);
                }
                Arrays.sort(ans);
            }

        
            return ans;
    }
}