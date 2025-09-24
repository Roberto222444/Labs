#include <stdio.h>

int main() {
    printf("Розмір char: %zu байт\n", sizeof(char));
    printf("Розмір int: %zu байт\n", sizeof(int));
    printf("Розмір float: %zu байт\n", sizeof(float));
    printf("Розмір double: %zu байт\n", sizeof(double));
    printf("Розмір long: %zu байт\n", sizeof(long));
    printf("Розмір long long: %zu байт\n", sizeof(long long));
    return 0;
}