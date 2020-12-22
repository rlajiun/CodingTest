#include <iostream>

using namespace std;

int main() {
	int n = 0, k = 0;
	int a[10] = { 0 };
	int result = 0;

	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}

	for (int i = 1; i <= n; i++)
	{
		result += k / a[n - i];
		k %= a[n - i];
	}

	cout << result;
	return 0;
}
