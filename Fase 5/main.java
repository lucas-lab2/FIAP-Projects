public class Main{
    public static void main (String[] args){
    
        //tipos primitivos
        //byte, short, int, long 
        int idade;
        idade = 10;
        System.out.println(idade);
        //float, double
        double altura = 1.75;
        float altura2 = 1.75f;
        System.out.println(altura);
        System.out.println(altura2);
        //char
        char letra = 'a';
        System.out.println(letra);
        //boolean
        boolean verdade = true;
        System.out.println(verdade);

        //Tipo de referencia
        //string
        String nome = "Lucas"; //para tipo referencia a letra inicial é maiuscula e para string, a informaçao fica entre aspas duplas
        System.out.println(nome);

        int a = 5;
        int b = 10;

        System.out.println(a > b);   // Isso retorna falso, já que 'a' não é maior que 'b'
        System.out.println(a <= b);  // Isso retorna verdadeiro, já que 'a' é menor ou igual a 'b'
        System.out.println(a == b);  // Isso retorna falso, já que 'a' não é igual a 'b'
        System.out.println(a != b);  // Isso retorna verdadeiro, já que 'a' é diferente de 'b'

    }
}
