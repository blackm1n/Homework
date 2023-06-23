import java.util.Date;
import java.util.LinkedList;
import java.util.Queue;

class HashMap {
    private class Entity {
        int key;
        int value;
    }

    private class Basket { // СЃРїРёСЃРѕРє
        private Node head;

        class Node {
            Entity entity;
            Node next;
        }

        public Integer find(int key) { // O(N) -> O(1)
            Node node = head;
            while (node != null) {
                if (node.entity.key == key) {
                    return node.entity.value;
                }
                node = node.next;
            }
            return null;
        }

        public boolean push(int key, int value) {
            Node node = new Node();
            node.entity = new Entity();
            node.entity.key = key;
            node.entity.value = value;

            if (head == null) {
                head = node;
            } else {
                Node cur = head;

                while (cur.next != null) {
                    if (cur.entity.key == key) {
                        return false;
                    }
                    cur = cur.next;
                }
                cur.next = node;
            }
            return true;
        }
    }

    final static int INIT_SIZE = 16;
    private Basket[] baskets;

    public HashMap(int size) {
        baskets = new Basket[size];
    }

    public HashMap() {
        this(INIT_SIZE);
    }

    public int getIndex(int key) { // O(1)
        return key % baskets.length; // [0, baskets.length - 1]
    }

    public Integer find(int key) {
        int index = getIndex(key);
        Basket basket = baskets[index];
        if (basket == null)
            return null;
        return basket.find(key);
    }

    public boolean push(int key, int value) {
        int index = getIndex(key);
        Basket basket = baskets[index];
        if (basket == null) {
            Basket b = new Basket();
            boolean res = b.push(key, value);
            baskets[index] = b;
            return res;
        } else {
            return basket.push(key, value);
        }
    }
}

class BinaryTree {
    Node root;

    class Node {
        int value;
        Node left;
        Node right;
        Color color;
    }

    enum Color {
        RED,
        BLACK
    }

    public void add(int value) {
        if (root != null) {
            addNode(root, value);
            root = balance(root);
            root.color = Color.BLACK;
        }
        else {
            root = new Node();
            root.color = Color.BLACK;
            root.value = value;
        }
    }

    private void addNode(Node node, int value) {
        if (node.value != value) {
            if (node.value > value) {
                if (node.left != null) {
                    addNode(node.left, value);
                    node.left = balance(node.left);
                }
                else {
                    node.left = new Node();
                    node.left.color = Color.RED;
                    node.left.value = value;
                }
            }
            else {
                if (node.right != null) {
                    addNode(node.right, value);
                    node.right = balance(node.right);
                }
                else {
                    node.right = new Node();
                    node.right.color = Color.RED;
                    node.right.value = value;
                }
            }
        }
    }

    public Node balance(Node node) {
        Node result = node;
        boolean needBalance;
        do {
            needBalance = false;
            if (result.right != null && result.right.color == Color.RED && (result.left == null || result.left.color == Color.BLACK)) {
                needBalance = true;
                result = rightTurn(result);
            }
            if (result.left != null && result.left.color == Color.RED && result.left.left != null && result.left.left.color == Color.RED) {
                needBalance = true;
                result = leftTurn(result);
            }
            if (result.left != null && result.left.color == Color.RED && result.right != null && result.right.color == Color.RED) {
                needBalance = true;
                swapColor(result);
            }
        } while (needBalance);
        return result;
    }

    public Node leftTurn(Node node) {
        Node left = node.left;
        Node between = left.right;
        left.right = node;
        node.left = between;
        left.color = node.color;
        node.color = Color.RED;
        return left;
    }

    public Node rightTurn(Node node) {
        Node right = node.right;
        Node between = right.left;
        right.left = node;
        node.right = between;
        right.color = node.color;
        node.color = Color.RED;
        return right;
    }

    public void swapColor(Node node) {
        node.color = Color.RED;
        node.left.color = Color.BLACK;
        node.right.color = Color.BLACK;
    }

    public boolean find(int value) { // O(log N)
        Node cur = root;
        while (cur != null) {
            if (cur.value == value) {
                return true;
            }
            if (cur.value < value) {
                cur = cur.right;
            } else {
                cur = cur.left;
            }
        }
        return false;
    }


    public void print() {
        print(root);
    }

    private void print(Node node) {
        if (node == null)
            return;
        System.out.println(node.value + " " + node.color);

        if (node.left != null)
            System.out.println("L:" + node.left.value + " " + node.left.color);

        if (node.right != null)
            System.out.println("R:" + node.right.value + " " + node.right.color);

        print(node.left);
        print(node.right);
    }

}

public class Main2 {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        for (int i = 1; i <= 10; i++) {
            tree.add(i);
        }
        tree.print();
    }
}