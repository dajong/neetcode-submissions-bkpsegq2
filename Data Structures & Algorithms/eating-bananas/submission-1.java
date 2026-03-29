class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        
        int upperBound = 0;
        for(int i = 0; i < piles.length; i++){
            upperBound = Math.max(piles[i], upperBound);
        }
        int minRate = upperBound;
        int l = 1;

        while(upperBound >= l){
            int mid = l + (upperBound - l) / 2;
            boolean check = checkRateValid(piles, mid, h);

            if(!check){
                l = mid + 1;
            } else if(check){
                minRate = Math.min(minRate, mid);
                upperBound = mid - 1;
            }
        }

        return minRate;
    }

    boolean checkRateValid(int[] piles, int rate, int h){
        int totalTime = 0;

        for(int i = 0; i < piles.length; i++){
            totalTime += Math.ceil((double) piles[i] / rate);
            if(totalTime > h) return false;
        }

        return true;
    }
}
