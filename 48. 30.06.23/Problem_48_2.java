// Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?

public class Problem_48_2 {
    public static void main(String[] args) {
        String[][] arr1 = {{"1", "2", "3"}, {"4", "5", "6"}};
        String[][] arr2 = {{"hello", "this", "is"}, {"a", "string", "array"}};
        // System.out.println(sum2d(arr1));
        // System.out.println(sum2d(arr2));
    }

    public static int sum2d(String[][] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < 5; j++) { // ArrayIndexOutOfBoundsException
                int val = Integer.parseInt(arr[i][j]); // NumberFormatException
                sum += val;
            }
        }
        return sum;
    }
}
