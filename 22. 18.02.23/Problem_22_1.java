// Реализовать алгоритм сортировки слиянием
// Приведено два варианта деления массива. Единично и пополам.

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Random;

public class Problem_22_1 {
    public static void main(String[] args) {
        int[] variables = initVariables();
        int[] arr = randomArray(variables[0], variables[1], variables[2]);
        int[] result = mergeSort(arr);
        for (int i : result) {
            System.out.printf("%d ", i);
        }
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

    private static int[] mergeSort(int[] input) {
        // Queue<int[]> queue = splitVar1(input);
        Queue<int[]> queue = splitVar2(input);
        while (queue.size() != 1) {
            int[] arr1 = queue.remove();
            int[] arr2 = queue.remove();
            int[] arr3 = new int[arr1.length + arr2.length];
            int i = 0;
            int j = 0;
            for (int k = 0; k < arr3.length; k++) {
                if (i != arr1.length && j != arr2.length) {
                    if (arr1[i] <= arr2[j]) {
                        arr3[k] = arr1[i];
                        i++;
                    } else {
                        arr3[k] = arr2[j];
                        j++;
                    }
                } else if (i != arr1.length) {
                    arr3[k] = arr1[i];
                    i++;
                } else if (j != arr2.length) {
                    arr3[k] = arr2[j];
                    j++;
                }
            }
            queue.add(arr3);
        }
        return queue.remove();
    }

    private static Queue<int[]> splitVar1(int[] input) {
        Queue<int[]> queue = new LinkedList<>();
        for (int i : input) {
            queue.add(new int[]{i});
        }
        return queue;
    }

    private static Queue<int[]> splitVar2(int[] input) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(input);
        int size = input.length;
        while (queue.size() != size) {
            int[] arr1 = queue.remove();
            if (arr1.length == 1) {
                queue.add(arr1);
                continue;
            }
            int[] arr2 = new int[arr1.length / 2];
            int[] arr3 = new int[arr1.length - arr2.length];
            for (int i = 0; i < arr1.length; i++) {
                if (i < arr2.length) {
                    arr2[i] = arr1[i];
                } else {
                    arr3[i - arr2.length] = arr1[i];
                }
            }
            queue.add(arr2);
            queue.add(arr3);
        }
        return queue;
    }
}
