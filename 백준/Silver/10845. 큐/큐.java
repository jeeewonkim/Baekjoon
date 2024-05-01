import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        String str = st.nextToken();

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> deq = new LinkedList<Integer>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if (str.equals("push")) deq.add(Integer.parseInt(st.nextToken()));
            else if (str.equals("front")) {
                if (deq.isEmpty()) sb.append(-1).append("\n");
                else sb.append(deq.peekFirst()).append("\n");
            }
            else if (str.equals("back")){
                if(deq.isEmpty()) sb.append(-1).append("\n");
                else sb.append(deq.peekLast()).append("\n");
            }
            else if(str.equals("size")){
                sb.append(deq.size()).append("\n");
            }
            else if(str.equals("pop")){
                if(deq.isEmpty()) sb.append(-1).append("\n");
                else sb.append(deq.pollFirst()).append("\n");
            }
            else if(str.equals("empty")){
                if(deq.isEmpty()) sb.append(1).append("\n");
                else sb.append(0).append("\n");
            }
        }

        System.out.println(sb.toString());

    }

}