#include <iostream>
#include <cmath>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int n, s, j;
	j = 1;
	s = 0;
	cout << "Задайте число" << endl;
	cin >> n;
	if (n < 0 || n == 10000000000000000)
		cout << "Введите корректные данные";
	else
	{
		while (n >= j) {
			j *= 2;
			s++;
		}
		cout << s;
	}
	system("pause>nul");
	return 0;
}