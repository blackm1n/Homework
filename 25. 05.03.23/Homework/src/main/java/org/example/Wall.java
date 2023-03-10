package org.example;

public class Wall extends BaseObstacle{

    private int height;

    public Wall(int height) {
        this.height = height;
    }

    public int getHeight() {
        return height;
    }
}
