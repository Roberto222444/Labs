#include <stdio.h>

// Функція для обчислення факторіала (рекурсивна)
int factorial(int n) {
    if (n == 0) {
        // Базовий випадок: 0! = 1
        return 1;
    } else {
        // Рекурсивний виклик
        return n * factorial(n - 1);
    }
}

int main() {
    int number;

    // Введення числа користувачем
    printf("Введіть ціле число: ");
    scanf("%d", &number);

    // Перевірка, щоб число не було від’ємним
    if (number < 0) {
        printf("Факторіал від’ємного числа не визначено!\n");
    } else {
        int result = factorial(number);
        printf("Факторіал числа %d дорівнює %d\n", number, result);
    }

    return 0;
}