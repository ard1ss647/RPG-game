from operator import invert
from random import randint

races = ['human', 'elf', 'dwarf']
classes = ['barbarian', 'wizard', 'rogue']
lvls = {i: round(300 * (i - 1) ** 1.5) for i in range(1, 21)}  # More balanced XP curve
marker = 0

def roll(dice):
    return randint(1,dice)

class Player:

    def __init__(self, name, race, p_class):
        self.name = name
        self.race = race
        self.p_class = p_class

        self.stren = 0
        self.dex = 0
        self.con = 0
        self.intel = 0
        self.wis = 0
        self.cha = 0
        self.maxhp = 10
        self.hp = self.maxhp
        self.lvl = 1
        self.xp = 0
        self.defence = 10
        self.basic_defence = 10
        self.attack = 0
        self. basic_attack = 0
        self.gold = 500
        self.damage = 4
        self.maxmana = 0
        self.mana = 0
        self.spells = []
        self.potions = []
        self.equipment = {
            'weapon': None,
            'body_armor': None,
            'head': None,
            'gloves': None,
            'boots': None,
            'ring_l': None,
            'ring_r': None,
            'artefact_1': None,
            'artefact_2': None
        }
        self.inventory = []
        self.scrolls = []

        self.food = 5

        self.choose_race(race)
        self.choose_class(p_class)

    def choose_race(self, race='human'):
        if race not in races:
            print("Invalid race chosen!")
            return

        self.race = race

        if race == 'human':
            self.stren += 1
            self.dex += 1
            self.con += 1
            self.intel += 1
            self.wis += 1
            self.cha += 1
            self.hp += 2
            self.maxhp += 2
        elif race == 'elf':
            self.dex += 3
            self.con += 1
            self.intel += 2
            self.wis += 2
            self.cha += 1
            self.hp += 1
            self.maxhp += 1
            self.defence += 1
            self.basic_defence += 1
        elif race == 'dwarf':
            self.stren += 2
            self.dex += 1
            self.con += 3
            self.intel += 1
            self.wis += 2
            self.cha -= 1
            self.hp += 3
            self.maxhp += 3
            self.defence += 1
            self.basic_defence += 1

    def choose_class(self, p_class='barbarian'):
        if p_class not in classes:
            print("Invalid class chosen!")
            return

        self.p_class = p_class

        if p_class == 'barbarian':
            self.stren += 3
            self.con += 1
            self.hp += 4
            self.maxhp += 4
            self.attack += 2
            self.basic_attack += 2
        elif p_class == 'wizard':
            self.intel += 3
            self.wis += 2
            self.maxmana = 60
            self.mana = 60
            self.spells = []
        elif p_class == 'rogue':
            self.dex += 3
            self.intel += 2
            self.cha += 1
            self.attack += 2
            self.basic_attack += 2
            self.defence += 1
            self.basic_defence += 1
    def count_xp(self):
        print(f'{self.name} is {self.lvl} lvl, has {self.xp} xp and need {lvls[self.lvl + 1] - self.xp} more to get to {self.lvl +1 } lvl')
    def lvl_up(self):
        self.lvl += 1
        pts = 3
        self.maxhp += 1
        if self.lvl % 2 == 0:
            self.attack += 1
        elif self.p_class == 'wizard':
            self.maxmana += 75
        while pts>0:
            self.stats()
            choise = int(input(f"You've got {pts} more points. Choose what aspect do you want to improve: \n\t1 - STR 4 - INT\n\t2 - DEX 5 - WIS\n\t3 - CON 6 - CHA\nYour choise: "))
            if choise == 1:
                self.stren += 1
                pts -= 1
            elif choise == 2:
                self.dex += 1
                pts -= 1
            elif choise == 3:
                self.con += 1
                pts -= 1
            elif choise == 4:
                self.intel += 1
                pts -= 1
            elif choise == 5:
                self.wis += 1
                pts -= 1
            elif choise == 6:
                self.cha += 1
                pts -= 1
            else:
                print("No such aspect. Try again")
        self.stats()
    def check_xp(self):
        while self.xp >= lvls[self.lvl + 1]:
            self.lvl_up()
    def get_xp(self, xp):
        self.xp += xp
        self.check_xp()
        self.count_xp()

    def stats(self):
        print(f'STR = {self.stren}')
        print(f'DEX = {self.dex}')
        print(f'CON = {self.con}')
        print(f'INT = {self.intel}')
        print(f'WIS = {self.wis}')
        print(f'CHA = {self.cha}\n')
        print(f'HP = {self.hp}/{self.maxhp}')
        if player_clas == 'wizard':
            print(f'MANA = {self.mana}/{self.maxmana}')
        print(f'DEFENCE = {self.defence}')
        print(f'ATTACK = {self.attack}\n')
        print(f'LVL = {self.lvl}')
        print(f'XP = {self.xp}\n')
    def item_name(self, slot):
        if self.equipment[slot] == None:
            return 'Empty'
        else:
            return self.equipment[slot].name
    def equipment_(self):
        print(f'Weapon - {self.item_name('weapon')}')
        print(f'Body armor - {self.item_name('body_armor')}')
        print(f'Head - {self.item_name('head')}')
        print(f'Gloves - {self.item_name('gloves')}')
        print(f'Boots - {self.item_name('boots')}')
        print(f'Left ring - {self.item_name('ring_l')}')
        print(f'Right ring - {self.item_name('ring_r')}')
        print(f'First artefact - {self.item_name('artefact_1')}')
        print(f'Second artefact - {self.item_name('artefact_2')}')

    def equip(self):
        for item in self.inventory:
            print(item.name)
        item_chosen = input('Choose your item: ')
        for item in self.inventory:
            if item_chosen.lower() == item.name.lower() and item in self.inventory:
                if self.equipment[item.slot] is not None:
                    Item.put_off(self.equipment[item.slot], self)
                    self.inventory.append(self.equipment[item.slot])
                self.equipment[item.slot] = item
                self.inventory.remove(item)
                Item.put_on(item, self)
            else:
                print('You do not posses this item')
            break
    #add item removal => stats back to 0
    def unequip(self):
        self.equipment_()
        item_chosen = input('Choose an item you want to put off: ')
        for equipped_item in self.equipment.values():
            if equipped_item != None:
                if equipped_item.name.lower() == item_chosen.lower():
                    for item in items:
                        if item.name.lower() == equipped_item.name.lower():
                            item_chosen = item
                            self.equipment[item_chosen.slot] = None
                            Item.put_off(item_chosen, self)
                            self.inventory.append(item_chosen)
                            break
                    break




