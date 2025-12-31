def tower_of_hanoi(n, A, B, C):
    if n == 1:
        print(f"Move disk 1 from {A} to {C}")
        return

    tower_of_hanoi(n - 1, A, C, B)
    print(f"Move disk {n} from {A} to {C}")
    tower_of_hanoi(n - 1, B, A, C)
tower_of_hanoi(3, 'A', 'B', 'C')
