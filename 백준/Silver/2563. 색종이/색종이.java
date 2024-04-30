import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int [][] color = new int[100][100];
        for(int i = 0 ; i< num ; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            for (int n = x; n<x+10; n++){
                for(int m = y; m<y+10; m++){
                    color[n][m] = 1;
                }
            }
        }
        int result = 0;
        for(int i =0 ; i<100; i++){
            for(int j = 0 ; j<100; j++){
                if(color[i][j] == 1){
                    result +=1;
                }
            }
        }
        System.out.println(result);
        sc.close();
    }
}