import pygame
import pygame_gui
from pygame_gui.elements import UILabel

manager = pygame_gui.UIManager((900, 700))

#TEXT BOX
text_box = pygame_gui.elements.UITextBox(
    html_text="You almost made it through to your home village which has been troubled by monster attacks. But first; Who are you?",
    relative_rect=pygame.Rect(50, 500, 800, 150),
    manager=manager
)
text_box.hide()

#CHARACTER SELECTION
name_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect = pygame.Rect(650,420,200,50),
    manager=manager
)
name_entry.hide()

fighter_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(150, 300, 100, 50),
    text="Fighter",
    manager=manager
)
fighter_button.hide()

mage_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 300, 100, 50),
    text="Mage",
    manager=manager
)
mage_button.hide()

ranger_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(650, 300, 100, 50),
    text="Ranger",
    manager=manager
)
ranger_button.hide()

#BATTLE GUI
attack_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(250, 440, 100, 50),
    text="Attack",
    manager=manager
)
attack_button.hide()

special_attack_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 440, 100, 50),
    text="Special",
    manager=manager
)
special_attack_button.hide()

inventory_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(550, 440, 100, 50),
    text="Inventory",
    manager=manager
)
inventory_button.hide()

#SPECIAL ATTACKS
back = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(700, 440, 100, 50),
    text="BACK",
    manager=manager
)
back.hide()

#fighter
reckless_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(250, 440, 100, 50),
    text="Reckless Strike",
    manager=manager
)
reckless_b.hide()

anticipation_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 440, 100, 50),
    text="Anticipation",
    manager=manager
)
anticipation_b.hide()

retribution_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(550, 440, 100, 50),
    text="Retribution",
    manager=manager
)
retribution_b.hide()

#mage
blinding_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(250, 440, 100, 50),
    text="Blinding Light",
    manager=manager
)
blinding_b.hide()

mana_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 440, 100, 50),
    text="Mana Burst",
    manager=manager
)
mana_b.hide()

fireball_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(550, 440, 100, 50),
    text="Fireball",
    manager=manager
)
fireball_b.hide()

iceshard_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(250, 370, 100, 50),
    text="Iceshard",
    manager=manager
)
iceshard_b.hide()

electric_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 370, 100, 50),
    text="Electric Shots",
    manager=manager
)
electric_b.hide()

#ranger
final_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(250, 440, 100, 50),
    text="Final Blow Strike",
    manager=manager
)
final_b.hide()

triple_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 440, 100, 50),
    text="Triple Arrow",
    manager=manager
)
triple_b.hide()

toxic_b = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(550, 440, 100, 50),
    text="Toxic Shot",
    manager=manager
)
toxic_b.hide()


#LEVEL UP
up_health = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(250, 440, 100, 50),
    text="Health",
    manager=manager
)
up_health.hide()

up_attack = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 440, 100, 50),
    text="Attack",
    manager=manager
)
up_attack.hide()

up_mana = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(550, 440, 100, 50),
    text="Mana",
    manager=manager
)
up_mana.hide()

#LINOS SHOP
shop_window = pygame_gui.elements.UIWindow(
    rect=pygame.Rect((200, 100), (400, 300)),
    manager=manager,
    window_display_title='Lino\'s Shop',
    object_id='#shop_window'
)
shop_window.hide()

item1_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((280, 5), (80, 20)),
    text="BUY",
    manager=manager,
    container=shop_window
)
item1_button.hide()

item2_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((280, 50), (80, 20)),
    text="BUY",
    manager=manager,
    container=shop_window
)
item2_button.hide()

item3_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((280, 95), (80, 20)),
    text="BUY",
    manager=manager,
    container=shop_window
)
item3_button.hide()

close_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((140, 200), (80, 30)),
    text="Close",
    manager=manager,
    container=shop_window
)
close_button.hide()

healthpot_label = UILabel(
    relative_rect=pygame.Rect((2, 5), (200, 30)),  #
    text="Health Potion________10G",
    manager=manager,
    container=shop_window  
)
healthpot_label.hide()

manapot_label = UILabel(
    relative_rect=pygame.Rect((2, 50), (200, 30)),  #
    text="Mana Potion________10G",
    manager=manager,
    container=shop_window  
)
manapot_label.hide()

ticket_label = UILabel(
    relative_rect=pygame.Rect((2, 95), (200, 30)),  #
    text="Ticket________80G",
    manager=manager,
    container=shop_window  
)
ticket_label.hide()

#startscreen
newgame = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(400, 440, 100, 50),
    text="Start Again",
    manager=manager
)
newgame.hide()
