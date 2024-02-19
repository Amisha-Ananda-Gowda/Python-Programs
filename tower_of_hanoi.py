def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    if n == 0: 
        return TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
        print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
        n = int(input("Enter the number of disks:"))
        TowerOfHanoi(n, 'A', 'C', 'B') 


# Get user input for number of disks
num_disks = int(input("Enter the number of disks: "))

# Run Tower of Hanoi solver
TowerOfHanoi(num_disks, 'A', 'C', 'B')
