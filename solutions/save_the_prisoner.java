public class SavePrisoner {

	private static int getPrisoner(int N, int M, int S) {
		final int prisonerId = (S + (M - 1)) % N;
		//if prisonerId comes as 0 means we are talking about Nth as Mod will never give us N
		return prisonerId == 0 ? N : prisonerId;
	}

	public static void main(String[] args) {
		final Scanner in = new Scanner(System.in);
		final int T = Integer.parseInt(in.next());
		for(int i = 0; i < T; i++) {
			final int N = Integer.parseInt(in.next());
			final int M =  Integer.parseInt(in.next());
			final int S = Integer.parseInt(in.next());
			System.out.println(getPrisoner(N, M, S));
		}
		in.close();
	}
}