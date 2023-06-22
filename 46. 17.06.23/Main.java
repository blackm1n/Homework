import java.util.Date;

class List{
    static Node head;
    static class Node{
        int value;
        Node next;
    }

    public static void pushFront(int value){ // O(1)
        Node node = new Node();
        node.value = value;
        node.next = head;
        head = node;
    }

    public static void popFront(){ // O(1)
        if(head != null){
            head = head.next;
        }
    }

    public static void print(){
        Node node = head;
        while(node != null){
            System.out.printf("%d ", node.value);
            node = node.next;
        }
        System.out.println();
    }

    public static boolean contains(int value){
        Node node = head;
        while(node != null){
            if(node.value == value){
                return true;
            }
            node = node.next;
        }
        return false;
    }

    public static void pushBack(int value){ // O(N)
        Node node = new Node();
        node.value = value;

        if(head == null){
            head = node;
        }else{
            Node cur = head;
            while(cur.next != null){
                cur = cur.next;
            }

            cur.next = node;
        }
    }

    public static void popBack(){ // O(N)
        if(head != null){
            if(head.next == null){
                head = null;
            }else {
                Node cur = head;
                while (cur.next.next != null) {
                    cur = cur.next;
                }
                cur.next = null;
            }
        }
    }

    public static void reverse(){
        // Мне кажется можно сделать это и получше, но хотя-бы работает.
        Node node1 = head;
        if (node1.next != null) {
            Node node2 = node1.next;
            node1.next = null;
            if (node2.next == null) {
                node2.next = node1;
                head = node2;
            }
            else {
                while (node2 != null) {
                    Node node3 = node2.next;
                    node2.next = node1;
                    node1 = node2;
                    node2 = node3;
                    if (node2 != null) {
                        head = node2;
                    }
                }
            }
        }
    }
}

class dList{
    static Node head;
    static Node tail;
    static class Node{
        int value;
        Node next;
        Node prev;
    }

    public static void pushFront(int value){ // O(1)
        Node node = new Node();
        node.value = value;

        if(head == null){
            tail = node;
        }else{
            node.next = head;
            head.prev = node;
        }
        head = node;
    }

    public static void popFront(){ // O(1)
        if(head != null){
            if(head.next == null){
                head = null;
                tail = null;
            }else {
                head = head.next;
                head.prev = null;
            }
        }
    }
    public static void print(){
        Node node = head;
        while(node != null){
            System.out.printf("%d ", node.value);
            node = node.next;
        }
        System.out.println();
    }

    public static boolean contains(int value){
        Node node = head;
        while(node != null){
            if(node.value == value){
                return true;
            }
            node = node.next;
        }
        return false;
    }

    public static void pushBack(int value){ // O(1)
        Node node = new Node();
        node.value = value;

        if(tail == null){
            head = node;
        }else{
            node.prev = tail;
            tail.next = node;
        }
        tail = node;
    }

    public static void popBack(){ // O(1)
        if(tail != null){
            if(tail.prev == null){
                head = null;
                tail = null;
            }else {
                tail = tail.prev;
                tail.next = null;
            }
        }
    }

    public static void sort(){ // O(N^2)
        //bubble sort
        //for(int i = 0; i < n; i++)
        //for(int j = 0; j < n - 1 - i; j++)
        // if(A[j] > A[j+1])
        //swap(A[j], A[j+1]);

        boolean needSort = true;
        do{
            needSort = false;
            Node node = head;
            while(node != null && node.next != null){
                if(node.value > node.next.value){
                    Node before = node.prev;
                    Node cur = node;
                    Node next = node.next;
                    Node after = next.next;

                    cur.next = after;
                    cur.prev = next;
                    next.next = cur;
                    next.prev = before;

                    if(before != null)
                        before.next = next;
                    else
                        head = next;

                    if(after != null)
                        after.prev = cur;
                    else
                        tail = cur;

                    needSort = true;
                }
                node = node.next;
            }

        }while(needSort);
    }

    public static void reverse(){
        Node node = head;
        while (node != null) {
            Node temp = node.next;
            node.next = node.prev;
            node.prev = temp;
            node = node.prev;
        }
        Node temp = head;
        head = tail;
        tail = temp;
    }
}
public class Main {
    public static void main(String[] args) {
        int num = 10;

        System.out.println("Двухсвязный список:");
        System.out.print("До:    ");

        dList list1 = new dList();
        for(int i=1; i<=num; i++){
            list1.pushFront(i);
        }

        list1.print();

        System.out.print("После: ");

        list1.reverse();
        list1.print();

        System.out.println();

        System.out.println("Односвязный список:");
        System.out.print("До:    ");

        List list2 = new List();

        for(int i=1; i<=num; i++){
            list2.pushFront(i);
        }

        list2.print();

        System.out.print("После: ");

        list2.reverse();
        list2.print();


//        list.print();
//
//        list.popFront();
//        list.popFront();
//
//        list.print();
//
//        System.out.println(list.contains(2));
//        System.out.println(list.contains(5));
//
//        list.pushBack(7);
//
//        list.print();
//
//        list.popBack();
//
//        list.print();
    }
}
// FIFO = First In First Out - Очередь
// LIFO = Last In First Out - Стек