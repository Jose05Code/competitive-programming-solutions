#include <iostream>
#include <map> // for map

using namespace std;

// Function to read numbers and count their occurrences
map<int, int> readNumbers(int count) {
    map<int, int> compuestos;
    for(int i = 0; i < count; i++){
        int input;
        cin >> input;
        compuestos[input]++;
    }
    return compuestos;
}

// Function to find the maximum value in a map
int findMaxValue(const map<int, int>& compuestos) {
    int maxValue = 0;
    for(const auto& pair : compuestos) {
        if(pair.second > maxValue) {
            maxValue = pair.second;
        }
    }
    return maxValue;
}

int main(){
    map<int, int> compuestos = readNumbers(3);
    int maxValue = findMaxValue(compuestos);
    cout << maxValue << endl;
}