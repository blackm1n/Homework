package org.example;

import java.util.ArrayList;

public class Basket {

    private ArrayList<Product> products;
    private int totalPrice;


    public Basket() {
        this.products = new ArrayList<>();
        this.totalPrice = 0;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

    public void removeProduct(int id) {
        this.products.removeIf(product -> product.getId() == id);
    }

    public void countPrice() {
        this.totalPrice = 0;
        for (Product product : this.products) {
            this.totalPrice += product.getPrice() * product.getCount();
        }
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

    public int getTotalPrice() {
        return this.totalPrice;
    }

    public int getLength() {
        return this.products.size();
    }

    @Override
    public String toString() {
        return "Basket{" +
                "products=" + this.products +
                ", totalPrice=" + this.totalPrice +
                '}';
    }
}
