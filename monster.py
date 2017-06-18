'''Raja said: A monster is chasing after Rick and Morty on another planet.
   They're so frightened that sometimes they scream. More accurately,
   Rick screams at times b, b+a, b+2a,b+3a... and Morty screams at times
   d, d+c, d+2c, d+3c.... The monster will catch them if at any point they
   scream at the same time. Your task is to determine if the monster will
   ever catch them or not. Output the time if the monster will be able to
   catch them, otherwise print -1. Input : a=20,b=2,c=9,d=19 Output: 82.
   Input: a=2, b=1, c=16, d=12 Output: -1'''

a = int(raw_input("a: "))
b = int(raw_input("b: "))
c = int(raw_input("c: "))
d = int(raw_input("d: "))

x=[]
for i in range(1, 100):
    for j in range(1, 100):
        if (b + i*a == d + j*c):
                x.append(b + i*a)
                print min(x)
        else:
            print "-1"
            break





