# import pyautogui

# ##############Mouse
# pyautogui.size()                                         # Gives screen size
# pyautogui.position()                                  # Co-ordinates of cursor
# pyautogui.moveTo(0, 0)                            # Move mouse position
# pyautogui.moveTo(0, 0, duration=1.5)      # Move mouse position at 1.5 pixel
# pyautogui.displayMousePosition()             # In Python shell (black & white) to display mouse position.
# pyautogui.moveRel()                                  # Move mouse related to the current position
# pyautogui.click()                                         # click left
# pyautogui.rightClick()                                  # right click
# pyautogui.middleClick()                               # middle click
# pyautogui.leftClick()                                      # Left Click               
# pyautogui.doubleClick()                               # double left click
# pyautogui.dragTo()  O .dragRel()                  # Move mouse while draging


# #######Implementation Mouse
# pyautogui.size()    # Size(width=1024, height=768)
# width, height  = pyautogui.size()
# print(width)    # 1024
# print(height)  # 768
# pyautogui.position()    # Point(x=0, y=0)
# pyautogui.moveTo(0, 0)
# pyautogui.moveTo(0, 0, duration=1.5)


# #########Mouse: Display pattern in MS Paint
# import pyautogui

# pyautogui.click()
# distance = 200
# while distance > 0:
#     print(distance, 0)
#     pyautogui.dragRel(distance, 0, duration=0.1)
#     distance -= 25
    
#     print(0, distance)
#     pyautogui.dragRel(0, distance, duration=0.1)
     
#     print(-distance, 0)
#     pyautogui.dragRel(-distance, 0, duration=0.1)
#     distance -= 25

#     print(0, -distance)
#     pyautogui.dragRel(0, -distance, duration=0.1)

# #===============================

# ############
.
>>> import pyautogui
>>> pyautogui.click(18, 64)
>>> pyautogui.typewrite('Hello World')
Hello World
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World')
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World', interval= 1)
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World', interval= 0.7)
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World', interval= 0.4)
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World', interval= 0.3)
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World', interval= 0.2)
>>> pyautogui.click(18, 64);pyautogui.typewrite('Hello World', interval= 0.1)
>>> pyautogui.click(18, 64);pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval= 0.1)
>>> pyautogui.click(18, 64);pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval= 0.1)
>>> pyautogui.click(18, 64);pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval= 0.1)
>>> pyautogui.KEYBOARD_KEY
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pyautogui.KEYBOARD_KEY
AttributeError: module 'pyautogui' has no attribute 'KEYBOARD_KEY'
>>> pyautogui.KEYBOARD_KEYs
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    pyautogui.KEYBOARD_KEYs
AttributeError: module 'pyautogui' has no attribute 'KEYBOARD_KEYs'
>>> pyautogui.KEYBOARD_KEYS
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']
>>> pyautogui.press('f1')
>>> pyautogui.hotkey('ctrl', 'o')
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> pyautogui.screenshot()
<PIL.Image.Image image mode=RGB size=1024x768 at 0x3960EB8>
>>> pyautogui.screenshot("c:\\screen_shot.png")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    pyautogui.screenshot("c:\\screen_shot.png")
  File "C:\Users\Family\AppData\Local\Programs\Python\Python37\lib\site-packages\pyscreeze\__init__.py", line 357, in _screenshot_win32
    im.save(imageFilename)
  File "C:\Users\Family\AppData\Local\Programs\Python\Python37\lib\site-packages\PIL\Image.py", line 2085, in save
    fp = builtins.open(filename, "w+b")
PermissionError: [Errno 13] Permission denied: 'c:\\screen_shot.png'
>>> pyautogui.screenshot("c:\users\Family\Desktop\screen_shot.png")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> pyautogui.screenshot(r"c:\users\Family\Desktop\screen_shot.png")
<PIL.Image.Image image mode=RGB size=1024x768 at 0x3E804E0>
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\7.png')
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\7.png')
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\5.png')
Box(left=204, top=373, width=40, height=36)
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\plus.png')
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\equals.png')
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\7.png')
Box(left=169, top=346, width=35, height=29)
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\plus.png')
Box(left=283, top=440, width=38, height=30)
>>> pyautogui.locateOnScreen(r'C:\Users\Family\Pictures\calculator\equals.png')
Box(left=322, top=407, width=38, height=63)
>>> pyautogui.locateCenterOnScreen(r'C:\Users\Family\Pictures\calculator\equals.png')
Point(x=341, y=438)
>>> pyautogui.locateCenterOnScreen(r'C:\Users\Family\Pictures\calculator\7.png')
Point(x=185, y=359)
>>> pyautogui.locateCenterOnScreen(r'C:\Users\Family\Pictures\calculator\5.png')
Point(x=224, y=391)
>>> pyautogui.locateCenterOnScreen(r'C:\Users\Family\Pictures\calculator\plus.png')
Point(x=302, y=455)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> pyautogui.click(185, 359); pyautogui.click(302, 455); pyautogui.click(224, 391); pyautogui.click(341, 438)
>>> 
