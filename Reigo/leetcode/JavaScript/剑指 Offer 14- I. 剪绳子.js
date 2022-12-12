/**
 * @param {number} n
 * @return {number}
 */
 var cuttingRope = function(x) {
    if(x==2){
        return 1;
    }else if(x==3){
        return 2;
    }else if(x==4){
        return 4;
    }
    n=parseInt(x/3);
    if(x%3==0){
        return Math.pow(3,n);
    }else if(x%3==1){
        return Math.pow(3,n-1)*4;
    }else if(x%3==2){
        return Math.pow(3,n)*2;
    }
};