import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int m = sc.nextInt();
        if ((b+m) >= 60){
            a+=(b+m)/60;
            b = (b+m)%60;
        }
        else{
            b+=m;
        }
        if (a>=24){
            a %= 24;
        }
        sc.close();
        System.out.print(a + " " +  b);
    }
}
