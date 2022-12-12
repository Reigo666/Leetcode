/**
 * @param {number[]} postorder
 * @return {boolean}
 */
 var verifyPostorder = function(postorder) {
    function check(postorder){
        if(postorder.length>=3){
            var val=postorder[postorder.length-1];
            var l=0;
            var idx=-1;
            while(l<postorder.length-1){
                while(l<postorder.length-1 && postorder[l]<val){
                    l+=1;
                }
                idx=l;
                while(l<postorder.length-1 && postorder[l]>val){
                    l+=1;
                }
                if(l<postorder.length-1){
                    return false;
                }
            }
            if(!check(postorder.slice(0,idx))){
                return false;
            }
            if(!check(postorder.slice(idx,postorder.length-1))){
                return false;
            }
            return true;
        }else{
            return true;
        }
    }
    return check(postorder);
};