import java.util.Scanner;

class Solution
{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n =sc.nextInt();
        while(n-->0){
            String s=sc.next();
            check(s);
        }
    }

    static void check(String s){
        int len=s.length();
        int[] ch=new int[26];
        for(int i=0;i<s.length();i++){
            if(i<s.length()/2){
                ch[s.charAt(i)-'a']++;
            }
            else{
                ch[s.charAt(i)-'a']--;
            }
        }

        for(int x: ch){
            if(x!=0){
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}