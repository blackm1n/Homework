// Если необходимо, исправьте данный код

public class Problem_49_2 {
    public static void main(String[] args) {
        int[] intArray = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Добавлен массив intArray
        try {
            int d = 0; // Впринципе можно заменить на не нулевое число, и тогда код будет работать без исключений.
            // int d = 2;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (Exception e) { // Обработаны все возможные исключения (ArrayIndexOutOfBoundsException, NullPointerException и ArithmeticException)
            System.out.println("Catching exception: " + e);
        }
    }
}
