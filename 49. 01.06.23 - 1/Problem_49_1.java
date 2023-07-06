// Реализуйте метод, который запрашивает у пользователя ввод
// дробного числа (типа float), и возвращает введенное значение.
// Ввод текста вместо числа не должно приводить к падению приложения,
// вместо этого, необходимо повторно запросить у пользователя ввод данных.

import java.util.InputMismatchException;
import java.util.Scanner;

public class Problem_49_1 {
    public static void main(String[] args) {
        System.out.println(inputFloat("Введите дробное число: "));
    }

    public static float inputFloat(String mes) {
        float res = 0;
        boolean inputted = false;
        while (!inputted) {
            Scanner in = new Scanner(System.in);
            System.out.print(mes);
            try {
                res = in.nextFloat();
                inputted = true;
            }
            catch(InputMismatchException e) {
                System.out.println("Ошибка при введении числа.");
            }
        }
        return res;
    }
}
