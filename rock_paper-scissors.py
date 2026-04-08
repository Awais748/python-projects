
import random


print("=" * 60)
print("🪨 ROCK PAPER SCISSORS GAME 📄")
print("=" * 60)
print("\n📋 Rules:")
print("- Rock beats Scissors (✊ > ✂️)")
print("- Scissors beats Paper (✂️ > 📄)")
print("- Paper beats Rock (📄 > ✊)")
print("- Enter: r (rock), p (paper), s (scissors), q (quit)\n")

player_score = 0
computer_score = 0
rounds_played = 0


while True:
    player_choice = input("🎮 Your choice (r/p/s) or q to quit: ").lower().strip()
    
    if player_choice == 'q':
        print("\n" + "=" * 60)
        print("📊 FINAL SCORE")
        print("=" * 60)
        print(f"You: {player_score} | Computer: {computer_score}")
        print("Thanks for playing! 🎉")
        break
    
    if player_choice not in ['r', 'p', 's']:
        print("❌ Invalid choice! Enter r, p, or s only.\n")
        continue
    
    computer_choice = random.choice(['r', 'p', 's'])
    
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    emojis = {'r': '✊', 'p': '📄', 's': '✂️'}
    
    player_display = choices[player_choice]
    computer_display = choices[computer_choice]
    
    print(f"\n{emojis[player_choice]} You chose: {player_display}")
    print(f"{emojis[computer_choice]} Computer chose: {computer_display}")
    
    if player_choice == computer_choice:
        print("🤝 It's a TIE!")
    
    elif (player_choice == 'r' and computer_choice == 's'):
        print("🎉 YOU WIN THIS ROUND!")
        player_score += 1
    
    elif (player_choice == 'p' and computer_choice == 'r'):
        print("🎉 YOU WIN THIS ROUND!")
        player_score += 1
    
    elif (player_choice == 's' and computer_choice == 'p'):
        print("🎉 YOU WIN THIS ROUND!")
        player_score += 1
    
    else:
        print("😢 COMPUTER WINS THIS ROUND!")
        computer_score += 1
    
    rounds_played += 1
    
    print(f"\n📊 Score: You {player_score} | Computer {computer_score}")
    print(f"📈 Rounds played: {rounds_played}")
    print("-" * 60 + "\n")
