#!python3
# -*- coding: utf-8 -*-

import pyautogui as gui
import random

words = ["pillow","abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]

def start():
    global tries,chosen_word,letters_chosen_word,board,words
    tries = 5
    chosen_word = words[random.randint(0,len(words)-1)]
    letters_chosen_word = list(chosen_word)
    board = ["__"] * len(chosen_word)

start()

while True:
    if "__" not in board:
        gui.alert(text='You guessed correctly!\nGiving a new word!', title='Hangman', button='OK')
        start()
    if tries == 0:
        gui.alert(text='No more tries left!\nThe word was: {}\nGiving a new word!'.format(chosen_word), title='Hangman', button='OK')
        start()

    guessed_letter = gui.prompt(text=(" ".join(board)), title='Hangman' , default='')


    if len(guessed_letter) == 1:
        if guessed_letter in letters_chosen_word:
            index = letters_chosen_word \
                    .index(guessed_letter)
            board[index] = guessed_letter
            letters_chosen_word[index] = '#'
        elif guessed_letter in board:
            gui.alert(text=("Already tried {}!".format(guessed_letter)), title='Hangman', button='OK')
        else:
            gui.alert(text=("There is no {} in the word!".format(guessed_letter)), title='Hangman', button='OK')
            tries -= 1
    else:
        gui.alert(text="Your guess must be one letter!", title='Hangman', button='OK')