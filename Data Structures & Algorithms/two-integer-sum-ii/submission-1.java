class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;

        while(r > l){
            int left = numbers[l];
            int right = numbers[r];
            int sum = left + right;

            if(sum == target) return new int[]{l + 1, r + 1};

            if(sum > target) r--;
            else l++;
        }

        return null;
    }
}
