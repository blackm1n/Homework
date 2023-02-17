// Написать программу вычисления n-ого треугольного числа.

import java.util.Scanner;

public class Problem_20_1 {
    public static void main(String[] args) {
        int n = InputN();
        System.out.printf("Треугольное число от %d - %d", n, TriangleNum(n));
    }

    private static int InputN() {
        Scanner input = new Scanner(System.in);
        System.out.print("Введите n: ");
        return input.nextInt();
    }

    private static int TriangleNum(int n) {
        int result = 0;
        for (int i = 1; i <= n; i++) {
            result += i;
        }
        return result;
    }
}
