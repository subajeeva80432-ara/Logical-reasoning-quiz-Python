score = 0

print("Welcome to Logical Reasoning Quiz")
print("Each correct answer = 1 mark\n")

# Question 1
ans = input("1. 2, 4, 8, 16, ?\n a)18  b)24  c)32  d)34\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 2
ans = input("2. Odd one out:\n a)Square  b)Rectangle  c)Triangle  d)Circle\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 3
ans = input("3. A > B, B > C. Shortest?\n a)A  b)B  c)C  d)Cannot say\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 4
ans = input("4. 5 + 3 = 28, then 9 + 1 = ?\n a)91  b)910  c)18  d)10\n").lower()
if ans == "b":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: b\n")

# Question 5
ans = input("5. 3, 6, 9, ?, 15\n a)10  b)11  c)12  d)13\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 6
ans = input("6. Odd one out:\n a)Apple  b)Mango  c)Carrot  d)Banana\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 7
ans = input("7. 1, 4, 9, 16, ?\n a)20  b)25  c)30  d)36\n").lower()
if ans == "b":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: b\n")

# Question 8
ans = input("8. Pen, Pencil, Eraser, ?\n a)Book  b)Paper  c)Sharpener  d)Ink\n").lower()
if ans == "a":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: a\n")

# Question 9
ans = input("9. Monday + 3 days = ?\n a)Thursday  b)Friday  c)Wednesday  d)Sunday\n").lower()
if ans == "a":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: a\n")

# Question 10
ans = input("10. 2, 6, 12, 20, ?\n a)28  b)30  c)24  d)32\n").lower()
if ans == "a":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: a\n")

# Question 11
ans = input("11. 5, 10, 20, 40, ?\n a)60  b)80  c)100  d)45\n").lower()
if ans == "b":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: b\n")

# Question 12
ans = input("12. Odd one out:\n a)Gold  b)Silver  c)Iron  d)Plastic\n").lower()
if ans == "d":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: d\n")

# Question 13
ans = input("13. 7, 14, 21, 28, ?\n a)30  b)32  c)35  d)36\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 14
ans = input("14. Cube, Sphere, Cylinder, ?\n a)Circle  b)Cone  c)Square  d)Triangle\n").lower()
if ans == "a":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: a\n")

# Question 15
ans = input("15. 100, 90, 80, 70, ?\n a)60  b)55  c)65  d)50\n").lower()
if ans == "a":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: a\n")

# Question 16
ans = input("16. Odd one out:\n a)January  b)March  c)June  d)December\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 17
ans = input("17. 1=3, 2=6, 3=9, 4=?\n a)10  b)11  c)12  d)13\n").lower()
if ans == "c":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: c\n")

# Question 18
ans = input("18. All BLOOMS are FLOWERS, all FLOWERS are PLANTS. True?\n a)All plants are blooms\n b)All blooms are plants\n c)Some plants are blooms\n d)None\n").lower()
if ans == "b":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: b\n")

# Question 19
ans = input("19. North + East direction = ?\n a)North-East  b)South-East  c)South-West  d)North-West\n").lower()
if ans == "a":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: a\n")

# Question 20
ans = input("20. 11, 22, 33, ?, 55\n a)40  b)44  c)45  d)50\n").lower()
if ans == "b":
    score += 1
    print("Correct\n")
else:
    print("Wrong. Correct answer: b\n")

print("Quiz Completed")
print("Your Score:", score, "/ 20")
