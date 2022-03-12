import java.util.*;

class Solution {
	public class Coin implements Comparable<Coin> {
		int idx;
		double avg;

		public Coin(int idx, double avg) {
			this.idx = idx;
			this.avg = avg;
		}

		public int compareTo(Coin o) {
			return Double.compare(avg, o.avg);
		}

	}

	public int solution(int money, int[] costs) {
		int answer = 0;
		int[] unit = { 1, 5, 10, 50, 100, 500 };
		PriorityQueue<Coin> pq = new PriorityQueue<>();

		for (int i = 0; i < costs.length; i++) {
			pq.add(new Coin(i, costs[i] / (double) unit[i]));
		}
		
		while(!pq.isEmpty()) {
			Coin coin = pq.poll();
			int cnt = money / unit[coin.idx];
			money %= unit[coin.idx];
			
			answer += cnt * costs[coin.idx];
		}
		
		return answer;
	}
}
