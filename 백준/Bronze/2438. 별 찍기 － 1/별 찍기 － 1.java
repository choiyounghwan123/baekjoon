import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a  = sc.nextInt();

        for (int i = 1; i <= a; i++){
            for (int j = 1 ; j <= i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}