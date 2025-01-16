# base amount = 0
# number of questions = 10
# amount per question = 10000
# we will use list to store answers to each question
print("\nWelcome to KBC!!!")


    
def checkanswer(QuestionNo,answers,amount):
    ans = input("Enter your answer: ")
    i = QuestionNo - 1
    if(ans == answers[i]):
        print("\nThat is the correct answer!!")
        amount += 10000
        return amount
    else: 
        print("\nOops! Wrong Answer")
        print("\nYour final amount won is:",amount)
        print("\nThank you for playing with us <3")
        raise SystemExit


amount = 0
answers = ["Indira Gandhi", "Jupiter", "Diwali", "Alexander Fleming", "Tiger"]

print("\nHere is the first question:\n")
print("Who is the first woman Prime Minister of India?")
print("A. Sonia Gandhi")
print("B. Indira Gandhi")
print("C. Pratibha Patil")
print("D. Sarojini Naidu")

amount = checkanswer(1,answers,amount)
print("Current Winning is",amount)

print("\nHere is the second question:\n")
print("What is the largest planet in our Solar System?")
print("A. Earth")
print("B. Mars")
print("C. Jupiter")
print("D. Saturn")

amount = checkanswer(2,answers,amount)
print("\nCurrent Winning is",amount)

print("\nHere is the third question:\n")
print("Which Indian festival is known as the \"Festival of Lights\"?")
print("A. Holi")
print("B. Diwali")
print("C. Dusshera")
print("D. Eid")

amount = checkanswer(3,answers,amount)
print("\nCurrent Winning is",amount)

print("\nHere is the fourth question:\n")
print("Who discovered penicillin?")
print("A. Louis Pasteur")
print("B. Alexander Fleming")
print("C. Marie Curie")
print("D. Robert Koch")

amount = checkanswer(4,answers,amount)
print("\nCurrent Winning is",amount)

print("\nHere is the fifth question:\n")
print("What is the national animal of India?")
print("A. Lion")
print("B. Tiger")
print("C. Elephant")
print("D. Peacock")

amount = checkanswer(5,answers,amount)
print("\nCurrent Winning is",amount)




