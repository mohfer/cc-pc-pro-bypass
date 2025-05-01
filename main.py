# Script Dibuat Oleh @yogakokxd
# Recode Boleh Jangan Lupa Credit:v

import os
import sys
import time
import glob
import shutil
import ctypes
import webbrowser
import datetime

# ascii nya ini brok
def print_banner():
    banner = r"""

 ██████╗ █████╗ ██████╗  ██████╗██╗   ██╗████████╗    ██████╗ ██████╗  ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔═══██╗
██║     ███████║██████╔╝██║     ██║   ██║   ██║       ██████╔╝██████╔╝██║   ██║
██║     ██╔══██║██╔═══╝ ██║     ██║   ██║   ██║       ██╔═══╝ ██╔══██╗██║   ██║
╚██████╗██║  ██║██║     ╚██████╗╚██████╔╝   ██║       ██║     ██║  ██║╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═════╝    ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
                                                                               
"""
    print(banner)
    print("CapCut Pro Bypasser By @yogakokxd")

# box alert
def show_alert(title, text):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x40)

# ubah nama jika udah ada nama yg sama
def unique_filename(path):
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}({counter}){ext}"
        counter += 1
    return new_path

# clear
def clear_screen():
    os.system('cls')

def main():
    clear_screen()
    print_banner()
    print("Perintah Yang Tersedia : start, help, tutor, exit")
    while True:
        cmd = input('> ').strip().lower()
        if cmd == 'help':
            clear_screen()
            print_banner()
            print("Perintah Yang Tersedia : start, help, exit")
        elif cmd == "tutor":
            print("Untuk Tutorial Bisa Cek Di Youtube :\nhttps://youtu.be/v52G-vHkqoE")
            tutorial_url = "https://youtu.be/v52G-vHkqoE"
            webbrowser.open(tutorial_url)
        elif cmd == 'start':
            project = input('Masukkan Nama Project CapCut : ').strip()
            proj_dir = os.path.join(
                os.path.expanduser('~'),
                'AppData', 'Local', 'CapCut', 'User Data',
                'Projects', 'com.lveditor.draft', project
            )
            if not os.path.isdir(proj_dir):
                print(f"[!] Project '{project}' tidak ditemukan.")
                continue
            print(f"[+] Ditemukan Project : {project}")

            comb_dir = os.path.join(proj_dir, 'Resources', 'combination')
            print("[+] Processing Export... (Pre-processing 0%)")
            pct = 0
            while True:
                # ambil hanya file .mp4 tanpa alpha
                files = [f for f in glob.glob(os.path.join(comb_dir, '*.mp4')) if 'alpha' not in os.path.basename(f).lower()]
                if files:
                    break
                pct = min(pct + 5, 95)
                print(f"[+] Processing Export... (Pre-processing {pct}%)")
                time.sleep(1)
            print("[+] Processing Export... (Pre-processing 100%)")

            mp4_files = [f for f in glob.glob(os.path.join(comb_dir, '*.mp4')) if 'alpha' not in os.path.basename(f).lower()]
            latest = max(mp4_files, key=os.path.getmtime)
            mtime = os.path.getmtime(latest)
            dt = datetime.datetime.fromtimestamp(mtime)
            print(f"[+] File terbaru: {os.path.basename(latest)} (Modified: {dt.strftime('%Y-%m-%d %H:%M:%S')})")

            dest_dir = os.path.join(os.path.expanduser('~'), 'Videos')
            os.makedirs(dest_dir, exist_ok=True)
            dest_path = unique_filename(os.path.join(dest_dir, f"{project}.mp4"))
            shutil.copy2(latest, dest_path)
            print(f"[!] Video Telah Tersimpan Di {dest_path}")
            show_alert("Selesai", f"Video telah disimpan di {dest_path}")
        elif cmd == 'exit':
            print("Bye!")
            sys.exit(0)
        else:
            print("Perintah tidak dikenali. Ketik 'help' untuk melihat perintah yang tersedia.")

if __name__ == '__main__':
    main()
