class Solution {
    
    lateinit var visited: Array<BooleanArray>
    lateinit var maps: Array<String>
    val moves = arrayOf(-1 to 0, 0 to -1, 1 to 0, 0 to 1)
    var food = 0
    
    fun solution(maps: Array<String>): IntArray {
        var answer = mutableListOf<Int>()
        this.maps = maps
        
        visited = Array(maps.size) {BooleanArray(maps[0].length){false}}
        
        for (i in maps.indices) {
            for (j in maps[0].indices) {
                if (!visited[i][j]) {
                    visited[i][j] = true
                    food = 0
                    dfs(i, j)
                    if (food != 0) answer.add(food)
                }
            }
        }
        
        return if (answer.isEmpty()) intArrayOf(-1) else answer.sorted().toIntArray()
    }
    
    fun dfs(x: Int, y: Int) {
        if (maps[x][y] == 'X') return
        
        food += maps[x][y].digitToInt()
        
        for ((tx, ty) in moves) {
            val nx = x + tx
            val ny = y + ty
            
            if (nx in maps.indices && ny in maps[0].indices && !visited[nx][ny]) {
                visited[nx][ny] = true
                dfs(nx, ny)
            }
        }
    }
}