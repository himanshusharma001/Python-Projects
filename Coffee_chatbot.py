def coffee_bot():
    print("Welcome to the cafe!")
    name=input("Can I get your name please?")
    order_drink='y'
    drinks=[]
    
    while order_drink=='y':
        size=get_size()
        drink_type=get_drink_type()
        print("\n\nAlright, that's a",size,drink_type,"!")
        drinks.append(drink_type)
        i=0
        while i==0:
            order_drink=input("Would you like to order another drink? (y/n)")
            if order_drink=='y':
                break
            elif order_drink=='n':
                break
            else:
                print_message()
    print("OK so the order is")
    for a in drinks:
        print("->",a)
    print("Thanks,",name,"! Your Drink will be ready Shortly")
    
    
def get_size():
    res=input("What size drink can I get for you?\n[a] Small\n[b] Medium\n[c] Large \n(Enter in small letter)")
    if res =='a':
        return "Small"
    elif res == 'b':
        return "Medium"
    elif res =='c':
        return "Large"
    else:
        print_message()
        return get_size()
    
    
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
    
    
def get_drink_type():
    res=input("\nWhat type of drink would you like? \n[a] Brewed Coffee\n[b] Mocha\n[c] Latte \n(Enter in small letter)")
    if res =='a':
        return "Brewed Coffee"
    elif res == 'b':
        return order_mocha()
    elif res =='c':
        
        return order_latte()
    else:
        print_message()
        return get_drink_type()   
    
    
def order_latte():
    res=input("\nAnd what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk\n[c] Soy milk\n(Enter in small letter)")
    if res =='a':
        return "Latte"
    elif res == 'b':
        return "Non-Fat Latte"
    elif res =='c':
        return "Soy Latte"
    else:
        print_message()
        return order_latte()
    
    
def order_mocha():
    i=0
    while i==0:
       res=input('\nWould you like to try our limited-edition Peppermint Mocha?\n[a] Sure!\n[b] Maybe next time!\n(Enter in small letter)')
       if res=='a':
           return 'Peppermint Mocha'
       elif res=='b':
           return 'Mocha'
       print_message()
        
    
    
    
    
    
    
    
#Calling the chatbot
coffee_bot()
