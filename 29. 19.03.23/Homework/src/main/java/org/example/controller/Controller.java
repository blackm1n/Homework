package org.example.controller;

import org.example.model.Model;
import org.example.datatypes.*;
import org.example.view.*;

import java.util.Collections;
import java.util.List;

public class Controller {

    Model model = new Model();
    View view = new UserView();

    public void createUser(int type, String fio) {
        if (type == 0) view.info(view.userView(Collections.singletonList(model.createStudent(fio))));
        else view.info(view.userView(Collections.singletonList(model.createTeacher(fio))));
    }

    public void createGroup(List<Integer> studentIdList, int teacherId) {
        view.info(view.userView(model.createGroup(studentIdList, teacherId).getUsers()));
    }

    public void viewUsers() {
        view.info(view.userView(model.getUsers()));
    }

    public void viewGroups() {
        for (Group group : model.getGroups()) {
            view.info(view.userView(group.getUsers()));
        }
    }
}
