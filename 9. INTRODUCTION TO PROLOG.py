'''
#Done by M Harish AIML-A 231501058
KB1:

woman(mia). 
woman(jody). 
woman(yolanda). 
playsAirGuitar(jody). 
party.
Query1:?-woman(mia). 
Query2:?-playsAirGuitar(mia). 
Query3:?-party.
Query4:?-concert.


KB2:

happy(yolanda). 
listens2music(mia).
Listens2music(yolanda):-happy(yolanda). 
playsAirGuitar(mia):-listens2music(mia). 
playsAirGuitar(Yolanda):-listens2music(yolanda).


KB3:

likes(dan,sally). likes(sally,dan). likes(john,brittney).
married(X,Y):- likes(X,Y), likes(Y,X).
friends(X,Y):-likes(X,Y) ;likes(Y,X).
 

KB4:

food(burger).
food(sandwich). 
food(pizza).
lunch(sandwich).
dinner(pizza).
meal(X):-food(X).


KB5:

owns(jack,car(bmw)). 
owns(john,car(chevy)). 
owns(olivia,car(civic)). 
owns(jane,car(chevy)). 
sedan(car(bmw)). 
sedan(car(civic)). 
truck(car(chevy)).
 

KB6: Find minimum maximum of two numbers

find_max(X,Y,X):-X>=Y,!.
find_max(X,Y,Y):-X<Y.
find_min(X,Y,X):-X=<Y,!.
find_min(X,Y,Y):-X>Y.

Output:

| ?- find_max(100,200,Max).
Max = 200
yes
| ?- find_max(40,10,Max).
Max = 40 yes
| ?- find_min(40,10,Min).
Min = 10 yes
| ?- find_min(100,200,Min).
Min = 100
yes
| ?-
 
 
KB7: 

Here are some simple clauses.
likes(mary,food). 
likes(mary,wine). 
likes(john,wine). 
likes(john,mary).

The following queries yield the specified answers.
| ?- likes(mary,food). 
yes.
| ?- likes(john,wine). 
yes.
| ?- likes(john,food). 
no.
#Done by M Harish AIML-A 231501058