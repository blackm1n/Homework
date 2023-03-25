package org.example.model;

import org.example.datatypes.Student;
import org.example.datatypes.Teacher;
import org.example.datatypes.User;

public interface UserCreator extends DataService{
    User create(Student student, String fio);
    User create(Teacher teacher, String fio);
}
