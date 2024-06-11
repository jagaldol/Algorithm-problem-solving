import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
    private static final List<String> vowels = List.of("a", "e", "i", "o", "u");

    private static String[] alphabets;

    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int L = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        alphabets = Arrays.stream(br.readLine().split(" ")).sorted().toArray(String[]::new);

        Queue<List<Integer>> queue = new LinkedList<>();

        for (int i = 0; i < C; i++) {
            queue.add(List.of(i));
        }

        while (!queue.isEmpty()) {
            List<Integer> now = queue.poll();

            if (now.size() == L) {
                check(now);
            } else {
                for (int i = now.get(now.size() - 1) + 1; i < C; i++) {
                    List<Integer> next = new ArrayList<>(List.copyOf(now));
                    next.add(i);
                    queue.add(next);
                }
            }
        }
    }

    private static void check(List<Integer> indexList) {
        StringBuilder sb = new StringBuilder();
        int vowelCount = 0;

        for (int i : indexList) {
            String now = alphabets[i];
            sb.append(now);

            if (vowels.contains(now))
                vowelCount++;
        }
        if (vowelCount < 1 || indexList.size() - vowelCount < 2)
            return;
        System.out.println(sb);
    }
}
