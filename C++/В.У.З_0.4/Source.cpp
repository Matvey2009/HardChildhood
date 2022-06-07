#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");

	int a, b, c;
	
	cout << ("¬ведите число A: ");
	cin >> a;
	cout << ("¬ведите число B: ");
	cin >> b;

	c = a;
	a = b;
	b = c;
	cout << ("ќбмен с дополнительной переменной") << endl;
	cout << "A: " << a << endl;
	cout << "B: " << b << endl;

	a ^= b ^= a ^= b;
	cout << ("ќбмен без дополнительной переменной") << endl;
	cout << "A: " << a << endl;
	cout << "B: " << b << endl;
	

	system("pause>nul");
	return 0;
}