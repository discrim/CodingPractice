struct TreeNode{
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
}

#define MAX(x, y) (x > y ? x : y)

// WRONG CODE
int longestUnivaluePath(struct TreeNode* root){
	if ((root->left == NULL && root->right == NULL) || root == NULL)	// If leaf or NULL
		return 0;
	
	else if (root->right == NULL)
		if (root->val == root->left->val)
			return 1 + longestUnivaluePath(root->left);
		else
			return longestUnivaluePath(root->left);
	
	else if (root->left == NULL)
		if (root->val == root->right->val)
			return 1 + longestUnivaluePath(root->right);
		else
			return longestUnivaluePath(root->right);
	
	else
		if (root->val == root->left->val && root->val == root->right->val)
			return 2 + longestUnivaluePath(root->left) + longestUnivaluePath(root->right);
		else if (root->val == root->left->val)
			return MAX(1 + longestUnivaluePath(root->left), longestUnivaluePath(root->right));
		else if (root->val == root->right->val)
			return MAX(longestUnivaluePath(root->left), 1 + longestUnivaluePath(root->right));
		else
			return MAX(longestUnivaluePath(root->left), longestUnivaluePath(root->right));
}