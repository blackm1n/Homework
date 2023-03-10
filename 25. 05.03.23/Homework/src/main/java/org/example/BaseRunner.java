package org.example;

public abstract class BaseRunner {

    protected String name;
    protected double runSpeed;
    protected double jumpHeight;
    protected int state;

    public BaseRunner(String name, double runSpeed, double jumpHeight) {
        this.name = name;
        this.runSpeed = runSpeed;
        this.jumpHeight = jumpHeight;
    }

    public void startCourse(BaseObstacle[] course) {
        int time = 0;
        for (BaseObstacle obstacle : course) {
            if (checkState()) {
                if (obstacle instanceof Track) {
                    time += run((Track) obstacle);
                }
                else if (obstacle instanceof Wall) {
                    if (!jump((Wall) obstacle)) {
                        this.state = -1;
                    }
                    time += 1;
                }
            } else {
                System.out.println(this.name + " не преодолел набор препятствий. Бежал он " + time + " единиц времени.");
                return;
            }
        }
        System.out.println(this.name + " смог преодолеть данный набор препятсвия с временем " + time + " единиц времени!");
    }

    public abstract int run(Track track);

    public abstract boolean jump(Wall wall);

    public abstract boolean checkState();
}
