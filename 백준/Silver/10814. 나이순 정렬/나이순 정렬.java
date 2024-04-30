import java.util.Scanner;
import java.util.Arrays;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String [][] info = new String[n][2];
        //int [] age = new int[n];
        for(int i =0 ; i<n; i++){
            info[i][0] = sc.next();
            info[i][1] = sc.next();
            //age[i] = sc.nextInt();
        }
        Arrays.sort(info, (e1,e2)->{
            return Integer.parseInt(e1[0])-Integer.parseInt(e2[0]);
        });

        for(int i =0 ; i<n; i++){
            System.out.println(info[i][0] + " "+ info[i][1]);
        }

    }
}