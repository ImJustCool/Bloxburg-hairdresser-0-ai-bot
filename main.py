import os, pyautogui, time

input("enter to start")

image_files_list = []

color_list = [(27, 42, 53), (239, 184, 56), (13, 105, 172), (106, 57, 9), (231, 231, 236), (0, 255, 0), (255, 0, 191), (151, 0, 0)] 

for filename in os.listdir('hairs'):
    image_files_list.append(os.path.join('hairs', filename))

pyautogui.confirm("Click the top-right corner and press OK.")
top_right_x, top_right_y = pyautogui.position()

# Prompt the user to click on the bottom-left corner of the box
pyautogui.confirm("Click the bottom-left corner and press OK.")
bottom_left_x, bottom_left_y = pyautogui.position()

pyautogui.confirm("Click the color and press OK.")
color_x, color_y = pyautogui.position()

pyautogui.confirm("Click the hair next and press OK.")
hairx, hairy = pyautogui.position()

pyautogui.confirm("Click the color next and press OK.")
colorx, colory = pyautogui.position()

pyautogui.confirm("Click the complete next and press OK.")
completex, completey = pyautogui.position()

width = top_right_x - bottom_left_x
height = bottom_left_y - top_right_y
left = bottom_left_x
top = top_right_y

# Print out the results
print(f"Left: {left}, Top: {top}, Width: {width}, Height: {height}")



pyautogui.click(800, 100) 


while True:

    location = pyautogui.locateOnScreen("plus.png", region=(left, top, width, height), confidence=0.8)
    if location:
        print("scanning")

        time.sleep(0.25)

        for image in image_files_list:
            location = pyautogui.locateOnScreen(image, region=(left, top, width, height), confidence=0.85)
            if location:
                print("Found", image)
                number = int(str(image).split("\\")[-1].split(".")[0])
                for i in range(0, number):
                    print("clicking hair")
                    pyautogui.moveTo(hairx, hairy)
                    time.sleep(0.1)
                    pyautogui.click()

        current_color = pyautogui.pixel(color_x, color_y)
        for color in color_list:
            if color == current_color:
                print("Found", color)
                number = int(color_list.index(current_color))
                for i in range(0, number):
                    print("clicking color")
                    pyautogui.moveTo(colorx, colory)
                    time.sleep(0.1)
                    pyautogui.click()

        pyautogui.moveTo(completex, completey)
        print("clicking complete")
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.25)




        