import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;
import java.util.Arrays;
import java.util.Scanner;

public class Problem_50_1 {

    public static void main(String[] args) {
        savePerson();
    }

    public static void savePerson() {
        String input = inputValues("Введите Фамилию, Имя, Отчество, Дату Рождения, Номер Телефона и пол разделенные пробелом.");

        if (input.equals("42")) {
            System.out.println("Вы ввели меньше или больше данных чем требуется");
            return;
        }

        try {
            String[] parsedInput = parseInput(input);
            try (BufferedWriter bw = new BufferedWriter(new FileWriter("50. 01.06.23 - 2\\" + parsedInput[0] + ".txt", true))) {
                bw.write(input);
                bw.newLine();
            }
            catch (IOException e) {
                System.out.println("Ошибка при записи в файл");
                System.out.println(Arrays.toString(e.getStackTrace()));
            }
        } catch (DateTimeParseException e) {
            System.out.println("Дата должна быть в формате YYYY-MM-DD");
        } catch (NumberFormatException e) {
            System.out.println("Номер телефона должен быть целым, беззнаковым числом.");
        } catch (GenderParseException e) {
            System.out.println("Пол может быть только m или f");
        }
    }

    public static String inputValues(String mes) {
        Scanner in = new Scanner(System.in);
        System.out.println(mes);
        String res = in.nextLine();
        if (res.split(" ").length != 6) {
            return "42";
        }
        return res;
    }

    public static String[] parseInput(String input) throws DateTimeParseException, NumberFormatException, GenderParseException {
        String[] in = input.split(" ");
        for (int i = 0; i < 6; i++) {
            switch (i) {
                case 3: {
                    LocalDate.parse(in[i]);
                    break;
                }
                case 4: {
                    int num = Integer.parseInt(in[i]);
                    if (num < 0) {
                        throw new NumberFormatException("Число имеет знак");
                    }
                    break;
                }
                case 5: {
                    if (!in[i].equals("f") && !in[i].equals("m")) {
                        throw new GenderParseException("Ошибка ввода пола");
                    }
                    break;
                }
            }
        }
        return in;
    }
}

class GenderParseException extends Exception {

    public GenderParseException(String s) {
        super(s);
    }
}
