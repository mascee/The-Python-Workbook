# This program reads sound levels in dB from the user and prints what kind of sound this is.

sound_dB = int(input("Please enter sound level in dB and I will tell you what kind of sound it is: "))

Jackhammer = 130
Gas_Lawnmower = 106
Alarm_Clock = 70
Quiet_Room = 40


if sound_dB < Quiet_Room:
    {
        print("This sound is quieter then a quiet room. ")
    }
elif sound_dB == Quiet_Room:
    {
        print("This is the sound of the quiet room. ")
    }
elif sound_dB > Quiet_Room and sound_dB < Alarm_Clock:
    {
        print("This sound is between quiets room and an alarm clock. ")
    }
elif sound_dB == Alarm_Clock:
    {
        print("This is the sound of an alarm clock. ")
    }
elif sound_dB > Alarm_Clock and sound_dB < Gas_Lawnmower:
    {
        print("This sound is between an alarm clock and a gas lawnmower. ")
    }
elif sound_dB == Gas_Lawnmower:
    {
        print("This sound is of a lawnmower. ")
    }
elif sound_dB > Gas_Lawnmower and sound_dB < Jackhammer:
    {
        print("This sound is between Gas Lawnmower and Jackhammer. ")
    }
elif sound_dB == Jackhammer:
    {
        print("This is the sound of the Jackhammer. ")
    }
else:
    {
        print("This sound is out of the range. ")
    }

