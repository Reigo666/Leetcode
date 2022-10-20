/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
 var maxDepth = function(root) {
    function depth(root){
        if(root){
            var lh=depth(root.left)+1;
            var rh=depth(root.right)+1;
            return Math.max(lh,rh);
        }
        else{
            return 0;
        }
    }
    return depth(root);
};