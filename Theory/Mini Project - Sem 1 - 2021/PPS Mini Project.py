import time
import sys
import random

def Invalid_Syntax(user_input):
    if user_input == 'A' or user_input == 'B' or user_input == 'C':
        return 1
    else:
        return 0

class Character:
    character_gender = ""
    character_name = ""
    character_health = 100
    character_weapon = "Sword"
    character_intelligence = 50
    character_power = 50
    character_charisma = 50
    character_coins = 0
    def print_stats(self):
        print("Name:",self.character_name)
        print("Gender:",self.character_gender)
        print("Health:",self.character_health)
        print("Intelligence:",self.character_intelligence)
        print("Power:",self.character_power)
        print("Charisma:",self.character_charisma)
        print("Coins:",self.character_coins)
        print()

obj_character = Character()

class Weapon:
    weapon_damage = 0
    weapon_special_ability = ""

class Choose_Character:
    n=0
    while True:
        if n < 3:
            gender = input("Please choose what gender is your character:\nMale\nFemale\nOthers\n")
            gender = gender.title()
            gender_list = ['Male', 'Female', 'Others']
            if gender not in gender_list:
                n+=1
                continue
            else:
                obj_character.character_gender = gender
                break
        else:
            sys.exit("Repeated Invalid Output")
            
    name = input("Please enter a name for your character\n")
    obj_character.character_name = name.title()
    print()

