#include <iostream>

using namespace std;
/*这是注释
char 1
unsigned char 1
signed char 1
int 4
unsigned int 4
signed int 4
short int 2
unsigned short int 2
long int 8
signed long int 8
unsigned long int 8
float  4
double 8 
long double 16
wchar_t 2 or 4

*/
class Box
{
	public:
		double length;
		double breadth;
		double height;
};
int main()
{
	Box box1;
	double volume = 0;
	box1.length = 5;
	box1.breadth = 2;
	box1.height = 3;
	volume = box1.height*box1.breadth*box1.length;
	cout <<"box1"<<endl;
	return 0;
}