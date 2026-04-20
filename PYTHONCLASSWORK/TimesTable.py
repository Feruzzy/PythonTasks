print("Multiplication Table")
for count in range(1, 10):
    print(count, end=" | ")
    

    for result in range(1, 10): 
        total = count * result
        print(f"{total:>4}", end="")
    print()
    

