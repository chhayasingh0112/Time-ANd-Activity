import random
def time_activity( *args ,**kwargs):
   
    min = sum(args) + random.randint(0,60)
   
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spend {min} mins for {kwargs[choice]}")
time_activity(10, 20, 10 , hobby="Painting"  , work="DevOps" , fun ="Watching Sunset")
