package silver2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Test11060 {
	static int N;
	static int[] map, dp;
	static final int MAX = 1000;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N];
		dp = new int[N];
		Arrays.fill(dp, MAX);
		dp[0] = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < map.length; i++) {
			map[i] = Integer.parseInt(st.nextToken());
		} // input end

		// dp[i] : i번째까지 갈 수 있는 최소 점프 수
		for (int i = 0; i < map.length; i++) {
			int idx = i + map[i];
			for (int j = i; j < dp.length && j <= idx; j++) {
				dp[j] = Math.min(dp[j], dp[i] + 1);
			}
			if (idx >= dp.length) {
				dp[dp.length - 1] = Math.min(dp[dp.length - 1], dp[i] + 1);
			}

		}

		System.out.println(dp[dp.length - 1] == MAX ? -1 : dp[dp.length - 1]);
	}

}
