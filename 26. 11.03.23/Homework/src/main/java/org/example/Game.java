package org.example;

import java.util.List;

public interface Game {
    void start( Integer sizeWord, Integer maxTry, int type);
    Answer inputAnswer(String value);
    GameStatus getGameStatus();

    int getCountTry();

    List<Answer> getHistory();

    String getWord();
}
