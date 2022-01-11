import pyautogui as pg
import subprocess
## /run/media/partuser/xdrive/z/
subprocess.run('thunar /run/media/partuser/xdrive/z/'.split())
pg.click()
pg.hotkey('ctrl', 'shift', 'p')
pg.hotkey('alt', 'home')
