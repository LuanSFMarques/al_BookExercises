#Write a rpsWinner() function with parameters player1 and player2. These parameters are
#passed one of the strings 'rock', 'paper', or 'scissors' representing that player’s move. If
#this results in player 1 winning, the function returns 'player one'. If this results in player 2
#winning, the function returns 'player two'. Otherwise, the function returns 'tie'

#Finished
def rpsWinner(player1,player2):
    if player1 != "rock" and player1 != "paper" and player1 != "scissors":
        return 'invalid'
    if player2 != "rock" and player2 != "paper" and player2 != "scissors":
        return 'invalid'
    if player1 == player2:
        return 'tie'
    if player1.lower() == "rock":
        if player2.lower() == "paper":
            return 'player two'
        elif player2.lower() == "scissors":
            return 'player one'
    elif player1.lower() == "paper":
        if player2.lower() == "scissors":
            return 'player two'
        elif player2.lower() == "rock":
            return 'player one'

    elif player1.lower() == "scissors":
        if player2.lower() == "rock":
            return 'player two'
        elif player2.lower() == "paper":
            return 'player one'
#-------------------------------------------------------------RESULTS      
try:
    assert rpsWinner('rock', 'paper') == 'player two'
    assert rpsWinner('rock', 'scissors') == 'player one'
    assert rpsWinner('paper', 'scissors') == 'player two'
    assert rpsWinner('paper', 'rock') == 'player one'
    assert rpsWinner('scissors', 'rock') == 'player two'
    assert rpsWinner('scissors', 'paper') == 'player one'
    assert rpsWinner('rock', 'rock') == 'tie'
    assert rpsWinner('paper', 'paper') == 'tie'
    assert rpsWinner('scissors' , 'scissors') == 'tie'
    print("All right!")
except:
    print("WRONG ALGORITHM")




