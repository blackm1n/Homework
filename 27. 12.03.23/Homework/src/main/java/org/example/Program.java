package org.example;

import java.util.ArrayList;
import java.util.Arrays;

public class Program {
    public static void main(String[] args) {
        Calc calc1 = new Calc();
        System.out.println(calc1.sum(new ArrayList<>(Arrays.asList(1.0, 2.0, 3.5))));
        System.out.println(calc1.mult(new ArrayList<>(Arrays.asList(1.0, 2.0, 3.5))));
        System.out.println(calc1.div(new ArrayList<>(Arrays.asList(3.5, 2.0, 1.0))));
        System.out.println(calc1.binary(3.5));
    }
}