class Enemy:
    def __init__(self, name, hp, attack, defence, xp, damage, deal, gold, lvl):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.xp = xp
        self.damage = damage
        self.deal = deal
        self.gold = gold
        self.lvl = lvl

    def damage_enemy(self, p_attack, p_damage):
        p_hit = p_attack + roll(20)
        print(f"You've got {p_hit} for this attack")
        if p_hit >= self.defence:
            dealt = roll(p_damage) + 2
            self.hp -= dealt
            print(f"\tYou've dealt {dealt} damage! {self.name} has {max(0, self.hp)} HP left.")
            if self.hp < 0:
                self.hp = 0
        else:
            print(f"\tYou've missed! {self.name} still has {self.hp} HP left.")

    def damage_player(self, player):
        hit = self.attack + roll(20)
        print(f"{self.name} has got {hit} for this attack, while your AC is {player.defence}")
        if hit >= player.defence:
            dealt = roll(self.damage)
            player.hp -= dealt
            print(f"\tYou got hit for {dealt} damage! You have {max(0, player.hp)} HP left.")
        else:
            print(f"\t{self.name} has missed! You still have {player.hp} HP left.")

    def drop(self, player):
        drop_items = []
        chance = roll(10)
        if chance >= 6:
            for item in items:
                if -2 <= item.lvl - self.lvl <= 2:
                    drop_items.append(item)
            player.inventory.append(drop_items[randint(0,len(drop_items)-1)])
            print(f"{item.name} has been added to your inventory.")




class Spell:
    def __init__(self, name, damage=0, mana=0, wis=0, healing=0, defense_boost=0):
        self.name = name
        self.damage = damage
        self.mana = mana
        self.wis = wis
        self.healing = healing
        self.defense_boost = defense_boost

    def magic_damage(self, player, enemy):
        hit = roll(20) + player.attack
        print(f"You've got {hit} for this attack.")
        if hit >= enemy.defence:
            damage = self.damage + player.intel // 2 + roll(player.damage)
            enemy.hp -= damage
            if enemy.hp < 0:
                enemy.hp = 0
            print(f"\tYou've dealt {damage} magic damage! Now {enemy.name} has {enemy.hp} HP.")
        else:
            print('\tMiss!')
    def heal(self, player):
        if self.healing > 0:
            player.hp += self.healing + player.int // 2
            print(f"{player.name} heals for {self.healing} HP! Now they have {player.hp} HP.")


    def boost_defense(self, player):
        if self.defense_boost > 0:
            player.defence += self.defense_boost
            print(f"{player.name}'s defense increased by {self.defense_boost}!")

