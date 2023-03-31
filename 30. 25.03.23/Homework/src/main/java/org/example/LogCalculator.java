package org.example;

import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class LogCalculator extends SpecialCalculator {

    private Logger logger;

    public LogCalculator(Calculable calculator) throws IOException {
        super(calculator);
        logger = Logger.getLogger(LogCalculator.class.getName());
        FileHandler fh = new FileHandler("log.txt");
        SimpleFormatter sFormat = new SimpleFormatter();
        fh.setFormatter(sFormat);
        logger.addHandler(fh);
    }

    private void log(Complex old_result, Complex num, String arith, Complex result) {
        logger.info("("+old_result+")" + arith + "("+num+")="+result);
    }

    @Override
    public Calculable sum(Complex arg) {
        Complex oldResult = calculator.getResult();
        calculator.sum(arg);
        this.log(oldResult, arg, "+", calculator.getResult());
        return this;
    }

    @Override
    public Calculable sub(Complex arg) {
        Complex oldResult = calculator.getResult();
        calculator.sub(arg);
        this.log(oldResult, arg, "-", calculator.getResult());
        return this;
    }

    @Override
    public Calculable multi(Complex arg) {
        Complex oldResult = calculator.getResult();
        calculator.multi(arg);
        this.log(oldResult, arg, "*", calculator.getResult());
        return this;
    }

    @Override
    public Calculable div(Complex arg) {
        Complex oldResult = calculator.getResult();
        calculator.div(arg);
        this.log(oldResult, arg, "/", calculator.getResult());
        return this;
    }

    @Override
    public Complex getResult() {
        return calculator.getResult();
    }
}
