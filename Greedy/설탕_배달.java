import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = Integer.parseInt(scan.next());
		int cnt = 0;

		while (N >= 0) {
			if (N % 5 == 0) {
				System.out.printf("%d", N / 5 + cnt);
				return;
			}
			N -= 3;
			cnt++;
		}
		System.out.println("-1");
		return;
	}

}
