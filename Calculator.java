import java.util.*;

class calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Scanner operator = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int o = operator.nextInt();

        switch(o) {
            case 1: System.out.println(a + b);
            break;
            case 2: System.out.println(a - b);
            break;
            case 3: System.out.println(a * b);
            break;
            case 4: System.out.println(a / b);
            default: System.out.println("Invalid button!");
        }
    }
}
