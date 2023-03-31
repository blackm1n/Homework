package org.example;

import java.io.IOException;
import java.util.Scanner;

public class ViewCalculator {

    private ICalculableFactory calculableFactory;

    public ViewCalculator(ICalculableFactory calculableFactory) {
        this.calculableFactory = calculableFactory;
    }

    public void run() throws IOException {
        Calculable calculator = calculableFactory.create();
        int log = 0;
        while (true) {
            System.out.println("\n" + breakLine());
            System.out.println(calculator.getResult());
            int option = menu(log);
            switch (option) {
                case 1: {
                    log = (log + 1) % 2;
                    calculator = new LogCalculator(calculator);
                    break;
                }
                case 2: {
                    Complex primaryArg = promptComplex("Введите реальное число первого аргумента: ", "Введите мнимое число первого аргумента: ");
                    calculator = calculableFactory.create(primaryArg);
                    if (log == 1) {
                        calculator = new LogCalculator(calculator);
                    }
                }
                case 3: {
                    while (true) {
                        String cmd = prompt("Введите команду (+, -, *, /) : ");
                        if (cmd.equals("+")) {
                            Complex arg = promptComplex("Введите реальное число второго аргумента: ", "Введите мнимое число второго аргумента: ");
                            calculator.sum(arg);
                            break;
                        }
                        if (cmd.equals("-")) {
                            Complex arg = promptComplex("Введите реальное число второго аргумента: ", "Введите мнимое число второго аргумента: ");
                            calculator.sub(arg);
                            break;
                        }
                        if (cmd.equals("*")) {
                            Complex arg = promptComplex("Введите реальное число второго аргумента: ", "Введите мнимое число второго аргумента: ");
                            calculator.multi(arg);
                            break;
                        }
                        if (cmd.equals("/")) {
                            Complex arg = promptComplex("Введите реальное число второго аргумента: ", "Введите мнимое число второго аргумента: ");
                            calculator.div(arg);
                            break;
                        }
                    }
                    break;
                }
                case 4: {
                    calculator = calculableFactory.create();
                    if (log == 1) {
                        calculator = new LogCalculator(calculator);
                    }
                    break;
                }
                case 5: {
                    System.exit(0);
                }
            }
        }
    }

    private String breakLine() {
        return "=".repeat(20);
    }
    private int menu(int log) {
        Scanner in = new Scanner(System.in);
        System.out.println("\n" + breakLine());
        System.out.println("Выберите необходимое дейтсвие");
        if (log == 0) {
            System.out.println("1. Включить логирование");
        }
        else {
            System.out.println("1. Выключить логирование");
        }
        System.out.println("2. Ввести новое число");
        System.out.println("3. Ввести арифметическое действие");
        System.out.println("4. Обнулить число");
        System.out.println("5. Выйти из программы");
        System.out.print("Введите номер необходимого действия: ");
        return in.nextInt();
    }
    private String prompt(String message) {
        Scanner in = new Scanner(System.in);
        System.out.println("\n" + breakLine());
        System.out.print(message);
        return in.nextLine();
    }

    private Complex promptComplex(String message1, String message2) {
        System.out.println("\n" + breakLine());
        Double real = promptDouble(message1);
        Double imaginary = promptDouble(message2);
        return new Complex(real, imaginary);
    }

    private Double promptDouble(String message) {
        double real = 0.0;
        boolean caught = true;
        while (caught) {
            Scanner in = new Scanner(System.in);
            System.out.print(message);
            try {
                real = in.nextDouble();
                caught = false;
            } catch (Exception e) {
                System.out.println("Что-то пошло не так во время ввода числа.");
            }
        }
        return real;
    }
}
