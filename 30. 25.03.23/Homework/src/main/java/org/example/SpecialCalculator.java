package org.example;

public abstract class SpecialCalculator implements Calculable {

    protected Calculable calculator;

    public SpecialCalculator(Calculable calculator) {
        this.calculator = calculator;
    }
}
