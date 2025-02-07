import utils
import utils.inputs
numberIn = int(input("Enter number"))
divIn = int(input("Enter division"))

leaderNumber = utils.inputs.TakeInput(numberIn, divIn)
def run():
    print("manipulating")
    print("result is : ",leaderNumber.calculate())
if __name__ == "__main__":
    run()