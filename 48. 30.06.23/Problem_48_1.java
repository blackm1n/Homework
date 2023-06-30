// Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

public class Problem_48_1 {
    public static void main(String[] args) {
        int[] arr = {7, 2, 5, 3, 0, 7, 9, 1};
        // ArrayIndexOutOfBoundsException(arr);
        // ArithmeticException(arr);

        String notnum = "124O";
        // int num = NumberFormatException(notnum);
    }

    public static void ArrayIndexOutOfBoundsException(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > arr[i + 1]) {
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }

    public static void ArithmeticException(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            arr[i] = arr[i] / arr[i + 1];
        }
    }

    public static int NumberFormatException(String num) {
        return Integer.parseInt(num);
    }
}