class Chapter_Cave:
    def scene_1(self):
        print("So, what will you do? (Please select the letters)")
        print("A. Explore the cave")
        print("B. Run straight into the cave")
        print("C. Call out for people")
        choice_1 = input().upper()
        while Invalid_Syntax(choice_1) == 0:
            print("Please choose the correct option.")
            choice_1 = input().upper()
            Invalid_Syntax(choice_1)
        return choice_1
        
    def scene_2_a(self):
        print()
        print("You start looking around the cave. The damp air, the feeling of uncertainity, the cold touch of the walls, all caution you.", end="")
        print(' "Maybe I should come here with some help?" Is what you think to yourself, when suddenly, your instinct warns you.')
        print("You hear soft footsteps, approaching towards you, not too quickly, but with quite a steady pace.")
        print("What do you do?")
        print("A. Freeze in place")
        print("B. Look in the direction of the footsteps")
        print("C. Close your eyes and sprint down the cave")
        choice_4_a_a = input().upper()
        while Invalid_Syntax(choice_4_a_a) == 0:
            print("Please choose the correct option.")
            choice_4_a_a = input().upper()
            Invalid_Syntax(choice_4_a_a)
        return choice_4_a_a
    def scene_2_b(self):
        print("As you sprint down the darkness of the cave, grinning, you hear a voice.",end="")
        print(' Help!', end = "")
        print(" What will you do?")
        print("A. Ignore the voice and go ahead.")
        print("B. Go to where the voice is coming from.")
        choice_4_a_b = input().upper()
        while Invalid_Syntax(choice_4_a_b) == 0:
            print("Please choose the correct option.")
            choice_4_a_b = input().upper()
            Invalid_Syntax(choice_4_a_b)
        return choice_4_a_b
    def scene_2_c(self):
        print("You use all the strength your lungs can conjure to shout asking for anyone's presence")
        print("Your voice echoes, but you get no reply, instead", end = "")
        print(" you hear soft footsteps, approaching towards you, not too quickly, but with quite a steady pace.")
        print("As you turn your head to look in the direction of the footsteps, you see an old woman. She is sitting with her eyes closed", end ="")
        print(" seeming to be in deep meditation.")
        print(" She suddenly opens her eyes and stares into your's, as if piercing your soul itself.", end="")
        print(''' You try to appreciate her beauty, but your heart feels cold.\n"Do not make the same mistake I made. You will only end up as a dead man, stalking the night aimlessly."''', end="")
        print(" Turn back! Run! *Screams gibberish*")
        print("A. Try to fight the woman")
        print("B. Sprint down the cave")
        choice_4_a_c = input().upper()
        while Invalid_Syntax(choice_4_a_c) == 0:
            print("Please choose the correct option.")
            choice_4_a_c = input().upper()
            Invalid_Syntax(choice_4_a_c)
        return choice_4_a_c
    def scene_2_conclude_a(self):
        print("As you freeze up, you feel a peculiar coldness on your neck. ", end="")
        print("Upon touching your neck, you feel a familiar human touch.", end = "")
        print("As you turn your head, you see an apparition. It's face looks like that of a handsome man,", end ="")
        print(" however, it is weirdly disturbing. The loss of a hand makes it no more appealing.", end = "")
        print(" It's eye, rolling aimlessly in it's socket, suddenly turns and stares into your's, as if piercing your soul itself.", end="")
        print(''' As you smell it's horrid breath, you hear, "Do not make the same mistake I made. You will only end up as a dead man, stalking the night aimlessly."''', end="")
        print(" Turn back! Run! *Screams gibberish*")
        print()
        print("A. Try to fight the apparition")
        print("B. Sprint down the cave")
        choice_4_a_conclude_a = input().upper()
        while Invalid_Syntax(choice_4_a_conclude_a) == 0:
            print("Please choose the correct option.")
            choice_4_a_conclude_a = input().upper()
            Invalid_Syntax(choice_4_a_conclude_a)
        return choice_4_a_conclude_a
    def scene_2_conclude_b(self):
        print("As you turn your head, you see an apparition. It's face looks like that of a handsome man,", end ="")
        print(" however, it is weirdly disturbing. The loss of a hand makes it no more appealing.", end = "")
        print(" It's eye, rolling aimlessly in it's socket, suddenly turns and stares into your's, as if piercing your soul itself.", end="")
        print(''' As you smell it's horrid breath, you hear, "Do not make the same mistake I made. You will only end up as a dead man, stalking the night aimlessly."''', end="")
        print(" Turn back! Run! *Screams gibberish*")
        print()
        print("A. Try to fight the apparition")
        print("B. Sprint down the cave")
        choice_4_a_conclude_b = input().upper()
        while Invalid_Syntax(choice_4_a_conclude_b) == 0:
            print("Please choose the correct option.")
            choice_4_a_conclude_b = input().upper()
            Invalid_Syntax(choice_4_a_conclude_b)
        return choice_4_a_conclude_b
    
    def scene_2_5_a(self):
        print("You ignore the voice and run ahead. You see the cave exit in the distance.",end="")
        print("As you are about to rejoice your fiding of the exit, you come across a big boulder.",end="")
        print("It takes you weeks to move the boulder, but you finally do it. Your power has increased due to this.")
        obj_character.character_power += 20
    def scene_2_5_b(self):
        print("You run towards the voice that is calling out for help.",end="")
        print(f"You see a man who is badly wounded. You run towards him. Since your intelligence is {obj_character.character_intelligence}",end="")
        print(" You are able to perform basic aid to help him.")
        print("The both of you have a talk, and he let's you know how to get out of the cave from a shortcut.",end="")
        print("As you turn away for a second to look for the shortcut, the man disappears. You walk out of the cave. Your charisma has increased")
        obj_character.character_charisma += 20

obj_cavechp = Chapter_Cave()


