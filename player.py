import random
random.seed()
import pygame
import pygame_gui
pygame.init()
pygame.freetype.init()
manager = pygame_gui.UIManager((900,700))
from GUI import *

class Fighter:
    def __init__(self):
        self.name = "Fighter"
        self.attack = 18
        self.health = 100
        self.defense = 40
        self.mana = 20
        self.crit_chance = 0
        self.evasion = 2

        self.special_attacks = [
            ("Reckless Strike", 0, self.Reckless_Strike),
            ("Anticipation", 10, self.Anticipation)
            ]

    def Reckless_Strike(self,player, enemy, text_box):   #specials deal true damage as of now
        num=random.randint(1,10)
        if num>=4:
            dmg=player.attack*2+2
            enemy.health -= dmg
            player.health -= 10
            sdmg=10
            text_box.set_text(f"{player.name} dealt {dmg} damage to {enemy.name}!\nBut you hurt yourself for {sdmg} damage.\nHealth: {player.health}")
        else:
            text_box.set_text("You missed.")
        reckless_b.hide()
        anticipation_b.hide()
        retribution_b.hide()
        back.hide()
                

    def Anticipation(self,player, enemy, text_box):   #only works once???
        mana_cost = 10
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            player.defense= min(player.defense+30, 90)
            text_box.set_text(f"You strenghened your defense! Defense: {player.defense}")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.") #and let them get back to choosing one
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"
                
    def Retribution(self,player, enemy, text_box):
        dmg= player.defense/2 +5
        enemy.health -= dmg
        num = random.randint(1,10)
        if num > 3:
            enemy.blind_counter += 1
            text_box.set_text(f"You use your defense to retaliate for {dmg} damage and stunned the {enemy.name} for 1 round!")
        elif num < 4:
            text_box.set_text(f"You use your defense to retaliate for {dmg} damage!")
        reckless_b.hide()
        anticipation_b.hide()
        retribution_b.hide()
        back.hide()

class Mage:
    def __init__(self):
        self.name = "Mage"
        self.attack = 10
        self.health = 80
        self.defense = 10
        self.mana = 85
        self.crit_chance = 0
        self.evasion = 0

        self.special_attacks = [
            ("Blinding Light", 20, self.Blinding_Light),
            ("Mana Burst", 0, self.Mana_Burst),
            ("Fireball", 20, self.Fireball),
            ("Iceshard", 10, self.Iceshard)
            ]

    def Blinding_Light(self,player, enemy, text_box):
        mana_cost = 20
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            enemy.blind_counter=3
            text_box.set_text(f"You use magic to create a blinding light that blinds the enemy for 3 turns.")
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"

    def Mana_Burst(self,player, enemy, text_box):
        if player.mana > 1:
            mana_cost = player.mana / 2
            player.mana -= mana_cost
            dmg= (player.mana/2) + 15
            enemy.health -= dmg
            text_box.set_text(f"You used up half your Mana to deal {dmg} damage! Mana remaining: {player.mana}")
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"
        
    def Fireball(self,player, enemy, text_box):
        mana_cost = 20
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            dmg= player.attack * 3+2
            enemy.health -= dmg
            text_box.set_text(f"You created a flaming ball of fire and threw it onto the enemy, dealing {dmg} damage!")
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"
        
    def Iceshard(self,player, enemy, text_box):
        mana_cost = 10
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            dmg = player.attack * 2
            enemy.health -= dmg
            text_box.set_text(f"You threw a shard of ice into the enemy, dealing {dmg} damage!")        
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"

    def Electric_Shots(self,player, enemy, text_box):
        mana_cost = 20
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            shots= random.randint(1,3)
            dmg_value= random.randint(5,20)
            dmg= shots*dmg_value
            enemy.health -= dmg
            text_box.set_text(f"You send out {shots} electric shots, each dealing {dmg_value} damage for a total of {dmg}!")
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"
        
class Ranger:
    def __init__(self):
        self.name = "Ranger"
        self.attack = 20
        self.health = 90
        self.defense = 25
        self.mana = 50
        self.crit_chance = 5
        self.evasion = 2

        self.special_attacks = [
            ("Triple Arrow", 10, self.Triple_Arrow),
            ("Final Blow", 20, self.Final_Blow)
            ]

    def Final_Blow(self,player, enemy, text_box):
        mana_cost = 15
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            if enemy.health < (enemy.max_health/2):
                dmg= player.attack*2
                enemy.health -= dmg
                text_box.set_text(f"You abused the enemies weakness for a critical hit and dealt {dmg} damage!")
            else:
                dmg= (player.attack/2) - 5
                enemy.health -= dmg
                text_box.set_text(f"The enemy wasn't quite weak enough for a critical hit. You dealt {dmg} damage.")
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"

    def Triple_Arrow(self,player, enemy, text_box):
        mana_cost = 10
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            num=random.randint(1,10)
            if num>=4:
                dmg=player.attack*2-5
                text_box.set_text(f"You shot 3 arrows at once and hit the {enemy.name} for {dmg} damage!")
            else:
                dmg=8
                text_box.set_text(f"You tried to do something cool but failed. At least you dealt {dmg} damage.")       
            enemy.health -= dmg
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"
        
    def Toxic_Shot(self, player, enemy, text_box):
        mana_cost = 15
        if player.mana >= mana_cost:
            player.mana -= mana_cost
            dmg = player.attack - 5
            enemy.tox_counter += 3
            enemy.health -= dmg
            text_box.set_text(f"You hit the {enemy.name} with a poisoned arrow for {dmg} damage. The enemy is poisoned for 3 rounds.")
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "enemy_attack"
        else:
            text_box.set_text("Not enough mana.")
            reckless_b.hide()
            anticipation_b.hide()
            retribution_b.hide()
            blinding_b.hide()
            mana_b.hide()
            fireball_b.hide()
            iceshard_b.hide()
            electric_b.hide()
            final_b.hide()
            triple_b.hide()
            toxic_b.hide()
            back.hide()
            return "mana_missing"
            
class Player:
    def __init__(self,name,character_class):    #add charisma??
        self.name = name
        self.character_class = character_class
        self.attack = character_class.attack
        self.health = character_class.health
        self.defense = character_class.defense
        self.max_health = self.health
        self.max_defense = self.defense
        self.evasion = character_class.evasion
        self.mana = character_class.mana
        self.crit_chance = character_class.crit_chance
        self.max_mana = self.mana
        self.special_attacks = character_class.special_attacks
        self.level = 1
        self.gold = 0
        self.ritual = 0
        self.reputation = 0
        self.exp = 0

        self.inventory = []             # .append mit name(, func)


Fighter1 = Fighter()
Mage1=Mage()
Ranger1=Ranger()
