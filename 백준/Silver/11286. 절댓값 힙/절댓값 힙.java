import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1,o2)->{
            int abs1 = Math.abs(o1);
            int abs2 = Math.abs(o2);

            if(abs1 == abs2){
                return o1>o2 ? 1:-1;
            }
            return abs1-abs2;
        });

        for(int i = 0; i<n; i++){
            int op = Integer.parseInt(br.readLine());
            if(op == 0){
                if(pq.isEmpty()) sb.append(0).append("\n");
                else sb.append(pq.poll()).append("\n");
            }
            else{
                pq.add(op);
            }
        }


        System.out.println(sb.toString());

    }

}
