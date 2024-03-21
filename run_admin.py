import ctypes
import sys
import customtkinter  as ctk


def run_as_admin(root):
    if sys.platform == 'win32':
        script_path = "main.py"
    
        try:
            # Use ctypes to call the ShellExecute function with "runas" verb
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd", f'/c python "{script_path}"', None, 1)
        except ctypes.WinError as e:
            print(f"Error: {e}")
