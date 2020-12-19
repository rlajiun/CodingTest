import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = Integer.parseInt(scan.nextLine()); // 테스트 케이스의 수
		int[] n_array = new int[10];
		int[] dp = new int[10];

		for (int i = 0; i < t; i++) {
			n_array[i] = Integer.parseInt(scan.nextLine());
		}

		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 4;

		for (int i = 0; i < t; i++) {
			for (int j = 4; j <= n_array[i]; j++) {
				if (dp[j] == 0) {
					dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
				}
			}
		}

		for (int j = 0; j < t; j++) {
			System.out.println(dp[n_array[j]]);
		}

	}

}
