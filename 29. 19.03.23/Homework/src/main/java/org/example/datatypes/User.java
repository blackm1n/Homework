package org.example.datatypes;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public abstract class User {

    Date dateBirth;
    String fio;
    int id;
    static List<Integer> idList = new ArrayList<>();

    public User(Date dateBirth, String fio) {
        this.dateBirth = dateBirth;
        this.fio = fio;
        int id = 0;
        while (idList.contains(id)) {
            id += 1;
        }
        idList.add(id);
        this.id = id;
    }

    public User() {
    }

    @Override
    public String toString() {
        return "User{" +
                "dateBirth=" + dateBirth +
                ", fio='" + fio + '\'' +
                ", id=" + id +
                '}';
    }

    public int getId() {
        return id;
    }
}
