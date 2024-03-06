import sys
import cx_Freeze
from cx_Freeze import setup, Executable

# base = "Win32GUI" allows your application to open without a console window
executables = [cx_Freeze.Executable('snek.py', base = "Win32GUI")]

cx_Freeze.setup(
    name = "snek!",
    options = {"build_exe" : 
        {"packages" : ["pygame"], "include_files" : ["save_file.csv", "bonus_fruit.py",
                                                     "button.py", "fruit.py",
                                                     "highscore.py", "player.py",
                                                     "scorelabel.py", "title_screen.png",
                                                     "score_screen.png", "bonus_timer.mp3",
                                                     "button.mp3", "end.mp3",
                                                     "end_2.mp3", "intro.mp3", "pickup_1.mp3",
                                                     "pickup_bonus.mp3", "pickup_bonus_2.mp3",
                                                     "playing.mp3", "speedup.mp3"]}}, 
    executables = executables
)