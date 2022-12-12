/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
 var buildTree = function(preorder, inorder) {
    function build(preorder,inorder){
        if(preorder.length){
            // console.log(preorder,inorder);
            var val=preorder[0];
            var root=new TreeNode(val)
            var idx=inorder.indexOf(val);
            root.left=build(preorder.slice(1,idx+1),inorder.slice(0,idx));
            root.right=build(preorder.slice(idx+1),inorder.slice(idx+1));
            return root;
        }
        else{
            return null;
        }
    }
    return build(preorder,inorder);
};