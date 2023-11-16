import win32gui
import win32api
import screeninfo

# Get information about all monitors
monitors = screeninfo.get_monitors()

# Get the handle of the active window
active_window = win32gui.GetForegroundWindow()

# Get the coordinates of the active window
active_rect = win32gui.GetWindowRect(active_window)

# Iterate through monitors and find the active one
active_monitor = None
while True:
    print(active_rect[1])
    # for monitor in monitors:
    #     if monitor.x <= active_rect[0] <= monitor.x + monitor.width and \
    #     monitor.y <= active_rect[1] <= monitor.y + monitor.height:
    #         active_monitor = monitor
    #         break

    # if active_monitor:
    #     print(f"Active window is on Monitor {active_monitor.name} - {active_monitor.width}x{active_monitor.height}")
    # else:
    #     print("Active window is not on any monitor")
