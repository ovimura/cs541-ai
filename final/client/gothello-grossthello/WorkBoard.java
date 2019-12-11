import java.util.Vector;

public class WorkBoard extends Board {
    static final int INF = 5 * 5 + 1;
    Move best_move = null;

    public WorkBoard() {
    }

    public WorkBoard(WorkBoard w) {
	super(w);
    }

    int heval() {
	int nstones = 0;
	int ostones = 0;
	for (int i = 0; i < 5; i++)
	    for (int j = 0; j < 5; j++)
		if (square[i][j] == checker_of(to_move))
		    nstones++;
	        else if (square[i][j] == checker_of(opponent(to_move)))
		    ostones++;
	return nstones - ostones;
    }

    static java.util.Random prng = new java.util.Random();

    static int randint(int n) {
	return Math.abs(prng.nextInt()) % n;
    }

    int negamax(int depth, boolean find_move) {
	Vector<Move> moves = genMoves();
	int nmoves = moves.size();
	if (nmoves == 0) {
	    best_move = new Move();
	    WorkBoard scratch = new WorkBoard(this);
	    int status = scratch.try_move(best_move);
	    if (status != GAME_OVER)
		return -scratch.negamax(25, false);
	    int result = scratch.referee();
	    if (result == to_move)
		return INF;
	    if (result == opponent(to_move))
		return -INF;
	    return 0;
	}
	if (depth <= 0) {
	    if (find_move)
		throw new Error("move without search");
	    return heval();
	}
	Vector<Integer> values = null;
	if (find_move)
	    values = new Vector<Integer>(nmoves);
	int maxv = -INF;
	for (int i = 0; i < nmoves; i++) {
	    Move m = moves.get(i);
	    /* XXX do-undo is very difficult here, since we
	       may capture a large number of stones.  For
	       now, just punt. */
	    WorkBoard scratch = new WorkBoard(this);
	    int status = scratch.try_move(m);
	    if (status == ILLEGAL_MOVE)
		throw new Error("unexpectedly illegal move");
	    if (status == GAME_OVER)
		throw new Error("unexpectedly game over");
	    int v = -scratch.negamax(depth - 1, false);
	    if (find_move)
		values.add(i, new Integer(v));
	    if (v >= maxv)
		maxv = v;
	}
	if (!find_move)
	    return maxv;
	int nbest = 0;
	for (int i = 0; i < nmoves; i++)
	    if (((Integer)(values.get(i))).intValue() == maxv)
		nbest++;
	int randmove = randint(nbest);
	for (int i = 0; i < nmoves; i++)
	    if (((Integer)values.get(i)).intValue() == maxv)
		if (randmove-- == 0)
		    best_move = moves.get(i);
	return maxv;
    }

    void bestMove(int depth) {
	int v = negamax(depth, true);
    }
}
