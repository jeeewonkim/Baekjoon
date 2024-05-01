import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0 ; i< n ; i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        StringBuilder sb = new StringBuilder();
        Collections.sort(arr);
        for(int val: arr){
            sb.append(val+"\n");
        }
        //System.out.println(sb.toString());
        System.out.println(sb);
    }

}