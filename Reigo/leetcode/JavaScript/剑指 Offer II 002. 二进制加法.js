/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
 var addBinary = function(a, b) {
    if(a.length>b.length){
        [a,b]=[b,a];
    }
    a="0".repeat(b.length-a.length)+a;
    
    console.log(a);
    a=a.split('').reverse();
    b=b.split('').reverse();
    var ans=[];
    var carry=0;
    for(var i=0;i<a.length;i++){
        n1=Number(a[i]);
        n2=Number(b[i]);
        var val=n1+n2+carry;
        
        carry=0;
        if(val>=2){
            val-=2;
            carry=1;
        }
        ans.push(val);
    }
    if(carry){
        ans.push(1);
    }
    return ans.reverse().join('');
};