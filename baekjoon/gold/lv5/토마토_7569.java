package gold.lv5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 토마토_7569 {
    private static class Point {

        int x, y, z;

        public Point(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        @Override
        public String toString() {
            return "[" + x + ", " + y + ", " + z + "]";
        }
    }

    static int M, N, H;
    static int[][][] array;
    static boolean[][][] visited;
    static int[] deltaX = {1, -1, 0, 0, 0, 0},
            deltaY = {0, 0, 1, -1, 0, 0},
            deltaZ = {0, 0, 0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        array = new int[H][N][M];
        visited = new boolean[H][N][M];
        int cnt = 0;
        Queue<Point> queue = new LinkedList<>();
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < array[i][j].length; k++) {
                    array[i][j][k] = Integer.parseInt(st.nextToken());
                    if (array[i][j][k] == 1) {
                        queue.offer(new Point(i, j, k));
                        visited[i][j][k] = true;
                    } else if(array[i][j][k] == 0) {
                        cnt++;
                    }
                }
            }
        } // input end
        int answer = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                Point p = queue.poll();

                for (int d = 0; d < 6; d++) {
                    int x = p.x + deltaX[d];
                    int y = p.y + deltaY[d];
                    int z = p.z + deltaZ[d];

                    if (x < 0 || y < 0 || z < 0 || x >= H || y >= N || z >= M || visited[x][y][z]) continue;

                    if (array[x][y][z] == 0) { // 있을 때
                        queue.offer(new Point(x, y, z));
                        visited[x][y][z] = true;
                        cnt--;
                    }
                }
            }
            if (!queue.isEmpty())
                answer++;
        }

        if(cnt > 0)
            answer = -1;
        System.out.println(answer);
    }
}
