import pygame
import random
import pygame_gui
from sys import exit
from player import *
from enemies import *
pygame.init()
pygame.freetype.init()
manager = pygame_gui.UIManager((900,700))
from GUI import *
from functions import *

screen = pygame.display.set_mode((900,700))
pygame.display.set_caption("RUNEWOOD")
clock = pygame.time.Clock()

name_set = 0
battle = None
enemy = None
runewood = None
battle_counter = 0
linos_shop = None
nyx_counter = None
player= None
startscreen = False
name_entry_done = False
day = 1
tavern = None
chosen_class = None
ritual = None
used_item = None

#ENEMY SPRITES
goblin_port = pygame.image.load("portraits/Goblin.png").convert_alpha() #200x200
goblin_rect = goblin_port.get_rect(topleft = (50,50))

rat_sprite = pygame.image.load("sprite/rat_sprite.gif").convert_alpha()
rat_sp_rect = rat_sprite.get_rect(topleft = (570, 120))

orc_sprite = pygame.image.load("sprite/orc_sprite.png").convert_alpha()
orc_sp_rect = orc_sprite.get_rect(topleft = (570, 120))

goblin_sprite = pygame.image.load("sprite/goblin_sprite.png").convert_alpha()
goblin_sp_rect = goblin_sprite.get_rect(topleft = (570, 120))

salamander_sprite = pygame.image.load("sprite/salamander_sprite.png").convert_alpha()
salamander_sp_rect = salamander_sprite.get_rect(topleft = (570, 120))

shaman_sprite = pygame.image.load("sprite/shaman.png").convert_alpha()
shaman_sp_rect = shaman_sprite.get_rect(topleft = (570, 120))

young_dragon_sprite = pygame.image.load("sprite/young dragon.png").convert_alpha()
young_dragon_rect = young_dragon_sprite.get_rect(topleft = (570, 120))

black_wyvern_sprite = pygame.image.load("sprite/wyvern.png").convert_alpha()
black_wyvern_sprite_rect = black_wyvern_sprite.get_rect(topleft = (570, 120))

ritual_light = pygame.image.load("sprite/ritual_light.png").convert_alpha()
ritual_light_rect = ritual_light.get_rect(topleft = (570, 120))

#PLAYER SPRITES
fighter_portrait = pygame.image.load("portraits/portrait_fighter.png").convert_alpha()
fighter_rect = fighter_portrait.get_rect(topleft = (50, 150))

mage_portrait = pygame.image.load("portraits/player_mage.png").convert_alpha()
mage_rect = mage_portrait.get_rect(topleft = (50, 150))

ranger_portrait = pygame.image.load("portraits/portrait_ranger.png").convert_alpha()
ranger_rect = ranger_portrait.get_rect(topleft = (50, 150))

fighter_sprite = pygame.image.load("sprite/fighter sprite.png").convert_alpha()
fighter_sprite_rect = fighter_sprite.get_rect(topleft = (450, 350))

mage_sprite = pygame.image.load("sprite/mage sprite.png").convert_alpha()
mage_sprite_rect = mage_sprite.get_rect(topleft = (450, 350))

ranger_sprite = pygame.image.load("sprite/sprite ranger.png").convert_alpha()
ranger_sprite_rect = ranger_sprite.get_rect(topleft = (450, 350))

class_sprite_rects = {
    "fighter": (fighter_sprite,fighter_sprite_rect),
    "mage": (mage_sprite,mage_sprite_rect),
    "ranger": (ranger_sprite,ranger_sprite_rect)
}

#NPC SPRITES
lino_portrait = pygame.image.load("portraits/Lino.png").convert_alpha()
lino_rect = lino_portrait.get_rect(bottomleft = ((50,503)))
nyx_portrait = pygame.image.load("portraits/nyx.png").convert_alpha()
nyx_rect = nyx_portrait.get_rect(bottomleft = ((50,503)))


