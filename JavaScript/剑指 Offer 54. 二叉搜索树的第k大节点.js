/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
 var kthLargest = function(root, k) {
    var ans=-1;
    function midOrder(root){
        if(root){
            if(k<=0)return;
            midOrder(root.right);
            k-=1;
            if(k==0){
                ans=root.val;
                return;
            }
            midOrder(root.left);
        }
    }
    midOrder(root);

    return ans;
};