class Item:
    def __init__(self, name, slot, stats, cost, lvl, id):
        self.name = name
        self.slot = slot
        self.stats = stats
        self.cost = cost
        self.lvl = lvl
        self.id = id
    #stats = [hp, mana, attack, defence]
    def put_on(self, player):
        player.maxhp += self.stats[0]
        player.hp += self.stats[0]
        player.maxmana += self.stats[1]
        player.mana += self.stats[1]
        player.attack += self.stats[2]
        player.defence += self.stats[3]
    def put_off(self, player):
        player.maxhp -= self.stats[0]
        player.hp -= self.stats[0]
        player.maxmana -= self.stats[1]
        player.mana -= self.stats[1]
        player.attack -= self.stats[2]
        player.defence -= self.stats[3]

    def __str__(self):
        return f"{self.name} (Slot: {self.slot}, Stats: {self.stats}, Cost: {self.cost}, Level: {self.lvl})"
    def __repr__(self):
        return self.__str__()

def item_gen():
    original_items = items.copy()
    for item in original_items:
        new_stats = []
        for stat in item.stats:
            stat -= 2
            if stat < 0:
                stat = 0
            new_stats.append(stat)
        items.append(Item(f'Broken {item.name}', item.slot, new_stats, item.cost // 2, item.lvl, 0))

        new_stats = []
        for stat in item.stats:
            if item.stats.index(stat) % 2 == 0:
                stat -= 2
            else:
                stat -= 1
            if stat < 0:
                stat = 0
            new_stats.append(stat)
        items.append(
            Item(f'Unprepared {item.name}', item.slot, new_stats, item.cost // 1.75, item.lvl, 1))

        new_stats = []
        for stat in item.stats:
            stat -= 1
            if stat < 0:
                stat = 0
            new_stats.append(stat)
        items.append(
            Item(f'Weak {item.name}', item.slot, new_stats, item.cost // 1.25, item.lvl, 2))

        new_stats = []
        for stat in item.stats:
            if stat != 0:
                stat += 1
            if stat < 0:
                stat = 0
            new_stats.append(stat)
        items.append(
            Item(f'Sharpened {item.name}', item.slot, new_stats, item.cost // 0.8, item.lvl, 4))

        new_stats = []
        for stat in item.stats:
            if stat != 0:
                if item.stats.index(stat) % 2 == 0:
                    stat += 2
                else:
                    stat += 1
            if stat < 0:
                stat = 0
            new_stats.append(stat)
        items.append(
            Item(f'Prepared {item.name}', item.slot, new_stats, item.cost // 0.66, item.lvl, 5))

        new_stats = []
        for stat in item.stats:
            if stat != 0:
                stat += 2
            if stat < 0:
                stat = 0
            new_stats.append(stat)
        items.append(
            Item(f'Legendary {item.name}', item.slot, new_stats, item.cost // 0.5, item.lvl, 6))


class Potion:
    def __init__(self, name, mana, hp, defence, attack, cost):
        self.name = name
        self.mana = mana
        self.hp = hp
        self.defence = defence
        self.attack = attack
        self.cost = cost
    def drink(self, player):
        print(f"You've used {self.name}.")
        if self.mana != 0:
            player.mana += self.mana
            if player.mana > player.maxmana:
                player.mana = player.maxmana
            print(f"{self.mana} mana have been restored and now you have {player.mana}/{player.maxmana} mana")
        if self.hp != 0:
            player.hp += self.hp
            if player.hp > player.maxhp:
                player.hp = player.maxhp
            print(f"{self.hp} HP have been restored and now you have {player.hp}/{player.maxhp} HP")
        if self.defence != 0:
            player.defence += self.defence
            print(f'Your defence has been increased by {self.defence} and now you have {player.defence}')
        if self.attack != 0:
            player.attack += self.attack
            print(f'Your attack has been increased by {self.attack} and now you have {player.attack}')

class Trader:
    def __init__(self, items, food):
        self.items = items
        self.food = food
    def trade(self, player):
        print("You've encountered a wardening trader")
        food = roll(4)+4
        item_names = []
        for item in items:
            item_names.append(item.name.lower())
        while True:
            print(f'You have {player.gold} gold\nWould you like to buy or sell anything?\n\t1 - buy\n\t2 - sell\n\t3 - leave')
            action = input('Your choice: ')
            if action == '1':
                for item in items:
                    print(f'{item.name} - {item.cost}')
                print(f'Food - 25 (x{food})')
                choise = input('Choose an item to buy: ')
                if choise.lower() == 'food':
                    amount = int(input(f'Choose the amount(1-{food}): '))
                    if 0 < amount <= food and player.gold >= 25*amount:
                        food -= amount
                        player.food += amount
                        player.gold -= 25*amount
                        print(f"You've bought {amount} food and now you have {player.food} food and {player.gold} gold.")
                    else:
                        print('Insufficient amount of food!')
                elif choise in item_names:
                    for item in items:
                        if item.name.lower() == choise.lower():
                            if item.cost <= player.gold:
                                player.inventory.append(item)
                                player.gold -= item.cost
                                print(f"You've bought {item.name} and now you have {player.gold} gold.")
                            else:
                                print('No enough gold!')
                            break
                else:
                    print('No such item, try again.')
            elif action == '2':
                print('\nInventory:')
                for item in player.inventory:
                    print(f'{item.name}')
                print(f'\nGOLD = {player.gold}')
                print('\nWhat would you like to sell?')
                sell = input('Item: ')
                inventory_item_names = []
                for item in player.inventory:
                    inventory_item_names.append(item.name.lower())
                if sell.lower() in inventory_item_names:
                    for item in player.inventory:
                        if item.name.lower() == sell.lower():
                            sure = input(f"Are you sure you want to sell {item.name} for {int(item.cost // 1.42)} gold? (y/n): ")
                            if sure.lower() == 'y':
                                player.inventory.remove(item)
                                player.gold += int(item.cost // 1.42)
                                break
                            elif sure.lower() == 'n':
                                print('You have not sold your item.')
                                break
                            else:
                                print('You have to choose between yes and no (y/n).')
                                break
                else:
                    print("You do not possess such item")
            elif action == '3':
                print('Okay, bye!')
                break
            else:
                print('No such option, try again')

class Scroll:
    def __init__(self, lvl, spell, cost):
        self.lvl = lvl
        self.spell = spell
        self.cost = cost
    def get(self, player):
        player.scrolls.append(self)
    def use(self, player):
        if player.lvl >= self.lvl:
            if player.wis >= self.spell.wis:
                player.spells.append(self.spell)
                player.scrolls.remove(self)
            else:
                print('Your wisdom is not high enough.')
        else:
            print('Your level is not high enough.')

# class ItemGen:
#     def item_generation(self, item):
#         new_item = item
#         for stat in new_item.stats:
#             if stat != 0:
#                 stat += randint(-2,2)
#                 if stat < 1:
#                     stat = 1
#         new_items.append(new_item)
#


def cast(player, enemy):
    for spell in player.spells:
        print(f"{spell.name} - DMG = {spell.damage}, Healing = {spell.healing}, Defense Boost = {spell.defense_boost}, Mana = {spell.mana}")
    print(f"You have {player.mana} mana")
    spell_chosen = input("Choose your spell: ")
    for spell in player.spells:
        if spell.name.lower() == spell_chosen.lower():
            if player.mana < spell.mana:
                print("Not enough mana!")
                return
            player.mana -= spell.mana
            if spell.damage > 0:
                spell.magic_damage(player, enemy)
            elif spell.healing > 0:
                spell.heal(player)
            elif spell.defense_boost > 0:
                spell.boost_defense(player)
            return
    print("Invalid spell choice!")

def fight(player, enemy):
    print(f"You've encountered {enemy.name}, and he has {enemy.hp} HP")

    while player.hp > 0 and enemy.hp > 0:
        print("\n1 - Flee \n2 - Make a deal \n3 - Fight\n4 - Drink a potion")
        choice = input("Choose your action: ")

        if choice == "1":
            if player.dex + roll(20) >= roll(20):
                print("You've successfully left the fight")
                return
            print(f"You didn't flee and now {enemy.name} attacks first")
            enemy.damage_player(player)

        elif choice == "2":
            if enemy.deal and player.cha + roll(20) > roll(20):
                print(f"{enemy.name} has decided not to fight you.")
                return
            print(f"You didn't make a deal and now {enemy.name} attacks first")
            enemy.damage_player(player)

        elif choice == "3":
            if player.p_class == 'wizard':
                cast(player, enemy)
                if enemy.hp <= 0:
                    print(f"Congratulations! You won and gained {enemy.xp} XP!")
                    player.get_xp(enemy.xp)
                    player.defence = player.basic_defence
                    return
            else:
                enemy.damage_enemy(player.attack, player.damage)
                if enemy.hp <= 0:
                    got_gold = enemy.gold + roll(3)
                    print(f"Congratulations! You won and gained {enemy.xp} XP and {got_gold} gold!")
                    player.get_xp(enemy.xp)
                    player.gold += got_gold
                    return
            enemy.damage_player(player)
        elif choice == "4":
            print("Your potions:")
            for potion in player.potions:
                print(f'{potion.name} - Mana = {potion.mana}, HP = {potion.hp}, Defence = {potion.defence}, Attack = {potion.attack}')
            chosen_potion = input('Choose your potion: ')
            for potion in player.potions:
                if potion in player.potions:
                    if potion.name.lower() == chosen_potion.lower():
                        Potion.drink(potion, player)
                        player.potions.remove(potion)
                        break
                else:
                    print('No such potion found.')
                    break
            enemy.damage_player(player)
        else:
            print('Invalid option. Try again.')
    if player.hp <= 0:
        print("You've lost!")
        exit()
    player.attack = player.basic_attack
    player.defence = player.basic_defence


# Character creation
#Enemy -> name, hp, attack, defence, xp, damage
def enemy_lvl(lvl):
    if lvl % 2 != 0:
        return lvl+1
    else:
        return lvl


enemies = {
    2: [
        Enemy("Goblin", 7, 4, 12, 50, 5, True, 10, 2),
        Enemy("Kobold", 5, 3, 10, 25, 4, True, 8, 2),
        Enemy("Giant Rat", 6, 2, 11, 30, 3, False, 6, 2),
        Enemy("Skeleton", 8, 3, 13, 40, 4, False, 9, 2),
        Enemy("Zombie", 9, 4, 12, 45, 5, False, 10, 2)
    ],
    4: [
        Enemy("Orc", 15, 6, 13, 100, 8, True, 20, 4),
        Enemy("Hobgoblin", 11, 5, 15, 75, 6, True, 18, 4),
        Enemy("Gnoll", 12, 5, 14, 80, 7, False, 19, 4),
        Enemy("Giant Spider", 10, 4, 12, 70, 6, False, 17, 4),
        Enemy("Bandit", 13, 5, 13, 85, 7, True, 18, 4)
    ],
    6: [
        Enemy("Ogre", 300, 8, 11, 300, 13, True, 60, 6),
        Enemy("Bugbear", 180, 6, 16, 200, 11, True, 50, 6),
        Enemy("Worg", 30, 7, 14, 220, 10, False, 25, 6),
        Enemy("Harpy", 25, 6, 13, 180, 9, False, 22, 6),
        Enemy("Giant Lizard", 35, 7, 15, 250, 12, False, 28, 6)
    ],
    8: [
        Enemy("Ettin", 85, 10, 14, 1100, 18, False, 70, 8),
        Enemy("Owlbear", 59, 9, 13, 700, 15, False, 55, 8),
        Enemy("Troll", 84, 8, 15, 1200, 16, True, 75, 8),
        Enemy("Giant Crocodile", 85, 9, 14, 1000, 17, False, 70, 8),
        Enemy("Chimera", 114, 11, 16, 2500, 19, False, 85, 8)
    ],
    10: [
        Enemy("Hill Giant", 105, 11, 15, 1800, 21, True, 90, 10),
        Enemy("Frost Giant", 138, 12, 16, 3900, 25, True, 110, 10),
        Enemy("Fire Giant", 162, 13, 18, 5000, 28, False, 125, 10),
        Enemy("Cloud Giant", 200, 14, 19, 7200, 30, True, 140, 10),
        Enemy("Stone Giant", 126, 12, 17, 4500, 26, True, 115, 10)
    ],
    12: [
        Enemy("Young Red Dragon", 178, 14, 18, 11000, 40, False, 200, 12),
        Enemy("Young Blue Dragon", 152, 13, 17, 8400, 36, False, 180, 12),
        Enemy("Young Green Dragon", 136, 12, 16, 7200, 32, True, 160, 12),
        Enemy("Young Black Dragon", 127, 11, 15, 5900, 30, False, 150, 12),
        Enemy("Young White Dragon", 133, 10, 14, 5500, 28, False, 140, 12)
    ],
    14: [
        Enemy("Adult Red Dragon", 256, 19, 22, 50000, 60, False, 400, 14),
        Enemy("Adult Blue Dragon", 225, 18, 21, 45000, 55, False, 380, 14),
        Enemy("Adult Green Dragon", 207, 17, 20, 40000, 50, True, 350, 14),
        Enemy("Adult Black Dragon", 195, 16, 19, 35000, 45, False, 330, 14),
        Enemy("Adult White Dragon", 200, 15, 18, 30000, 40, False, 310, 14)
    ],
    16: [
        Enemy("Ancient Red Dragon", 546, 24, 28, 180000, 90, False, 900, 16),
        Enemy("Ancient Blue Dragon", 481, 23, 27, 150000, 85, False, 850, 16),
        Enemy("Ancient Green Dragon", 432, 22, 26, 130000, 80, True, 800, 16),
        Enemy("Ancient Black Dragon", 367, 21, 25, 110000, 75, False, 750, 16),
        Enemy("Ancient White Dragon", 333, 20, 24, 90000, 70, False, 700, 16)
    ],
    18: [
        Enemy("Lich", 135, 18, 20, 50000, 50, False, 450, 18),
        Enemy("Beholder", 180, 19, 22, 75000, 55, False, 480, 18),
        Enemy("Death Knight", 180, 20, 21, 80000, 60, False, 500, 18),
        Enemy("Balor", 262, 22, 24, 120000, 70, False, 600, 18),
        Enemy("Pit Fiend", 300, 21, 23, 100000, 65, False, 580, 18)
    ],
    20: [
        Enemy("Tarrasque", 676, 30, 35, 500000, 120, False, 1200, 20),
        Enemy("Kraken", 472, 28, 32, 300000, 100, False, 1000, 20),
        Enemy("Tiamat", 615, 30, 34, 400000, 110, False, 1150, 20),
        Enemy("Bahamut", 615, 30, 34, 400000, 110, False, 1150, 20),
        Enemy("Empyrean", 313, 26, 30, 200000, 90, True, 950, 20)
    ]
}


spells = [
    Spell("Firebolt", 6, 6, 2),
    Spell("Ice Shard", 8, 12, 3),
    Spell("Lightning Strike", 14, 28, 7),
    Spell("Earthquake", 20, 45, 10),
    Spell("Meteor Shower", 30, 70, 15),

    Spell("Wind Slash", 7, 10, 4),
    Spell("Water Jet", 10, 18, 5),
    Spell("Firestorm", 16, 35, 10),
    Spell("Arcane Blast", 22, 55, 12),

    # Healing Spells
    Spell("Healing Light", healing=10, mana=15, wis=2),
    Spell("Greater Heal", healing=18, mana=35, wis=5),
    Spell("Divine Restoration", healing=30, mana=70, wis=8),

    # Defensive Spells
    Spell("Magic Shield", defense_boost=6, mana=20, wis=4)
]

scrolls = [
    Scroll(1, Spell('Firebolt'), 6),
    Scroll(3, Spell('Ice Shard'), 12),
    Scroll(7, Spell('Lightning Strike'), 28),
    Scroll(10, Spell('Earthquake'), 45),
    Scroll(15, Spell('Meteor Shower'), 70),

    Scroll(4, Spell('Wind Slash'), 10),
    Scroll(5, Spell('Water Jet'), 18),
    Scroll(10, Spell('Firestorm'), 35),
    Scroll(12, Spell('Arcane Blast'), 55),

    Scroll(2, Spell('Healing Light'), 15),
    Scroll(5, Spell('Greater Heal'), 35),
    Scroll(8, Spell('Divine Restoration'), 70),

    Scroll(4, Spell('Magic Shield'), 20)
]

items = [                                    #stats = [hp, mana, attack, defence]
    Item('Advanced armor', 'body_armor', [0, 0, 2, 5], 350, 1, 3),
    Item('Basic armor', 'body_armor', [0, 0, 1, 3], 150, 1, 3),
    Item('Short sword', 'weapon', [0, 0, 3, 0], 100, 1, 3)
]

potions = [
    Potion('Minor healing potion', 0, 5, 0, 0, 25),
    Potion('Minor mana potion', 25, 0, 0, 0, 25),
    Potion('Minor defence potion', 0, 0, 3, 0, 30),
    Potion('Minor attack potion', 0, 0, 0, 3, 30)
]

trader = Trader(items, 4+roll(3))

player_name = 'Alex'
player_race = 'elf'
player_clas = 'barbarian'

'''Main game'''

'''player_name = input("Choose your character's name: ")
print(f'Available races are: {races}')
player_race = input("Choose your character's race: ").lower()
print(f'Available classes are: {classes}')
player_clas = input("Choose your character's class: ").lower()'''
player = Player(player_name, player_race, player_clas)
Player.stats(player)

for i in range(4):
    player.potions.append(potions[i])

Scroll.get(scrolls[0], player)

item_gen()

turn = 0
trader = 6 + roll(4)
trader_check = 0
while True:
    turn += 1
    trader_check += 1
    print("\nWhat do you want to do?")
    print('\t1 - go deeper\n\t2 - make a rest\n\t3 - see your stats\n\t4 - inventory\n\t5 - spells')
    if player_clas == 'wizard':
        print('\t5 - see your spells')
    action = input('Your choice: ')
    if action == '1':
        if trader - trader_check <= 0:
            Trader.trade(trader, player)
            trader = 6 + roll(4)
            trader_check = 0
        else:
            enemy_template = enemies[enemy_lvl(player.lvl)][roll(5) - 1]
            enemy = Enemy(enemy_template.name, enemy_template.hp, enemy_template.attack,
                          enemy_template.defence, enemy_template.xp, enemy_template.damage, enemy_template.deal, enemy_template.gold, enemy_template.lvl)
            fight(player, enemy)
            print(f'Now you have {player.hp} HP')
    elif action == '2':
        if player.food > 0:
            player.hp = player.maxhp
            player.mana = player.maxmana
            player.food -= 1
            print(f"You spent one food and now you're fully healed and ready to fight!\n\tCurrent HP: {player.hp}\n\tCurrent food = {player.food}")
            if player_clas == 'wizard':
                print(f'\tCurrent MANA: {player.mana}')
        else:
            print("You don't have enough food!")
    elif action == '3':
        Player.stats(player)
    elif action == '4':
        print('\nEquipment:')
        Player.equipment_(player)
        print('\nInventory:')
        for item in player.inventory:
            print(f'{item.name}')
        print(f'\nGOLD = {player.gold}')
        print('\nFood x', player.food)
        if player.potions != []:
            print('\nPotions:')
            for potion in player.potions:
                    print(f'{potion.name} - Mana = {potion.mana}, HP = {potion.hp}, Defence = {potion.defence}, Attack = {potion.attack}')
        if player.scrolls != []:
            print('\nScrolls:')
            for scroll in player.scrolls:
                print(f'Scroll of {scroll.spell.name}')
        print('\n1 - go back\n2 - equip item\n3 - unequip item')
        if player.scrolls != []:
            print('4 - use a scroll')
        action_chosen = input('Choose your action: ')
        if action_chosen == "1":
            continue
        elif action_chosen == "2":
            Player.equip(player)
        elif action_chosen == "3":
            Player.unequip(player)
        elif action_chosen == "4":
            while True:
                for scroll in player.scrolls:
                    print(f'Scroll of {scroll.spell.name}')
                chosen_scroll = input("Choose your scroll: ")
                for scroll in scrolls:
                    if chosen_scroll.lower() == scroll.spell.name.lower():
                        Scroll.use(scroll, player)
                        print(f"You've used the scroll of {scroll.spell.name}")
                        marker = 1
                        break
                if marker == 0:
                    print('No such scroll! Try again.')
                elif marker == 1:
                    marker = 0
        else:
            print('No such option.')
            continue

    elif action == '5':
        for spell in player.spells:
            print(f"{spell.name} - DMG = {spell.damage}, Healing = {spell.healing}, Defense Boost = {spell.defense_boost}, Mana = {spell.mana}")
        if player.spells == []:
            print("You don't have any spells")
    elif action == 'trade':
        Trader.trade(trader, player)
    elif action == 'test':
        Enemy.drop(enemies[2][0], player)
    else:
        print('\tNo such option, choose something else.')