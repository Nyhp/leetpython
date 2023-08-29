#Given a string of length n consisting only of characters 'L', 'R' and '_' 
#(represent respectively Left, Right and either-left-or-right). 
#Return the distance from the origin of the furthest point after n moves.

def furthestDistanceFromOrigin(moves: str) -> int:
    counter=0
    u=0
    for i in moves:
        if i == 'L':
            counter -=1
            print(counter)
        elif i =='R':
            counter +=1
            print(counter)
        else:
            u +=1
    print(counter)
    return u+abs(counter)   

print (furthestDistanceFromOrigin("L_RL__R"))    