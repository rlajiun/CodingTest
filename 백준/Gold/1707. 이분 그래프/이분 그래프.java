import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static class Node {
		int vertex;
		Node link;

		public Node(int vertex, Node link) {
			this.vertex = vertex;
			this.link = link;
		}
	}

	static String answer;
	static boolean[] visited, check;
	static Node[] list;
	static Queue<Integer> queue;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int V = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			list = new Node[V + 1];
			for (int e = 0; e < E; e++) {
				st = new StringTokenizer(br.readLine());
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());
				list[from] = new Node(to, list[from]);
				list[to] = new Node(from, list[to]);
			} // input end
			visited = new boolean[V + 1];
			check = new boolean[V + 1];
			queue = new LinkedList<>();
			answer = "YES";
					
			for (int i = 1; i < visited.length; i++) {
				if (!visited[i]) {
					queue.offer(i);
					visited[i] = true;
					DFS();
				}
			}

			System.out.println(answer);
		} // TC end
	}

	private static void DFS() {
		while (!queue.isEmpty()) {
			int pre = queue.poll();
			Node node = list[pre];

			while (node != null) {
				int to = node.vertex;
				node = node.link;

				if (visited[to]) {
					if (check[to] != check[pre]) {
						continue;
					} else {
						answer = "NO";
						return;
					}
				}
				queue.offer(to);
				visited[to] = true;
				check[to] = !check[pre];
			}
		}
	}

}