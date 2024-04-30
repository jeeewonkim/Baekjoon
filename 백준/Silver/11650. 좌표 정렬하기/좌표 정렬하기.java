import java.util.Comparator;
import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [][] graph = new int[n][2];
        for(int i = 0 ; i< n ; i++){
            graph[i][0] = sc.nextInt();
            graph[i][1] = sc.nextInt();
        }
        Arrays.sort(graph, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2)
            {
                if(o1[0]== o2[0]){
                    return o1[1]-o2[1];
                }
                else{
                    return o1[0]- o2[0];
                }
            }
        });
        for(int i = 0 ; i< n; i++){
            System.out.println(graph[i][0]+ " " + graph[i][1]);
        }
        sc.close();
        }
    }