class Story:
    print("Around 250 A.D, the world had fallen into utter chaos. Today's historians would come to call this era as the dark ages. An era, which had lost it's light.", end = " ")
    print(f"Around this time, in a small town called Alryne, a child was born, who was named, {obj_character.character_name}")
    print()
    print(f"Born into poverty, the young one did not have too many options. Their father was a stubborn man, whose objective in life had become war.", end = "")
    print(f"He dreamed of achieving glory day and night, and only pushed his own expectations onto {obj_character.character_name}.")
    print()
    print(f"Many years passed by, and {obj_character.character_name} grew to the age of 15.")
    print(f"Since a very young age, {obj_character.character_name} was fond of exploration. And what a day it is today, as you come across a cave and enter. That is right,", end = "")
    print(f" you are {obj_character.character_name}. Your choices will affect how {obj_character.character_name}'s life goes.")
    print("Your Current stats are as follows, they will change as your progress.\n")
    obj_character.print_stats()

    chp1_result_1 = obj_cavechp.scene_1().upper()

    if chp1_result_1 == 'A':
        result_2_a_a = obj_cavechp.scene_2_a().upper()
        result_2_b = "NIL"
        result_2_a_c = "NIL"
    elif chp1_result_1 == 'B':
        result_2_b = obj_cavechp.scene_2_b().upper()
        result_2_a_a = "NIL"
        result_2_a_c = "NIL"
    elif chp1_result_1 == 'C':
        result_2_a_c = obj_cavechp.scene_2_c().upper()
        result_2_b = "NIL"
        result_2_a_a = "NIL"

    if result_2_a_a != "NIL":
        if result_2_a_a == 'A':
            result_2_a_c = obj_cavechp.scene_2_conclude_a().upper()
        elif result_2_a_a == 'B':
            result_2_a_c = obj_cavechp.scene_2_conclude_b().upper()
        elif result_2_a_a == 'C':
            result_2_b = obj_cavechp.scene_2_b().upper()
        else:
            print("Please choose the correct option")

    if result_2_a_c != "NIL":
        if result_2_a_c == 'A':
            print(f"Since your current power is {obj_character.character_power}, you are unable to defeat the apparition, and it kills you.")
            print(f"You lost.")
            exit()
        elif result_2_a_c == 'B':
            result_2_b = obj_cavechp.scene_2_b().upper()
    
    if result_2_b != "NIL":
        if result_2_b == 'A':
            obj_cavechp.scene_2_5_a()
        elif result_2_b == 'B':
            obj_cavechp.scene_2_5_b()


class Chapter_Inn:
    print(f"Entering a small town near Old Alryne {obj_character.character_name} disturbed now seeks out an Inn to rest in.")

    def Scene_3(self) : 
        print("You have no money ! How shall you convince the Innkeeper to let you in ? (Please select the letters)")
        print("A. Sway the Innkeeper to let you in")
        print("B. Intimidate the Innkeeper to let you in")
        choice_2 = input().upper()
        while Invalid_Syntax(choice_2) == 0:
            print("Please choose the correct option.")
            choice_2 = input().upper()
            Invalid_Syntax(choice_2)
        return choice_2
        
    def Scene_3_a(self) :
       print()
       if obj_character.character_charisma <60 :
        print("Nice try mate but you shan't be bewitching me ")
        print("You have no choice left now but to Intimidate him. The poor bastard !")
        choice_2 = 'B_'
        return choice_2
       else :
        print("Sure mate I'd be delighed to have thee")
        print(f"{obj_character.character_name} enters the inn still traumatised by the encounter with the Apparition.")
        print("Feeling tired you conceal yourself under the warm blanket while lying on bed.")
        print("How long do you plan to sleep ?")
        print("A. 2 hours")
        print("B. 5 hours")
        print("C. 7 hours")
        choice_3 = input().upper()
        while Invalid_Syntax(choice_3) == 0:
            print("Please choose the correct option.")
            choice_3 = input().upper()
            Invalid_Syntax(choice_3)
        return choice_3
    def Scene_3_b(self) :
        print()
        print("Umm yeah sure mate no need to get edgy it's alright the room's over there")
        print("Annoyed and still contemplating about the encounter you lie down on the bed knowing that you can't stay at the Inn too long having threatened the Innkeeper ")
        print(" How long do you plan to sleep ?")
        print(" A. 1 hour")
        print(" B. 2 hours")
        print(" C. 3 hours")
        choice_4 = input().upper()
        while Invalid_Syntax(choice_4) == 0:
            print("Please choose the correct option.")
            choice_4 = input().upper()
            Invalid_Syntax(choice_4)
        return choice_4
    def Scene_choice_3_a(self) :
        time.sleep(2)
        obj_character.character_health += 10
        obj_character.character_power += 5
        obj_character.character_charisma += 10
        print(" You slept for only 2 hours")
        obj_character.print_stats()
    def Scene_choice_3_b(self) :
        time.sleep(5)
        obj_character.character_health += 20
        obj_character.character_power += 10
        obj_character.character_charisma += 15
        print(" You slept for 5 hours")
        obj_character.print_stats()
    def Scene_choice_3_c(self) :
        time.sleep(7)
        obj_character.character_health += 25
        obj_character.character_power += 15
        obj_character.character_charisma += 20
        print(" You slept for 7 hours")
        obj_character.print_stats()
    def Scene_choice_4_a(self) :
        time.sleep(1)
        obj_character.character_health += 5
        obj_character.character_charisma += 5
        print(" You slept for 1 hour")
        obj_character.print_stats()
    def Scene_choice_4_b(self) :
        time.sleep(2)
        obj_character.character_health += 10
        obj_character.character_power += 5
        obj_character.character_charisma += 10
        print(" You slept for only two hours")
        obj_character.print_stats()
    def Scene_choice_4_c(self) :
        time.sleep(3)
        obj_character.character_health += 15
        obj_character.character_power += 8
        obj_character.character_charisma += 12
        print(" You slept for only three hours")
        obj_character.print_stats()

