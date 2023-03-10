package org.example;

public class User {

    private String login;
    private String password;
    private Basket basket;
    private int money;
    private int key;

    public User(String login, String password, Shop shop) {
        this.login = login;
        this.password = password;
        this.money = 0;
        this.basket = new Basket();
        this.key = shop.getKey();
    }

    public void addMoney(int money) {
        this.money += money;
    }

    public Basket getBasket() {
        return basket;
    }

    public int getMoney() {
        return money;
    }

    public void leaveRating(Shop shop, int id, int rating) {
        if (!shop.checkKey(this.key)) {
            System.out.println("Вы не зарегистрированы в этом магазине");
            return;
        }
        Product product = shop.getProduct(id);
        product.addRating(rating);
        System.out.printf("%s оценил %s на %d/10\n", this.login, product.getName(), rating);
    }

    public void addToBasket(Shop shop, int id, int count) {
        if (!shop.checkKey(this.key)) {
            System.out.println("Вы не зарегистрированы в этом магазине");
            return;
        }
        Product product = shop.getProduct(id);
        if (product.getCount() == 0) {
            System.out.println("Таково товара нет в начилие");
            return;
        }
        if (this.basket.getProduct(id) != null) {
            this.basket.getProduct(id).addCount(count);
        } else {
            this.basket.addProduct(product.copyProduct());
            this.basket.getProduct(id).setCount(count);
        }
        if (product.getCount() < this.basket.getProduct(id).getCount()) {
            this.basket.getProduct(id).setCount(product.getCount());
        }
        this.basket.countPrice();
    }

    public void removeFromBasket(Shop shop, int id, int count) {
        if (!shop.checkKey(this.key)) {
            System.out.println("Вы не зарегистрированы в этом магазине");
            return;
        }
        Product product = this.basket.getProduct(id);
        if (product == null) {
            System.out.println("Таково товара нет в корзине");
            return;
        }
        if (product.getCount() >= count) {
            product.removeCount(count);
        } else {
            this.basket.removeProduct(id);
        }
        this.basket.countPrice();
    }

    public void buyBasket(Shop shop) {
        if (!shop.checkKey(this.key)) {
            System.out.println("Вы не зарегистрированы в этом магазине");
            return;
        }
        if (this.basket.getTotalPrice() <= this.money) {
            int size = this.basket.getLength();
            for (int i = 0; i < size; i++) {
                Product product = this.basket.getProducts().get(0);
                this.money -= product.getPrice() * product.getCount();
                shop.removeCount(product.getId(), product.getCount());
                this.basket.removeProduct(product.getId());
                this.basket.countPrice();
                System.out.printf("%s купил %d %s за %d\n", this.login, product.getCount(), product.getName(), product.getPrice());
            }
        } else {
            System.out.println("Недостаточно денег для покупки");
        }
    }
}
