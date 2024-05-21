    ------------------------GALACTIC BLAST GAME----------------------
        Welcome to Galactic Blast, an exciting arcade-style shooter game where you defend your planet from waves 
    of alien invaders. Control your spaceship using the arrow keys and fire bullets with the "space bar" to destroy 
    the aliens. The aliens move horizontally and descend towards the bottom each time they reach the screen's edge. 
    You have three lives, so dodge enemy bullets carefully and prevent the aliens from attacking you, the player.

        GAME INTERFACE
        The game has three main windows: the main menu, the actual game, and the save score & player name screen.
        In the main menu, there are two buttons: one is START GAME, which, when clicked, will start the game, 
    and the other is SCOREBOARD, which, when clicked, will display all the scores achieved by players, their names, 
    and the date the scores were obtained.
    
        HOW TO PLAY
        At the start of the game, the player will have 3 lives and 1 minute 30 seconds (90 seconds) to accumulate as 
    many points as possible while being attacked by aliens. An alien will attack every 5 seconds, randomly chosen. 
    The player earns points by shooting aliens with bullets; aliens also shoot bullets back at the player. 
    Hitting an alien earns the player 10 points, while being hit by an alien causes the player to lose one of their 3 lives. 
    If the player loses all 3 lives or the timer runs out, the game will proceed to the final window where the player can 
    see their score and enter their name, which will then be saved in "scores.txt".

        IMPLEMENTATION
        Regarding the implementation, the application itself runs in game.py, where I have imported other classes and functions 
    created in separate files. Firstly, to develop the game, I needed to create the player and the aliens. For these characters 
    to attack, it was easier for me to create a "bullet.py" file, which I then used for both the player and the aliens. 
    Finally, for simplicity, I decided to create a config.py file to manage the positioning of the characters and the game itself, 
    as well as the interface during the game.
        For the aliens, it was necessary to display them, position them, and handle their movement, as well as determine when and 
    how they attack. Regarding the player, it involved creating the player character and handling their movement. Additionally, 
    the player has three lives displayed on the screen, and one life is lost each time they are shot by an alien. For the bullet, 
    I created its appearance and behavior in the game. Finally, the config.py file was used to set up the game's layout and interface.
        About the implementation of the actual match, I imported the previously created files and other necessary libraries. Then, I 
    created the functions for the game: writing and saving the score in the scoreboard, creating the main menu and the scoreboard, 
    the end-of-match window, writing the player's name at the end of the round in the input box, and most importantly, a function 
    where the actual gameplay takes place.


    




    
