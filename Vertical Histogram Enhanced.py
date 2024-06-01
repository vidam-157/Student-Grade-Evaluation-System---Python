#Vidam Sathnindu - w1830118
#date:30/04/2021

print("****************>>STUDENT'S PROGRESS EVALUATION SYSTEM <<*************************")

Progressed_Students = 0
Trailored_Students = 0
Retriever_Students = 0
Excluded_Students = 0

marks = [0, 20, 40, 60, 80, 100, 120]

def markInputValidator(Marks):
    while True:
        try:
            MarkInput = int(input(f"Enter {Marks} Marks: "))
            if (MarkInput not in marks):
                print("Marks out of Range:")
                print(" ")
            else:
                return MarkInput
        except ValueError:
            print("Integer Required")
            print(" ")


def histogram(h):
    # making the histogram
    star = "*" * h
    return star

while True:

    Pass = markInputValidator("Pass")
    Defer = markInputValidator("Defer")
    Fail = markInputValidator("Fail")

    if (Pass + Defer + Fail == 120):
        if (Pass == 120):
             print(">>> Progress")
             print("-------------------------------------")
             Progressed_Students = Progressed_Students + 1
        elif (Pass == 100):
            print(">>> Progress (module trailer)")
            print("-------------------------------------")
            Trailored_Students = Trailored_Students + 1
        elif (Pass <= 80 and Defer >= 0 and Fail < 80):
                print(">>> Do not Progress – module retriever")
                print("-------------------------------------")
                Retriever_Students = Retriever_Students + 1
        elif (Fail >= 80):
            print(">>> Exclude")
            print("-------------------------------------")
            Excluded_Students = Excluded_Students + 1
    else:
        print(" ")
        print("Total Incorrect")
        print(" ")

    while True:

        print(" ")
        exit = input("Press 'y' to continue or 'q' to quit and view results: ")

        if exit == 'q':
            print("")
            break
        elif exit == 'y':
            print(" ")
            break
        else:
            print(" ")
            print("Invalid Input. Please press 'y' to continue or 'q' to quit and view results.")
            print("-------------------------------------")

    if exit == 'q':
        break


print("****************>> HISTOGRAM <<*************************")

print_vertical_histogram(Progressed_Students, Trailored_Students, Retriever_Students, Excluded_Students)

print(Progressed_Students + Trailored_Students + Retriever_Students + Excluded_Students, "outcomes in total")