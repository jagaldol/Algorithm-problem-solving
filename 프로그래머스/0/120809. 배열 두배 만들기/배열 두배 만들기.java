import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        return Arrays.stream(numbers)
            .map(x -> x * 2)
            .toArray();
    }
}