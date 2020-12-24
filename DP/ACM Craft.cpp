#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int t; // 테스트케이스의 개수
	cin >> t;
	vector<int> res(t, 0);
	int n, k, w; // 건물의 개수, 건물간의 건설순서규칙의 총 개수, 건설해야 할 건물 번호
	for (int i = 0; i < t; i++) // 테스트케이스 개수 만큼 반복
	{
		cin >> n >> k;
		vector<int> d(n + 1, 0); // 각 건물당 건설에 걸리는 시간
		vector<vector<int> > map(n + 1 , vector<int>(n + 1, 0)); // 건설 순서
		vector<int> degree(n + 1, 0); // 진입 차수
		vector<int> time(n + 1, 0); // 각 건물까지 걸리는 시간
		queue<int> q;
		for (int j = 1; j <= n; j++)
		{
			cin >> d[j];
		}
		for (int j = 0; j < k; j++)
		{
			int a, b;
			cin >> a >> b;
			map[a][b] = 1;
			degree[b]++;
		}
		cin >> w;

		for (int j = 1; j <= n; j++)
		{
			if (degree[j] == 0) q.push(j);
		}

		// 위상정렬 알고리즘
		int now = 0;
		while (!q.empty() && now != w) {
			now = q.front();
			q.pop();
			int maxT = 0;
			for (int j = 1; j <= n; j++)
			{
				if (map[j][now] == 1) maxT = max(maxT, time[j]);
				time[now] = maxT + d[now];
				if (map[now][j] == 1) {
					degree[j]--;
					if (degree[j] == 0) q.push(j);
				}
			}
		}
		res[i] = time[w];
	}
	for (int i = 0; i < t; i++)
	{
		cout << res[i] << endl;
	}

	return 0;
}
