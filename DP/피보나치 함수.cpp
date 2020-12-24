#include <iostream>
#include <vector>
using namespace std;

int zero[41], one[41];

void fibo(int num) {
	if (zero[num] != 0 || num == 1) return; // 값이 이미 있을때
	else {
		//값이 없으면 구해와야함
		fibo(num - 1);
		zero[num] = zero[num - 1] + zero[num - 2];
		one[num] = one[num - 1] + one[num - 2];
	}
}

int main() {
	int t;
	cin >> t;
	vector<int> n;
	for (int i = 0; i < t; i++)
	{
		int num;
		cin >> num;
		n.push_back(num);
	}

	zero[0] = 1;
	zero[1] = 0;
	one[0] = 0;
	one[1] = 1;

	for (int i = 0; i < n.size(); i++)
	{
		fibo(n[i]);
		cout << zero[n[i]] << " " << one[n[i]] << endl;
	}

	return 0;
}
