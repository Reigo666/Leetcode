/**
 * @param {number[][]} grid
 * @return {number}
 */
var closedIsland = function(grid) {
    function dfs(i,j){
        if(grid[i][j]==1)return false;
        let flag=true;
        grid[i][j]=1
        let directions=[[0,1],[0,-1],[1,0],[-1,0]];
        for(let direction of directions){
            let tx=i+direction[0];
            let ty=j+direction[1];
            // console.log(tx,ty)
            if(tx<0 || tx>=m || ty<0 || ty>=n){
                flag=false
                continue;
            }
            if(grid[tx][ty]==0){
                if(!dfs(tx,ty))flag=false;
            }
        }
        if(flag)return true
        return false;
    }
    let m=grid.length;
    let n=grid[0].length
    let ans=0
    for(let i=0;i<m;i++){
        for(let j=0;j<n;j++){
            if(dfs(i,j)){
                ans+=1
            }
        }
    }
    // console.log(grid)
    return ans;
};