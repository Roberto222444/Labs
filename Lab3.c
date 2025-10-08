#include <stdio.h>

int main() {
    float tC, tF;

    printf("Celsius\tFahrenheit\n");
    printf("---------------------\n");

    for (tC = -40; tC <= 120; tC += 10) {
        tF = (9.0 / 5.0) * tC + 32;
        printf("%.1f\t%.1f\n", tC, tF);
    }

    return 0;
}
