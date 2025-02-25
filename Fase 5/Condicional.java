import java.util.Scanner;

public class Condicional{

    public static void main (String[] args){
        System.out.println("Digite a idade do aluno:");
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        int idade = scanner.nextInt();
        if (idade >= 18){
            System.out.println("Aluno maior de idade");
        } else {
            System.out.println("Aluno menor de idade");
        }   

    }
}
