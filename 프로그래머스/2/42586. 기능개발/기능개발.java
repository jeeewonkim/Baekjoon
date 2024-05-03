import java.util.*;
import java.io.*;
class Solution {
    Queue<Integer> q = new LinkedList<>();
    List<Integer> list = new ArrayList<>();
    public int[] solution(int[] progresses, int[] speeds) {
        for(int i =0 ;i<progresses.length; i++){
            q.add((int) Math.ceil((100-progresses[i])/(double)speeds[i]));
        }
        int count = 0;
        int now = q.peek();
        while(!q.isEmpty()){
            System.out.println(q.peek() + " "+ now);
            if (q.peek()<=now){
                count ++;
                q.poll();
            }
            else{
                list.add(count);
                count = 0;
                now = q.peek();
            }
        }
        list.add(count);
        int[] answer = new int [list.size()];
        for(int i =0 ; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}