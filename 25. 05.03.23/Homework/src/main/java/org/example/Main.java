package org.example;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        BaseRunner[] runners = new BaseRunner[20];
        BaseObstacle[] obstacles = new BaseObstacle[10];
        Random random = new Random();

        // Можно тестировать различные рандомные характеристики и проверять их исход.
        int randClass;
        for (int i = 0; i < runners.length; i++) {
            randClass = random.nextInt(0, 3);
            if (randClass == 0) {
                runners[i] = new Human("Человек " + (Human.getCount() + 1), random.nextInt(10, 17), random.nextInt(25, 60), random.nextInt(75, 125), 100, random.nextInt(2, 8), random.nextInt(2, 8));
            }
            else if (randClass == 1) {
                runners[i] = new Cat("Кот " + (Cat.getCount() + 1), random.nextInt(25, 40), random.nextInt(80, 120), random.nextInt(90, 140), 20, random.nextInt(6, 15), random.nextInt(2, 8));
            }
            else if (randClass == 2) {
                runners[i] = new Robot("Робот " + (Robot.getCount() + 1), random.nextInt(20, 30), random.nextInt(70, 120), 250, random.nextInt(2, 10));
            }
        }
        for (int i = 0; i < obstacles.length; i++) {
            randClass = random.nextInt(0, 2);
            if (randClass == 0) {
                obstacles[i] = new Track(random.nextInt(50, 100));
            }
            else if (randClass == 1) {
                obstacles[i] = new Wall(random.nextInt(35, 50));
            }
        }

        for (BaseRunner runner : runners) {
            runner.startCourse(obstacles);
        }
    }
}