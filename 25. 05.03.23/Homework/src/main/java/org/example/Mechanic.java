package org.example;

public class Mechanic extends BaseRunner{

    protected int fuel;
    protected int fuelConsumption;

    public Mechanic(String name, int runSpeed, int jumpHeight, int fuel, int fuelConsumption) {
        super(name, runSpeed, jumpHeight);
        this.fuel = fuel;
        this.fuelConsumption = fuelConsumption;
    }

    @Override
    public int run(Track track) {
        int time = 0;
        int length = track.getLength();
        while (length > 0) {
            if (checkState()) {
                time++;
                this.fuel -= this.fuelConsumption;
                length -= this.runSpeed;
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
        this.fuel -= this.fuelConsumption;
        return true;
    }

    @Override
    public boolean checkState() {
        if (state == 0 && this.fuel <= 0) {
            return false;
        }
        else return state != -1;
    }
}
