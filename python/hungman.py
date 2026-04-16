from wordlist import words 
import random


hman_art={0:("   "
             "   "
             "   "),
          1:(" O "
             "   "
             "   "),
          2:(" O  "
             " | "
             "   "),
          3:(" O "
             "/| "
             "   "),
          4:(" O "
             "/|\\"
             "   "),
          5:(" O "
             "/|\\"
             "/  "),
          6:(" O "
             "/|\\"
             "/ \\")}

def display_man(wrong_guesses):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    answer=random.choice(words)
    print(answer)

if __name__ =="__main__":
    main()