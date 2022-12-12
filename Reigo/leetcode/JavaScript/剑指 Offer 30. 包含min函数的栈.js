/**
 * initialize your data structure here.
 */
 var MinStack = function() {
    this.minStack=[];
    this.stack=[];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    var stack=this.stack;
    var minStack=this.minStack;
    if(!stack.length){
        stack.push(x);
        minStack.push(x);
    }else{
        stack.push(x);
        minnum=minStack[minStack.length-1];
        if(x<minnum){
            minStack.push(x);
        }else{
            minStack.push(minnum);
        }
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    var stack=this.stack;
    var minStack=this.minStack;
    stack.pop();
    minStack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    var stack=this.stack;
    return stack[stack.length-1];
};

/**
 * @return {number}
 */
MinStack.prototype.min = function() {
    var minStack=this.minStack;
    return minStack[minStack.length-1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.min()
 */