package org.example;

public class Cat extends Organic{

    private static int count;

    public Cat(String name, int runSpeed, int jumpHeight, int stamina, int health, int staminaConsumption, int healthConsumption) {
        super(name, runSpeed, jumpHeight, stamina, health, staminaConsumption, healthConsumption);
        count++;
    }

    public static int getCount() {
        return count;
    }
}
