class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 1) return nums[0];

        int curSum = 0, maxSum = nums[0];

        for(int r = 0; r < nums.length; r++){
            curSum = Math.max(curSum, 0);
            curSum += nums[r];
            maxSum = Math.max(curSum, maxSum);
        }


        return maxSum;
    }
}
