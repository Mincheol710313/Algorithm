#include <iostream>
using namespace std;

int arr[26]; 

int main() {
    // Source Code
    string s; cin >> s;
    for(char& c : s){
        arr[c - 'a']++;
    }

    for(int& i : arr){
        cout << i << " ";
    }
    
    return 0;
}