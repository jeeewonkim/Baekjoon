import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int num[] = new int[n];
        int mid = n / 2;
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int m = num[i] = Integer.parseInt(br.readLine());
            sum += m;
            if (hashMap.containsKey(m)) {
                hashMap.put(m, hashMap.get(m) + 1);
            } else {
                hashMap.put(m, 1);
            }
        }
        List<Integer> keyList = new ArrayList<>(hashMap.keySet());
        ArrayList<Integer> maxCountList = new ArrayList<>();

        int max_count = 0;
        keyList.sort((o1, o2) -> hashMap.get(o2).compareTo(hashMap.get(o1)));
        for (int key : keyList) {
            if (hashMap.get(key) >= max_count) {
                max_count = hashMap.get(key);
                maxCountList.add(key);
            } else break;
        }
        Collections.sort(maxCountList);
        Collections.sort(keyList);
        Arrays.sort(num);
        //산술평균
        System.out.println(Math.round(sum / (double) n));
        //중앙 값
        System.out.println(num[mid]);
        //최빈 값
        if (maxCountList.size() < 2) {
            System.out.println(maxCountList.get(0));
        } else {
            System.out.println(maxCountList.get(1));
        }
        //범위
        System.out.println(keyList.get(keyList.size() - 1) - keyList.get(0));

    }


}
