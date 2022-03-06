#include<iostream>

using namespace std;

int arrayAdd(int* array, int num);

void in_out();

void pointer();

int main()
{
	//int data[] = { 0,1,2,9,4,6 };
	//int size = sizeof(data) / sizeof(data[0]);
	//int sum = arrayadd(data, size);
	//cout << "the sum of array number is " << sum << endl;

	//in_out();

	pointer();

	return 0;
}

int arrayAdd(int* array, int num) {
	
	int sum = 0;
	for (int i = 0; i < num; i++) {
		sum += *(array + i);
		cout << "array's address is : " << *(array + i) << endl;

	}
	return sum;
}

void in_out() {
	const int allworld = 100;
	const char* lex = "abcdefg"; //字符串是一个常量
	char c = 'a';
	char cc[] = "acc";
	cc[1]= 'b';
	cout << lex << endl << c << endl << *&cc << endl;

}

void pointer() {
	void* pc = 0;
	int i = 1000;
	char c = 'w';
	char cc[5] = "abcd";
	const char* d = "h";
	pc = &i;
	cout << pc << endl << *(int*)pc << endl;
	pc = &c;
	cout << pc << endl << *(char*)pc << endl;
	pc = &cc;
	cout << pc << endl << *(char*)pc << endl;

//	??pc = d;
//	cout << pc << endl << d << endl << *(char*)pc << endl;
}