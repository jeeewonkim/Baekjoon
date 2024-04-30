import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] num = new int[5];
        int sum = 0;
        for(int i =0 ; i<5; i++){
            int a = sc.nextInt();
            sum +=a;
            num[i] = a;

        }
        Arrays.sort(num);
        System.out.println(sum/5);
        System.out.println(num[2]);
    }
}