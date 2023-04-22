rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



import random
list1=[rock,paper,scissors]

#what choice we want to make
your_choice=int(input("choose 0 for Rock, 1 for Paper or 2 for Scissors.\t"))

if your_choice>=3 or your_choice<=-1:
    print("choose valid number")
else:
    list2=["Rock","Paper","Scissors"]
    #printing our choice with icon
    print(f"You have choosen {list2[your_choice]}")
    print(list1[your_choice])

    #computer choice
    computer=random.randint(0,2)
    #printing computer choice with icon
    print(f"Computer has choosen {list2[computer]}")
    print(list1[computer])

    #when we win
    if (your_choice==0 and computer==2) or (your_choice==1 and computer==0) or (your_choice==2 and computer==1):
        print("You win")
    #when computer wins
    elif (your_choice==0 and computer==1) or (your_choice==1 and computer==2) or (your_choice==2 and computer==0):
        print("You lose")
    #when both choose same match is draw
    else:
        print("match is draw")
