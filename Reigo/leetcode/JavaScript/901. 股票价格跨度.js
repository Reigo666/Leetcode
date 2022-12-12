var StockSpanner = function() {
    this.idx=0;
    this.stack=[[-1,Math.pow(10,6)]];
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    var idx=this.idx;
    var stack=this.stack;
    while(stack && price>=stack[stack.length-1][1]){
        stack.pop();
    }
    stack.push([idx,price]);
    //console.log(stack)
    this.idx+=1;
    return stack[stack.length-1][0]-stack[stack.length-2][0];
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */