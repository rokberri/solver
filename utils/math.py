def P(x:int, y:int):
    if x > y: 
        main, add= x, y
    else:
        main, add= y, x
    for i in range(main):
        for j in range(add):
            