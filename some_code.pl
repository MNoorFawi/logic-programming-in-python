food_type(gouda, cheese). %% fact
food_type(ritz, cracker). %% fact etc.
food_type(steak, meat).
food_type(sausage, meat).
food_type(limonade, juice).
food_type(cookie, dessert).

flavor(sweet, dessert).
flavor(savory, meat).
flavor(savory, cheese).
flavor(sweet, juice).

food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z). %% rule

%% food_flavor(What, dessert). %% question: what flavor does dessert have?

likes(noor, sausage).
likes(melissa, pasta).
likes(dmitry, cookie).
likes(nikita, sausage).
likes(assel, limonade).

friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).

