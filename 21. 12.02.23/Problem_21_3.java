// Дана json строка, Написать метод(ы), который распарсит json и, используя StringBuilder, создаст строки вида:
// Студент [фамилия] получил [оценка] по предмету [предмет].

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Problem_21_3 {
    public static void main(String[] args) {
        String filepath = GetFilePath();
        String filedata = FileRead(filepath);
        String gradestring = GradeString(filedata);
        System.out.println(gradestring);
    }

    private static String GetFilePath() {
        Scanner input = new Scanner(System.in);
        System.out.print("Введите путь до файла: ");
        return input.nextLine();
    }

    private static String FileRead(String filepath) {
        StringBuilder filedata = new StringBuilder();
        try {
            File myObj = new File(filepath);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                filedata.append(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return filedata.toString();
    }

    private static String GradeString(String filedata) {
        StringBuilder gradestring = new StringBuilder();
        String[] filearray = filedata.replace("[", "").replace("]", "")
                                    .replace("{", "").replace("}", "")
                                    .split(",");
        for (int i = 0; i < filearray.length; i++) {
            String[] values = filearray[i].replace("\"", "").split(":");
            if (i % 3 == 0) {
                if (i != 0){
                    gradestring.append("\n");
                }
                gradestring.append("Студент ");
            } else if (i % 3 == 1) {
                gradestring.append(" получил ");
            }
            else {
                gradestring.append(" по предмету ");
            }
            gradestring.append(values[1]);
        }
        return gradestring.toString();
    }
}

