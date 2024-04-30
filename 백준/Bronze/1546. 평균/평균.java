import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] score = new int[n];
        float max = 0;
        for(int i = 0 ; i<n; i++){
            int a  = sc.nextInt();
            if (max < a){
                max = a;
            }
            score[i] = a;
        }
        float sum = 0;
        for(int i = 0 ; i< n; i++){
            sum+=(score[i]/max)*100;
        }
        sc.close();
        System.out.println(sum/n);
    }
}