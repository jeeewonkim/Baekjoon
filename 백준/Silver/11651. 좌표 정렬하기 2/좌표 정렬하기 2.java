import java.util.Scanner;
import java.util.Arrays;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [][] graph = new int[n][2];
        for(int i =0 ; i<n; i++){
            graph[i][0] = sc.nextInt();
            graph[i][1] = sc.nextInt();
        }

        Arrays.sort(graph, (e1,e2)->{
            if(e1[1] == e2[1]){
                return e1[0] - e2[0];
            }
            else{
                return e1[1] - e2[1];
            }
        });

        for(int i = 0; i< n; i++){
            System.out.println(graph[i][0] + " " + graph[i][1]);
        }
    }
}