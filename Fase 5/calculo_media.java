import java.util.Scanner;

public class Calculo_media {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor da primeira nota: ");
        double nota1 = scanner.nextDouble();
        System.out.println("Digite o valor da segunda nota: ");
        double nota2 = scanner.nextDouble();

        double media = (nota1+nota2)/2;

        System.out.println("A média é: " + media);
        scanner.close();
    }
}
