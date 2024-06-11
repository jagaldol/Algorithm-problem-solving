import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] buildings = new int[N];
        for (int i = 0; i < N; i++) {
            buildings[i] = Integer.parseInt(st.nextToken());
        }

        int[] count = new int[N];

        for (int i = 0; i < N; i++) {
            int mainBuilding = buildings[i];
            double a = 0, b = 0;
            for (int j = i + 1; j < N; j++) {
                int targetBuilding = buildings[j];
                // Y = aX + b
                // (i, mainBuilding) , (j, targetBuilding)

                if (a * j + b < targetBuilding) {
                    count[i]++;
                    count[j]++;
                    a = (double) (mainBuilding - targetBuilding) / (i - j);
                    b = mainBuilding - a * i;
                }
            }
        }
        System.out.println(Arrays.stream(count).max().orElse(0));
    }
}
