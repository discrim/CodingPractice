#include <stdio.h>
#include <stdlib.h>	// atoi()

int tribonacci(int n);
int iterTribo(int n);

int main(int argc, char *argv[])
{
    printf("Tribonacci Number\n");
	int x = atoi(argv[1]);

    for (int ii = 0; ii <= x; ii++)
        printf("Input %d -> Output %d\n", ii, iterTribo(ii));
}

int tribonacci(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1 || n == 2)
        return 1;
    else
        return tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1);
}

int iterTribo(int n)
{
    int arr[n + 1];
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 1;
	for (int ii = 3; ii <= n; ii++)
		arr[ii] = arr[ii - 3] + arr[ii - 2] + arr[ii - 1];
    return arr[n];
}
