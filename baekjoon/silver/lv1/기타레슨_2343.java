package silver.lv1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 기타레슨_2343 {
    static int N, M;
    static int[] array;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        array = new int[N];
        int right = 0, left = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < array.length; i++) {
            array[i] = Integer.parseInt(st.nextToken());
            right += array[i];
            left = Math.max(left, array[i]);
        } // input end

        while (left <= right) {
            int mid = (left + right) / 2;
            int sum = 0, cnt = 0;
            for (int i = 0; i < array.length; i++) {
                if (sum + array[i] <= mid) {
                    sum += array[i];
                } else {
                    sum = array[i];
                    cnt++;
                }
            }
            if (sum != 0)
                cnt++;
            if (cnt > M)
                left = mid + 1;
            else
                right = mid - 1;
        }
        System.out.println(left);
    }
}
