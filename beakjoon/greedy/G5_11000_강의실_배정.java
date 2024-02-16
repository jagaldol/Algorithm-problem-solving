package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class G5_11000_강의실_배정 {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[][] reservation = new int[2 * n][2];


        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            reservation[2 * i][0] = Integer.parseInt(st.nextToken());
            reservation[2 * i][1] = 1;
            reservation[2 * i + 1][0] = Integer.parseInt(st.nextToken());
            reservation[2 * i + 1][1] = -1;
        }

        Arrays.sort(reservation, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0])
                    return o1[1] - o2[1];
                return o1[0] - o2[0];
            }
        });

        int result = 0;
        int activeRooms = 0;

        for (int i = 0; i < 2 * n; i++) {
            activeRooms += reservation[i][1];
            result = Math.max(result, activeRooms);
        }
        System.out.println(result);
    }
}