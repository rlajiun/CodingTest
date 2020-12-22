#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a[1000] = { 0 };
	int dp[1000] = { 0 };
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	dp[0] = 1;
	for (int i = 1; i < n; i++)
	{
		int maxLen = 0;
		for (int j = 0; j < i; j++)
		{
			if (a[j] < a[i])
			{
				maxLen = max(maxLen, dp[j]);
			}
		}
		dp[i] = maxLen + 1;
	}

	int result = 0;

	for (int i = 0; i < n; i++)
	{
		result = max(result, dp[i]);
	}
	cout << result;

	return 0;
}
