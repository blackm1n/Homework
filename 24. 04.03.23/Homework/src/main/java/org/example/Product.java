package org.example;

import java.util.ArrayList;
import java.util.Random;

public class Product {

    private int id;
    private String name;
    private int price;
    private int count;
    private double rating;
    private ArrayList<Integer> ratingList = new ArrayList<>();
    private static Random random = new Random();

    public Product(int id, String name, int price, int count, double rating, ArrayList<Integer> ratingList) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.count = count;
        this.rating = rating;
        this.ratingList = ratingList;
    }

    public Product(int id, String name, int price, int count) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.count = count;
        for (int i = 0; i < 10; i++) {
            ratingList.add(random.nextInt(0, 11));
        }
        this.evaluateRating();
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    public ArrayList<Integer> getRatingList() {
        return ratingList;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public void addCount(int count) {
        this.count += count;
    }

    public void removeCount(int count) {
        if (this.count >= count) {
            this.count -= count;
        } else {
            this.count = 0;
        }
    }

    public void addRating(int rating) {
        this.ratingList.add(rating);
        this.evaluateRating();
    }

    public void evaluateRating() {
        this.rating = 0;
        for (int i : this.ratingList) {
            this.rating += i;
        }
        this.rating /= this.ratingList.size();
    }

    public Product copyProduct() {
        return new Product(this.id, this.name, this.price, this.count, this.rating, this.ratingList);
    }

    @Override
    public String toString() {
        return String.format("Product{id=%s, name='%s', price=%d, count=%d, rating=%.2f}", this.id, this.name, this.price, this.count, this.rating);
    }
}
