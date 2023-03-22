package org.example.model;

import org.example.datatypes.Student;
import org.example.datatypes.Teacher;
import org.example.datatypes.User;

import java.util.List;

public interface DataService {
    User create(Student student, String fio);
    User create(Teacher teacher, String fio);
    List<User> read(List<User> users);
}
