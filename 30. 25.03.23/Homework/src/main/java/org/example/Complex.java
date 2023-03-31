package org.example;

public class Complex {
    private Double real;
    private Double imaginary;

    public Complex(Double real, Double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    public Double getReal() {
        return real;
    }

    public Double getImaginary() {
        return imaginary;
    }

    @Override
    public String toString() {
        if (imaginary > 0.0) {
            return real + "+" + imaginary + "i";
        }
        else if (imaginary < 0.0) {
            return String.valueOf(real) + imaginary + "i";
        }
        else return String.valueOf(real);
    }
}
