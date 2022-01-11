import pyautogui as pg
import subprocess
## /run/media/partuser/xdrive/z/
subprocess.run('thunar /run/media/partuser/xdrive/z/'.split())
pg.click()
pg.hotkey('ctrl', 'T')
pg.hotkey('alt', 'home')
