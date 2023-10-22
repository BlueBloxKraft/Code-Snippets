import java.util.Arrays;


public class Primes {

    //Test
    public static void main(String[] args) {
        System.out.println(getNthPrime(Integer.parseInt(args[0])));
    }

    private static int sieve(int m){
        boolean[] primes = new boolean[m+1];
        Arrays.fill(primes, true);
        primes[0] = primes[1] = false;

        for(int i = 2; i <= Math.sqrt(m); i++)
            if(primes[i])
                for(int j = i*i; j <= m; j+=i)
                    primes[j] = false;

        int sum = 0;
        for(boolean b : primes) if(b) sum++;
        return sum;
    }

    private static int getNthPrime(int i){
        int x  = 1;
        while(sieve(x) < i) x++;
        return x;
    }

}
