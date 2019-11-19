import random
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
choice_one = random.choice(deck)
deck.remove(choice_one)

choice_two = random.choice(deck)
deck.remove(choice_two)

total = choice_one + choice_two
turn = 0
hand = [choice_one, choice_two]
dealer_total = 0

choice_one = random.choice(deck)
deck.remove(choice_one)
flag=0
choice_two = random.choice(deck)
deck.remove(choice_two)
dealer_total = choice_one + choice_two

############################
cheat = 0
############################

def get_avg(ls):
    total = 0
    for i in ls:
        total += i
    return i / len(ls)

while True:
    if turn == 0:
        print("dealer's total: " + str(dealer_total))
        print("")
        print("your total: " + str(total))
        print("your hand: " + str(hand))
        
        decision = input("Would you like to (S)tay, or (H)it: ")

        if decision == "S":
            flag = 1

        elif decision == "H":
            choice = random.choice(deck)
            deck.remove(choice)
            if choice == 11:
                print("You got an Ace! We will handle processing.")
                if total + 11 > 21:
                    total -= 10
                    hand.append("A")
                else:
                    total += 11
                    hand.append("A")
            else:
                total += choice
                hand.append(choice)
        
        if total > 21:
            print("You lost!")
            print("Final Total: "+ str(total))
            print("Dealer's total: "+ str(dealer_total))
            break

        turn = 1
        print("")
    
    else:
        #-----------Dealer-Code----------------#
        if cheat == 0:
            choice = random.choice(deck)
            deck.remove(choice)

            if choice + dealer_total <= 21:
                print("The dealer chose to Hit")
                if choice == 11:
                    print("Dealer got an Ace! We will handle processing.")
                    if dealer_total + 11 > 21:
                        dealer_total -= 10
                    else:
                        dealer_total += 11
                else:
                    dealer_total += choice

            else:
                print("Final Total: "+ str(total))
                print("Dealer's total: "+ str(dealer_total))
                if total > dealer_total:
                    print("You won!")
                elif dealer_total > total:
                    print("Dealer won!")
                else:
                    print("Tie!")
                break

            if flag == 1:
                print("Final Total: "+ str(total))
                print("Dealer's total: "+ str(dealer_total))
                if total > dealer_total:
                    print("You won!")
                elif dealer_total > total:
                    print("Dealer won!")
                else:
                    print("Tie!")
                break
        else:
            choice = random.choice(deck)
            deck.remove(choice)

            if get_avg(deck) + dealer_total <= 21:
                print("The dealer chose to Hit")
                if choice == 11:
                    print("Dealer got an Ace! We will handle processing.")
                    if dealer_total + 11 > 21:
                        dealer_total -= 10
                    else:
                        dealer_total += 11
                else:
                    dealer_total += choice

            else:
                print("Final Total: "+ str(total))
                print("Dealer's total: "+ str(dealer_total))
                if total > dealer_total:
                    print("You won!")
                elif dealer_total > total:
                    print("Dealer won!")
                else:
                    print("Tie!")
                break

            if flag == 1:
                print("Final Total: "+ str(total))
                print("Dealer's total: "+ str(dealer_total))
                if total > dealer_total:
                    print("You won!")
                elif dealer_total > total:
                    print("Dealer won!")
                else:
                    print("Tie!")
                break




        #-----------Dealer-Code----------------#
        turn = 0
        print("")
            


