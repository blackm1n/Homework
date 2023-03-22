package org.example;

import org.example.controller.Controller;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Controller controller = new Controller();

        for (int i = 0; i < 20; i++) {
            controller.createUser(0, "student" + i);
        }

        for (int i = 0; i < 2; i++) {
            controller.createUser(1, "teacher" + i);
        }

        System.out.println();

        controller.viewUsers();

        System.out.println();

        for (int i = 0; i < 4; i++) {
            controller.createGroup(Arrays.asList((5 * i), 1 + (5 * i), 2 + (5 * i), 3 + (5 * i), 4 + (5 * i)), 20 + (i % 2));
        }

        System.out.println();

        controller.viewGroups();
    }
}
