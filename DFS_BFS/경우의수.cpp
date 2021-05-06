/* N개의 자연수로 구성된 집합이 주어졌을 때
'+', '-' 연산을 사용하여 자연수인 M을 만드는 경우의 수
(존재하지 않으면 -1 출력) */

#include <iostream>
using namespace std;

int n, m, num[1000], ck[1000], cnt;

void DFS(int level, int sum) {
	if (level > n) {
		if (sum == m) {
			int flag = 0;
			cnt++;
			for (int i = 1; i <= n; i++) {
				switch (ck[i])
				{
				case 1:
					if (flag == 0) flag = 1;
					else cout << "+";
					cout << num[i];
					break;
				case 0:
					if (flag == 0) flag = 1;
					cout << "-" << num[i];
					break;
				case -1:
					break;
				}
			}
			cout << "=" << m << endl;
		}
	}
	else {
		ck[level] = 1;
		DFS(level + 1, sum + num[level]);
		ck[level] = 0;
		DFS(level + 1, sum - num[level]);
		ck[level] = -1;
		DFS(level + 1, sum);
	}
}

int main() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
	{
		cin >> num[i];
	}

	DFS(1, 0);
	if (cnt == 0) cout << -1;
	else cout << cnt;

	return 0;
}
