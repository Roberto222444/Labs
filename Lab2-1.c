#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c, d, x1, x2;

    printf("Вeдiть a, b, c: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    d = b*b - 4*a*c;
    printf("Диcкpимiнaнт = %.2f\n", d);

    if (d > 0) {
        x1 = (-b + sqrt(d)) / (2*a);
        x2 = (-b - sqrt(d)) / (2*a);
        printf("x1 = %.2f , x2 = %.2f\n", x1, x2);
    } else if (d == 0) {
        x1 = -b / (2*a);
        printf("x = %.2f\n", x1);
    } else {
        printf("Дiйcниx кopeнiв немає\n");
    }

    return 0;
}