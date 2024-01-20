package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class G5_10026_적록색약 {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static final int[] tx = new int[]{1, 0, -1, 0};
    private static final int[] ty = new int[]{0, -1, 0, 1};

    private static int N;
    private static boolean[][] visited;

    private static void dfs(char[][] paint, int x, int y) {
        char color = paint[x][y];
        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + tx[i];
            int ny = y + ty[i];
            boolean isInRange = 0 <= nx && nx < N && 0 <= ny && ny < N;

            if (isInRange && !visited[nx][ny] && paint[nx][ny] == color) {
                dfs(paint, nx, ny);
            }
        }
    }

    private static int solution(char[][] paint) {
        for (boolean[] vi : visited)
            Arrays.fill(vi, false);

        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    dfs(paint, i, j);
                    result++;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());

        visited = new boolean[N][N];
        char[][] paint = new char[N][N];
        char[][] paintBlind = new char[N][N];

        for (int i = 0; i < N; i++) {
            paint[i] = br.readLine().toCharArray();
            for (int j = 0; j < N; j++) {
                paintBlind[i][j] = paint[i][j] == 'B' ? 'B' : 'R';
            }
        }

        StringBuilder sb = new StringBuilder();

        System.out.println(sb.append(solution(paint)).append(' ').append(solution(paintBlind)));
    }
}
