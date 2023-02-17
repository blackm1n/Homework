// Реализуйте алгоритм сортировки пузырьком числового массива, результат после каждой итерации запишите в лог-файл.

import java.util.Scanner;
import java.util.Random;
import java.util.logging.*;
import java.io.IOException;

public class Problem_21_2 {
    public static void main(String[] args) throws IOException {
        int[] variables = InitVariables();
        int[] arr = RandomArray(variables[0], variables[1], variables[2]);
        BubbleSort(arr);
    }

    private static int InputNumber() {
        Scanner input = new Scanner(System.in);
        return input.nextInt();
    }

    private static int[] InitVariables() {
        int[] variables = new int[3];
        System.out.print("Введите n: ");
        variables[0] = InputNumber();
        System.out.print("Введите min: ");
        variables[1] = InputNumber();
        System.out.print("Введите max: ");
        variables[2] = InputNumber();
        return variables;
    }

    private static int[] RandomArray(int n, int min, int max) {
        Random random = new Random();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = random.nextInt(min, max);
        }
        return arr;
    }

    private static String ViewArray(int[] array) {
        StringBuilder str = new StringBuilder();
        for (int i : array) {
            str.append(i).append(" ");
        }
        return str.toString();
    }

    private static void BubbleSort(int[] arr) throws IOException {
        int size = arr.length;
        Logger logger = LogInit();
        logger.info("Before - " + ViewArray(arr));
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
                LogArray(logger, arr, i, j);
            }
        }
        logger.info("After - " + ViewArray(arr));
    }

    private static Logger LogInit() throws IOException {
        Logger logger = Logger.getLogger(Problem_21_2.class.getName());
        FileHandler fh = new FileHandler("21. 12.02.23\\log_2.txt");
        SimpleFormatter sFormat = new SimpleFormatter();
        fh.setFormatter(sFormat);
        logger.addHandler(fh);
        return logger;
    }

    private static void LogArray(Logger logger, int[] arr, int i, int j) {
        logger.info("i = " + i + ", j = " + j + " - " + ViewArray(arr));
    }
}
