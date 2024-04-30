
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int[] alpha = new int[26];
        for(int i =0 ; i<26; i++){
            alpha[i] = -1;
        }
        for (int i = 0 ; i<s.length(); i++){
            char ch = s.charAt(i);
            if (alpha[ch-'a'] == -1){
                alpha[ch-'a']= i;
            }

        }

        for (int a:alpha){
            System.out.print(a + " ");
        }
        sc.close();
    }
}
