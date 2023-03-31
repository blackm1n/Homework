package org.example;

public final class Calculator implements Calculable {

    private Complex primaryArg;

    public Calculator(Complex primaryArg) {
        this.primaryArg = primaryArg;
    }

    public Calculator() {
        this.primaryArg = new Complex(0.0, 0.0);
    }

    @Override
    public Calculable sum(Complex arg) {
        Double real1 = primaryArg.getReal();
        Double imaginary1 = primaryArg.getImaginary();
        Double real2 = arg.getReal();
        Double imaginary2 = arg.getImaginary();
        primaryArg = new Complex(real1 + real2, imaginary1 + imaginary2);
        return this;
    }

    @Override
    public Calculable sub(Complex arg) {
        Double real1 = primaryArg.getReal();
        Double imaginary1 = primaryArg.getImaginary();
        Double real2 = arg.getReal();
        Double imaginary2 = arg.getImaginary();
        primaryArg = new Complex(real1 - real2, imaginary1 - imaginary2);
        return this;
    }

    @Override
    public Calculable multi(Complex arg) {
        Double real1 = primaryArg.getReal();
        Double imaginary1 = primaryArg.getImaginary();
        Double real2 = arg.getReal();
        Double imaginary2 = arg.getImaginary();
        primaryArg = new Complex((real1 * real2) - (imaginary1 * imaginary2), (imaginary1 * real2) + (real1 * imaginary2));
        return this;
    }

    @Override
    public Calculable div(Complex arg) {
        Double real1 = primaryArg.getReal();
        Double imaginary1 = primaryArg.getImaginary();
        Double real2 = arg.getReal();
        Double imaginary2 = arg.getImaginary();
        primaryArg = new Complex(((real1 * real2) + (imaginary1 * imaginary2)) / ((real2 * real2) + (imaginary2 * imaginary2)), ((imaginary1 * real2) - (real1 * imaginary2)) / ((real2 * real2) + (imaginary2 * imaginary2)));
        return this;
    }

    @Override
    public Complex getResult() {
        return primaryArg;
    }
}
