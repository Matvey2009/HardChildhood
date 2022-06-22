#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");

	double num1, num2;
	char word;

	cout << "Введите пример" << endl;
	cin >> num1 >> word >> num2;

	if (word == '-')
		cout << num1 - num2;
	else if (word == '+')
		cout << num1 + num2;
	else if (word == '*')
		cout << num1 * num2;
	else if (word == '/')
		cout << num1 / num2;
	else
		cout << "Введён не правильный матиматический знак" << endl;

	system("pause>nul");
	return 0;
}