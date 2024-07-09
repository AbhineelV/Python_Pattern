
def star_pattern(rows):
    for i in range(0,rows):
     print()
     for j in range(0, rows- i - 1):
        print(" ",end="")
     for j in range (0, i + 1):
            print("* ",end ="")
star_pattern(10)     


