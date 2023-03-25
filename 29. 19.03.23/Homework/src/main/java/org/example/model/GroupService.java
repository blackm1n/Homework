package org.example.model;

import org.example.datatypes.Group;
import org.example.datatypes.Student;
import org.example.datatypes.Teacher;
import org.example.datatypes.User;

import java.util.List;

public class GroupService implements GroupCreator {

    public Group create(int id, Teacher teacher, List<Student> studentList) {
        return new Group(id, teacher, studentList);
    }

    @Override
    public List<User> read(List<User> users) {
        return users;
    }
}
