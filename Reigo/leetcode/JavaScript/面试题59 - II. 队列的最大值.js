var MaxQueue = function() {
    this.q=[];
    this.mq=[];
};

/**
 * @return {number}
 */
MaxQueue.prototype.max_value = function() {
    q=this.q;
    mq=this.mq;
    if(q.length==0)return -1;
    return mq[0];
};

/** 
 * @param {number} value
 * @return {void}
 */
MaxQueue.prototype.push_back = function(value) {
    q=this.q;
    mq=this.mq;
    q.push(value);
    while(mq.length && value>mq[mq.length-1]){
        mq.pop();
    }
    mq.push(value);
};

/**
 * @return {number}
 */
MaxQueue.prototype.pop_front = function() {
    q=this.q;
    mq=this.mq;
    if(q.length==0)return -1;

    if(q[0]==mq[0]){
        mq.shift();
    }
    return q.shift();
};

/**
 * Your MaxQueue object will be instantiated and called as such:
 * var obj = new MaxQueue()
 * var param_1 = obj.max_value()
 * obj.push_back(value)
 * var param_3 = obj.pop_front()
 */