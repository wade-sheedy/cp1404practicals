COLORS_HEXI = {"#fof8ff": "AliceBlue", "#faebd7": "AntiqueWhite", "#7fffd4": "aquamarine1", "#e0eeee": "azure2",
          "#000000": "black", "#ffebcd": "BlanchedAlmond", "#8a2be2": "BlueViolet", "#0000ee": "blue2",
          "#76ee00": "chartreuse2", "#ff1493": "DeepPink1"}

color = input("Enter a color Hexi-Decimal Code Here:  ")
while color != "":
    if color in COLORS_HEXI:
        print(color, "is" ,COLORS_HEXI[color])
    else:
        print("Invalid Hexidecimal Code enter a new code")
    color = input("Enter a color Hexi-Decimal Code Here:  ")