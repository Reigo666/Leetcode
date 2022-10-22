/**
 * initialize your data structure here.
 */
var MedianFinder = function() {
    this.arr=[];
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    var arr=this.arr;
    bisect_insort(arr,num);
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    var arr=this.arr;
    var n=arr.length;
    if(n%2==1){
        return arr[parseInt(n/2)];
    }else{
        return (arr[parseInt(n/2)-1]+arr[parseInt(n/2)])/2;
    }
};

function bisect_left(arr,num){
    var l=0,r=arr.length;
    while(l<r){
        var mid=parseInt((l+r)/2);
        if(arr[mid]<num){
            l=mid+1;
        }else{
            r=mid;
        }
    }
    return l;
}

function bisect_insort(arr,num){
    var idx=bisect_left(arr,num);
    arr.splice(idx,0,num);
}
/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */