import java.util.*;
public class birds {
    public static int maxHeads(int[] birds, int m) {
        long startTime = System.nanoTime();
        int answer = 0;//initialization
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());//change to max priority queue
        for (int a : birds) {
            pq.offer(a);//push a into pq queue
        }
        while (m > 0) {
            int maxElement = pq.poll();//pop a max number
            answer += maxElement;//add the max num to answer
            pq.offer((int) Math.floor(maxElement / 2));//push round down num back to pq
            m--;
        }
        long endTime = System.nanoTime();
        long total = endTime - startTime;
        System.out.println("time: " + total + " ns");
        return answer;
    }
    public static void main(String args[]) {
        int arr1[] = {20, 1, 15};

        int arr2[] = {2, 1, 7, 4, 2};

        int arr3[] = {4, 10, 6, 7, 3, 1};

        System.out.println("Test 1, Total Heads 20 = " + maxHeads(arr1, 1)); //m =1, bird 1 cut 20 heads, arr1 is now {10,1,15}
        System.out.println("Test 2, Total Heads 35 = " + maxHeads(arr1, 2)); //m=2, bird 3 cut 15 head, arr1 is now {10,1,7}
        System.out.println("Test 3, Total Heads 45 = " + maxHeads(arr1, 3)); //m=3, bird 1 cut 10 heads, arr1 is now {5,1, 7}

        System.out.println("Test 4, Total Heads 7 = " + maxHeads(arr2, 1)); //m=1
        System.out.println("Test 5, Total Heads 11 = " + maxHeads(arr2, 2)); //m=2
        System.out.println("Test 6, Total Heads 14 = " + maxHeads(arr2, 3)); //m=3

        System.out.println("Test 7, Total Heads 10 = " + maxHeads(arr3, 1)); //m=1
        System.out.println("Test 8, Total Heads 17 = " + maxHeads(arr3, 2)); //m=2
        System.out.println("Test 9, Total Heads 23 = " + maxHeads(arr3, 3)); //m=3
        System.out.println("Test 10, Total Heads 28 = " + maxHeads(arr3, 4));//m=4
        System.out.println("Test 11, Total Heads 32 = " + maxHeads(arr3, 5));//m=5
        System.out.println("Test 12, Total Heads 35 = " + maxHeads(arr3, 6));//m=6
    }

}