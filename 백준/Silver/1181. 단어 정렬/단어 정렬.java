import java.util.Scanner;
import java.util.Arrays;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String [] words = new String[n];
        for(int i =0 ; i<n; i++){
            words[i] = sc.next();

        }

        Arrays.sort(words, (e1,e2)->{
            if (e1.toString().length() == e2.toString().length()){
                return e1.compareTo(e2);
            }
            else{
                return e1.length() - e2.length();
            }
        });
        System.out.println(words[0]);
        for(int i = 1; i< n; i++){
            if(!words[i].equals(words[i-1])){
                System.out.println(words[i]);
            }
        }
    }
}