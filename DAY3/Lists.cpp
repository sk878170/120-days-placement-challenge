// You can store multiple elements of same data type in a list.
// Lists are mutable and non-unique
// Include list package
#include<list>
#include<iostream>
using namespace std;

int main(){
    // To create a list use list keywords
    list<string> lang = {"Python", "Java", "C++", "php"};

    // Printing the elements using for loop

    for (string i:lang){
        cout << i << "\n" << endl;
    }

    // fet the first and last element of a list

    cout << lang.front() << endl;
    cout << lang.back() << endl;
    lang.front() = "php";
    lang.back() = "Python";

    for (string i:lang){
        cout << i << "\n" << endl;
    }

    // add elemenets in front or back
    lang.push_back("SQL");
    lang.push_front("R");

    for (string i:lang){
        cout << i << "\n" << endl;
    }

    cout << lang.size();

    if (lang.empty()){
        cout << "List is empty";
    }
}