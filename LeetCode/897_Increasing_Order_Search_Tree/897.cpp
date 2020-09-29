#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
	vector<int> iov {};
public:
	TreeNode* increasingBST(TreeNode* root) {
		inorderRearrange(root, &iov);
		TreeNode *result = new TreeNode(0), *cur = result;
		for (vector<int>::iterator iter = iov.begin(); iter != iov.end(); ++iter) {
			cur->right = new TreeNode(*iter);
			cur = cur->right;
		}
		return result->right;
	}
	
	void inorderRearrange(TreeNode* root, vector<int> *iov) {
		if (!root) return;
		inorderRearrange(root->left, iov);
		(*iov).push_back(root->val);
		inorderRearrange(root->right, iov);
	}
	
	void inorderShow(TreeNode* root) {
		if (!root) {
			cout << "null" << endl;
			return;
		}
		inorderShow(root->left);
		cout << root->val << endl;
		inorderShow(root->right);
	}

};

int main(void) {
	TreeNode* rptr1;
	TreeNode n1(1);
	TreeNode n2(2, &n1, nullptr);
	TreeNode n4(4);
	TreeNode n3(3, &n2, &n4);
	TreeNode n7(7);
	TreeNode n9(9);
	TreeNode n8(8, &n7, &n9);
	TreeNode n6(6, nullptr, &n8);
	TreeNode n5(5, &n3, &n6);
	rptr1 = &n5;
	
	TreeNode *rptr2;
	TreeNode m9(9);
	TreeNode m8(8, nullptr, &m9);
	TreeNode m7(7, nullptr, &m8);
	TreeNode m6(6, nullptr, &m7);
	TreeNode m5(5, nullptr, &m6);
	TreeNode m4(4, nullptr, &m5);
	TreeNode m3(3, nullptr, &m4);
	TreeNode m2(2, nullptr, &m3);
	TreeNode m1(1, nullptr, &m2);
	rptr2 = &m1;
	
	Solution sol;
	
	sol.inorderShow(sol.increasingBST(rptr1));
	
	return 0;
}