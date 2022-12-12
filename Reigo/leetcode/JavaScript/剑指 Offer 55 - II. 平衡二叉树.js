/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isBalanced = function(root) {
    function check(root){
        if(root){
            var lh=check(root.left);
            if(lh==-1)return -1;
            var rh=check(root.right);
            if(rh==-1)return -1;
            if(Math.abs(lh-rh)<=1)return Math.max(lh,rh)+1;
            else return -1;
        }else{
            return 0;
        }
    }
    if(check(root)==-1)return false;
    return true;
};