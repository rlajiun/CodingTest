package bronze.lv1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 연산자끼워넣기_14888 {
    static int N, max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
    static int[] nums, oper, selected;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        nums = new int[N];
        oper = new int[4];
        selected = new int[N - 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < oper.length; i++) {
            oper[i] = Integer.parseInt(st.nextToken());
        }
        calc(0, 0, 0, 0, 0);
        System.out.println(max);
        System.out.println(min);
    }

    public static void calc(int idx, int plus, int minus, int mult, int divi) {
        if (plus == oper[0] && minus == oper[1] && mult == oper[2] && divi == oper[3]) {
            int num = nums[0];
            for (int i = 0; i < selected.length; i++) {
                switch (selected[i]) {
                    case 1:
                        num += nums[i + 1];
                        break;
                    case 2:
                        num -= nums[i + 1];
                        break;
                    case 3:
                        num *= nums[i + 1];
                        break;
                    case 4:
                        num /= nums[i + 1];
                        break;
                }
            }
            max = Math.max(max, num);
            min = Math.min(min, num);
            return;
        }

        if (plus > oper[0] || minus > oper[1] || mult > oper[2] || divi > oper[3]) return;

        selected[idx] = 1;
        calc(idx + 1, plus + 1, minus, mult, divi);
        selected[idx] = 2;
        calc(idx + 1, plus, minus + 1, mult, divi);
        selected[idx] = 3;
        calc(idx + 1, plus, minus, mult + 1, divi);
        selected[idx] = 4;
        calc(idx + 1, plus, minus, mult, divi + 1);
    }
}
