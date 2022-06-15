#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");

	double x0, v0, t;
	cout << "Ведите число 'x0'" <<  endl;
	cin >> x0;
	cout << "Ведите число 'v0'" << endl;
	cin >> v0;
	cout << "Ведите число 't'" << endl;
	cin >> t;
	cout << endl << "x(t) = " << x0 + v0 * t - (9.8 * (t * t) / 2);
	
	system("pause>nul");
	return 0;
}