package org.example;

public interface ICalculableFactory {
    Calculable create(Complex primaryArg);
    Calculable create();
}
