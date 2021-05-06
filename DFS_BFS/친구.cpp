#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<vector<int>> ck(n + 1, vector<int>(n + 1, 0));
	vector<vector<int>> ck2(n + 1, vector<int>(n + 1, 0));
	cin.get();
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			char c;
			cin.get(c);
			if (c == 'Y') ck[i][j] = 1;
		}
		cin.get();
	}
	ck2 = ck;

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			if (ck[i][j] == 1) {
				for (int k = 1; k <= n; k++)
				{
					if (ck[j][k] == 1 && i != k) ck2[i][k] = 1;
				}
			}
		}
	}

	int maxCk = 0;
	for (int i = 1; i <= n; i++)
	{
		int cnt = 0;
		for (int j = 1; j <= n; j++)
		{
			if (ck2[i][j] == 1) cnt++;
		}
		maxCk = max(maxCk, cnt);
	}
	cout << maxCk;

	return 0;
}
