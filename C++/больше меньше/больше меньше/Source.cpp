//игра Больше-меньше.
//Матвей Покидько 
//11.08.2018 Крым, Саки.
#include <iostream>
#include <ctime>
using namespace std;
void main()

{
	//START
	setlocale(LC_ALL, "RUS");
	srand(time(NULL));

start:
	int F,D=0;
	F = rand() % 1000 + 1;

	//ЗАПРАШУЕТ ЧИСЛО
	PADS:
	int Z;
	cin >> Z;
	D++;
	system("cls");
	//СРАВНЕНИЕ
	if (F == Z)
	{
		cout << "вы победили" << endl;
		cout << "Число попыток:" << D << endl;
		goto start;
	}

	if (F > Z)
	{
		cout << "число большe" << endl;
		cout << "Число попыток:" << D << endl;
		goto PADS;
	}

	if (F < Z)
	{
		cout << "число меньше " << endl;
		cout << "Число попыток: " << D << endl;
		goto PADS;
	}	
}