class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int num: numbers){
            
            answer += num;
        }
        int len = numbers.length;
        return answer/len;
    }
}