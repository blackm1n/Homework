package org.example;

import java.util.List;
import java.util.Scanner;

public class UI {

    static String lineBreak = "=";
    static Scanner scanner = new Scanner(System.in);

    public static int chooseGame() {
        breakLine();
        System.out.println("Выберите игру:");
        System.out.println("1. С Числами");
        System.out.println("2. С Английскими символами");
        System.out.println("3. С Русскими символами");
        System.out.print("Выберите номер необходимого действия: ");
        return scanner.nextInt();
    }

    public static int chooseDiff() {
        breakLine();
        System.out.println("Выберите сложность:");
        System.out.println("1. Легко (3-4 символа)");
        System.out.println("2. Средне (5-6 символов)");
        System.out.println("3. Сложно (7-8 символов)");
        System.out.print("Выберите номер необходимого действия: ");
        return scanner.nextInt();
    }

    public static int chooseType() {
        breakLine();
        System.out.println("Выберите тип:");
        System.out.println("1. Рандомное слово");
        System.out.println("2. Из файла");
        System.out.print("Выберите номер необходимого действия: ");
        return scanner.nextInt();
    }

    public static String writeAnswer(int turn) {
        breakLine();
        System.out.println("ХОД " + turn);
        System.out.print("Введите ваш ответ: ");
        return scanner.next();
    }

    public static void gameNotExist() {
        breakLine();
        System.out.println("Такой игры не существует");
    }

    public static void diffNotExist() {
        breakLine();
        System.out.println("Такой сложности не существует");
    }

    public static void typeNotExist() {
        breakLine();
        System.out.println("Такого типа не существует");
    }

    public static int chooseHistory() {
        breakLine();
        System.out.println("Хотите видеть историю ваших ходов?");
        System.out.println("1. Да");
        System.out.println("2. Нет");
        System.out.print("Выберите номер необходимого действия: ");
        return scanner.nextInt();
    }

    public static void showHistory(List<Answer> history) {
        for (int i = 1; i <= history.size(); i++) {
            breakLine();
            System.out.printf("Ход %d\n", i);
            System.out.printf("Слово: %s\n", history.get(i - 1).getUserInput());
            System.out.printf("Коров: %s\n", history.get(i - 1).getCows());
            System.out.printf("Быков: %s\n", history.get(i - 1).getBulls());
        }
    }

    public static void showWord(GameStatus gameStatus, String word) {
        breakLine();
        if (gameStatus == GameStatus.WIN) {
            System.out.println("Вы победили!");
        }
        else {
            System.out.println("Вы проиграли!");
            System.out.println("Слово: " + word);
        }
    }

    public static void breakLine() {
        System.out.println(lineBreak.repeat(20));
    }
}
