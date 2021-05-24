import random
print('***************************** STORY ***********************************')
#Heading
print('CLICK ENTER TO READ STORY')
enter = input()
if enter == "ENTER" or "enter":
      names = random.choice(['Noah','Marukk','Finn','Mibi'])
      girlfriend = random.choice(['Rashmika','Sadie','Chole','Lucrecia'])
      place = random.choice(['Paris','Seattle','Madrid','London'])
      intro1 =" I am  " + names +"  From  " + place +  "  One day my Life is changed "
      thatday = "I met my love she is like a angel her name is " + girlfriend
      thatday1 ="When i go to Office I met a Man i do not Know Who he was but he is Trying to kill me "
      thatday2 = "I was so depressed so i am Going to park"
      thatday3 = "I were at theatre "
      expression1 = "And then i go to police station reported "
      expression2 = "Suddenly i See mY Old friend "
      expression3 = "i know I forget thinking about her "
      expression4 = "and then I Watched  stranger thigs "
      expression21 = "I would code  for a months "
      expression22 = "then i thout i was awefull "
      expression23 = " i see news but sudenly they say TODAY IS STROM  i was shocked"
      expression24 = "then i go to madagaser to seee penguins "
      expression31 = "i were dreamed avout when i was 8 at london "
      expression32 = "then i eat kit kat it was terrific "
      expression33 = "it was a night so i was go to the sleep"
      expression34 = " i was at the R language "
      thatdaystart = [thatday, thatday1, thatday2, thatday3]
      # we make a list of inputs
      expression = [expression24, expression21, expression22, expression23]
      expression20 = [expression3, expression4, expression1, expression2]
      expression30 = [expression31, expression32, expression33, expression34]
# print the introductionof the character
      print(intro1)
      print(random.choices(thatdaystart))
      print(random.choices(expression))
      print(random.choices(expression20)) 
      print(random.choices(expression30))      