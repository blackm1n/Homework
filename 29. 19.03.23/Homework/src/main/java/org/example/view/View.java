package org.example.view;

import org.example.datatypes.User;

import java.util.List;

public interface View {
    String userView (List<User> users);

    void info(Object data);
}
