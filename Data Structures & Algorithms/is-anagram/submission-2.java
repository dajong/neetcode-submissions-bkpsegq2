class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        int[] counter = new int[26];

        for(int i = 0; i < s.length(); i++){
            char cs = s.charAt(i);
            char ct = t.charAt(i);
            
            counter[cs - 'a']++;
            counter[ct - 'a']--;
        }

        return Arrays.stream(counter).allMatch(num -> num == 0);
    }
}
