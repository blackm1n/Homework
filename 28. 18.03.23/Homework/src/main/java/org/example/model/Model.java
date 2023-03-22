package org.example.model;

import org.example.datatypes.*;

import java.util.ArrayList;
import java.util.List;

public class Model {

    DataService dataService = new UserService();
    GroupService groupService = new GroupService();
    List<User> userList = new ArrayList<>();
    List<Group> groupList = new ArrayList<>();

    public Student createStudent(String fio) {
        Student student = (Student) dataService.create(new Student(), fio);
        userList.add(student);
        return student;
    }

    public Teacher createTeacher(String fio) {
        Teacher teacher = (Teacher) dataService.create(new Teacher(), fio);
        userList.add(teacher);
        return teacher;
    }

    public Group createGroup(List<Integer> studentIdList, int teacherId) {
        List<Student> students = new ArrayList<>();
        Teacher groupTeacher = new Teacher();
        Group group = new Group();
        for (User user : userList) {
            if (studentIdList.contains(user.getId())) {
                Student student = (Student) user;
                students.add(student);
                student.setGroupID(group.getId());
            }
            else if (teacherId == user.getId()) {
                Teacher teacher = (Teacher) user;
                groupTeacher = teacher;
                teacher.addGroup(group.getId());
            }
        }
        group = groupService.create(group.getId(), groupTeacher, students);
        groupList.add(group);
        return group;
    }

    public List<User> getUsers() {
        return userList;
    }

    public List<Group> getGroups() {
        return groupList;
    }
}
