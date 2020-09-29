#include <stdio.h>
#include <stdlib.h> // malloc

typedef struct LinkedList {
    int value;
    int count;
    struct LinkedList *next;
} Node;
typedef Node *NodePtr;

// Complete the sockMerchant function below.
int sockMerchant(int n, int ar_count, int* ar) {
    Node *headptr, *currptr, *newptr;
    headptr = (NodePtr) malloc(sizeof(Node));
    headptr->value = ar[0];
    headptr->count = 0;
    headptr->next = NULL;    

	printf("Store distinct colors in a linked list...");
    // Store distinct colors in a linked list.
    for (int ii = 1; ii < n; ii++) {
        currptr = headptr;
        while (currptr != NULL) {
            if (ar[ii] == currptr->value)
                break;
            else {
                if (currptr->next == NULL) {
                    newptr = (NodePtr) malloc(sizeof(Node));
                    currptr->next = newptr;
                    newptr->value = ar[ii];
                    newptr->count = 0;
                    newptr->next = NULL;
                }
            }
            currptr = currptr->next;
        }
    }
	printf("Complete\n");
	
	currptr = headptr;
	while (currptr != NULL) {
		printf("%d ", currptr->value);
		currptr = currptr->next;
	}
	printf("\n");

	printf("Count frequencies of each color...\n");
    // Count frequency of each color.
    for (int ii = 0; ii < n; ii++) {
		printf("ii: %d, color in the list: ", ii);
        currptr = headptr;
        while (currptr != NULL) {
			printf("%d ", currptr->value);
            if (ar[ii] == currptr->value) {
                ++(currptr->count);
				break;
            }
			currptr = currptr->next;
        }
		printf("\n");
    }
	printf("Complete\n");

	printf("Count pairs...");
    // Count pairs out of counts.
    int pair = 0;
    currptr = headptr;
    while (currptr != NULL) {
        pair += currptr->count / 2;
		currptr = currptr->next;
    }
	printf("Complete\n");

    return pair;
}

int main(void) {
	int arr[] = {2, 5, 2, 3, 1, 5, 1, 1, 3, 2, 4, 1, 4, 3, 1, 4};
	int len = sizeof(arr) / sizeof(int);
	int pairs;
	
	pairs = sockMerchant(len, len, arr);
	printf("Number of pairs: %d\n", pairs);
	return 0;
}