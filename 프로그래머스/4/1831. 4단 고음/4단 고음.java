class Solution {
    int answer = 0;
    
    void dfs(int n, int plus) {
        if (n < 3 || n < Math.pow(3, plus/2)) return;
        if (n == 3 && plus == 2) {
            answer++;
            return;
        }
        if (n % 3 == 0 && plus >= 2) dfs(n / 3, plus - 2);
        dfs(n - 1, plus + 1);
    }
    
    public int solution(int n) {
        dfs(n, 0);
        return answer;
    }
}