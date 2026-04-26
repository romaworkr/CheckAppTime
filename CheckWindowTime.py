import win32gui
import win32process
import psutil
import time as tim
import json
app_time = {}

while True:
    hwnd = win32gui.GetForegroundWindow()
    pid = win32process.GetWindowThreadProcessId(hwnd)[1]
    app = psutil.Process(pid).name()






    app_time[app] = app_time.get(app, 0) + 1
    with open("app_stats.json", "w", encoding="utf-8") as f:
        json.dump(app_time, f)
    print(app_time)

    tim.sleep(1)