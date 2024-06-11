import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final List<Integer> S = new ArrayList<>();

    private static void search(int n, int idx) {
        if (idx == 0) {
            if (n == 1) System.out.println("m");
            else System.out.println("o");
            return;
        }

        int leftEnd = S.get(idx - 1);
        int rightStart = leftEnd + idx + 4;

        if (n <= leftEnd) {
            search(n, idx - 1);
        } else if (rightStart <= n) {
            search(n - rightStart + 1, idx - 1);
        } else {
            if (n == leftEnd + 1) System.out.println("m");
            else System.out.println("o");
        }
    }

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        S.add(3);
        while (S.get(S.size() - 1) < N) {
            S.add(S.get(S.size() - 1) * 2 + S.size() + 3);
        }
        search(N, S.size() - 1);
    }
}
