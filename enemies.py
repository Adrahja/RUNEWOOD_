import random
random.seed()
import pygame
import pygame_gui
pygame.init()
pygame.freetype.init()
manager = pygame_gui.UIManager((900,700))
from GUI import *

class Goblin:
  def __init__(self):
      self.name = "Goblin"
      self.attack = 10
      self.health = 30
      self.defense = 10
      self.max_health = self.health
      self.blind_counter= 0
      self.tox_counter= 0

class Orc:
  def __init__(self):
      self.name = "Orc"
      self.attack = 20
      self.health = 40
      self.defense = 15
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0

class Salamander:
  def __init__(self):
      self.name = "Salamander"
      self.attack = 23
      self.health = 60
      self.defense = 20
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0

      self.special_attacks = [
          ("Fireclaw", 1, self.Fireclaw)
          ]

  def Fireclaw(self, player, text_box):
      dmg= (self.attack  * (1 - self.defense * 1e-2)) + 5 
      player.health -= dmg
      #self.health -= 10
      text_box.set_text(f"The {self.name}'s claw lights itself aflame and scratches you for {dmg} damage!\nYour Health: {player.health}") #\nIt also hurt itself for 10 damge.

class Young_Dragon:
  def __init__(self):
      self.name = "Young Dragon"
      self.attack = 25
      self.health = 80
      self.defense = 25
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0

class Black_Wyvern:
  def __init__(self):
      self.name = "Black Wyvern"
      self.attack = 25
      self.health = 200
      self.defense = 25
      self.max_health = self.health
      self.max_attack = self.attack
      self.blind_counter = 0 
      self.tox_counter= 0                         

      self.special_attacks = [
          ("Suck Life", 1, self.Suck_Life),
          ("Tail Whip", 2, self.Tail_Whip),
          ("Hone Claws", 3, self.Hone_Claws)
          ]
      
  def Suck_Life(self,player, text_box):
      dmg = self.attack
      leech = self.attack/2
      player.health -= dmg
      self.health = min(self.health + leech, self.max_health)
      text_box.set_text(f"The Wyvern sucks out your life force for {dmg} damage and heals itself for half of it.\nYour Health: {player.health}")

  def Tail_Whip(self,player, text_box):
      dmg = (self.attack +8) - (player.defense/7)
      player.health -= dmg
      text_box.set_text(f"It hits you hard with its tailspikes and deals {dmg} damage!.\nYour health: {player.health}")

  def Hone_Claws(self,player, text_box):
      self.attack += 10
      text_box.set_text("The Wyvern sharpens its claws on nearby stones and improves its attack.")

class Goblin_Shaman:
  def __init__(self):
      self.name = "Goblin Shaman"
      self.attack = 12
      self.health = 65
      self.defense = 15
      self.max_health = self.health
      self.blind_counter= 0
      self.tox_counter= 0

      self.special_attacks = [
          ("Heal", 1, self.Heal),
          ("Staff Attack", 2, self.Staff_Attack)
          ]

  def Heal(self,player, text_box):
      min(self.health + 20, 65)
      text_box.set_text(f"The {self.name} swings his staff and heals himself for 20 health.")

  def Staff_Attack(self, player, text_box):
      dmg = self.attack*2 
      player.health -= dmg
      text_box.set_text(f"The {self.name} bonked his staff on your head and dealt {dmg} damage!\nYour Health: {player.health}")
      

class Rat:
  def __init__(self):
      self.name = "Rat"
      self.attack = 8
      self.health = 20
      self.defense = 5
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0

class Farmer:
  def __init__(self):
      self.name = "Farmer"
      self.attack = 13
      self.health = 40
      self.defense = 15
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0

class Cassius:
  def __init__(self):
      self.name = "Cassius"
      self.attack = 28
      self.health = 70
      self.defense = 5
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0

class Eris:
  def __init__(self):
      self.name = "Eris"
      self.attack = 40
      self.health = 300
      self.defense = 20
      self.max_health = self.health
      self.blind_counter = 0
      self.tox_counter= 0
