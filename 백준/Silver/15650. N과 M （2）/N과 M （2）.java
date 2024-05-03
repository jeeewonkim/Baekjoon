import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] num;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        num = new int[n];
        for (int i = 1; i <= n; i++) {
            num[i - 1] = i;
        }
        back(1);

    }

    //static ArrayList<Integer> list = new ArrayList<>();
    static Stack<Integer> list = new Stack<>();

    static void back(int a) {
        if (list.size() == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(list.get(i) + " ");
            }
            System.out.println();
            return;
        } else {
            for (int i = 1; i <= n; i++) {
                if((!list.isEmpty() && i>list.get(list.size()-1))||list.isEmpty()){
                list.add(i);
                back(i + 1);
                list.pop();}
            }
        }
    }
}