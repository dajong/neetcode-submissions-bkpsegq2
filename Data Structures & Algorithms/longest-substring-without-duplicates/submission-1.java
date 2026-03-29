class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<Character>();
        int res = 0;

        for(int l = 0, r = 0; r < s.length(); r++){
            Character curChar = s.charAt(r);

            while(set.contains(curChar)){
                set.remove(s.charAt(l));
                l++;
            }

            res = Math.max(res, r - l + 1);
            set.add(curChar);
        }

        return res;
    }
}
