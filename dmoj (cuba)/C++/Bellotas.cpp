#include <iostream>
#include <vector>

int main() {
    int rep;
    std::cin >> rep;

    std::vector<int> arreglo(rep);
    for (int i = 0; i < rep; i++) {
        std::cin >> arreglo[i];
    }

    int resultado = 0;
    for (int i = 0; i < rep; i++) {
        if (arreglo[i] > 10) {
            resultado += arreglo[i] - 10;
        }
    }

    std::cout << resultado << std::endl;

    return 0;
}