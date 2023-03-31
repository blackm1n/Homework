package org.example;

public class CalculableFactory implements ICalculableFactory {
    public Calculable create(Complex primaryArg) {
        return new Calculator(primaryArg);
    }

    public Calculable create() {
        return new Calculator();
    }
}
