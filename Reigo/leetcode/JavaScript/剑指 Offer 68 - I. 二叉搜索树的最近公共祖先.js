/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
 var lowestCommonAncestor = function(root, p, q) {
    var findans=false;
    var ans=null;
    function dfs(root){
        if(root){
            var tv=(root.val==p.val ||root.val==q.val);
            var lv=dfs(root.left);
            var rv=dfs(root.right);
            if(!findans&&(lv&&rv)||(lv&&tv)||(rv&&tv)){
                ans=root;
                findans=true;
            }
            return tv||lv||rv;
        }
    }
    dfs(root);
    return ans;
    
};