package org.example;

import java.util.Random;

public class Application {
    public static void main(String[] args) {
        Game game = null;
        while (game == null) {
            switch (UI.chooseGame()) {
                case 1 -> game = new NumberGame();
                case 2 -> game = new WordGame();
                case 3 -> game = new WordRussianGame();
                default -> UI.gameNotExist();
            }
        }
        Random random = new Random();
        int length = 0;
        while (length == 0) {
            switch (UI.chooseDiff()) {
                case 1 -> length = random.nextInt(3, 5);
                case 2 -> length = random.nextInt(5, 7);
                case 3 -> length = random.nextInt(7, 9);
                default -> UI.diffNotExist();
            }
        }
        if (game instanceof NumberGame) {
            game.start(length, 6, 1);
        }
        else {
            while (game.getGameStatus().equals(GameStatus.INIT)) {
                switch (UI.chooseType()) {
                    case 1 -> game.start(length, 6, 1);
                    case 2 -> game.start(length, 6, 2);
                    default -> UI.typeNotExist();
                }
            }
        }
        if (game.getWord().length() <= 4) {
            System.out.println(game.getWord().length() + " символа");
        }
        else {
            System.out.println(game.getWord().length() + " символов");
        }
        while (game.getGameStatus().equals(GameStatus.START)) {
            String answer = UI.writeAnswer(game.getCountTry());
            Answer answerGame = game.inputAnswer(answer);
            System.out.printf("Найдено %d коров и %d быков%n", answerGame.getCows(), answerGame.getBulls());
        }
        UI.showWord(game.getGameStatus(), game.getWord());
        if (UI.chooseHistory() == 1) {
            UI.showHistory(game.getHistory());
        }
    }
}
