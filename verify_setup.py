import sys
import os
import subprocess

def check_import(module_name):
    try:
        __import__(module_name)
        print(f"[OK] {module_name} is installed.")
        return True
    except ImportError:
        print(f"[FAIL] {module_name} is NOT installed.")
        return False

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[OK] FFmpeg is found in PATH.")
        return True
    except FileNotFoundError:
        print("[FAIL] FFmpeg is NOT found in PATH. Please install it.")
        return False

def main():
    print("--- Verifying Setup ---")
    all_good = True
    
    # Check imports
    modules = ["customtkinter", "faster_whisper", "ffmpeg", "deep_translator"]
    for mod in modules:
        if not check_import(mod):
            all_good = False
            
    # Check FFmpeg
    if not check_ffmpeg():
        all_good = False
        
    print("-" * 20)
    if all_good:
        print("Everything looks ready! You can run 'python main.py'")
    else:
        print("Some requirements are missing. Check above.")

if __name__ == "__main__":
    main()
