package org.example.datatypes;

import java.util.ArrayList;
import java.util.List;

public class Group {

    int id;
    Teacher teacher;
    List<Student> studentList;
    static List<Integer> idList = new ArrayList<>();

    public Group(int id, Teacher teacher, List<Student> studentList) {
        this.id = id;
        this.teacher = teacher;
        this.studentList = studentList;
    }

    public Group() {
        int id = 0;
        while (idList.contains(id)) {
            id += 1;
        }
        idList.add(id);
        this.id = id;
    }

    public List<User> getUsers() {
        List<User> userList = new ArrayList<>();
        userList.add(teacher);
        userList.addAll(studentList);
        return userList;
    }

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "Group{" +
                "teacher=" + teacher +
                ", studentList=" + studentList +
                '}';
    }
}
