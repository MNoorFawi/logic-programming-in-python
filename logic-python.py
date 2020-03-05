from kanren import *

#food_type(gouda, cheese).
#food_type(ritz, cracker).
#food_type(steak, meat).
#food_type(sausage, meat).
#food_type(limonade, juice).
#food_type(cookie, dessert).
#flavor(sweet, dessert).
#flavor(savory, meat).
#flavor(savory, cheese).
#flavor(sweet, juice).
#food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z).
#food_flavor(What, sweet).

food_type = Relation()
flavor = Relation()
facts(food_type, ("gouda", "cheese"),
                 ("ritz", "cracker"),
                 ("steak", "meat"),
                 ("sausage", "meat"),
                 ("limonade", "juice"),
                 ("cookie", "dessert"))
facts(flavor, ("sweet", "dessert"),
              ("savory", "meat"),
              ("savory", "cheese"),
              ("sweet", "juice"))

food_flavor, food_v, flavor_v = var(), var(), var()
run(0, food_flavor, food_type(food_flavor, food_v),
                    flavor("sweet", food_v))
                    
def food_flavor(x, y):
    z = var()
    #return lall(food_type(x, z), flavor(y, z))
    return conde((food_type(x, z), flavor(y, z)))

what = var()
print(run(0, what, food_flavor(what, "sweet")))
print(run(0, what, food_flavor(what, "savory")))

#likes(noor, sausage).
#likes(melissa, pasta).
#likes(dmitry, cookie).
#likes(nikita, sausage).
#likes(assel, limonade).
#friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).

likes = Relation()
facts(likes, ("Noor", "sausage"),
             ("Melissa", "pasta"),
             ("Dmitry", "cookie"),
             ("Nikita", "sausage"),
             ("Assel", "limonade"))

def friend(x, y):
    z = var()
    return conde((likes(x, z), likes(y, z)))

who = var()
name = "Noor"
output = run(0, who, friend(who, name))
print([x for x in output if x != name])

def dish_to_like(person, what):
    liked = var()
    foodtype = var()
    foodflavor = var()
    return lall(likes(person, liked), food_type(liked, foodtype), 
                flavor(foodflavor, foodtype), food_type(what, foodtype))
what = var()
dish = run(0, what, dish_to_like("Noor", what))
print("since Noor has liked Sausage, he would like:", dish)

parent = Relation()
x = var()
facts(parent, ("Adam", "John"),
              ("Adam", "Emma"),
              ("William",  "Adam"))

print(run(1, x, parent(x, "John")))
print(run(0, x, parent("Adam", x)))

grandparent, Parent = var(), var()
print(run(0, grandparent, parent(grandparent, Parent),
                          parent(Parent, 'Emma')))
                          
                          
def right(x, y, lst):
    return membero((x, y), zip(lst[1:], lst))
def next(x, y, lst):
    return conde([right(x, y, lst)], [right(y, x, lst)])

houses = var()

zebra_riddle = lall(
   (eq, (var(), var(), var(), var(), var()), houses),
   (membero,('Englishman', var(), var(), var(), 'red'), houses),
   (membero,('Spaniard', var(), var(), 'dog', var()), houses),
   (membero,('Ukrainian', var(), 'tea', var(), var()), houses),
   (right,(var(), var(), var(), var(), 'ivory'),
   (var(), var(), var(), var(), 'green'), houses),
   (membero,(var(), var(), 'coffee', var(), 'green'), houses),
   (membero,(var(), 'Old Gold', var(), 'snails', var()), houses),
   (membero,(var(), 'Kools', var(), var(), 'yellow'), houses),
   (eq,(var(), var(), (var(), var(), 'milk', var(), var()), var(), var()), houses),
   (eq,(('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
   (next,(var(), 'Chesterfield', var(), var(), var()),
   (var(), var(), var(), 'fox', var()), houses),
   (next,(var(), 'Kools', var(), var(), var()),
   (var(), var(), var(), 'horse', var()), houses),
   (membero,(var(), 'Lucky Strike', 'Orange Juice', var(), var()), houses),
   (membero,('Japanese', "Parliaments", var(), var(), var()), houses),
   (next,('Norwegian', var(), var(), var(), var()),
   (var(), var(), var(), var(), 'blue'), houses),
   (membero,(var(), var(), "water", var(), var()), houses),
   (membero,(var(), var(), var(), 'zebra', var()), houses)
)

run(0, houses, zebra_riddle)

