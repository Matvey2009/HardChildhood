#include<stdio.h>
#include<locale.h>

int main(void)
{
	setlocale(LC_ALL, "RUS");

	int x = 125;
	printf("Значение переменной %d\n", x);
	printf("Адрес в памяти %p\n", &x);
	int* p = &x;
	printf("Адрес указателя %p\n", p);
	printf("Значение по указателю %d\n", *p);
	p++;
	printf("Переход по памяти %p\n", p);
	printf("Мусорное значение %d\n", p);

	system("pause>nul");
	return 0;
}

