while True:
    menu_num = int(input())
    
    if menu_num == 1:
        print("NEW")
    elif menu_num == 2:
        print("OPEN")
    elif menu_num == 3:
        print("SAVE")
    elif menu_num == 4:
        print("QUIT")
        break  
    else:
        print("AGAIN")
