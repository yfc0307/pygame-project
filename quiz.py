import random
import time

class QuickMathGame:
    def __init__(self):
        self.listA = list(range(1, 100))
        self.listB = list(range(1, 20))
        self.questionType = 1
        self.ques = []
        self.time = 120
        self.gameStatus = False
        self.input = 0
        self.sol = 0
        self.score = 0
        self.quesString = ""

    def InitQtypeAPlusNumbers(self):
        numA = random.choice(self.listA)
        numB = random.choice(self.listA)
        ans = numA + numB
        return [numA, numB, ans]

    def InitQtypeAMinusNumbers(self):
        numA = random.choice(self.listA)
        numB = random.choice(self.listA)
        if numA > numB:
            ans = numA - numB
        else:
            ans = numB - numA
        return [numA, numB, ans] if numA > numB else [numB, numA, ans]

    def InitQtypeBTimesNumbers(self):
        numA = random.choice(self.listB)
        numB = random.choice(self.listB)
        ans = numA * numB
        return [numA, numB, ans]

    def DecideQuestionType(self):
        self.questionType = random.randint(1, 13)

    def RefreshQuestion(self):
        self.DecideQuestionType()
        if self.questionType == 1:
            self.ques = self.InitQtypeAPlusNumbers()
            self.quesString = f"{self.ques[0]} + {self.ques[1]} = ???"
            self.sol = self.ques[2]
        elif self.questionType == 2:
            self.ques = self.InitQtypeAPlusNumbers()
            self.quesString = f"??? + {self.ques[1]} = {self.ques[2]}"
            self.sol = self.ques[0]
        elif self.questionType == 3:
            self.ques = self.InitQtypeAPlusNumbers()
            self.quesString = f"{self.ques[0]} + ??? = {self.ques[2]}"
            self.sol = self.ques[1]
        elif self.questionType == 4:
            self.ques = self.InitQtypeAMinusNumbers()
            self.quesString = f"{self.ques[0]} - {self.ques[1]} = ???"
            self.sol = self.ques[2]
        elif self.questionType == 5:
            self.ques = self.InitQtypeAMinusNumbers()
            self.quesString = f"??? - {self.ques[1]} = {self.ques[2]}"
            self.sol = self.ques[0]
        elif self.questionType == 6:
            self.ques = self.InitQtypeAMinusNumbers()
            self.quesString = f"{self.ques[0]} - ??? = {self.ques[2]}"
            self.sol = self.ques[1]
        elif self.questionType == 7:
            self.ques = self.InitQtypeBTimesNumbers()
            self.quesString = f"{self.ques[0]} × {self.ques[1]} = ???"
            self.sol = self.ques[2]
        elif self.questionType == 8:
            self.ques = self.InitQtypeBTimesNumbers()
            self.quesString = f"??? × {self.ques[1]} = {self.ques[2]}"
            self.sol = self.ques[0]
        elif self.questionType == 9:
            self.ques = self.InitQtypeBTimesNumbers()
            self.quesString = f"{self.ques[0]} × ??? = {self.ques[2]}"
            self.sol = self.ques[1]
        elif self.questionType == 10:
            self.ques = self.InitQtypeBTimesNumbers()
            self.quesString = f"{self.ques[2]} ÷ {self.ques[1]} = ???"
            self.sol = self.ques[0]
        elif self.questionType == 11:
            self.ques = self.InitQtypeBTimesNumbers()
            self.quesString = f"??? ÷ {self.ques[1]} = {self.ques[0]}"
            self.sol = self.ques[2]
        elif self.questionType == 12:
            self.ques = self.InitQtypeBTimesNumbers()
            self.quesString = f"{self.ques[2]} ÷ ??? = {self.ques[0]}"
            self.sol = self.ques[1]

    def RefreshGame(self):
        self.RefreshQuestion()
        self.score = 0

    def play(self):
        self.RefreshGame()
        start = time.time()
        while self.score < 2:
            print(self.quesString)
            self.input = int(input("Please input your answer: "))
            if self.input == self.sol:
                print("Answer Correct")
                self.score += 1
            else:
                print("Answer Incorrect")
            self.RefreshQuestion()
            self.time -= 1
        end = time.time()
        length = end - start
        print(f"You did it! Your time is: " + str(round(length, 3)) + " seconds.")

if __name__ == "__main__":
    game = QuickMathGame()
    game.play()