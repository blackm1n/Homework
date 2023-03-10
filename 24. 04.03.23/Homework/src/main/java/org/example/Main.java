package org.example;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();

        Shop shop1 = new Shop("Shop 1");

        shop1.addProduct("Product 1", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 2", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 3", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 4", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 5", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 6", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 7", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 8", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 9", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 10", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 11", random.nextInt(100, 1000), random.nextInt(1, 10));
        shop1.addProduct("Product 12", random.nextInt(100, 1000), random.nextInt(1, 10));

        shop1.addCategory("Category 1");
        shop1.addCategory("Category 2");
        shop1.addCategory("Category 3");

        Category category1 = shop1.getCategory(0);
        category1.addProduct(shop1.getProduct(0));
        category1.addProduct(shop1.getProduct(1));
        category1.addProduct(shop1.getProduct(2));
        category1.addProduct(shop1.getProduct(3));

        Category category2 = shop1.getCategory(1);
        category2.addProduct(shop1.getProduct(4));
        category2.addProduct(shop1.getProduct(5));
        category2.addProduct(shop1.getProduct(6));
        category2.addProduct(shop1.getProduct(7));

        Category category3 = shop1.getCategory(2);
        category3.addProduct(shop1.getProduct(8));
        category3.addProduct(shop1.getProduct(9));
        category3.addProduct(shop1.getProduct(10));
        category3.addProduct(shop1.getProduct(11));

        System.out.println(shop1.getCategories());

        User user1 = new User("user1", "password1", shop1);
        User user2 = new User("user2", "password2", shop1);
        User user3 = new User("user3", "password3", shop1);

        user1.addMoney(random.nextInt(1000,10000));
        user1.addToBasket(shop1, random.nextInt(0, 12), random.nextInt(1, 4));
        user1.buyBasket(shop1);

        user2.addMoney(random.nextInt(1000,10000));
        user2.addToBasket(shop1, random.nextInt(0, 12), random.nextInt(1, 4));
        user2.addToBasket(shop1, 5, 1);
        user2.buyBasket(shop1);
        user2.leaveRating(shop1, 5, 8);

        user3.addMoney(random.nextInt(1000,10000));
        user3.addToBasket(shop1, random.nextInt(0, 12), random.nextInt(1, 4));
        user3.buyBasket(shop1);
    }
}