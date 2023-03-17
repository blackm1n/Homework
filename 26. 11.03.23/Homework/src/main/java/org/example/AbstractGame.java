package org.example;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

@Data
@AllArgsConstructor
@NoArgsConstructor
public abstract class AbstractGame implements Game {
    Integer sizeWord;
    String word;
    Integer maxTry;
    int countTry;
    GameStatus gameStatus = GameStatus.INIT;
    List<Answer> history = new ArrayList<>();

    private String generateWord() {
        List<String> charList = generateCharList();
        SecureRandom random = new SecureRandom();
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < sizeWord; i++) {
            int randomIndex = random.nextInt(charList.size());
            res.append(charList.get(randomIndex));
            charList.remove(randomIndex);
        }
        return res.toString();
    }

    private String wordFromFile() {
        SecureRandom random = new SecureRandom();
        List<String> words = new ArrayList<>();
        try {
            File myObj = new File(getFilePath());
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                words.add(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        String res = "";
        while (res.equals("")) {
            String word = words.get(random.nextInt(words.size())).toLowerCase();
            if (!word.contains(" ") && !word.contains("-") && !word.contains(".") && word.length() == sizeWord) {
                res = word;
            }
        }
        return res;
    }

    @Override
    public void start(Integer sizeWord, Integer maxTry, int type) {
        this.maxTry = maxTry;
        this.sizeWord = sizeWord;
        this.countTry = 1;
        if (type == 1) {
            word = generateWord();
        }
        else {
            word = wordFromFile();
        }
        this.gameStatus = GameStatus.START;
    }

    @Override
    public Answer inputAnswer(String value) {
        int bull = 0;
        int cow = 0;
        for (int i = 0; i < value.length(); i++) {
            if (word.contains(Character.toString(value.charAt(i)))) {
                cow++;
            }
            if (word.charAt(i) == value.charAt(i)) {
                bull++;
            }
        }
        countTry++;
        Answer answer = new Answer(cow, bull, value);
        history.add(answer);
        gameStatus = checkState(value);
        return answer;
    }

    private GameStatus checkState(String value) {
        if (value.equals(word)) {
            return gameStatus = GameStatus.WIN;
        } else {
            if (countTry > maxTry) {
                return gameStatus = GameStatus.LOSE;
            } else {
                return gameStatus = GameStatus.START;
            }
        }
    }

    abstract List<String> generateCharList();
    abstract String getFilePath();
}

