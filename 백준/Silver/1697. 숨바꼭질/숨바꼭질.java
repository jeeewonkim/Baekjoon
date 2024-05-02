import java.io.*;
import java.util.*;


public class Main {
    static boolean[] visited;
    static int s;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        s = n < m ? m : n;
        visited = new boolean[s + 2];
        dist = new int[s + 2];
        bfs(n);
        System.out.println(dist[m]);
    }

    static void bfs(int n) {
        Queue<Integer> q = new LinkedList<>();
        visited[n] = true;
        q.add(n);
        while (!q.isEmpty()) {
            int now = q.poll();

            if (0<= now-1 &&now - 1 <= s+1  && !visited[now - 1]) {
                visited[now - 1] = true;
                dist[now - 1] = dist[now] + 1;
                q.add(now - 1);
            }
            if (now + 1 <= s+1 && !visited[now + 1]) {
                q.add(now + 1);
                dist[now + 1] = dist[now] + 1;
                visited[now + 1] = true;
            }
            if (now * 2 <= s+1  && !visited[now * 2]) {
                q.add(now * 2);
                dist[now *2] = dist[now] + 1;
                visited[now * 2] = true;
            }
        }
    }
}