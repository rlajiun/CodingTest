package sliver2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Test11055 {
	static int N;
	static int[] array, dp;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		array = new int[N + 1];
		dp = new int[N + 1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i < array.length; i++) {
			array[i] = Integer.parseInt(st.nextToken());
		} // input end

		int answer = 0;

		for (int i = 0; i < array.length; i++) {
			for (int j = i + 1; j < array.length; j++) {
				if (array[i] < array[j]) {
					dp[j] = Math.max(dp[j], dp[i] + array[j]);
					answer = Math.max(answer, dp[j]);
				}
			}
		}

		System.out.println(answer);
	}

}
