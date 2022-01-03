# Programming-Assignment-2
Assignment: Programming Assignment 2: High and Low Game

In this python excercise, i use a series of function that is built with simple if_else statements,  while loops to repeate and statisfy the user questions and value returning functions

There are 3 files in this project: 
  1- art1.py contains logo anb vs. There are both graphical representation for the game 
![image](https://user-images.githubusercontent.com/16805149/147981811-66597fc0-459d-4552-96f1-9903a9c1c80d.png)

  2- game_data.py which all all the social media data in form of dictionary. 
  3- 'low t0 high.py' which has all the codes to run the project. 
  
  
This is exercise that will help you understand while loop or any repeatable sequence in programming project. all the steps have comments to help you undestand the code. 

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

Thank You !
