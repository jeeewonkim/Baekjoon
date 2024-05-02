import java.io.*;
import java.util.*;


public class Main {
    public static class Node implements Comparable<Node> {
        int end;
        int weight;

        public Node(int end, int weight) {
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node o1) {
            return weight - o1.weight;
        }

    }

    static int n, m;
    static List<Node>[] graph;
    static boolean[] visited;
    static int[] distance;
    static int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        distance = new int[n + 1];
        visited = new boolean[n + 1];
        Arrays.fill(distance, INF);
        graph = new List[n + 1];
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b, w));
        }
        st = new StringTokenizer(br.readLine());

        int start = Integer.parseInt(st.nextToken());
        int land = Integer.parseInt(st.nextToken());
        dik(start);
        System.out.println(distance[land]);
    }

    public static void dik(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        visited = new boolean[n + 1];
        distance[start] = 0;
        pq.add(new Node(start, 0));
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int now = node.end;
            if (visited[now]) continue;
            visited[now] = true;

            for (Node n : graph[now]) {
                if (distance[now] + n.weight < distance[n.end]) {
                    distance[n.end] = distance[now] + n.weight;
                    pq.add(new Node(n.end, distance[n.end]));
                }
            }

        }

    }
}