#include <stdio.h>

int main() {
    int a, b, sum;

    printf("Введіть два числа: ");
    scanf("%d %d", &a, &b);

    sum = a + b;

    printf("Сума = %d\n", sum);

    return 0;
}