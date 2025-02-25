// The basic data types in C++ are int, float, char, bool and double
// We will initialise all of them

#include<iostream>
#include<string>
using namespace std;

int main(){
    int x = 4;
    cout << x <<"\n";

    float y = 3.14;
    cout << y <<"\n";

    char z = 'A';
    cout << z<<"\n";

    bool q = true;
    cout << q<<"\n";
    
    double d = 3.14159265358979323846;
    cout << d<<"\n";
    
    // NOTE: char represents ASCII values, hence it can store value of characters too
    
    char a = 65, b = 66, c = 67;
    cout << a << b << c<<"\n";

    string greet="Hello";
    cout << greet<<"\n";

    return 0;
}