//Реализуйте простой калькулятор, с консольным интерфейсом. К калькулятору добавить логирование.

import java.util.Scanner;
import java.lang.Math;
import java.util.logging.*;
import java.io.IOException;
public class Problem_21_4 {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        double result = 0;
        int arith;
        double num = 0;
        Logger logger = LogInit();
        while (true) {
            System.out.println("\n" + Separate());
            System.out.println(result);
            int option = PrintStartOptions(input);
            switch (option) {
                case 1 -> {
                    result = InputNum(input);
                    arith = PrintArithOptions(input);
                    if (arith < 6) {
                        num = InputNum(input);
                    }
                    result = Calc(logger, result, num, arith);
                }
                case 2 -> {
                    arith = PrintArithOptions(input);
                    if (arith < 6) {
                        num = InputNum(input);
                    }
                    result = Calc(logger, result, num, arith);
                }
                case 3 -> result = 0;
                case 4 -> System.exit(0);
            }
        }
    }

    private static String Separate(){
        return "=".repeat(20);
    }

    private static double InputNum(Scanner input){
        System.out.println("\n" + Separate());
        System.out.print("Введите число: ");
        return input.nextInt();
    }
    private static int PrintStartOptions(Scanner input){
        System.out.println("\n" + Separate());
        System.out.println("Выберите необходимое дейтсвие");
        System.out.println("1. Ввести новое число");
        System.out.println("2. Ввести арифметическое действие");
        System.out.println("3. Обнулить число");
        System.out.println("4. Выйти из программы");
        System.out.print("Введите номер необходимого действия: ");
        return input.nextInt();
    }

    private static int PrintArithOptions(Scanner input){
        System.out.println("\n" + Separate());
        System.out.println("Выберите необходимое дейтсвие");
        System.out.println("1. +");
        System.out.println("2. -");
        System.out.println("3. *");
        System.out.println("4. /");
        System.out.println("5. %");
        System.out.println("6. 1/x");
        System.out.println("7. x^2");
        System.out.println("8. 2√x");
        System.out.print("Введите номер необходимого действия: ");
        return input.nextInt();
    }

    private static Logger LogInit() throws IOException {
        Logger logger = Logger.getLogger(Problem_21_4.class.getName());
        FileHandler fh = new FileHandler("21. 12.02.23\\log_4.txt");
        SimpleFormatter sFormat = new SimpleFormatter();
        fh.setFormatter(sFormat);
        logger.addHandler(fh);
        return logger;
    }

    private static void LogCalc(Logger logger, double old_result, double num, String arith, int mode, double result){
        switch (mode) {
            case 1 -> logger.info(old_result + " " + arith + " " + num + " = " + result);
            case 2 -> logger.info("1 / " + old_result + " = " + result);
            case 3 -> logger.info(old_result + " ^ 2 = " + result);
            case 4 -> logger.info("2√" + old_result + " = " + result);
        }
    }

    private static double Calc(Logger logger, double result, double num, int arith){
        double old_result = result;
        switch (arith) {
            case 1 -> {
                result += num;
                LogCalc(logger, old_result, num, "+", 1, result);
            }
            case 2 -> {
                result -= num;
                LogCalc(logger, old_result, num, "-", 1, result);
            }
            case 3 -> {
                result += num;
                LogCalc(logger, old_result, num, "*", 1, result);
            }
            case 4 -> {
                result /= num;
                LogCalc(logger, old_result, num, "/", 1, result);
            }
            case 5 -> {
                result %= num;
                LogCalc(logger, old_result, num, "%", 1, result);
            }
            case 6 -> {
                result = 1/result;
                LogCalc(logger, old_result, num, "+", 2, result);
            }
            case 7 -> {
                result = Math.pow(result, 2);
                LogCalc(logger, old_result, num, "+", 3, result);
            }
            case 8 -> {
                result = Math.pow(result, 1.0/2.0);
                LogCalc(logger, old_result, num, "+", 4, result);
            }
        }
        return result;
    }
}
