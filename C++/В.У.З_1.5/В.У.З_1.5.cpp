#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");
	int n, r, i, o;
	i = 0;
	o = 1;
	srand(time(NULL));
	r = rand() % 100 + 1;


while (o == 1) {
	i = 0;
	n = 0;
	srand(time(NULL));
	r = rand() % 100 + 1;
	cout << "Введите своё число, что-бы попытаться угадать загадоное число" << endl;
	while (i < 5) {
		cin >> n;
		if (n < 0 or n > 100)
			cout << "Введены некорректные данные" << endl;
		i++;
		if (n == r) {
			cout << "Поздравляю! Вы угадали" << endl;
			cout << "Хотите начать сначала? (1 - ДА )" << endl;
			cin >> o;
			break;
		}
		else if (n > r)
			cout << "Загаданное число меньше" << endl;
		else
			cout << "Загаданное число больше" << endl;
		if (i == 5 && n != r) {
			cout << "Вы проиграли. Было загадано: " << r << endl;
			cout << "Хотите начать сначала? (1 - ДА )" << endl;
			cin >> o;
			break;
		}
		else if (n == r) {
			cout << "Поздравляю! Вы угадали" << endl;
			cout << "Хотите начать сначала? (1 - ДА )" << endl;
			cin >> o;
			break;
		}
	}
}
	
	system("pause>nul");
	return 0;
}