while True:
    menu_num = int(input())
    
    if menu_num == 1:
        print("ADD")
    elif menu_num == 2:
        print("DELETE")
    elif menu_num == 3:
        print("SEARCH")
    elif menu_num == 4:
        print("PRINT")
    elif menu_num == 5:
        print("EXIT")
        break  
    else:
        print("ERROR")
