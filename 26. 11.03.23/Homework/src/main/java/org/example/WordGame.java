package org.example;

import java.util.ArrayList;
import java.util.List;

public class WordGame extends AbstractGame{

    static String filepath = "src\\main\\java\\org\\example\\english.txt";
    @Override
    List<String> generateCharList() {
        List<String> charList = new ArrayList<String>();
        for (int i = 0; i < 26; ++i) {
            charList.add(String.valueOf((char)(i + 'a')));
        }
        System.out.println(charList);
        return charList;
    }

    @Override
    String getFilePath() {
        return filepath;
    }
}
