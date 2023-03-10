package org.example;

import java.util.ArrayList;

public class Category {

    private int id;
    private String name;
    private ArrayList<Product> products;


    public Category(int id, String name) {
        this.id = id;
        this.name = name;
        this.products = new ArrayList<>();
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

    public void removeProduct(int id) {
        this.products.removeIf(product -> product.getId() == id);
    }

    public int getId() {
        return id;
    }

    public ArrayList<Product> getProducts() {
        return this.products;
    }

    public Product getProduct(int id) {
        for (Product product : this.products) {
            if (product.getId() == id) {
                return product;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        return "Category{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", products=" + products +
                '}';
    }
}
