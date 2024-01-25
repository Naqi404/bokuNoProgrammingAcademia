def double():
    value = 5.0
    for i in range(30):
        value = value*2
        i+=1
    
    value = value/100
    print(f"It doubled to $" + str(value))


double()
