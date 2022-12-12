/**
 * // Definition for a Node.
 * function Node(val,left,right) {
 *    this.val = val;
 *    this.left = left;
 *    this.right = right;
 * };
 */
/**
 * @param {Node} root
 * @return {Node}
 */
 var treeToDoublyList = function(root) {
    var nodelist=[];
    if(!root){
        return null;
    }
    function midOrder(root){
        if(root){
            midOrder(root.left);
            nodelist.push(root);
            midOrder(root.right);
        }
    }
    midOrder(root);
    var pre=nodelist[nodelist.length-1];
    var cur=nodelist[0];
    pre.right=cur;
    cur.left=pre;
    for(var i=1;i<nodelist.length;i++){
        pre=nodelist[i-1];
        cur=nodelist[i];
        pre.right=cur;
        cur.left=pre;
    }
    return nodelist[0];
};