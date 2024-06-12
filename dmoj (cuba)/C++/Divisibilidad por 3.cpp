#include <iostream>
using namespace std;

struct Numbers {
    int number1;
    int number2;
    int number3;

    void sortNumbers() {
        if (number1 > number2) {
            swap(number1, number2);
        }
        if (number2 > number3) {
            swap(number2, number3);
        }
        if (number1 > number2) {
            swap(number1, number2);
        }
    }
};

bool isDivisibleBy3(int number) {
    return number % 3 == 0;
}

int numberResult(const Numbers& input) {
    if(isDivisibleBy3(input.number1)){
        return input.number1;
    } else
    if(isDivisibleBy3(input.number2)){
        return input.number2;
    } else
    if(isDivisibleBy3(input.number3)){
        return input.number3;
    } else 
        if(isDivisibleBy3(input.number1 + input.number1)){
        return input.number1 + input.number1*10;
    } else
        if(isDivisibleBy3(input.number2 + input.number1)){
        return input.number2 + input.number1*10;
    } else
        if(isDivisibleBy3(input.number3 + input.number1)){
        return input.number3 + input.number1*10;
    } else
        if(isDivisibleBy3(input.number3 + input.number2)){
        return input.number3 + input.number2*10;
        } 
    return input.number1 + input.number1*10 + input.number1*100;
}

int main() {
    Numbers input;
    cin >> input.number1 >> input.number2 >> input.number3;

    input.sortNumbers();

    cout << numberResult(input);

    return 0;
}