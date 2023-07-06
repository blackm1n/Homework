// Разработайте программу, которая выбросит Exception, когда
// пользователь вводит пустую строку. Пользователю должно
// показаться сообщение, что пустые строки вводить нельзя.

import java.util.InputMismatchException;
import java.util.Scanner;

public class Problem_49_4 {
    public static void main(String[] args) {
        System.out.println(inputString("Введите строку: "));
    }

    // Огромная проблема с этим заданием в том, что пустые строки в IntelliJ невозможно ввести вообще.
    // Поэтому данный код может не работать если реально ввести пустую строку.

    public static String inputString(String mes) {
        Scanner in = new Scanner(System.in);
        System.out.print(mes);
        String res = in.next();
        if (res == null) {
            throw new InputMismatchException("Пустую строку ввести нельзя");
        }
        return res;
    }
}
