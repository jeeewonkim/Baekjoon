import java.util.*;
class Solution {
    static boolean[] visited;
    static int[] dist;
    static int INF = Integer.MAX_VALUE;
    static List<Node>[] graph;

    public static class Node implements Comparable<Node>{
        int end;
        int weight;
        public Node(int end, int weight){
            this.end = end;
            this.weight = weight;
        }
        @Override
        public int compareTo(Node n){
            return this.weight - n.weight;
        }
    }
    public int solution(int n, int[][] edge) {
        graph = new ArrayList[n+1];
        for(int i = 0 ; i<graph.length; i++){
            graph[i] = new ArrayList<>();
        }
        visited = new boolean[n+1];
        dist = new int[n+1];
        Arrays.fill(dist,INF);
        for(int i =0 ; i<edge.length;i++){
            graph[edge[i][0]].add(new Node(edge[i][1], 1));
            graph[edge[i][1]].add(new Node(edge[i][0], 1));
        }
        
        dik();
        int max_num = 0 ;
        int answer = 0;
        for(int i =1 ; i<n+1; i++){
            if(dist[i] > max_num){
                max_num = dist[i];
                answer = 1;
            }
            else if(dist[i] == max_num){
                answer++;
            }
        }
        return answer;
    }
    static void dik(){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1,0));
        dist[1] = 0;
        while(!pq.isEmpty()){
            Node now_node = pq.poll();
            int now = now_node.end;
            if(visited[now] == true) continue;
            visited[now] = true;
            for(Node n : graph[now]){
                if(dist[now]+n.weight < dist[n.end]){
                    dist[n.end] = dist[now]+n.weight;
                    pq.add(new Node(n.end, dist[n.end]));
                }
            }
        }
    }
}