#BACKGROUND
bg = pygame.image.load("background/backg2.png").convert()
bg_runewood = pygame.image.load("background/back_runewood.png").convert()
recharge = pygame.image.load("background/recharge.png").convert_alpha()
recharge_rect = recharge.get_rect(topleft = (50,20))
linos = pygame.image.load("background/shop.png").convert_alpha()
linos_rect = linos.get_rect(topleft = (360,30))
drunken_d = pygame.image.load("background/tavern.png").convert_alpha()
drunken_d_rect = drunken_d.get_rect(topleft = (500,140))
nyx_shop = pygame.image.load("background/nyx.png").convert_alpha()
nyx_shop_rect = nyx_shop.get_rect(topleft = (200,535))
welcome = pygame.image.load("background/welcome.png").convert_alpha()
welcome_rect = welcome.get_rect(midbottom = (450,685))

#TEXT
font1 = pygame.font.Font("font/pxint.ttf", 20)
#runewood_day = font1.render(f"RUNEWOOD - day {day}", True, ("White"))

        
while True:
    time_delta = clock.tick(60) / 1000.0
    screen.blit(bg,(0,0))
    mouse_pos = pygame.mouse.get_pos()
    runewood_day = font1.render(f"RUNEWOOD - day {day}", True, ("White"))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if startscreen == True:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == newgame:
                    newgame.hide()
                    name_entry_done = False
                    startscreen = False
                    text_box.set_text("You almost made it through to your home village which has been troubled by monster attacks. But first; Who are you?")
                    
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN and startscreen == False:
            text_box.show()
            if name_entry_done == False:
                name_entry.show()
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            player_name = event.text
            name_entry.hide()
            name_entry_done = True
            text_box.set_text(f"Welcome {player_name}!")
            name_set += 1
        if event.type == pygame.KEYDOWN and name_set == 1 or event.type == pygame.MOUSEBUTTONDOWN and name_set == 1:
            text_box.set_text(f"What class are you?")
            fighter_button.show()
            mage_button.show()
            ranger_button.show()
            name_set += 1 #name_set = 2
        if event.type == pygame_gui.UI_BUTTON_PRESSED and name_set == 2:
            if event.ui_element == fighter_button:
                player_class = Fighter()
                chosen_class = "fighter"
            if event.ui_element == mage_button:
                player_class = Mage()
                chosen_class = "mage"
            if event.ui_element == ranger_button:
                player_class = Ranger()
                chosen_class = "ranger"
            fighter_button.hide()
            mage_button.hide()
            ranger_button.hide()
            active_sprite, active_sprite_rect = class_sprite_rects[chosen_class]
            player = Player(player_name, player_class)
            text_box.set_text(f"Your name: {player.name}\nYour class: {player.character_class.name}")
            name_set += 1 #name_set = 3
        if event.type == pygame.KEYDOWN and name_set == 3 or event.type == pygame.MOUSEBUTTONDOWN and name_set == 3:
            enemy = get_random_enemy(player, ritual)
            name_set += 1 #NAME_SET IS 4
            battle = "intro"
        if battle == "intro":
            if enemy.name == "Black Wyvern":
                ritual = None
                text_box.set_text(f"The gound shakes and a special enemy comes out of a bright \nA wild {enemy.name} has appeared!")
            else:
                text_box.set_text(f"A wild {enemy.name} has appeared!")
            battle= "choice"
            
        if battle == "choice":
            if enemy.health <= 0 or player.health <= 0: 
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    battle = "end"
            else:
                if attack_button.relative_rect.collidepoint(mouse_pos):
                    text_box.set_text("You do a normal attack, based on you Attack Stat.")
                elif special_attack_button.relative_rect.collidepoint(mouse_pos):
                    text_box.set_text("You get to choose a special attack.")
                elif inventory_button.relative_rect.collidepoint(mouse_pos):
                        text_box.set_text("You open your Inventory.")
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == attack_button:                           #N-ATTACK
                        #battle = "n_attack"
                        chancecrit=random.randint(1,100)
                    
                        if chancecrit > player.crit_chance:
                            pdmg= player.attack * (1 - enemy.defense * 1e-2)
                            enemy.health -= pdmg
                            text_box.set_text(f"{player.name} dealt {pdmg} damage to {enemy.name}!")
                        else:
                            pdmg= (player.attack * (1 - enemy.defense * 1e-2))*1.5  # CRIT HIT
                            enemy.health -= pdmg
                            text_box.set_text(f"{player.name} did a critical hit! You dealt {pdmg} damage to {enemy.name}!")
                        if enemy.health <= 0 or player.health <= 0:
                            battle = "end"
                        else:
                            battle= "enemy_attack"
                    if event.ui_element == special_attack_button:   #S-ATTACK BUTTON
                        battle = "s_attack"
                    if event.ui_element == inventory_button:        #INVENTORY BUTTON
                        used_item = None
                        battle = "inventory"

        if event.type == pygame.KEYDOWN and battle == "inventory":
            if pygame.K_1 <= event.key <= pygame.K_9:
                index = event.key - pygame.K_1
                if index < len(player.inventory):
                    item = player.inventory[index]
                    if item[0] == "Ticket":
                        item[1](player, ritual)
                        ritual = True
                        print("function of ticket is called")
                    else:
                        item[1](player) #calls function
                    used_item = True
                    player.inventory.pop(index) #removes item from inventory
        if event.type == pygame_gui.UI_BUTTON_PRESSED and battle == "inventory":
            if event.ui_element == back:
                back.hide()
                battle="choice"
             
        if event.type == pygame_gui.UI_BUTTON_PRESSED and battle == "s_attack": #S ATTACK
            if event.ui_element == back:
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
                battle = "choice" 
            if event.ui_element == reckless_b:
                player.character_class.Reckless_Strike(player, enemy, text_box)
                if player.health <= 0:
                    battle = "end"
                else:
                    battle="enemy_attack"
            if event.ui_element == anticipation_b:
                battle = player.character_class.Anticipation(player, enemy, text_box)
            if event.ui_element == retribution_b:
                battle = player.character_class.Retribution(player, enemy, text_box)
            if event.ui_element == blinding_b:
                battle = player.character_class.Blinding_Light(player, enemy, text_box)
            if event.ui_element == mana_b:
                battle = player.character_class.Mana_Burst(player, enemy, text_box)
            if event.ui_element == fireball_b:
                battle = player.character_class.Fireball(player, enemy, text_box)
            if event.ui_element == iceshard_b:
                battle = player.character_class.Iceshard(player, enemy, text_box)
            if event.ui_element == electric_b:
                battle = player.character_class.Electric_Shots(player, enemy, text_box)
            if event.ui_element == final_b:
                battle = player.character_class.Final_Blow(player, enemy, text_box)
            if event.ui_element == triple_b:
                battle = player.character_class.Triple_Arrow(player, enemy, text_box)
            if event.ui_element == toxic_b:
                battle = player.character_class.Toxic_Shot(player, enemy, text_box)
                
        if event.type == pygame.KEYDOWN and battle == "mana_missing" or event.type == pygame.MOUSEBUTTONDOWN and battle == "mana_missing":
            text_box.set_text("Not enough mana.")
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                battle = "s_attack"
            
        if battle =="enemy_attack":
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if player.health <= 0 or enemy.health <= 0: 
                    battle = "end"
                else:
                    evasionch = random.randint(1, 100)  #evasion
                    if evasionch <= player.evasion:
                        text_box.set_text("You evaded the incoming attack!")
                    elif enemy.blind_counter>0:
                        text_box.set_text(f"{enemy.name} is blinded and missed!")
                        enemy.blind_counter -= 1
                    else:
                        if hasattr(enemy, "special_attacks") and enemy.special_attacks:
                            enemy_attack = random.randint(-1, len(enemy.special_attacks))
                        else:
                            enemy_attack = -1
                        
                        if enemy_attack > 0:
                            name, num, func = enemy.special_attacks[enemy_attack -1]
                            func(player, text_box)

                        elif enemy_attack <= 0:
                            edmg= enemy.attack * (1 - player.defense * 1e-2) 
                            player.health -= edmg
                            text_box.set_text(f"{enemy.name} dealt {edmg} damage to {player.name}!\nYou have {player.health} health left!")
                        #if enemy kills itself with special, it doesnt show text of attack
                        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                            battle = "choice"
        if event.type == pygame.KEYDOWN and name_set == 5 or event.type == pygame.MOUSEBUTTONDOWN and name_set == 5:
            experience(player, previous_enemy, text_box)
            battle_counter += 1
            #LVL UPS HERE
            name_set = levelup(player, battle_counter, exp_needed)
            if name_set == 0:
                runewood = True
                
        if name_set == 6 and event.type == pygame.KEYDOWN or name_set == 6 and event.type == pygame.MOUSEBUTTONDOWN:
            text_box.set_text(f"{player.name} reached level {level}!\nChoose which attribute to increase.")
            up_health.show()
            up_attack.show()
            up_mana.show()
        if event.type == pygame_gui.UI_BUTTON_PRESSED and name_set == 6:
            player.level += 1
            if event.ui_element == up_health:
                player.max_health += h_lvlup
                player.health = player.max_health
                text_box.set_text(f"Your Health increased by 20 and you got healed. Health: {player.health}")
            if event.ui_element == up_attack:
                player.attack += a_lvlup
                text_box.set_text(f"Your attack increased by 5. Attack: {player.attack}")
            if event.ui_element == up_mana:
                player.max_mana += m_lvlup
                player.mana = player.max_mana
                text_box.set_text(f"Your Mana increased by 15 and filled up. Mana: {player.mana}")
            up_health.hide()
            up_attack.hide()
            up_mana.hide()
            name_set = 7
        if name_set == 7 and event.type == pygame.KEYDOWN or name_set == 7 and event.type == pygame.MOUSEBUTTONDOWN: 
            if battle_counter == 3:
                active_sprite_rect.x = 450 ###
                active_sprite_rect.y = 350 ###
                runewood = True
                name_set = 0
            else:
                name_set = 3
                    
        if battle =="lost" and event.type == pygame.KEYDOWN or battle =="lost" and event.type == pygame.MOUSEBUTTONDOWN:
            startscreen = True
            
        if runewood == True:
            if recharge_rect.colliderect(active_sprite_rect):
                print("coll with recharge")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        print("recharge happens")
                        day += 1
                        player.health = player.max_health
                        player.mana = player.max_mana
                        battle_counter = 0
                        name_set = 3
                        text_box.show()
                        text_box.set_text("You rested and filled your health and mana. Monsters attack.")
                        runewood = False
                        #active_sprite_rect.x = 450
                        #active_sprite_rect.y = 350
                        
            if linos_rect.colliderect(active_sprite_rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and linos_shop == None:
                        text_box.set_text("-You are at Lino's Shop-\nOh, hey there! Nice to welcome a customer.")
                        linos_shop = 1

                elif linos_shop == 1:
                    #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                    linos_shop =2
                        
                elif linos_shop == 2:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                        text_box.set_text("Interested in any of my wares?")
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == item1_button:
                            if player.gold >= 10:
                                player.gold -= 10
                                text_box.set_text("The health potion has been added to your inventory.")
                                player.inventory.append(("Health Potion", health_potion))         
                            else:
                                text_box.set_text("Not enough gold.")
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == item2_button:
                            if player.gold >= 10:
                                player.gold -= 10
                                text_box.set_text("The mana potion has been added to your inventory.")      
                                player.inventory.append(("Mana Potion", mana_potion))             
                            else:
                                text_box.set_text("Not enough gold.")

                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == item3_button:
                            if player.gold >= 5: #80
                                player.gold -= 5 #80
                                text_box.set_text("The ticket has been added to your inventory.")      
                                player.inventory.append(("Ticket", ticket))
                                ticket_label.kill()
                                item3_button.kill()
                            else:
                                text_box.set_text("Not enough gold.")  
                    
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == close_button:
                            shop_window.hide()
                            linos_shop = None

                    if event.type == pygame_gui.UI_WINDOW_CLOSE:
                        if event.ui_element == shop_window:
                            shop_window.hide()
                            linos_shop = None

            if nyx_shop_rect.colliderect(active_sprite_rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and nyx_counter == None:
                        text_box.set_text("-You are at Nyx's Shop-\nHi.")
                        nyx_counter = 1

                elif nyx_counter == 1:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                        if player.level < 3:
                            text_box.set_text("Come back when you've grown.")
                            nyx_counter = 2
                        else:
                            pass
                        
                elif nyx_counter == 2:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                        nyx_counter = None
                        text_box.hide()

            if drunken_d_rect.colliderect(active_sprite_rect):
                print("colliding")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        tavern = "open"
                        runewood = None

        if tavern == "open":
            if welcome_rect.colliderect(active_sprite_rect):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        tavern = None
                        runewood = True
                        
     
        manager.process_events(event)
                    
    #CLASS DESCRIPTION
    if fighter_button.relative_rect.collidepoint(mouse_pos)and name_set == 2:
        text_box.set_text(f"FIGHTER\nHealth: {Fighter1.health}\nMana: {Fighter1.mana}\nAttack: {Fighter1.attack}\nDefense: {Fighter1.defense}")
    elif mage_button.relative_rect.collidepoint(mouse_pos)and name_set == 2:
        text_box.set_text(f"MAGE\nHealth: {Mage1.health}\nMana: {Mage1.mana}\nAttack: {Mage1.attack}\nDefense: {Mage1.defense}")
    elif ranger_button.relative_rect.collidepoint(mouse_pos)and name_set == 2:
        text_box.set_text(f"RANGER\nHealth: {Ranger1.health}\nMana: {Ranger1.mana}\nAttack: {Ranger1.attack}\nDefense: {Ranger1.defense}")
            
    # PORTRAITS/SPRITES
    if battle is not None and enemy is not None:
        if enemy.name == "Goblin":
            screen.blit(goblin_sprite, goblin_sp_rect)
        elif enemy.name == "Rat":
            screen.blit(rat_sprite, rat_sp_rect)
        elif enemy.name == "Orc":
            screen.blit(orc_sprite, orc_sp_rect)
        elif enemy.name == "Salamander":
            screen.blit(salamander_sprite, salamander_sp_rect)
        elif enemy.name == "Goblin Shaman":
            screen.blit(shaman_sprite, shaman_sp_rect)
        elif enemy.name == "Young Dragon":
            screen.blit(young_dragon_sprite, young_dragon_rect)
        elif enemy.name == "Black Wyvern":
            screen.blit(black_wyvern_sprite, black_wyvern_sprite_rect)

        if ritual == True:
            screen.blit(ritual_light, ritual_light_rect)

        if player.character_class.name == "Fighter":
            screen.blit(fighter_portrait, fighter_rect)
        elif player.character_class.name == "Mage":
            screen.blit(mage_portrait, mage_rect)
        elif player.character_class.name == "Ranger":
            screen.blit(ranger_portrait, ranger_rect)
        #class select
    if name_set== 2:
        screen.blit(fighter_portrait, (100,100))
        screen.blit(mage_portrait, (350,100))
        screen.blit(ranger_portrait, (600,100))

    #MANA/HEALTH BARS/GOLD/EXP
    if battle is not None and enemy is not None:        
        #enemy
        current_bar_width = int((enemy.health / enemy.max_health) * 200)
        if current_bar_width < 0:
            current_bar_width = 0
        #player
        current_bar_width_player = int((player.health / player.max_health) * 200)
        if current_bar_width_player < 0:
            current_bar_width_player = 0
        #mana
        current_mana_bar_width = int((player.mana / player.max_mana) * 200)
        if current_mana_bar_width < 0:
            current_mana_bar_width = 0
            
        #enemy
        pygame.draw.rect(screen, "Black", pygame.Rect(650, 30, 210, 30))
        pygame.draw.rect(screen, "Grey55", pygame.Rect(655, 35, 200, 20))
        pygame.draw.rect(screen, "firebrick2", pygame.Rect(655, 35, current_bar_width, 20))
        #player
        pygame.draw.rect(screen, "Black", pygame.Rect(50, 350, 210, 30))
        pygame.draw.rect(screen, "Grey55", pygame.Rect(55, 355, 200, 20))
        pygame.draw.rect(screen, "Forestgreen", pygame.Rect(55, 355, current_bar_width_player, 20))

        health_num = font1.render(f"{round(player.health)} / {player.max_health}", False, "White")
        health_num_rect = health_num.get_rect(topleft = (93,352))
        screen.blit(health_num, health_num_rect)

        #mana
        pygame.draw.rect(screen, "Black", pygame.Rect(50, 380, 210, 30))
        pygame.draw.rect(screen, "Grey55", pygame.Rect(55, 385, 200, 20))
        pygame.draw.rect(screen, "royalblue3", pygame.Rect(55, 385, current_mana_bar_width, 20))

        mana_num = font1.render(f"{round(player.mana)} / {player.max_mana}", False, "White")
        mana_num_rect = health_num.get_rect(topleft = (93,382))
        screen.blit(mana_num, mana_num_rect)

        #gold + exp
        gold_ = font1.render(f"{player.gold} Gold                       {player.exp} Experience", False, "White")
        gold_rect = gold_.get_rect(topleft = (70,660))
        screen.blit(gold_, gold_rect)

    if battle == "choice":
            attack_button.show()
            special_attack_button.show()
            inventory_button.show()

    if battle =="enemy_attack":
            attack_button.hide()
            special_attack_button.hide()
            inventory_button.hide()

    if battle == "end":
        if enemy.health <= 0:
            attack_button.hide()
            special_attack_button.hide()
            inventory_button.hide()
            text_box.set_text(f"You defeated the {enemy.name}!")
            name_set = 5
            player.defense = player.max_defense
            previous_enemy = enemy
            enemy = None
            battle= None
        elif player.health <= 0:
            text_box.set_text(f"You lost.")
            battle="lost"

    if battle == "inventory":
        if used_item == None:
            if len(player.inventory) < 1:
                text_box.set_text("Your inventory is empty")
            else:
                text_box.set_text("Press a number to use the corresponding item.")
        back.show()
        attack_button.hide()
        inventory_button.hide()
        special_attack_button.hide()
        for idx, item in enumerate(player.inventory):
            text_surface = font1.render(f"{idx+1}. {item[0]}", True, ("White"))
            pygame.draw.rect(screen, "Black", (540, 195 + idx*30, 250, 40))
            screen.blit(text_surface,(550, 200 + idx*30))

    #S ATTACK GUI
    if battle == "s_attack": 
        attack_button.hide()
        special_attack_button.hide()
        inventory_button.hide()
        back.show()
        if player.character_class.name == "Fighter":
            reckless_b.show()
            anticipation_b.show()
            if player.level > 4:
                retribution_b.show()
            if reckless_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You deal a lot of damage, but hurt yourself in the process. Small chance to miss.")
            if anticipation_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You steel yourself for the rest of the fight. Defense goes up.")
            if retribution_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You do a powerful attack based on your defense. High chance to stun target for one round.")
        elif player.character_class.name == "Mage":
            blinding_b.show()
            mana_b.show()
            fireball_b.show()
            iceshard_b.show()
            if player.level > 4:
                electric_b.show()
            if blinding_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You blind the enemy for 3 turns.")
            if mana_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You use half of your current mana to deal a lot of damage based on the amount of mana used.")
            if fireball_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You deal a great amount of damage.")
            if iceshard_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You deal a medium amount of damage.")
            if electric_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You shoot 1-3 electric shots that each deal a randomized amount of damage.")
        elif player.character_class.name == "Ranger":
            final_b.show()
            triple_b.show()
            if player.level > 4:
                toxic_b.show()
            if final_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You deal a great amount of damage if the enemy is below 50% health. Otherwise it's little damage.")
            if triple_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You shoot 3 arrows and deal a lot of damage. Small chance to miss, but still deal little damage.")
            if toxic_b.relative_rect.collidepoint(mouse_pos):
                text_box.set_text("You deal medium damage but poison the enemy for 3 rounds.")

    #LVL UP
    if up_health.relative_rect.collidepoint(mouse_pos)and name_set == 6:
        text_box.set_text(f"Your health increases by {h_lvlup}. You will also be healed.")
    elif up_attack.relative_rect.collidepoint(mouse_pos)and name_set == 6:
        text_box.set_text(f"Your attack increases by {a_lvlup}.")
    elif up_mana.relative_rect.collidepoint(mouse_pos)and name_set == 6:
        text_box.set_text(f"Your mana increases by {m_lvlup}. Your mana will also be filled up.")
    
    if name_set > 2 or 0:
        if player.level == 1:
            h_lvlup = 20
            a_lvlup = 5
            m_lvlup = 15
            level = 2
            exp_needed = 120
        if player.level == 2:
            h_lvlup = 30
            a_lvlup = 8
            m_lvlup = 20
            level = 3
            exp_needed = 270
        if player.level == 3:
            h_lvlup = 40
            a_lvlup = 10
            m_lvlup = 25
            level = 4
            exp_needed = 600
        if player.level > 3:
            exp_needed = 100000000

    #RUNEWOOD
    if runewood == True:
        screen.blit(bg_runewood,(0,0))
        screen.blit(runewood_day,(5,5))
        text_box.hide()
        screen.blit(recharge, recharge_rect)
        screen.blit(linos, linos_rect)
        screen.blit(drunken_d,drunken_d_rect)
        screen.blit(nyx_shop, nyx_shop_rect)
        screen.blit(active_sprite, active_sprite_rect)
        
        if recharge_rect.colliderect(active_sprite_rect):
            interact_e(font1, screen)
        if linos_rect.colliderect(active_sprite_rect) and linos_shop is None:
            interact_e(font1, screen)
        if nyx_shop_rect.colliderect(active_sprite_rect) and nyx_counter is None:
            interact_e(font1, screen)
        if drunken_d_rect.colliderect(active_sprite_rect):
            interact_e(font1, screen)

        if (linos_shop and nyx_counter) is None:
            keys = pygame.key.get_pressed() #outside eventloop to limit clunkyness
            if keys[pygame.K_d]:
                active_sprite_rect.x += 5
            if keys[pygame.K_a]:
                active_sprite_rect.x -= 5
            if keys[pygame.K_w]:
                active_sprite_rect.y -= 5
            if keys[pygame.K_s]:
                active_sprite_rect.y += 5

        if active_sprite_rect.left <= 0: active_sprite_rect.left = 0
        if active_sprite_rect.right >= 900: active_sprite_rect.right = 900
        if active_sprite_rect.top <= 0: active_sprite_rect.top = 0
        if active_sprite_rect.bottom >= 700: active_sprite_rect.bottom = 700

        if linos_shop is not None:
            text_box.show()
            screen.blit(lino_portrait, lino_rect)
            if linos_shop == 2:
                wallet = font1.render(f"Gold: {player.gold}", False, "Black")
                wallet_rect = gold_.get_rect(topleft = (70,660))
                pygame.draw.rect(screen, "White", wallet_rect)
                screen.blit(wallet, wallet_rect)
                shop_window.show()
                item1_button.show()
                item2_button.show()
                item3_button.show()
                close_button.show()
                healthpot_label.show()
                manapot_label.show()
                ticket_label.show()
        if item1_button.relative_rect.collidepoint(mouse_pos): #these arent shown??
            text_box.set_text("Health +40. Usable in battle.")
        if item2_button.relative_rect.collidepoint(mouse_pos):
            text_box.set_text("Mana + 30. Usable in battle.")

        if nyx_counter is not None:
            text_box.show()
            screen.blit(nyx_portrait, nyx_rect)

    if tavern == "open":
        text_box.hide()
        screen.fill("Black")
        screen.blit(welcome, welcome_rect)
        screen.blit(active_sprite, active_sprite_rect)

        if welcome_rect.colliderect(active_sprite_rect):
            interact_e(font1, screen)

        #MOVEMENT
        keys = pygame.key.get_pressed() #outside eventloop to limit clunkyness
        if keys[pygame.K_d]:
            active_sprite_rect.x += 5
        if keys[pygame.K_a]:
            active_sprite_rect.x -= 5
        if keys[pygame.K_w]:
            active_sprite_rect.y -= 5
        if keys[pygame.K_s]:
            active_sprite_rect.y += 5

        if active_sprite_rect.left <= 0: active_sprite_rect.left = 0
        if active_sprite_rect.right >= 900: active_sprite_rect.right = 900
        if active_sprite_rect.top <= 0: active_sprite_rect.top = 0
        if active_sprite_rect.bottom >= 700: active_sprite_rect.bottom = 700
        

    if startscreen == True:
        text_box.hide()
        attack_button.hide()
        special_attack_button.hide()
        inventory_button.hide()
        battle = None
        enemy = None
        runewood = None
        battle_counter = 0
        linos_shop = None
        player= None
        name_set = 0
        newgame.show()
        
    manager.update(time_delta)
    
    manager.draw_ui(screen)
    pygame.display.update()

