/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
 var validateStackSequences = function(pushed, popped) {
    if(pushed.length!=popped.length)return false;
    var l2=0;
    var stack=[];
    for(var i=0;i<pushed.length;i++){
        stack.push(pushed[i]);
        while(stack.length && stack[stack.length-1]==popped[l2]){
            stack.pop();
            l2+=1;
        }
    }
    if(l2==popped.length)return true;
    return false;
};