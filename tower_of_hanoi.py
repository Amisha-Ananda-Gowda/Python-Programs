def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from {} to {}".format(source, target))
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print("Move disk {} from {} to {}".format(n, source, target))
    tower_of_hanoi(n-1, auxiliary, target, source)

# Get user input for number of disks
num_disks = int(input("Enter the number of disks: "))

# Run Tower of Hanoi solver
tower_of_hanoi(num_disks, 'A', 'C', 'B')
