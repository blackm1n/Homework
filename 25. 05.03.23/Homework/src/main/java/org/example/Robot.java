package org.example;

public class Robot extends Mechanic{

    private static int count;

    public Robot(String name, int runSpeed, int jumpHeight, int fuel, int fuelConsumption) {
        super(name, runSpeed, jumpHeight, fuel, fuelConsumption);
        count++;
    }

    public static int getCount() {
        return count;
    }
}
