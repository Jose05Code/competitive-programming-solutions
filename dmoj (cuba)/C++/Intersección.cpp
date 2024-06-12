#include <iostream>
#include <map> // for map

using namespace std;

// Function to read numbers and count their occurrences
int commonCharacters(const string& str1, const string& str2) {
    // map to store the frequency of each character of `str1`
    map<char, int> freq;
    for (char c : str1) {
        freq[c]++;
    }

    int common = 0; // number of common characters

    // iterate over the second string
    for (char c : str2) {
        if (freq[c] > 0) {
            common++;
            freq[c]--;
        }
    }

    return common;
}

// main function
int main() {
    string str1, str2; // input strings
    cin >> str1 >> str2; // read strings
    cout << commonCharacters(str1, str2) << endl; // print result
    return 0;
}