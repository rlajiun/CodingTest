#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int n = 0, result = 0;
	int p[1000] = { 0 };
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> p[i];
	}
	sort(p, p + n);

	for (int i = 0; i < n; i++)
	{
		result += p[i] * (n - i);
	}

	cout << result;
	return 0;
}
