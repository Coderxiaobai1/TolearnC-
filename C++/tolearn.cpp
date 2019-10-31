#include<iostream>
using namespace std;
class Box
{
    public:
        double length;
        double breadth;
        double height;
    
        double getvolume(void);
        void setlength(double len);
        void setbreadth(double bred);
        void setheight(double hei);
};
void Box::setlength(double len)
{
    length = len;

}
double Box::getvolume(void)
{
    return length*breadth*height;
}
void Box::setbreadth(double bred)
{
    breadth = bred;
}
void Box::setheight(double hei)
{
    height = hei;

}
int main()
{
    Box box1;
    double volume = 1.0;
    box1.setbreadth(1.0);
    box1.setlength(2.0);
    box1.setheight(3.0);
    volume = box1.getvolume();
    cout <<"volume is:"<< volume <<endl;
    return 0;
}