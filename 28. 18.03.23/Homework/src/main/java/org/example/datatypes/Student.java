package org.example.datatypes;

import java.util.Date;
import java.util.List;

public class Student extends User{
    int groupID = -1;
    List<Integer> grade;

    public Student(Date dateBirth, String fio) {
        super(dateBirth, fio);
    }

    public Student() {
    }

    public void setGroupID(int groupID) {
        this.groupID = groupID;
    }

    @Override
    public String toString() {
        return "Student{" +
                "groupID=" + groupID +
                ", grade=" + grade +
                ", dateBirth=" + dateBirth +
                ", fio='" + fio + '\'' +
                ", id=" + id +
                '}';
    }
}
