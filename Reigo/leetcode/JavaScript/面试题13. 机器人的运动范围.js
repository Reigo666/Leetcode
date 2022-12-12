/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
 var movingCount = function(m, n, k) {
    function check(x){
        var sum=0;
        var temp=x;
        while(x){
            sum+=x%10;
            x=parseInt(x/10);
        }
        return sum;
    }

    var all_direct=[[0,1],[0,-1],[1,0],[-1,0]];
    function dfs(dx,dy,k,m,n){
        if(isVisit[dx][dy]){
            return
        }
        isVisit[dx][dy]=true;
        if(check(dx)+check(dy)>k){
            return
        }
        ans+=1;
        for(direct of all_direct){
            var tx=dx+direct[0];
            var ty=dy+direct[1];
            if(tx>=0 && ty>=0 && tx<m && ty<n){
                dfs(tx,ty,k,m,n)
            }
        }
    }
    var isVisit=new Array(m).fill(0).map(()=>(new Array(n).fill(false)));
    var ans=0;
    dfs(0,0,k,m,n)
    return ans;
};