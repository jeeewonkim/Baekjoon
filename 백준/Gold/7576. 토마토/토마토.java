import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int m, n; //가로길이,세로길이,위치개수
    static int[][] graph;
    //static boolean [][] visited;
    static Queue<Tomato> q = new LinkedList<>();

    static class Tomato {
        int x;
        int y;
        int day;

        public Tomato(int x, int y, int day) {
            this.x = x;
            this.y = y;
            this.day = day;

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        //visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1) {
                    q.offer(new Tomato(i, j, 0));
                }
            }
        }
        bfs();
    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void bfs() {
        int day = 0;

        while (!q.isEmpty()) {
            Tomato t = q.poll();
            day = t.day;

            for (int i = 0; i < 4; i++) {
                int nx = t.x + dx[i];
                int ny = t.y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (graph[nx][ny] == 0) {
                        graph[nx][ny] = 1;
                        q.add(new Tomato(nx, ny, day + 1));
                    }
                }
            }
        }
        if (checkTomato()){
            System.out.println(day);
        }
        else{
            System.out.println(-1);
        }

    }
    static boolean checkTomato(){
        for(int i =0 ; i<n ; i++){
            for(int j = 0 ; j < m ; j++){
                if (graph[i][j] == 0) return false;
            }
        }
        return true;
    }
}