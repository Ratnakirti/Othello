# Othello

1. Did you attempt to make your computer player very smart -- i.e., do something more clever than
just pick a random legal move?

Yes, I actually made my computer player perform way better than just picking a random move. I
made sure to always let the computer pick a legal move that would be most efficient according
to my algorithm.

2. If so, were you able to accomplish this? Is your computer player as smart as you would like?

Yes, I was able to accomplish it by using a thorough mix of available positional checkers and
validators in my program. I have seen more efficient strategies to play as a computer which 
can result in a guaranteed win. But my approach was also one of the very basic algorithms that
could lead to a win against a novice human player.

3. How did you determine which piece to play next? Tell us about your “pick next move” algorithm.

After the human player has played a move, it switches to a computer player. The computer player then
checks all the empty squares on the board and creates the list of legal square positions that can
be played by the computer. Then it checks each and every legal square position and keeps a record
of the number of flips that can occur if that move is played by the computer. Once it finds the
legal position with the maximum flips, it chooses the same for the computer and the computer plays
it. In case of an equal number of flip counts, it just chooses the last legal move in the board with
the maximum flip count. Basically, the AI part of my program finds the position that would lead
to the maximum number of flips on the board and plays it.

4. How often did your computer program beat you, or your friends, or whoever tested it out for you?

The program was able to beat a lot of novice players in the early stages. Even while playing it myself,
if I start putting down tiles randomly as the human player, the computer would still make sure to pick
the position with maximum flips and I end up getting beaten. It required a bit of attention and
cautious playing to beat the computer opponent. So, I can say that the computer would usually beat
4 out of the 10 players it played against.

5. How would you improve it in the future?

The algorithm secures a guaranteed win against a novice human player, but the maximum flip count
method tends to be predictive after repeated gameplays. I could notice if I have fixed initial
moves then the computer would also play itself out in the same pattern every time. So, even though
it takes the moves with maximum flips, it always repeats itself. I can make an improvement by randomizing
the computer move in case there exist multiple moves with the same flip count. Also, according to a
good Othello playing strategy, initially one should flip fewer tiles and keep the longer flips for the
later part of the game to increase the chances of winning. I could improve my computer player to flip
fewer tiles till the board is 40% full, and after that going full power and flip the maximum tiles as
possible to get a guaranteed win.
