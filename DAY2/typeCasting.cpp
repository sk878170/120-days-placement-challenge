// we will learn about changing data types of a var
#include<iostream>
using namespace std;

int main(){
    int i = 10;
    char h = 'a';

    cout << int(h) << endl;

    int sum = i + h;
    cout << sum << endl;


    // Implicit type conversion : when the compiler automatically converts 
    
    float f = i + 1.2;
    cout << "f=" << f;
    
    i = i + h; // h is converted to int
    cout << "i=" << i;
    
    
    // Explicit type conversion : done by the user

    double x = 1.2;
    int sum = (int)x + 1;
    cout << "sum=" << sum;
}