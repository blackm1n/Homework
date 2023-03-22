package org.example.datatypes;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Teacher extends User{
    int exp;
    List<Integer> group = new ArrayList<>();

    public Teacher(Date dateBirth, String fio) {
        super(dateBirth, fio);
    }

    public Teacher() {
    }

    public void addGroup(int groupId) {
       group.add(groupId);
    }

    @Override
    public String toString() {
        return "Teacher{" +
                "exp=" + exp +
                ", group=" + group +
                ", dateBirth=" + dateBirth +
                ", fio='" + fio + '\'' +
                ", id=" + id +
                '}';
    }
}
