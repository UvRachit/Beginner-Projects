# Set Of Questions For User As Quiz In Python

YN = input("Do you want to play the quiz? \n")
if YN.lower() == "yes":
    print("Then lets start ")

question = ["What Does CPU stand for? \n","What is the name of the person who discovered 'Electromagnetic Induction'? \n","What's the third planet of the solar system? \n","Who is the father of physics? \n","What does 'U' in gravitational force represent? \n","Who Is the artist who created 'Mona Lisa'? \n","What gas do plants absorb during photosynthesis? \n","What is the SI unit of force? \n","Who proposed the theory of relativity? \n","What does ROM stand for? \n","What is the smallest storage unit in a quantum computer? \n"]
answers = ["central processing unit","michael faraday","earth","isaac newton","universal constant","leonardo da vinci","carbon dioxide","newton","albert einstein","read only memory","qubit"]

score = 0

for ques,ans in zip(question,answers):
    qans = input(ques)

    if qans.lower() == ans:
        print("Correct!! :) ")
        score += 1
    else:
        print("Incorrect!! :( : Correct Answer is :",answers)

print("You Recieved A Total Of " + str(score) + " Marks In this IQ Test")
print("You recieved "+ str((score/len(question))*100) + " Percentage")

