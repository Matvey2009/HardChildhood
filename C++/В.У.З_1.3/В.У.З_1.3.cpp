#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int n, i;
	string s;
	cout << "Введите число" << endl;
	cin >> n;
	s = "Простое";
	if (n < 2 || n > 10000000000)
		cout << "Введины не коректные данные";
	else {
		for (i = 2; i < n - 1; i++) {
			if (n % i == 0) {
				s = "Составное";
				break;
			}
		}
		cout << "Ответ: " << s;
	}

	system("pause>nul");
	return 0;
}