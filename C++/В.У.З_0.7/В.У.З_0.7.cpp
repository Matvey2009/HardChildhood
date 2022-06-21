#include <iostream>

using namespace std;

int main() {
	setlocale(LC_ALL, "RUS");

	int vib;
	cout << "Выберите каким вариантов вы хотите высчитать площадь треугольника" << endl;
	cout << "1 - Через длины" << endl;
	cout << "2 - Через Вершины" << endl;
	cin >> vib;
	if (vib == 1) {
		double a, b, c, p, S;
		cout << "Введите стороны треугольника" << endl;
		cin >> a;
		cin >> b;
		cin >> c;
		p = (a + b + c) / 2;
		S = sqrt(p*(p-a)*(p-b)*(p-c));
		if (S > 0)
			cout << "S = " << S;
		else
			cout << "Ошибочный ввод";
	}
	else if (vib == 2) {
		double Ax, Ay, Bx, By, Cx, Cy, S;
		cout << "Введите коордитаны вершин треугольника" << endl;
		cin >> Ax >> Ay;
		cin >> Bx >> By;
		cin >> Cx >> Cy;
		S = abs(((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay)) / 2);
		if (S > 0)
			cout << "S = " << S;
		else
			cout << "Ошибочный ввод";
	}
	else 
		cout << "Ошибочный ввод";


	

	system("pause>nul");
	return 0;
}