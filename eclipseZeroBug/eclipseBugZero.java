//BUG

package test;

public class zeroString {
	
	public static void main(String[] args) {
		char[] cA = new char[3];
		cA[0] = 'A';
		cA[1] = 0;
		cA[2] = 'B';
		String str = new String(cA);
		System.out.println(str);

	}
}


//doesnt print 'B'
