import random
random.seed()
import pygame
import pygame_gui
from player import *
from enemies import *
pygame.init()
pygame.freetype.init()
manager = pygame_gui.UIManager((900,700))
from GUI import *

def levelup(player, battle_counter, exp):
    if player.exp >= exp: #player.level == 1 and
        return 6
    else:
        if battle_counter == 3:
            return 0
        else:
            return 3

def health_potion(player):
    player.health = min(player.health + 40, player.max_health)
    text_box.set_text(f"You drank a Health Potion. Health: {player.health}")

def mana_potion(player):
    player.mana = min(player.mana + 30, player.max_mana)
    text_box.set_text(f"You drank a Mana Potion. Mana: {player.mana}")

def ticket(player, ritual):
    text_box.set_text("it looks like you may have started some sort of ritual.")
    ritual = True

def interact_e(font_name, screen):
    interact = font_name.render(f" (E) to interact ", False, "Black")
    interact_rect = interact.get_rect(midbottom = (450,680))
    pygame.draw.rect(screen, "White", interact_rect)
    screen.blit(interact, interact_rect)

def get_random_enemy(player, ritual):
    if ritual == True:
        print("get_random_enemy is in if ritual== true")
        return Black_Wyvern()
    else:
        if player.level < 4: 
            enemies = [Goblin(), Orc(), Salamander(), Rat()]
            return random.choice(enemies)
        elif player.level < 7:
            enemies= [Salamander(), Young_Dragon(), Goblin_Shaman()]
            return random.choice(enemies)  

def experience(player, enemy, text_box):
    exp = 0
    gold = 0
    if isinstance(enemy, Orc):
        exp = 30
        gold = random.randint(5, 10)
    elif isinstance(enemy, Goblin):
        exp = 25
        gold = random.randint(2, 6)
    elif isinstance(enemy, Salamander):
        exp = 45
        gold = random.randint(7, 15)
    elif isinstance(enemy, Rat):
        exp = 20
        gold = random.randint(0, 3)
    elif isinstance(enemy, Young_Dragon):
        exp = 70
        gold = random.randint(11, 18)
    elif isinstance(enemy, Farmer):
        exp = 15
        gold = 0
    elif isinstance(enemy, Cassius):
        exp = 40
        gold = random.randint(65, 80)
    elif isinstance(enemy, Eris):
        exp = 80
        gold = random.randint(18, 30)
    elif isinstance(enemy, Goblin_Shaman):
        exp = 80
        gold = random.randint(15, 23)
    elif isinstance(enemy, Black_Wyvern):
        exp = 120
        gold = random.randint(27, 38)

    player.exp += exp
    player.gold += gold

    text_box.set_text(f"You received {exp} experience and {gold} gold!")
