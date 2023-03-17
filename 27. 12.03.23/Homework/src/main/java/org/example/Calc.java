package org.example;

import java.util.List;
import java.lang.Math;

public class Calc {
    public Double sum (List<? extends Number> items){
        double sum = 0;
        for (Number i: items)
            sum += i.doubleValue();
        return sum;
    }

    public Double mult (List<? extends Number> items){
        double mult = 0;
        for (int i = 0; i < items.size(); i++) {
            if (i == 0) mult = items.get(i).doubleValue();
            else mult *= items.get(i).doubleValue();
        }
        return mult;
    }

    public Double div (List<? extends Number> items){
        double div = 0;
        for (int i = 0; i < items.size(); i++) {
            if (i == 0) div = items.get(i).doubleValue();
            else div /= items.get(i).doubleValue();
        }
        return div;
    }

    public Double binary (Number item) {
        String[] num = item.toString().split("\\.");
        StringBuilder temp;
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < num.length; i++) {
            temp = new StringBuilder();
            if (i == 0) {
                int number = Integer.parseInt(num[i]);
                while (number > 0) {
                    temp.append(number % 2);
                    number /= 2;
                }
                temp.reverse();
                res.append(temp);
            }
            if (i == 1) {
                res.append(".");
                double number = Double.parseDouble("0." + num[i]);
                while (number > 0) {
                    temp.append((int) (number * 2));
                    number = (number * 2) % 1;
                }
                res.append(temp);
            }
        }
        return Double.valueOf(res.toString());
    }
}
