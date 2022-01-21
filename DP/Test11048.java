package silver1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Test11048 {
	public static class Point {
		int x, y;

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	static int N, M;
	static int[][] map, dp;
	static int[][] delta = { { 1, 0 }, { 0, 1 }, { 1, 1 } };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		dp = new int[N][M];
		for (int i = 0; i < map.length; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < map[i].length; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		} // input end
		dp[0][0] = map[0][0];

		Queue<Point> queue = new LinkedList<>();
		boolean[][] visited = new boolean[N][M];
		queue.offer(new Point(0, 0));
		visited[0][0] = true;

		while (!queue.isEmpty()) {
			Point p = queue.poll();

			for (int d = 0; d < delta.length; d++) {
				int nextx = p.x + delta[d][0];
				int nexty = p.y + delta[d][1];

				if (nextx < 0 || nextx >= N || nexty < 0 || nexty >= M)
					continue;
				if(visited[nextx][nexty] && dp[nextx][nexty] == dp[p.x][p.y] + map[nextx][nexty])
					continue;
				
				if (dp[nextx][nexty] <= dp[p.x][p.y] + map[nextx][nexty]) {
					dp[nextx][nexty] = dp[p.x][p.y] + map[nextx][nexty];
					queue.offer(new Point(nextx, nexty));
					visited[nextx][nexty] = true;
				}
			}
		}
		System.out.println(dp[N - 1][M - 1]);
	}

}
