import autopy
import pyautogui

def main():
  print("Moving stuff!")
  pyautogui.moveTo(100, 100, duration = 2)
  pyautogui.moveRel(0, 50, duration = 2)

  
  # pyautogui.click(100, 100)
  # pyautogui.typewrite("hello Geeks !")
  # pyautogui.typewrite(["a", "left", "ctrlleft"])
  # pyautogui.hotkey("ctrlleft", "a")

if __name__ == "__main__":
  main()