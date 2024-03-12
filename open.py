from collections import defaultdict

visited = defaultdict(lambda: False)

def waterJugSolver(jug1, jug2, aim, amt1=0, amt2=0):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print("Steps to achieve", aim, "liters:")
        print(amt1,"\t",amt2)
        return True
    
    if visited[(amt1, amt2)] == False:
        print(amt1,"\t",amt2) 
        visited[(amt1, amt2)] = True
        return (waterJugSolver(jug1, jug2, aim, 0, amt2) or
                waterJugSolver(jug1, jug2, aim, amt1, 0) or
                waterJugSolver(jug1, jug2, aim, jug1, amt2) or
                waterJugSolver(jug1, jug2, aim, amt1, jug2) or
                waterJugSolver(jug1, jug2, aim, amt1 + min(amt2, (jug1 - amt1)), amt2 - min(amt2, (jug1 - amt1))) or
                waterJugSolver(jug1, jug2, aim, amt1 - min(amt1, (jug2 - amt2)), amt2 + min(amt1, (jug2 - amt2))))
    else:
        return False

def main():
    jug1 = int(input("Enter capacity of jug 1: "))
    jug2 = int(input("Enter capacity of jug 2: "))
    aim = int(input("Enter desired amount of water: "))
    
    print("Steps: ")
    print("Jug1\tJug2")
    waterJugSolver(jug1, jug2, aim)

if __name__ == "__main__":
    main()