package bronze.lv2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 알파벳찾기_10809 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int[] array = new int[26];
        Arrays.fill(array, -1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (array[c - 'a'] != -1)
                continue;
            array[c - 'a'] = i;
        }

        for (int i = 0; i < array.length; i++) {
            sb.append(array[i]);
            if (i + 1 < array.length)
                sb.append(" ");
        }

        System.out.println(sb.toString());
    }
}
