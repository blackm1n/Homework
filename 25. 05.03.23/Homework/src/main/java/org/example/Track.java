package org.example;

public class Track extends BaseObstacle{

    private int length;

    public Track(int length) {
        this.length = length;
    }

    public int getLength() {
        return length;
    }
}
