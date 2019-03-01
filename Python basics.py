# Написать программу, которая каждый час проигрывает песню (всего 3 раза)

import webbrowser
import time

n = 1
while (n <= 3):
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=Qm4pP_gy2cU&index=2&list=LLNp6OVbHywyyhIWWKzgc8CA&t=0s")
    n = n+1