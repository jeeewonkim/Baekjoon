import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        String[] str = s.split("");
        ArrayList<String> list = new ArrayList<>();
        for(int i =0 ; i < str.length; i++){
            if (str[i].equals("(")){
                list.add("(");
            }
            else{
                if(list.isEmpty()){
                    answer = false;
                    break;
                }
                else{
                    list.remove(list.size()-1);
                }
            }
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");
        if(!list.isEmpty()){
            answer = false;
        }
        return answer;
    }
}