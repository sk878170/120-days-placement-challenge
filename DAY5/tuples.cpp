// Tuple is same as list, but it is immuatble, i.e. we cannot change the values of tuple once it is assigned.

#include <iostream>
#include <tuple>

using namespace std;

int main() {
    tuple<char, int, float> x1;

    x1 = make_tuple('A', 10, 15.5);
    cout << get<0>(x1) << " " << get<1>(x1) << " " << get<2>(x1) << endl;

    get<0>(x1) = 'B'; // This will give error as tuple is immutable

    cout << "The size of tuple is: ";
    cout << tuple_size<decltype(x1)>::value << endl;
}