obj_innchp = Chapter_Inn()

chp2_result_1 = obj_innchp.Scene_3().upper()

if chp2_result_1 == 'A':
    result_3_a = obj_innchp.Scene_3_a().upper()
    result_3_b = "NIL"
elif chp2_result_1 == 'B':
    result_3_b = obj_innchp.Scene_3_b().upper()
    result_3_a = "NIL"

if result_3_a != "NIL":
    if result_3_a == 'A':
         result_inn_choice_3_a = obj_innchp.Scene_choice_3_a()
    elif result_3_a == 'B':
         result_inn_choice_3_a = obj_innchp.Scene_choice_3_b()
    elif result_3_a == "B_":
         result_inn_choice_3_a = obj_innchp.Scene_3_b()
    elif result_3_a == 'C':
         result_inn_choice_3_a = obj_innchp.Scene_choice_3_c()

if result_3_b != "NIL":
    if result_3_b == 'A':
         result_inn_choice_3_b = obj_innchp.Scene_choice_4_a()
    elif result_3_b == 'B':
         result_inn_choice_3_b = obj_innchp.Scene_choice_4_b()
    elif result_3_b == 'C':
         result_inn_choice_3_b = obj_innchp.Scene_choice_4_c()


class Chapter_Town :   
    def Scene_5(self) :
        print("You walk through the narrow and dim corridor exiting the Inn with a rather cautiously optimistic outlook.")
        print("Intending to find the ancient map, you head towards the local Imperial archive.")
        print("Little do you know that someone had already gotten to it first. You hear the aghast from the bystanding crowd. You see the look on Imperial Guards faces.") 
        print("The archive was burnt down to the last book. All that knowledge of the past now lost.")
        print("But as the Gods willed it you hear whispers also. Rumors that can lead you to them. The bandits who stole the Map. Rather crudely had they attempted to steal this old map giving away what they were after.") 
        print("Yet the Imperials had other concerns than to chase after some bandits and a mythical map. They had a war to prepare for.")
        print(" You aren't able to eavesdrop a whole lot from the crowd. But you are able to make out possible ways in which you could find the bandits.")
        print(" A. You overhear a middle aged man being melancholic and walking away from the scene. There is something different about him.  You follow him")
        print(" B. You eavesdrop on the conversion of two Imperial Officers. You hear them talking about the Bandits possible location. You can try to get the information at the Imperial Office")
        print(" C. You see a couple of suspicious looking folk wearing some rusted gear who exit the scene in a very suspicious manner. You can try to find their whereabouts. They are possibly Bandits themselves.")
        choice_5 = input().upper()
        while Invalid_Syntax(choice_5) == 0:
            print("Please choose the correct option.")
            choice_5 = input().upper()
            Invalid_Syntax(choice_5)
        return choice_5 
    def Scene_6_a(self) :
        print()
        print("You try to follow him upto a distance but fail to catch up to him due to the surrounding crowd. Now you try to look for him.")
        if obj_character.character_charisma > 70 :
            print(" You ask around the to know more about the Man")
            print(" A villager informs you about the man's whereabouts and you start travelling there. ")
        elif obj_character.character_intelligence > 60 :
            print(" You follow in the last known direction of the man and look around & are able to find and follow his footsteps")
        else :
            time.sleep(10)
        print("It took you ten hours to find the old man's house ! But hey better late than never right ? ")
    def  Scene_6_b(self) :
        print()
        print(" You reach the middling structure. Now you must enquire")
        print(" A. You feel creative and under the guise of applying for the Military you get into the Office ")
        print(" B. You try to bribe the small level officers into giving you the Bandits' whereabouts.")
        choice_scene_6_b = input().upper()
        while Invalid_Syntax(choice_scene_6_b) == 0:
            print("Please choose the correct option.")
            choice_scene_6_b = input().upper()
            Invalid_Syntax(choice_scene_6_b)
        return choice_scene_6_b
    def Scene_6_c(self) :
        print()
        print(" A dangerous approach. You sneakily follow them into a small compound which by the looks of it looks like a Outlaw house. What do you do ? ")
        print(f" A. There seems to be {obj_character.character_weapon} in the frontyard pick it up and barge through the front door.")
        print(f" B. Grab the {obj_character.character_weapon} and sneak in from the back.")
        choice_scene_6_c = input().upper()
        while Invalid_Syntax(choice_scene_6_c) == 0:
            print("Please choose the correct option.")
            choice_scene_6_c = input().upper()
            Invalid_Syntax(choice_scene_6_c)
        return choice_scene_6_c
    def Scene_6_a_conclude(self) :
        print()
        print(" You enter the ramshackled house. The old man is a little startled by the visit but he lets you in.")
        print(" He looks at your youthful appearance. Tears roll over his eyes.")
        print(" He apologizes and asks you why you are here ? ") 
        print(" You respond by saying you saw him at the Archive. That you suspected that he was somehow related to the bandits and he could make this out by his dejected face.")
        print(" You tell him that you require the map that was stolen. And that you need to find the location of the bandits camp if there exists one.")
        print(" My son is part of their wretched gang. I haven't seen him in two years. If they are here then they maybe at a place not so far from here but what would still be the outskirts")
        print(" I do not know if my Son is still alive. Young one would you please spare him and ask him to return if he is ? He isn't a barbaric man. I am assuming you are going to fight them.")
        print(" You accept the old Man's plea and take an oath no to kill him were to find him.")
        print(" He will wearing a star medallion given to him by his mother. He will never give that up. Atleast I hope not. He is a lanky fella and has small scar on his left ear.")
        print(f" You thank the old man and say that you will do your best to help him and leave having got a lead but before you go he offers you his family {obj_character.character_weapon} which you take.")
    def Scene_6_b_a(self) : 
        print()
        print(" A rather risky approach. They find out and you take an arrow to the Knee. Yes? You apply for the post ")
        if obj_character.character_power > 70 :
            print(" Welcome Young Lad. I see you have an impressive physique and we would be delighted to have you. Go to the armoury see what fits you.") 
            print("Let me remind you that it isn't an easy post choose what suits you best and are comfortable with. Offcourse you won't have access to everything yet. You're still a rookie ")
        elif obj_character.character_charisma > 60 :
            print(" I come from a very martial background Sir. My father was a Marshall in Alryne I have been trained to for combat since childhood. If only you could give me a chance to stand for the virtues of the Empire ")
            print(" Fine! We will watch your career with great interest! Go to the Armoury and see what you like & can use")
        else :
            print(" We got a maggot here on our hands don't we boys ! Yeah we will make you straight. Go to the armoury and pick that dagger up !")
    def Scene_6_b_b(self) :
        print()
        if obj_character.character_coins > 10 :
            print(" Sure friend! He is at the Outskirts to the left of the Watchtower.")
        else :
            print(" Hmm..you don't have any money ! Beat it imbecile !")
            print(" You now have to improvise. Try getting into the Armoury by posing as a recruit for the Imperial Military. Yes?")
        choice_scene_6_b = 'A_'
        return choice_scene_6_b
    def Scene_6_c_a(self) :
        print()
        print("As you barge in through the front door, all eyes turn towards you. None of the gangsters are pleased.")
        print('"Hey! Who is that?", one of them asks.')
        print('"You know the rule lad, says a man who looks like the leader of the gang. A stranger, whether they be a danger or not, never leaves alive from this place."')
        print("Grab your weapons! Let's get em.")
    def Scene_6_c_b(self) :
        print()
        print("As you sneak in from the back, you take down two gangsters, but one of them ring's the alarm, making everyone aware of your presence.")
        print('"You know the rule lad. A stranger, whether they be a danger or not, never leaves alive from this place."')
        print("Grab your weapons! Let's get em,",end="")
        print(" shouts a person who looks like their leader.")
    def Scene_6_b_a_conclude(self) :
        print()
        print(" You now enter the Armoury. Oh how magnicficent are these art of men !") 
        print("However before taking the armoury you enter the nearby Records office and as fate would have it the manuscript that describes their hideout is right there infront of you") 
        print(f"After having seized and planning an escape through the windows. You take {obj_character.character_weapon} and walk out. Ready for a fight.")

