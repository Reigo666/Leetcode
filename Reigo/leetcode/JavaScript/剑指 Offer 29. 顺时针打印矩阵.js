/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
 var spiralOrder = function(matrix) {
    if(matrix.length==0){
        return [];
    }
    var l=0,u=0,d=matrix.length-1,r=matrix[0].length-1;
    var ans=[];
    while(true){
        //->
        for(var i=l;i<=r;i++){
            ans.push(matrix[u][i]);
        }
        u+=1;
        if(u>d)break;

        //down
        for(var i=u;i<=d;i++){
            ans.push(matrix[i][r]);
        }
        r-=1;
        if(l>r)break;

        //left
        for(var i=r;i>=l;i--){
            ans.push(matrix[d][i]);
        }
        d-=1;
        if(u>d)break;

        //up
        for(var i=d;i>=u;i--){
            ans.push(matrix[i][l]);
        }
        l+=1;
        if(l>r)break;
    }
    return ans;
};