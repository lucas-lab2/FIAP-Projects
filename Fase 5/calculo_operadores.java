import java.util.Scanner;
public class calculo_operadores {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor do primeiro número: ");
        double numero1 = scanner.nextDouble();
        System.out.println("Digite o valor do segundo número: ");
        double numero2 = scanner.nextDouble();

        //Soma
        double soma = numero1 + numero2;
        System.out.println("S soma dos números é: : " + soma);

        //Subtração
        double Subtração = numero1 - numero2;
        System.out.println("A subtração dos números é: " + Subtração);

        //Multiplicação
        double multiplicacao = numero1 * numero2;
        System.out.println("A multiplicação dos número é:" + multiplicacao);

        //Divisão
        double divisao = numero1 / numero2;
        System.out.println("A divisão dos números é: " + divisao);
        
        
    }
}
