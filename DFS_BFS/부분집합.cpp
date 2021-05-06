#include <iostream>
using namespace std;

int n, ch[1000];

void DFS(int level) {
	if (level > n)
	{
		for (int i = 1; i <= level; i++)
		{
			if (ch[i]==1)
			{
				cout << i;
			}
		}
		cout << "\n";
	}
	else
	{
		ch[level] = 1;
		DFS(level + 1);
		ch[level] = 0;
		DFS(level + 1);
	}
}

int main() {
	cin >> n;
	DFS(1);
	return 0;
}
