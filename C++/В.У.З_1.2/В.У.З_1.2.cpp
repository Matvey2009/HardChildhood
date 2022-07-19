#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int n, s;
	cout << "Введите n" << endl;
	cin >> n;
	s = 1;
	for (int i = 1; i < n+1; i++) {
		s *= i;
	}
	cout << s;

	system("pause>nul");
	return 0;
}