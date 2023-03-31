package org.example;

public interface Calculable {
    Calculable sum(Complex arg);
    Calculable sub(Complex arg);
    Calculable multi(Complex arg);
    Calculable div(Complex arg);
    Complex getResult();
}
