import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test_case = Integer.parseInt(br.readLine());
        for (int i = 0; i < test_case; i++) {
            String s = br.readLine();

            StringTokenizer st = new StringTokenizer(s," ");
            int N = Integer.parseInt(st.nextToken());
            String sa = st.nextToken();

            for (int j = 0; j < sa.length(); j++){
                for(int k = 0; k < N; k++){
                    System.out.print(sa.charAt(j));
                }
            }
            System.out.println();
        }
    }
}
