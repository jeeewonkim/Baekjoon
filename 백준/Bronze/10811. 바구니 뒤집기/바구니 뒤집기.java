import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i<n; i++){
            arr[i] = i+1;
        }
        for (int i = 0; i<m; i++){
            int left = sc.nextInt()-1;
            int right = sc.nextInt()-1;

            while(left<right){
                int temp = arr[left] ;
                arr[left++] = arr[right];
                arr[right--] = temp;
            }
        }
        sc.close();

        for (int a: arr){
            System.out.print(a + " ");
        }


    }
}
