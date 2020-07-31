#magic function is to check weather the entered word can be formed with entered letters or not. It returns boolean value.
def magic(letters,word):
 flag = 0
 for i in letters:
    for j in word:
       #I am using nested for loop to get all possible combintions in a effective way
       # i=='?' combines both 1st and 2nd task that you gave me into one function
       if j==i or i=='?':
          flag+=1
          break
    
    if flag==len(word):
      break

 if flag == len(word):
    return 'true'

 else :
   return 'flase'

#longest function is to determine the longest word that can be created with entered letters from the enable1 dictioanary. It returns string value.
def longest(letters):
  all_words = list()
  possible_words = list()
  #This for loop is to extract all the words from enable1 text file and store it in a list named all_words.
  with open('enable1.txt','r') as f :
    for line in f :
      all_words.append(line.strip())

  #This for loop is to check which all word from all_words list can be formed with entered leeters and add to a list possible_words.
  for i in all_words :
     ans = magic(letters,i)
     if ans=='true' :
        possible_words.append(i)
     
  #max_len variable stores the length of word with maximum no of letters from the list possible_words.
  max_len = len(max(possible_words, key=len))
  #This for loop is to find which word in the list possible_words has the length equal to value of max_len variable and store it.
  for w in possible_words :
      if len(w) == max_len :
          longest_word = w
  
  
  return longest_word
 

#This is the main class with func method where all the above functions are called.
class main :
 #func method has a parameter r to be able restart the whole process again.
 def func(r) :
  while(r=='r') :    
   letters = input("Enter letter ")
   print("")
   print("1. To check if above letters can for the word you enter " )
   print("2. To print the longest word that can be formed by above letters ")
   choice = int(input("Enter your Choice? "))
   #If the user enters '1' if loop will be executed where we called the function magic.
   if choice==1 :
    word = input("Enter a word to check if it can be created with above enterd letters ")
    print("")
    ans = magic(letters,word)
    #Here we are printing weather the entered word can be formed from entered letters.
    if(ans=='true') :
      print("Yes , '{w}' can be created with '{l}' letters " .format(w=word,l=letters) )
    else:
      print("No ,  '{w}' cannot be created with '{l}' letters " .format(w=word,l=letters) )

    restart=input("Enter r to restart again ")
    print('')
    
    #This snippet is to restart the whole process once again.
    if restart=='r' or restart=='R' :
      main.func(r)
    else:
      print("Thank you see you again!")
      exit()

   #If the user enters '2' elif loop will be executed where we called the function longest.
   elif choice==2 :   
    longest_word = longest(letters)
    print("")
    #Here we are printing the longest word that can be formed using the entered letters
    print("The Longest word that can be created with'{l}' is '{lw}' ".format(l=letters,lw=longest_word))
    restart=input("Enter r to restart again ")
    print('')

    #This snippet is to restart the whole process once again.
    if restart=='r' or restart=='R' :
      main.func(r)
    else:
      print("Thank you see you again!")
      exit()
   else :
       print("Invalid input Try again ")
       

 
  return None


#This is to call the method inside main class to run program.
main.func('r')




    
