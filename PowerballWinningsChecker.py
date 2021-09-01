from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
Browser = webdriver.Chrome(ChromeDriverManager().install(),options =chrome_options)

rewards = {
    (0,False):0,
    (0,True): 4,
    (1,True): 4,
    (2,True): 7,
    (3,False):7,
    (3,True):100,
    (4,False):100,
    (4,True):50000,
    (5,False):1000000
}


def getrandompowerballnumbers():
    powerballnumbers = []

    for i in range(5):
        n =  random.randint(1,69)
        if 1 <= n <= 69 and n not in powerballnumbers:
            powerballnumbers.append(n)
    powerball = random.randint(1,26)
    powerballnumbers.sort()
    powerballnumbers.append(powerball)
    return powerballnumbers
def getPowerballNumbersandJackpotNumber():
    Browser.get("https://www.powerball.com/")
    numbers = Browser.find_elements_by_class_name("numbers-ball")
    lnum = []
    count = 0
    for i in numbers:
        if count < 6:
            lnum.append(i.text)
            count += 1
    jackpot = Browser.find_element_by_xpath("/html/body/div[2]/div/header/div[2]/div/div[1]/div[2]/span[2]").text
    Browser.quit()
    return lnum, jackpot

def getPowerballnumbersfromuser():
    numbers = []
    for i in range(6):
        print("Enter the numbers you played:")
        n = int(input())
        if i < 4:
            if 1 <= n <= 69:
                numbers.append(n)
            else:
                print("Number is lower than 1 or bigger than 69. This numbers are not possible because of the rules of the powerball game.")
                print("Enter a new number in the range from 1 to 69")
                n  = int(input())
                numbers.append(n)
        else:
            if 1 <= n <= 26:
                numbers.append(n)
            else:
                print("Number is lower than 1 or bigger than 26. This numbers are not possible because of the rules of the powerball game.")
                print("Enter a new number in the range from 1 to 26")
                n = int(input())
                numbers.append(n)
    print(f"This are the numbers you played.{numbers}")
    return numbers

def checkifallthenumbersarethesame(n,n1):
    for i in range(len(n)):
        if int(n[i]) != n1[i]:
            return False
def checkhowmanynumbersarethesame(n,n1):
    count = 0
    powerballisthesame = False
    powerballuser = n1[-1]
    powerball = int(n[-1])
    for i in range(len(n)-1):
        if int(n[i]) == n1[i]:
            count+=1
    if powerball == powerballuser:
        powerballisthesame = True
    return count,powerballisthesame

def basicrewards(count,powerball):
    return rewards.get((count,powerball))

def main():
    print("-"*100)
    working = True
    while working:
        print("Enter 1 to get Powerball numbers and Jackpot amount.")
        print("Enter 2 to check if you won or had any similar numbers.")
        print("Enter 3 to get random powerball numbers.")
        print("Enter 4 to quit the program.")
        n = int(input("Enter the option you want: "))
        if n == 1:
            numbers, jackpot = getPowerballNumbersandJackpotNumber()
            print(f"This are the winning numbers {numbers}, this is the jackpot amount {jackpot}")
            print("-" * 100)
        if n == 2:
            numbers, jackpot = getPowerballNumbersandJackpotNumber()
            yournumbers = getPowerballnumbersfromuser()
            print(f"This are the winning numbers {numbers}")
            if checkifallthenumbersarethesame(numbers,yournumbers) == False:
                count, powerball = checkhowmanynumbersarethesame(numbers,yournumbers)
                moneywon = basicrewards(count,powerball)
                print(f"This is the amount of money you won {moneywon}")
            else:
                print(f"You won the jackpot! Congratulations! This the amount of money you won {jackpot}")
            print("-" * 100)
        if n == 3:
            powerballnumbers = getrandompowerballnumbers()
            print(powerballnumbers)
            print("-" * 100)
        if n == 4:
            working = False
main()