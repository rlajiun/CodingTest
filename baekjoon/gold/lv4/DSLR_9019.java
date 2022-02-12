package gold.lv4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class DSLR_9019 {
    public static class Operand {
        int num;
        String command;

        public Operand(int num, String command) {
            this.num = num;
            this.command = command;
        }
    }

    static int A, B;
    static String answer;
    static Queue<Operand> queue;
    static boolean[] visited;
    static String[] commands = {"D", "S", "L", "R"};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            // input end
            visited = new boolean[10000];
            queue = new LinkedList<>();
            visited[A] = true;
            addDSLR(A, "");

            while (!queue.isEmpty()) {
                Operand oper = queue.poll();

                if (oper.num == B) {
                    answer = oper.command;
                    break;
                } else {
                    addDSLR(oper.num, oper.command);
                }
            }
            System.out.println(answer);
        } // TC end
    }

    public static void addDSLR(int num, String command) {
        for (int i = 0; i < commands.length; i++) {
            int n = calcDSLR(num, commands[i]);
            if(!visited[n]){
                queue.offer(new Operand(n, command + commands[i]));
                visited[n] = true;
            }
            if (n == B) break;
        }
    }

    public static int calcDSLR(int num, String operator) {
        switch (operator) {
            case "D":
                return 2 * num % 10000;
            case "S":
                return num != 0 ? num - 1 : 9999;
            case "L":
                return (num % 1000) * 10 + (num / 1000);
            case "R":
                return (num % 10) * 1000 + (num / 10);
        }
        return num;
    }
}
