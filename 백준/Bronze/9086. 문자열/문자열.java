import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 0 ; i< n ; i++){

            String s = sc.next();
            System.out.printf("%c%c", s.charAt(0), s.charAt(s.length()-1));
            System.out.println();
        }
        sc.close();
    }
}
