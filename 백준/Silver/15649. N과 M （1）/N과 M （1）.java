import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int [] result;
    static boolean [] visit;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        result = new int[m];
        visit = new boolean[n+1];
        back(n,m,0);
    }
    public static void back(int n, int m, int depth){
        if(depth == m){
            for(int i =0 ;i<m; i++){
                System.out.print(result[i] + " ");
            }
            System.out.println();
            return;
        }
        for(int i =1  ; i<=n; i++){
            if(!visit[i]){
                visit[i] = true;
                result[depth] = i;
                back(n,m,depth+1);
                visit[i] = false;
            }
        }
    }

}