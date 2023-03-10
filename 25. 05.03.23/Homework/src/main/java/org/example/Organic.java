package org.example;

public class Organic extends BaseRunner{

    protected int stamina;
    protected int health;
    protected int staminaConsumption;
    protected int healthConsumption;
    public Organic(String name, double runSpeed, double jumpHeight, int stamina, int health, int staminaConsumption, int healthConsumption) {
        super(name, runSpeed, jumpHeight);
        this.stamina = stamina;
        this.health = health;
        this.staminaConsumption = staminaConsumption;
        this.healthConsumption = healthConsumption;
    }

    @Override
    public int run(Track track) {
        int time = 0;
        int length = track.getLength();
        while (length > 0) {
            if (checkState()) {
                if (stamina > 0) {
                    time++;
                    this.stamina -= this.staminaConsumption;
                    length -= this.runSpeed;
                }
                else {
                    time++;
                    this.health -= this.healthConsumption;
                    length -= this.runSpeed;
                }
            }
            else {
                return time;
            }
        }
        return time;
    }

    @Override
    public boolean jump(Wall wall) {
        int height = wall.getHeight();
        if (height > this.jumpHeight) {
            return false;
        }
        if (stamina > 0) {
            this.stamina -= this.staminaConsumption;
        }
        else {
            this.health -= this.healthConsumption;
        }
        return true;
    }

    @Override
    public boolean checkState() {
        if (state == 0 && this.stamina <= 0) {
            this.runSpeed /= 10;
            this.jumpHeight /= 10;
            this.state = 1;
        }
        else if (state == 1 && this.health <= 0) {
            return false;
        }
        else return state != -1;
        return true;
    }
}
