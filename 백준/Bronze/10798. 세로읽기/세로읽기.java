import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char [][] words = new char[5][15];
        for(int i = 0 ; i<5; i++){
            String str = sc.next();
            for(int j = 0 ; j<str.length(); j++){
                words[i][j] = str.charAt(j);
            }
        }
        String result = "";
        for(int i =0 ; i<15; i++) {
            for (int j = 0; j < 5; j++) {
                if (words[j][i]!='\0') {
                    result += words[j][i];
                }
            }
        }
        System.out.println(result);
        sc.close();
    }
}