import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main{
    static int m,n,k; //가로길이,세로길이,위치개수
    static int [][] field;
    static Queue<int[] > q = new LinkedList<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int t =0 ; t<T; t++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken()); // 가로길이
            n = Integer.parseInt(st.nextToken()); // 세로길이
            k = Integer.parseInt(st.nextToken()); // 개수
            field = new int[n][m];
            for(int i =0 ; i< k ; i++){
                StringTokenizer str = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(str.nextToken());//x좌표
                int b = Integer.parseInt(str.nextToken());//y좌표
                field[b][a] = 1;
            }
            int count = 0;
            for(int x =0 ; x<n; x++){
                for(int y =0 ; y<m ;  y++){
                    if(field[x][y] == 1){
                        bfs(x,y);
                        count ++;
                    }
                }
            }
            System.out.println(count);
        }
    }
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};

    public static void bfs(int x, int y){
        q.add(new int[] {x,y});

        field[x][y] = 0;
        while(!q.isEmpty()){
            int []c = q.poll();
            for(int i = 0 ; i<4 ; i++){
                int nx = c[0]+dx[i];
                int ny = c[1]+dy[i];
                if(0<=nx && nx<n && 0<=ny && ny<m){
                    if(field[nx][ny] == 1){
                        field[nx][ny] = 0;
                        q.add(new int[] {nx,ny});
                    }
                }
            }
        }
    }
}
