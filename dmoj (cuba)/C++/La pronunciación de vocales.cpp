#include <iostream>
using namespace std;
int main(){
    string n; 
    cin >> n; // lee el string
    
    int orgullosa_maxima = 0; // maxima cantidad de vocales orgullosas
    int orgullosa = 0; // cantidad de vocales orgullosas en el momento

    for(int i=0; n.size()>i; i++){ // recorre el string
        if(n[i]=='a' || n[i]=='e' || n[i]=='i' || n[i]=='o' || n[i]=='u'){
            orgullosa++; // si es vocal orgullosa, aumenta el contador
            orgullosa_maxima = max(orgullosa_maxima, orgullosa); // actualiza el maximo
        }
        else
            orgullosa = 0; // si no es vocal orgullosa, reinicia el contador
        
    }

    cout << orgullosa_maxima << endl;

}