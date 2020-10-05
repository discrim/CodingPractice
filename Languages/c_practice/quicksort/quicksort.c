#include <stdio.h>

void swap(int* x, int* y){
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

int partition(int n, int* ar, int pivot) {
	
    swap(&ar[pivot], &ar[n - 1]);
	
    int less = -1;
    for (int ii = 0; ii < n - 1; ii++) {
        if (ar[ii] < ar[n - 1]) {
            less++;
            swap(&ar[less], &ar[ii]);
        }
    }
	less++;
    swap(&ar[n - 1], &ar[less]);
    return less;
}

void quicksort(int n, int* ar)
{
    int pivot, rr;
    if (n > 1) {
        pivot = 0;
        rr = partition(n, ar, pivot);
        quicksort(rr, ar);
		quicksort(n - rr - 1, &ar[rr]);
    }
}

int main(void) {
	int ar[] = {5, 1, 6, 4, 2, 3};
	int *pp = ar;
	int len = sizeof(ar) / sizeof(int);
	quicksort(len, pp);
	
	for (int jj = 0; jj < len; jj++) {
		printf("%d ", ar[jj]);
	}
	printf("\n");
	
	return 0;
}