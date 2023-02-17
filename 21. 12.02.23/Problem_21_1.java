// Дана строка sql-запроса "select * from students where ". Сформируйте часть WHERE этого запроса, используя StringBuilder.

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Problem_21_1 {
    public static void main(String[] args) {
        String filepath = GetFilePath();
        String filedata = FileRead(filepath);
        String sqlquery = SQLQuery(filedata);
        System.out.println(sqlquery);
    }

    private static String GetFilePath(){
        Scanner input = new Scanner(System.in);
        System.out.print("Введите путь до файла: ");
        return input.nextLine();
    }

    private static String FileRead(String filepath){
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

    private static String SQLQuery(String filedata){
        StringBuilder sqlquery = new StringBuilder();
        sqlquery.append("SELECT * FROM students WHERE");
        String[] filearray = filedata.replace("{", "").replace("}", "")
                                    .split(", ");
        for (int i = 0; i < filearray.length; i++) {
            String[] where = filearray[i].split(":");
            if (!where[1].replace("\"", "").equals("null")) {
                if (i != 0){
                    sqlquery.append(" AND");
                }
                sqlquery.append(" ").append(where[0].replace("\"", "")).append(" = ").append(where[1]);
            }
        }
        return sqlquery.toString();
    }
}
