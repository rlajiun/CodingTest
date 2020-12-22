#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, a[1000] = { 0 }, dp[1000] = { 0 };
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	dp[0] = a[0];
	for (int i = 0; i < n; i++)
	{
		int maxSum = 0;
		for (int j = 0; j < i; j++)
		{
			if (a[j] < a[i])
			{
				maxSum = max(maxSum, dp[j]);
			}
		}
		dp[i] = maxSum + a[i];
	}

	int result = 0;
	for (int i = 0; i < n; i++)
	{
		result = max(result, dp[i]);
	}

	cout << result;

	return 0;
}