obj_townchp = Chapter_Town()

chp3_result_1 = obj_townchp.Scene_5().upper()

if chp3_result_1 == 'A':
    chp3_result_b = "NIL"
    chp3_result_c = "NIL"
    obj_townchp.Scene_6_a()
    obj_townchp.Scene_6_a_conclude()
elif chp3_result_1 == 'B':
    chp3_result_b = obj_townchp.Scene_6_b()
    chp3_result_c = "NIL"
elif chp3_result_1 == 'C':
    chp3_result_c = obj_townchp.Scene_6_c()
    chp3_result_b = "NIL"

if chp3_result_b != "NIL":
    if chp3_result_b == 'A':
        obj_townchp.Scene_6_b_a()
        obj_townchp.Scene_6_b_a_conclude()
    else:
        obj_townchp.Scene_6_b_b()
        obj_townchp.Scene_6_b_a()
        obj_townchp.Scene_6_b_a_conclude()

if chp3_result_c != "NIL":
    if chp3_result_c == 'A':
        obj_townchp.Scene_6_c_a()
    else:
        obj_townchp.Scene_6_c_b()

class Chapter_Fight:
    def scene_7(self):
        print()
        print("You have no other option, but to fight the leader of the gang.")
        enemy_health = 100
        print(f"The boss's health is {enemy_health}.")
        print(f"Your health is {obj_character.character_health}.")
        while enemy_health >= 0 and obj_character.character_health >= 0:
            print(f"A. Slash with the {obj_character.character_weapon}.")
            print("B. Kick")
            print("C. Punch")
            fight_style = input().upper()

            if fight_style == 'A':
                your_damage = random.randint(5, 20)
                print(f"You did {your_damage} damage to the boss.")
                enemy_health -= your_damage
                print(f"The boss's health is {enemy_health}.")
            elif fight_style == 'B':
                your_damage = random.randint(0, 10)
                print(f"You did {your_damage} damage to the boss.")
                enemy_health -= your_damage
                print(f"The boss's health is {enemy_health}.")
            elif fight_style == 'C':
                your_damage = random.randint(0, 10) 
                print(f"You did {your_damage} damage to the boss.")
                enemy_health -= your_damage               
                print(f"The boss's health is {enemy_health}.")
            else:
                while Invalid_Syntax(fight_style) == 0:
                    print("Please choose the correct option.")
                    fight_style = input().upper()
                    Invalid_Syntax(fight_style)
                    continue
            
            print("The boss strikes back!")
            boss_damage = random.randint(0, 10)
            print(f"The boss does {boss_damage} damage to you!")
            obj_character.character_health -= boss_damage
            print(f"Your health is {obj_character.character_health}.")
        
        if enemy_health <= 0 and obj_character.character_health >= 0:
            print("You defeat the enemy leader, but are heavily bruised.")
            print("As you try to stand up, you feel some support. A guy helps you up to your feet.")
            print('You look at him, he has a scar on his left ear. He whispers, "I was on the wrong path. Seeing your fight I have understood, I will get strong to be good."')
            print("I have an old man waiting for me. I shall go. Thank you.")
            print("He helps you to your feet, and declares that he will not be a part of the gang. You smile.")
            print("As you get out of the hideout, the moonlight falls on your face. You feel tired, but relieved.")
            print("As you gaze far into the fields, you see a girl. It's as if she is calling to you.")
            print('You think to yourself...\n"The adventure is not yet over huh?"')
            print()
            print("To be continued.")
            print("Thank you for playing!")
        else:
            print("The boss defeats you and you die.")
            sys.exit("Better Luck Next Time !")

obj_fightchp = Chapter_Fight()
obj_fightchp.scene_7()