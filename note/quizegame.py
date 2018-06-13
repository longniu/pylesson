'''
Create a word quize by using generator
'''

def word_quiz(word):
    hint = ""
    for letter in word :
        hint += letter
        yield hint

# Question
ans = "Python"
quiz = word_quiz(ans)
while True:
    try:
        hint = next(quiz)
        print(hint)
        word = input("Type in your gessed word:")
        if ans.lower() == word.lower():
            point = len(ans) - len(hint)
            print( f"Bingo! Your Point:{point}")
            break
        else :
            print("Wrong!")
    except:
        print("Game Over, Your Point: 0")
        break
    
