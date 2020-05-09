from sys import platform
import os 
def main():
	if platform == "linux":
		os.system("shutdown /s /t 1")
	if platform == "win32":
		print("windows")
	#print("SHUTDOWN")

if __name__ == "__main__":
	pass