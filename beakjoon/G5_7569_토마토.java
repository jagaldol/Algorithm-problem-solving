import java.util.LinkedList;
import java.util.Queue;

public class G5_7569_토마토 {
    private static final int[] tx = {1, -1, 0, 0, 0, 0};
    private static final int[] ty = {0, 0, 1, -1, 0, 0};
    private static final int[] tz = {0, 0, 0, 0, 1, -1};
    private static final Queue<Key> queue = new LinkedList<>();

    private static int M, N, H;
    private static int[][][] box;

    private static boolean isRemain() {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    if (box[i][j][k] == 0)
                        return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        M = read();
        N = read();
        H = read();

        box = new int[H][N][M];

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    int value = read();
                    box[i][j][k] = value;
                    if (value == 1)
                        queue.add(new Key(i, j, k));
                }
            }
        }

        int result = 0;
        while (!queue.isEmpty()) {
            Key now = queue.poll();

            for (int i = 0; i < 6; i++) {
                int nx = now.i + tx[i];
                int ny = now.j + ty[i];
                int nz = now.k + tz[i];
                boolean isRange = 0 <= nx && nx < H && 0 <= ny && ny < N && 0 <= nz && nz < M;
                if (isRange && box[nx][ny][nz] == 0) {
                    box[nx][ny][nz] = box[now.i][now.j][now.k] + 1;
                    queue.add(new Key(nx, ny, nz));
                }
            }
        }
        int max = 0;
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < M; k++) {
                    if (box[i][j][k] == 0) {
                        System.out.println(-1);
                        return;
                    }
                    max = Math.max(max, box[i][j][k]);
                }

            }
        }
        System.out.println(Math.max(max - 1, 0));

    }

    private static int read() throws Exception {
        int c, n = System.in.read() & 15;
        boolean isNegative = n == 13;
        if (isNegative) n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        return isNegative ? ~n + 1 : n;
    }
}

class Key {
    public int i;
    public int j;
    public int k;


    public Key(int i, int j, int k) {
        this.i = i;
        this.j = j;
        this.k = k;
    }
}
