/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number[][]}
 */
 var pathSum = function(root, target) {
    var ans=[];
    function dfs(root,combinaiton,sum){
        if(root){
            sum+=root.val;
            var newcomb=combinaiton.concat([root.val]);
            if(!root.left && !root.right){
                if(sum==target){
                    ans.push(newcomb);
                }
                return;
            }
            else{
                // combinaiton.push(root.val);
                dfs(root.left,newcomb,sum);
                dfs(root.right,newcomb,sum);
            }
        }
    }
    dfs(root,[],0);
    return ans;
}