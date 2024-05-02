import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
            //this.count = count;
        }
    }

    static int n, m;
    static int[][] graph;
    static int[][] copyGraph;
    static Queue<Point> q;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int maxSafeZone = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0);
        System.out.println(maxSafeZone);
    }

    static void dfs(int wall) {
        if (wall == 3) {
            bfs();
            return;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 0) {
                    graph[i][j] = 1;
                    dfs(wall + 1);
                    graph[i][j] = 0;
                }
            }
        }

    }

    static void bfs() {
        q = new LinkedList<>();
        copyGraph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (graph[i][j] == 2) {
                    q.add(new Point(i, j));
                }
            }
        }
        for(int i =0 ; i< n; i++){
            copyGraph[i] = graph[i].clone();
        }
        while (!q.isEmpty()) {
            Point point = q.poll();
            int x = point.x;
            int y = point.y;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (copyGraph[nx][ny] == 0) {
                        q.add(new Point(nx, ny));
                        copyGraph[nx][ny] = 2;
                    }

                }
            }
        }

        findSafe(copyGraph);
    }

    static void findSafe(int[][] copyGraph){
        int safeZone = 0;
        for(int i =0 ; i<n; i++){
            for(int j = 0 ; j < m ; j++){
                if(copyGraph[i][j] == 0){
                    safeZone ++;
                }
            }
        }
        if(maxSafeZone < safeZone){
            maxSafeZone = safeZone;
        }
    }
}