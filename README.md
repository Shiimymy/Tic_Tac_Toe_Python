# Tic-Tac-Toe Game

This is the Milestone 1 Python lesson by [Pierian Data](https://github.com/Pierian-Data?tab=overview&from=2021-12-01&to=2021-12-31) to create a Tic Tac Toe Game that can be played in the Python Terminal.

## Fixed Issues

Fixed issues of the final lesson code:

| Issue                                        | Description                                                                              | Steps done to fix                                                       |
| -------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Error if invalid position                    | When player choose a non digit value as a position, throw a Valueerror and stop the game | Add handling exception to restart the game and throw a message for user |
| No clear direction when space is unavailable | Game would just ask again the position without indication                                | Update the print statment                                               |
