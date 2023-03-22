package org.example.model;


import org.example.datatypes.Student;
import org.example.datatypes.Teacher;
import org.example.datatypes.User;

import java.util.Date;
import java.util.List;

public class UserService implements DataService{

    @Override
    public User create(Student student, String fio) {
        return new Student(new Date(), fio);
    }

    @Override
    public User create(Teacher teacher, String fio) {
        return new Teacher(new Date(), fio);
    }

    // Функция которая возвращает входное значение... Не использована из-за ее безполезности, но все-равно ее оставил.
    @Override
    public List<User> read(List<User> users) {
        return users;
    }
}
