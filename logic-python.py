from kanren import *

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
                flavor(foodflavor, foodtype), food_flavor(what, foodflavor))
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

grandparent, parent_v = var(), var()
print(run(0, grandparent, parent(grandparent, parent_v),
                          parent(parent_v, 'Emma')))
                          
                          
# first define the right function which will set something to the right side of other things
def right(x, y, lst):
    # dict(zip([1, 2, 3], [2, 3])) ==>  {1: 2, 2: 3}
    return membero((x, y), zip(lst[1:], lst))

# next function will check if two things next to each other    
def next(x, y, lst):
    # they are next to each other if x is to y right OR y is to x right
    return conde([right(x, y, lst)], [right(y, x, lst)])

# houses
houses = var()

# puzzle rules
zebra_riddle = lall(
   # houses is equal to 5 var as there are 5 houses
   (eq, (var(), var(), var(), var(), var()), houses),
   # house members
   (membero,('Englishman', var(), var(), var(), 'red'), houses),
   (membero,('Spaniard', var(), var(), 'dog', var()), houses),
   (membero,('Ukrainian', var(), 'tea', var(), var()), houses),
   # put to the right
   (right,(var(), var(), var(), var(), 'ivory'),
    (var(), var(), var(), var(), 'green'), houses),
   (membero,(var(), var(), 'coffee', var(), 'green'), houses),
   (membero,(var(), 'Old Gold', var(), 'snails', var()), houses),
   (membero,(var(), 'Kools', var(), var(), 'yellow'), houses),
   # define the milk house as a 5-var tuple in the middle of the 5-var houses
   (eq,(var(), var(), (var(), var(), 'milk', var(), var()), var(), var()), houses),
   # the same with the Norwegian in the first
   (eq,(('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
   # check next to
   (next,(var(), 'Chesterfield', var(), var(), var()),
    (var(), var(), var(), 'fox', var()), houses),
   (next,(var(), 'Kools', var(), var(), var()),
    (var(), var(), var(), 'horse', var()), houses),
   (membero,(var(), 'Lucky Strike', 'Orange Juice', var(), var()), houses),
   (membero,('Japanese', "Parliaments", var(), var(), var()), houses),
   (next,('Norwegian', var(), var(), var(), var()),
    (var(), var(), var(), var(), 'blue'), houses),
   # insert the water and zebra houses
   (membero,(var(), var(), "water", var(), var()), houses),
   (membero,(var(), var(), var(), 'zebra', var()), houses)
)

# run the rules to see the houses structures.
print(run(0, houses, zebra_riddle))

