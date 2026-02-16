import  p1_random as p1

def print_menu():
    print('''1. Get another card
2. Hold hand
3. Print statistics
4. Exit\n''')

def type_of_card(card_number):
    if 2<=card_number<=10:
        return str(card_number)
    elif card_number == 1:
        return "ACE"
    elif card_number == 11:
        return "JACK"
    elif card_number == 12:
        return "QUEEN"
    else: # card_number == 13
        return "KING"

total_games = 1
player_wins = 0
dealer_wins = 0
tie_games = 0

player_hand = 0
dealer_hand = 0

rng = p1.P1Random()

print(f"START GAME #{total_games}\n")
card = rng.next_int(13) + 1
player_hand += card

print(f"Your card is a {type_of_card(card)}!")
print(f"Your hand is: {player_hand}\n")

while True:
    print_menu()

    option = int(input("Choose an option: "))
    print()

    if option == 1:
        card = rng.next_int(13) + 1
        player_hand += min(card, 10)

        print(f"Your card is a {type_of_card(card)}!")
        print(f"Your hand is: {player_hand}\n")

        if player_hand == 21:
            print("BLACKJACK! You win!\n")
            player_wins += 1
            total_games += 1
            player_hand, dealer_hand = 0, 0
            print(f"START GAME #{total_games}\n")

            card = rng.next_int(13) + 1
            player_hand += min(card, 10)

            print(f"Your card is a {type_of_card(card)}!")
            print(f"Your hand is: {player_hand}\n")
        elif player_hand > 21:
            print("You exceeded 21! You lose.\n")
            dealer_wins += 1
            total_games += 1
            player_hand, dealer_hand = 0, 0
            print(f"START GAME #{total_games}\n")

            card = rng.next_int(13) + 1
            player_hand += min(card, 10)

            print(f"Your card is a {type_of_card(card)}!")
            print(f"Your hand is: {player_hand}\n")

    elif option == 2:
        dealer_hand = rng.next_int(11) + 16
        print(f"Dealer's hand: {dealer_hand}")
        print(f"Your hand is: {player_hand}\n")

        if player_hand == dealer_hand:
            print("It's a tie! No one wins!\n")
            tie_games += 1
            total_games += 1
            player_hand, dealer_hand = 0, 0
            print(f"START GAME #{total_games}\n")

            card = rng.next_int(13) + 1
            player_hand += min(card, 10)

            print(f"Your card is a {type_of_card(card)}!")
            print(f"Your hand is: {player_hand}\n")
        elif dealer_hand == 21 or player_hand < dealer_hand < 21:
            print("Dealer wins!\n")
            dealer_wins += 1
            total_games += 1
            player_hand, dealer_hand = 0, 0
            print(f"START GAME #{total_games}\n")

            card = rng.next_int(13) + 1
            player_hand += min(card, 10)

            print(f"Your card is a {type_of_card(card)}!")
            print(f"Your hand is: {player_hand}\n")
        else:
            print("You win!\n")
            player_wins += 1
            total_games += 1
            player_hand, dealer_hand = 0, 0
            print(f"START GAME #{total_games}\n")

            card = rng.next_int(13) + 1
            player_hand += min(card, 10)

            print(f"Your card is a {type_of_card(card)}!")
            print(f"Your hand is: {player_hand}\n")

    elif option == 3:
        print(f'''Number of Player wins: {player_wins}
Number of Dealer wins: {dealer_wins}
Number of tie games: {tie_games}
Total # of games played is: {total_games-1}
Percentage of Player wins: {player_wins/(total_games-1) * 100:.1f}%
''')
    elif option == 4:
        break
    else:
        print("Invalid input!")
        print("Please enter an integer value between 1 and 4.\n")