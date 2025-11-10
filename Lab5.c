#include <stdio.h>
#include <stdlib.h>

#define NumRow 5  
#define NumCol 10  

int main(void)
{
    int InputArray[NumRow][NumCol];
    int i, j;

    printf("Початковий масив:\n");
    for (i = 0; i < NumRow; i++)
    {
        for (j = 0; j < NumCol; j++)
        {
            InputArray[i][j] = rand() % 10;
            printf("%3i", InputArray[i][j]);
        }
        printf("\n");
    }

    printf("\n");
    printf("Сума елементів у кожному стовпці:\n");
    for (j = 0; j < NumCol; j++)
    {
        int sum = 0;
        for (i = 0; i < NumRow; i++)
        {
            sum += InputArray[i][j];
        }
        printf("Стовпець %d: %d\n", j, sum);
    }

    printf("\n");
    for (j = 0; j < NumCol; j++)
    {
        for (int pass = 0; pass < NumRow - 1; pass++)
        {
            for (i = 0; i < NumRow - pass - 1; i++)
            {
                if (j % 2 == 0)
                {
                    if (InputArray[i][j] > InputArray[i + 1][j])
                    {
                        int temp = InputArray[i][j];
                        InputArray[i][j] = InputArray[i + 1][j];
                        InputArray[i + 1][j] = temp;
                    }
                }
                else
                {
                    if (InputArray[i][j] < InputArray[i + 1][j])
                    {
                        int temp = InputArray[i][j];
                        InputArray[i][j] = InputArray[i + 1][j];
                        InputArray[i + 1][j] = temp;
                    }
                }
            }
        }
    }
    printf("Відсортований масив:\n");
    for (i = 0; i < NumRow; i++)
    {
        for (j = 0; j < NumCol; j++)
        {
            printf("%3i", InputArray[i][j]);
        }
        printf("\n");
    }

    return 0;
}