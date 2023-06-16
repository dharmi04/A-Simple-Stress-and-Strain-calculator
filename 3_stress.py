import math
import time
import pyttsx3
import numpy as np
import pandas as pd

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    #print(audio)
    engine.runAndWait()

def spk(audio):
    engine.say(audio)
    print(audio, end="")
    engine.runAndWait()

#calculating stress & strain
def stress_strain(d,force, length, deformation):
    print("             -------------------------",length,"--------------------")
    print("            ________________________________________________________")
    print("           |                                                        |")
    print("           |________________________________________________________|")
    area = math.pi*d**2/4
    stress = force/area
    strain = deformation/length 
    e = stress/strain
    round_stress = round(stress, 2)
    round_strain = round(strain, 2)
    round_e = round(e, 2)
    print("stress of given data is: ",stress,"N/mm^2")
    speak("stress of given data is: ")
    speak(round_stress)
    speak("newton per milli meter square")
    print("  ")
    print("linear strain is: ",strain)
    speak("linear strain is: ")
    speak(round_strain)
    print("  ")
    print("Young's modulus is: ", e,"N/mm^2")
    speak("Young's modulus is: ")
    speak(round_e,)
    speak("newton per milli meter square")
    print(" ")


#poissons ratio
def poissons_ratio(il, fl, id, fd):
    print("           -------------------------",il,"---------------------------")
    print("            ________________________________________________________")
    print("           |                                                        |")
    print("           |________________________________________________________|")

    print("           -------------------------",fl,"---------------------------------------")
    print("            _____________________________________________________________________")
    print("           |                                                                     |")
    print("           |_____________________________________________________________________|")

    cl = fl-il
    cd = fd-id
    linear_strain = cl/il
    long_strain = cd/id
    pr = linear_strain/long_strain
    round_pr = round(pr, 2)
    print("poisson's ratio is: ", pr)
    speak("poisson's ratio is: ")
    speak(round_pr)

#working stress
def working_stress(w,u):
    f=u/w
    if f>1 and f<2:
        print ("Building structure with entered working load and ultimate stress is SAFE ")
        speak ("Building structure with entered working load and ultimate stress is SAFE ")
    else:
        print("Building structure with entered working load and ultimate stress is NOT SAFE ")
        speak("Building structure with entered working load and ultimate stress is NOT SAFE ")
def loop():
    print("Instructions to use:")
    speak("Instructions to use:")
    print("1.Enter values in specified units: Force-N, length-mm")
    speak("1.Enter values in specified units: Force in newton and length in mili meter")
    print("  ")
    print(" What do you want to calculate.")
    speak(" What do you want to calculate.")
    print("  ")
    print("The Available choices are:-")
    speak("The Available choices are:-")
    print("1. Stress and Strain ")
    speak("First, Stress and Strain")
    print("2. Poisson's ratio")
    speak("second, Poisson's ratio")
    print("3. Working stress")
    speak("third, Working stress")
    print("  ")
    n = int(input("Enter your choice:"))

    if n == 1:
        print("   ")
        spk("Enter Diameter")
        d = float(input(": "))
        print("  ")
        spk("Enter force applied")
        force = float(input(": "))
        print("   ")
        spk("Enter length of material")
        length = float(input(": "))
        print("  ")
        spk("Enter deformation in material due to force")
        deformation = float(input(": "))
        print("  ")
        spk("ENTERED DATA IS ")
        print(" ")
        dict1 = {"TOPIC": ['Diameter = ', 'Force  = ', 'Length  = ', 'Deformation = '], "VALUES": [d, force, length, deformation]}
        df = pd.DataFrame(dict1)
        print(df)
        print("")
        stress_strain(d, force, length, deformation)

    if n == 2:
        spk("Enter Length")
        il = float(input(": "))
        spk("Enter Final Length")
        fl = float(input(": "))
        spk("Enter inital diameter")
        id = float(input(": "))
        spk("Enter final diameter ")
        fd = float(input(": "))
        print("")
        spk("ENTERED DATA IS::")
        print("")
        dict2 = {"TOPIC": ["Length  = ", "Final Length = ", "Initial Diameter  = ", "Final Diameter = "], "VALUES": [il, fl, id, fd]}
        df1 = pd.DataFrame(dict2)
        print(df1)
        print("")
        poissons_ratio(il, fl, id, fd)


    if n == 3:
        spk("Enter working stress")
        w = float(input(": "))
        print("  ")
        speak("Enter ultimate stress")
        u = float(input(": "))
        print("  ")
        print("ENTERED DATA IS:")
        print("")
        dict3 = {"TOPIC": ["Working Stress = ", "Ultimate Stress = "], "VALUES": [w, u]}
        df3 = pd.DataFrame(dict3)
        print(df3)
        print("")
        working_stress(w, u)

def control():
    speak("Do you want to continue?")
    e = input("Do you want to continue (yes/no)?: ")
    if e == 'yes':
        loop()

    elif e == 'no':
        print("ThankYou for using me ")
        speak("ThankYou for using me ")
        time.sleep(5)
        exit()

    else:
        print("Invalid Option, Sir please try again")
        speak("Invalid Option, Sir please try again")
        control()

def repeat():
    loop()
    control()


if __name__ == "__main__":
    while True:
        repeat()