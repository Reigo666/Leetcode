var CQueue = function() {
    this.instack=[];
    this.outstack=[];
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function(value) {
    this.instack.push(value);
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function() {
    if(!this.outstack.length){
        while(this.instack.length){
            this.outstack.push(this.instack.pop());
        }
    }
    if(!this.outstack.length){
        return -1;
    }
    return this.outstack.pop();
};

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */