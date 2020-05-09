from sys import platform
import os 
def main():
	if platform == "linux":
		os.system('systemctl poweroff') 
	if platform == "win32":
		print("windows")


if __name__ == "__main__":
	pass