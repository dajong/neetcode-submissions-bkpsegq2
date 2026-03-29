class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        boolean exist = false;

        // find row
        int r = matrix.length - 1;
        int l = 0;
        int targetRow = 0;

        while(r >= l){
            int mid = l + (r - l) / 2;
            if(matrix[mid][0] <= target && target <= matrix[mid][0]){
                targetRow = mid;
                break;
            } else if(matrix[mid][0] > target) r = mid - 1;
            else l = mid + 1;
        }

        // find target
        l = 0;
        r = matrix[targetRow].length - 1;

        while (r >= l){
            int mid = l + (r - l) / 2;
            int curNum = matrix[targetRow][mid];

            if(curNum > target) r = mid - 1;
            else if(curNum < target) l = mid + 1;
            else return true;
        }

        return exist;
    }

}
