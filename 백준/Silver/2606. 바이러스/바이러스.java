import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static int n, m;
    static int[][] graph;
    static boolean[] visited;
    static Queue<Integer> q = new LinkedList<>();
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = graph[b][a] = 1;
        }

        bfs(1);
        System.out.println(count);
    }

    public static void bfs(int start) {
        visited[start] = true;
        q.add(start);
        while (!q.isEmpty()) {
            start = q.poll();
            for (int i = 1; i <= n; i++) {
                if (graph[start][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    count ++;
                    q.add(i);
                }
            }
        }
    }
}