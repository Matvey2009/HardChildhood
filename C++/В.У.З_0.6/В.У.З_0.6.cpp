#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");

	double a, b, c, de;
	cout << "Ведите число 'a'" << endl;
	cin >> a;
	cout << "Ведите число 'b'" << endl;
	cin >> b;
	cout << "Ведите число 'c'" << endl;
	cin >> c;

	de = b * b - 4 * a * c;
	if (a == 0)
		cout << "Ответ: " << -c / b << endl;
	else if (de == 0)
		cout << "Ответ: " << -b / (2*a) << endl;
	else if (de > 0) 
	{
		cout << "Ответ один: " << (-b + sqrt(de)) / (2 * a) << endl;
		cout << "Ответ два: " << (-b - sqrt(de)) / (2 * a) << endl;
	}
	else
		cout << "Корней нет";
	
	system("pause>nul");
	return 0;
}