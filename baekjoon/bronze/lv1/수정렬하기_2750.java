package bronze.lv1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 수정렬하기_2750 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] array = new int[N];
        for (int i = 0; i < array.length; i++) {
            array[i] = Integer.parseInt(br.readLine());
        } // input end

        Arrays.sort(array);
        for (int n :
                array) {
            System.out.println(n);
        }
    }
}
