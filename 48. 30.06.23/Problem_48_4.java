// Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
// и возвращающий новый массив, каждый элемент которого равен частному элементов
// двух входящих массивов в той же ячейке. Если длины массивов не равны,
// необходимо как-то оповестить пользователя. Важно: При выполнении метода
// единственное исключение, которое пользователь может увидеть - RuntimeException, т.е. ваше.

import java.util.Random;

public class Problem_48_4 {
    public static void main(String[] args) {
        int[] arr1 = randomArray(0, 100, 20);
        int[] arr2 = randomArray(0, 100, 20);

        int[] arr3 = divArray(arr1, arr2);
        System.out.println(printArray(arr3));
    }

    public static int[] divArray(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) {
            throw new RuntimeException("Длины массивов не равны");
        }
        int[] res = new int[arr1.length];
        for (int i = 0; i < arr1.length; i++) {
            if (arr2[i] == 0) {
                throw new RuntimeException("Делить на ноль нельзя");
            }
            res[i] = arr1[i] / arr2[i];
        }
        return res;
    }

    public static int[] randomArray(int min, int max, int length) {
        Random rand = new Random();
        int[] res = new int[length];
        for (int i = 0; i < res.length; i++) {
            res[i] = rand.nextInt(min, max);
        }
        return res;
    }

    public static String printArray(int[] arr) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            res.append(arr[i]);
            res.append(" ");
        }
        return res.toString();
    }
}
