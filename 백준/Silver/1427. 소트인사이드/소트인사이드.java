import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String st = sc.next();
        char [] num = new char[st.length()];
        for(int i =0 ; i<st.length(); i++){
            num[i] = st.charAt(i);
        }
        Arrays.sort(num);
        for(int i = num.length-1; i>=0; i--){
            System.out.print(num[i]);
        }
    }
}