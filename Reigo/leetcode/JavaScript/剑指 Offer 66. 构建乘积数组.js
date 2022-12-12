/**
 * @param {number[]} a
 * @return {number[]}
 */
 var constructArr = function(a) {
    la=[1];
    for(var i=0;i<a.length-1;i++){
        la.push(la[i]*a[i]);
    }
    //ra=new Array(a.length).fill(1);
    ra=[1];
    //ra[ra.length-1]=a[a.length-1];
    for(var i=a.length-1;i>=1;i--){
        ra.push(ra[ra.length-1]*a[i]);
    }
    console.log({la},{ra});
    ans=[]
    for(var i=0;i<a.length;i++){
        ans.push(la[i]*ra[a.length-1-i]);
    }
    return ans;
};