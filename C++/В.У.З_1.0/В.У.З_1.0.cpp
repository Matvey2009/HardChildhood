#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int s, l1, r1, l2, r2, x1, x2;
	cout << ("Введите 5 чисел") << endl;
	cin >> s >> l1 >> r1 >> l2 >> r2;

	if (abs(s) >= 1e15 || abs(l1) >= 1e15 || abs(r1) >= 1e15 || abs(l2) >= 1e15 || abs(r2) >= 1e15 || l1 >= r1 || l2 >= r2)
		cout << "Некорректный ввод" << endl;
	else
	{
		if (l1 + l2 > s || r1 + r2 < s)
			cout << -1;
		else
		{
			if (s-l1 < r2)
			{
				x1 = l1;
				x2 = s - x1;
			}
			else
			{
				x2 = r2;
				x1 = s - r2;
			}
		}
		cout << x1 << " " << x2 << endl;
	}
	system("pause>nul");
	return 0;
}