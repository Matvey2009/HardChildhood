#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");

	int h1, h2, m1, m2, t;
	char l;
label:
	cout << "Введите чаcы а затем минуты первого человека через ':'" << endl;
	cin >> h1 >> l >> m1;
	cout << "Введите чаcы а затем минуты второго человека через ':'" << endl;
	cin >> h2 >> l >> m2;
	if (h1 > 23 || h2 > 23 || m1 > 59 || m2 > 59 || h1 < 0 || h2 < 0 || m1 < 0 || m2 < 0)
	{
		cout << ("Данные не корректные") << endl;
		system("pause>nul");
		return 0;
	}
	
	t = abs((m1 + h1 * 60) - (m2 + h2 * 60));
	if (t < 15 || t > 1425)
		cout << ("Встреча состоится") << endl;
	else
		cout << ("Встреча не состоится") << endl;

	goto label;
	system("pause>nul");
	return 0;
}