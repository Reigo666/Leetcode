/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
 var serialize = function(root) {
    var ret="";
    function preOrder(root){
        if(root){
            ret+=String(root.val);
            ret+=','
            preOrder(root.left);
            preOrder(root.right);
        }else{
            ret+='None,';
        }
    }

    preOrder(root);
    ret=ret.slice(0,ret.length-1);
    //console.log(ret);
    return ret;
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    if(data.length==0)return null;
    function CreateTree(data){
        if(data.length){
            var cur=data.shift();
            var curnode=null;
            if(cur!='None'){
                curnode=new TreeNode(Number(cur));
                //console.log({cur},{curnode})
                curnode.left=CreateTree(data);
                curnode.right=CreateTree(data);
                return curnode;
            }else return null;
        }
    }
    data=data.split(',');
    //console.log(data);
    return CreateTree(data);
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */