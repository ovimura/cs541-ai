# Gothello Daemon Python Client Library
Bart Massey

The Python client "library" for the Gothello daemon
[`gthd`](http://github.com/pdx-cs-ai/gothello-gthd) is a standard
Python 3 module.  You will want to
import `gthclient.py` into your Python program.

In brief, the client stubs are used by creating a
`gthclient.GthClient` object which automatically connects to the
specified server on the specified host as the specified
player.  (See the documentation on running a Gothello game
for details.)  The code then handles the details of making
moves and getting moves from the server, using the
`client.make_move()` and `client.get_move()` methods.  These accept
and return move strings: either a coordinate or "pass".

**The time control portion of this client has not yet been
tested.** Time control tracking is performed by the client,
which caches a bunch of state information about the game in
progress in global variables.

Exceptions are raised when anything unexpected occurs in the
interaction with the server. Keep in mind that the server
connection will not be closed by the exception, so use the
`client.close_all()` method when you no longer want the
object. `client.close_all()` will be called automatically
when the game is over.

A random-player client has been included as an example.
Invoke with `python3 gthrandom.py black` (or `white`).
