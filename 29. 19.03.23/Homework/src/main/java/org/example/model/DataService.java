package org.example.model;

import org.example.datatypes.User;

import java.util.List;

public interface DataService {
    List<User> read(List<User> users);
}
