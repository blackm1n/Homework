// Разработайте программу, которая выбросит Exception, когда
// пользователь вводит пустую строку. Пользователю должно
// показаться сообщение, что пустые строки вводить нельзя.

import java.util.InputMismatchException;
import java.util.Scanner;

public class Problem_49_4 {
    public static void main(String[] args) {
        System.out.println(inputString("Введите строку: "));
    }

    public static String inputString(String mes) {
        Scanner in = new Scanner(System.in);
        System.out.print(mes);
        String res = in.nextLine();
        if (res.length() == 0) {
            throw new InputMismatchException("Пустую строку ввести нельзя");
        }
        return res;
    }
}
