import random
end_of_game = False
word_list=['words','wins','lose']
choose_word=random.choice(word_list)
lives=6
display=[]
for _ in range(len(choose_word)):
    display += "_"
    # print(display)
while not end_of_game:
    guess=input("guess a word:").lower()

    for pos in range(len(choose_word)):
        letter=choose_word[pos]
        if letter == guess:
            display [pos]=letter

    if guess not in choose_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("you lose")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game=True
        print("you win")
    print([lives])