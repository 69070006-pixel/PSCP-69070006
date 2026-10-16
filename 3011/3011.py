"""combinedcolor"""
color = input().lower().replace(" ", "")
color2 = input().lower().replace(" ", "")
if color == color2 and color in ["red", "yellow", "blue"]:
    print(color.capitalize())
elif color == "red" and color2 == "yellow":
    print("Orange")
elif color == "yellow" and color2 == "red":
    print("Orange")
elif color == "red" and color2 == "blue":
    print("Violet")
elif color == "blue" and color2 == "red":
    print("Violet")
elif color == "blue" and  color2 == "yellow":
    print("Green")
elif color == "yellow" and color2 == "blue":
    print("Green")
elif color == color2 and color not in ["red", "yellow", "blue"]:
    print("Error")
else:
    print("Error")
