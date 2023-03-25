package org.example.model;

import org.example.datatypes.Group;
import org.example.datatypes.Student;
import org.example.datatypes.Teacher;

import java.util.List;

public interface GroupCreator extends DataService{
    Group create(int id, Teacher teacher, List<Student> studentList);
}
