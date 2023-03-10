package org.example;

import java.util.ArrayList;
import java.util.Random;

public class Shop {

    private String name;
    private ArrayList<Category> categories;
    private ArrayList<Product> products;
    private ArrayList<Integer> productIdList;
    private ArrayList<Integer> categoryIdList;
    private int key;
    private static ArrayList<Integer> keyList = new ArrayList<>();
    private static Random random = new Random();

    public Shop(String name) {
        this.name = name;
        this.products = new ArrayList<>();
        this.categories = new ArrayList<>();
        this.productIdList = new ArrayList<>();
        this. categoryIdList = new ArrayList<>();
        int key = random.nextInt(100000, 1000000);
        while (keyList.contains(key)) {
            key = random.nextInt(100000, 1000000);
        }
        this.key = key;
    }

    public void addCategory(String name) {
        int id = 0;
        while (this.categoryIdList.contains(id)) {
            id++;
        }
        this.categoryIdList.add(id);
        Category category = new Category(id, name);
        this.categories.add(category);
    }

    public void addProduct(String name, int price, int count) {
        int id = 0;
        while (this.productIdList.contains(id)) {
            id++;
        }
        this.productIdList.add(id);
        Product product = new Product(id, name, price, count);
        this.products.add(product);
    }

    public void addCount(int id, int count) {
        for (Product product : this.products) {
            if (product.getId() == id) {
                product.addCount(count);
            }
        }
    }

    public void removeCount(int id, int count) {
        for (Product product : this.products) {
            if (product.getId() == id) {
                product.removeCount(count);
            }
        }
    }

    public ArrayList<Category> getCategories() {
        return categories;
    }

    public ArrayList<Product> getProducts() {
        return products;
    }

    public Category getCategory(int id) {
        for (Category category : this.categories) {
            if (category.getId() == id) {
                return category;
            }
        }
        return null;
    }

    public Product getProduct(int id) {
        for (Product product : this.products) {
            if (product.getId() == id) {
                return product;
            }
        }
        return null;
    }

    public int getKey() {
        return this.key;
    }

    public boolean checkKey(int key) {
        return this.key == key;
    }
}
