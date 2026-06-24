def Evaluate(average) :
    if average >= 50:
        return "SUCCESS"
    else:
        return "FAILED"


choice = "yes"
while choice == "yes":
    firstMark = float(input("Please enter first quiz mark(%100)  : "))
    secondMark = float(input("Please enter second quiz mark(%100) : "))
    thirdMark = float(input("Please enter third quiz mark(%100)  : "))

    average = float((firstMark + secondMark + thirdMark) / 3)

    print(f"THE AVERAGE IS : {average}")
    print(f"YOU ARE        : {Evaluate(average)}")
    choice = input("Do you want to try again ? (yes/no) : ")
