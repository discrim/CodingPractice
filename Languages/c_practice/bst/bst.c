#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE(arr) sizeof(arr) / sizeof(arr[0])

struct BSTNode;
typedef struct BSTNode *BST;

BST insert(int xx, BST TT);
void printPreorder(BST TT);
int sumBST(BST root);
int rangeSumBST(BST root, int L, int R);

struct BSTNode
{
	int val;
	struct BSTNode *left;
	struct BSTNode *right;
};

int main(void)
{
	BST T1 = NULL;
	int arr1[7] = {4, 2, 6, 7, 5, 3, 1};
	
	for (int ii = 0; ii < ARRAY_SIZE(arr1); ii++)
	{
		printf("Insert %d\n", arr1[ii]);
		T1 = insert(arr1[ii], T1);
	}
	
	printPreorder(T1);
	
	printf("sumBST(T1): %d\n", sumBST(T1));
	printf("rangeSumBST(T1, 2, 6): %d\n", rangeSumBST(T1, 2, 6));
	
	BST T2 = NULL;
	int arr2[6] = {10, 5, 15, 3, 7, 18};
	
	for (int ii = 0; ii < ARRAY_SIZE(arr2); ii++)
	{
		printf("Insert %d\n", arr2[ii]);
		T2 = insert(arr2[ii], T2);
	}
	printf("rangeSumBST(T2, 7, 15): %d\n", rangeSumBST(T2, 7, 15));
	
	return 0;
}

BST insert(int xx, BST TT)
{
	if (TT == NULL)
	{
		TT = malloc(sizeof(struct BSTNode));
		if (TT == NULL) printf("Out of space!");
		else
		{
			TT->val = xx;
			TT->left = TT->right = NULL;
		}
	}
	else if (xx < TT->val) TT->left = insert(xx, TT->left);
	else if (xx > TT->val) TT->right = insert(xx, TT->right);
	return TT;
}

void printPreorder(BST TT)
{
	printf("%d\n", TT->val);
	if (TT->left != NULL) printPreorder(TT->left);
	if (TT->right != NULL) printPreorder(TT->right);
}

int sumBST(BST root)
{
	if (root == NULL)
		return 0;
	else if (root->left == NULL && root->right == NULL)	// If leaf
		return root->val;
	return sumBST(root->left) + root->val + sumBST(root->right);
}

int rangeSumBST(BST root, int L, int R)
{
	if (root == NULL)
		return 0;
	else if (root->left == NULL && root->right == NULL)	// If leaf
		if (root->val >= L && root->val <= R)	// In range
			return root->val;
		else									// Out of range
			return 0;
	else										// Not a leaf
	{
		if (root->val >= L && root->val <= R)	// In range
			return rangeSumBST(root->left, L, R) + root->val + rangeSumBST(root->right, L, R);
		else if (root->val < L)					// Less than range
			return rangeSumBST(root->right, L, R);
		else if (root->val > R)					// Greater than range
			return rangeSumBST(root->left, L, R);
		else
			return rangeSumBST(root->left, L, R) + rangeSumBST(root->right, L, R);
	}
}