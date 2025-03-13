import random

def buy_weapon():
    """Allows the player to buy a weapon."""
    weapons = {
        'Pistol': {'damage': (10, 30), 'cost': 100},
        'Rifle': {'damage': (20, 50), 'cost': 300},
        'Sniper': {'damage': (50, 80), 'cost': 500}
    }
    print("Available weapons:")
    for weapon, stats in weapons.items():
        print(f"{weapon}: Damage {stats['damage'][0]}-{stats['damage'][1]}, Cost: {stats['cost']}")
    
    while True:
        choice = input("Choose a weapon (Pistol, Rifle, Sniper): ").capitalize()
        if choice in weapons:
            return weapons[choice]
        print("Invalid choice, try again.")

def shoot(attacker, defender, weapon):
    """Simulates a shooting event."""
    hit_chance = random.randint(1, 100)
    if hit_chance > 30:  # 70% chance to hit
        damage = random.randint(weapon['damage'][0], weapon['damage'][1])
        defender['health'] -= damage
        print(f"{attacker['name']} shoots {defender['name']} for {damage} damage!")
        if defender['health'] <= 0:
            print(f"{defender['name']} is eliminated!")
    else:
        print(f"{attacker['name']} missed the shot!")

def game_loop():
    """Main game loop."""
    print("Counter-Strike: Text Edition")
    print("Choose your side:\n1. Terrorist\n2. Counter-Terrorist")
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == '1':
            player = {'name': 'Terrorist', 'health': 100}
            enemy = {'name': 'Counter-Terrorist', 'health': 100}
            break
        elif choice == '2':
            player = {'name': 'Counter-Terrorist', 'health': 100}
            enemy = {'name': 'Terrorist', 'health': 100}
            break
        print("Invalid choice, try again.")
    
    print("You have $500 to buy a weapon.")
    weapon = buy_weapon()
    
    turn = 0
    while player['health'] > 0 and enemy['health'] > 0:
        turn += 1
        print(f"\n--- Round {turn} ---")
        shoot(player, enemy, weapon)
        if enemy['health'] > 0:
            enemy_weapon = {'damage': (20, 50)}  # Basic enemy weapon
            shoot(enemy, player, enemy_weapon)
    
    if player['health'] > 0:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    game_loop()
