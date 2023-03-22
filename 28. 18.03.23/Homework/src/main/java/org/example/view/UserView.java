package org.example.view;

import org.example.datatypes.User;

import java.util.List;

public class UserView implements View{

    @Override
    public String userView(List<User> users) {
        return users.toString();
    }

    @Override
    public void info(Object data) {
        System.out.println(data.toString());
    }
}
