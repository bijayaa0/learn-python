# Control Flow StatementsCreate a script that prints numbers from 1 to 50 but skips multiples of 5 using a for loop and continue.

for x in range(1,51):
    if x % 5 == 0:
        continue
    else:
        print(x,end=" ")
