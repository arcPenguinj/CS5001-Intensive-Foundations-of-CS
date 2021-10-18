'''
CS 5001 Lab2
Yici Zhu
harry potter buzzfeed quiz

'''

def main ():
    Question1 = input("When planning a trip, you...\nA: Find the hot parties.\nB: Sorts out all the logistics\nC: Lets everyone else take charge\n")
    Question2 = input("What are you most afraid of?\nA: Not being accepted\nB: Losing someone close to me\nC: Looking stupid in front of others\n")
    Question3 = input("What was your favourite toy as a kid?\nA: She-Ra\nB: He-Man\nC: Vedio Games\n")
    
    Question1lower = Question1.lower()
    Question2lower = Question2.lower()
    Question3lower = Question3.lower()

    if Question1lower == "a" or Question1lower == "find the hot parties":
       Question1 ="A"
    elif Question1lower=="b" or Question1lower == "sorts out all the logistics":
        Question1 = "B"
    elif Question1lower == "c" or Question1lower == "lets everyone else take charge":
        Question1 = "C"
    else: 
        Question1 = "A"

    if Question2lower == "a" or Question2lower == "not being accepted":
        Question2 = "A"
    elif Question2lower == "b" or Question2lower == "losing someone close to me":
        Question2 = "B"
    elif Question2lower == "c" or Question2lower == "looking stupid in front of others":
        Question2 = 'C'
    else: 
        Question2 = "A"

    if Question3lower == "a" or Question3lower == "she-ra":
        Question3 = "A"
    elif Question3lower == "b" or Question3lower == "he-man":
        Question3 = "B"
    elif Question3lower == "c" or Question3lower == "vedio games":
        Question3 = "C"
    else: 
        Question3 = "A"

    if Question1 == "A" and Question2 == "A" and Question3 == "A":
        print("Ginny")
    elif Question1 == "A" and Question2 == "A" and Question3 == "B":
        print("Draco")
    elif Question1 == "A" and Question2 == "A" and Question3 == "C":
        print("Sirius")
    elif Question1 == "A" and Question2 == "B":
        print("Dobby")
    elif Question1 == "A" and Question2 == "C":
        print("Voldemort")
    elif Question1 == "B":
        print("Hermione")
    elif Question1 == "C" and Question2 == "A" and Question3 == "A":
        print("Luna")
    elif Question1 == "C" and Question2 == "A" and Question3 == "B":
        print("Hagrid")
    elif Question1 == "C" and Question2 == "A" and Question3 == "C":
        print("Ron")
    elif Question1 == "C" and Question2 == "B":
        print("Tonks")
    elif Question1 == "C" and Question2 == "C":
        print("Slughorn")

if __name__ == "__main__":
    main()
