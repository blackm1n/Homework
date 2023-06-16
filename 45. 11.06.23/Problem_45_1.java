// Реализовать алгоритм пирамидальной сортировки (сортировка кучей).
// Имплементация по моему мнению так себе, но оно работает.

import java.util.Random;
import java.util.Scanner;

public class Problem_45_1 {
    public static void main(String[] args) {
        int[] variables = initVariables();
        int[] arr = randomArray(variables[0], variables[1], variables[2]);
        readArray(arr);
        int[] result = heapSort(arr);
        readArray(result);
    }

    private static void readArray(int[] arr) {
        for (int i : arr) {
            System.out.printf("%d ", i);
        }
        System.out.println();
    }

    private static int[] initVariables() {
        Scanner input = new Scanner(System.in);
        System.out.print("Введите длину массива: ");
        int length = input.nextInt();
        System.out.print("Введите минимум: ");
        int min = input.nextInt();
        System.out.print("Введите максимум: ");
        int max = input.nextInt();
        return new int[]{length, min, max};
    }

    private static int[] randomArray(int length, int min, int max) {
        int[] arr = new int[length];
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            arr[i] = random.nextInt(min, max);
        }
        return arr;
    }

    private static void restoreMaxHeap(int[] arr, int size) {
        for (int i = 0; i < size; i++) {
            while (i != 0 && arr[(i - 1) / 2] < arr[i]) {
                int temp = arr[i];
                arr[i] = arr[(i - 1) / 2];
                arr[(i - 1) / 2] = temp;
                i = (i - 1) / 2;
            }
        }
    }

    private static int[] heapSort(int[] arr) {
        int size = arr.length;
        for (int i = 0; i < size; i++) {
            restoreMaxHeap(arr, size - i);
            int temp = arr[0];
            arr[0] = arr[size - i - 1];
            arr[size - i - 1] = temp;
        }
        return arr;
    }
}
