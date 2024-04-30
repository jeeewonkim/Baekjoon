import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        String a_reverse = "";
        String b_reverse = "";
        for (int i = 2; i >=0; i--){
            a_reverse = a_reverse + a.charAt(i);
            b_reverse = b_reverse + b.charAt(i);
        }
        if(Integer.parseInt(a_reverse) < Integer.parseInt(b_reverse)){
            System.out.println(b_reverse);
        }
        else{
            System.out.println(a_reverse);
        }
    }
}
