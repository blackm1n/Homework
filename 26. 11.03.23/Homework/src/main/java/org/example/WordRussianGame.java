package org.example;

import java.util.ArrayList;
import java.util.List;

public class WordRussianGame extends AbstractGame{

    static String filepath = "src\\main\\java\\org\\example\\russian.txt";

    @Override
    List<String> generateCharList() {
        List<String> charList = new ArrayList<String>();
        for (int i = 0; i < 32; ++i) {
            charList.add(String.valueOf((char)(i + 'а')));
        }
        System.out.println(charList);
        return charList;
    }

    @Override
    String getFilePath() {
        return filepath;
    }
}
