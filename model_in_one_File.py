import os
import subprocess
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
import socket
from datetime import datetime
import time
import psutil

# Pfad zum aktuellen Skript ermitteln
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Pfad zum Speichern des Modells festlegen
model_path = os.path.join(current_script_path, 'port_model.pkl')

# Pfad zur Logdatei festlegen
log_file_path = os.path.join(current_script_path, 'offen_ports.txt')

# Überprüfen, ob das Modell bereits existiert
if os.path.exists(model_path):
    # Modell laden und für weiteres Training verwenden
    port_model = load(model_path)
    log_entry = "Modell geladen und bereit für weiteres Training."
    print(log_entry)
    with open(log_file_path, 'a') as f:
        f.write(log_entry + '\n')
else:
    # Erstellen Sie das Modell, wenn es nicht existiert
    port_model = RandomForestClassifier(n_estimators=100)
    log_entry = "Neues Modell erstellt."
    print(log_entry)
    with open(log_file_path, 'a') as f:
        f.write(log_entry + '\n')

# Funktion zum Überprüfen des Portstatus auf einem Remote-Host
def check_port(port, host):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        return result == 0  # True, wenn der Port offen ist

# Funktion zum Ermitteln des Prozesses, der einen bestimmten Port verwendet
def get_process_using_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    return proc.info
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return None

# Funktion zum Schreiben der Ausgabe in die Konsole und die Datei
def log_and_print(message):
    print(message)
    with open(log_file_path, 'a') as f:
        f.write(message + '\n')

# Funktion zum Hinzufügen einer Firewall-Regel mit netsh
def add_firewall_rule(port):
    rule_name = f"BlockPort{port}"
    subprocess.run(f"netsh advfirewall firewall add rule name=\"{rule_name}\" dir=in action=block protocol=TCP localport={port}", shell=True)
    log_and_print(f"Firewall-Regel hinzugefügt, um Port {port} zu blockieren.")

# Funktion zum Entfernen einer Firewall-Regel mit netsh
def remove_firewall_rule(port):
    rule_name = f"BlockPort{port}"
    subprocess.run(f"netsh advfirewall firewall delete rule name=\"{rule_name}\"", shell=True)
    log_and_print(f"Firewall-Regel entfernt, um Port {port} freizugeben.")

# Überwachungsfunktion
def monitor_ports(host, ports_to_monitor, check_interval=60):
    port_status = {}
    data = []
    labels = []

    while True:
        for port in ports_to_monitor:
            is_open = check_port(port, host)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if port not in port_status or port_status[port] != is_open:
                # Status hat sich geändert
                process_info = get_process_using_port(port) if is_open else None
                process_str = f" (genutzt von {process_info['name']} [PID: {process_info['pid']}])" if process_info else ""
                log_and_print(f"{current_time}: Statusänderung: Port {port} auf {host} ist {'offen' + process_str if is_open else 'geschlossen'}")
                port_status[port] = is_open

                # Wenn der Port unerwartet geöffnet wird, fügen Sie eine Firewall-Regel hinzu
                if is_open:
                    add_firewall_rule(port)
                else:
                    # Entfernen Sie die Firewall-Regel, wenn der Port geschlossen wird
                    remove_firewall_rule(port)

            # Daten sammeln
            data.append([port])
            labels.append(1 if is_open else 0)

        # Konvertieren Sie die Listen in NumPy-Arrays für das maschinelle Lernen
        data_array = np.array(data)
        labels_array = np.array(labels)

        # Überprüfen Sie die Anzahl der Beispiele
        if len(data_array) > 1:
            # Teilen Sie Ihre Daten in Trainings- und Testsets
            train_data, test_data, train_labels, test_labels = train_test_split(data_array, labels_array, test_size=0.2)

            # Trainieren Sie das Modell
            port_model.fit(train_data, train_labels)

            # Bewerten Sie das Modell
            accuracy = port_model.score(test_data, test_labels)
            log_and_print(f"Modellgenauigkeit: {accuracy}")

            # Modell speichern
            dump(port_model, model_path)
            log_and_print(f"Modell gespeichert unter: {model_path}")

        time.sleep(check_interval)  # Wartezeit bis zur nächsten Überprüfung
# Beispiel: Überwachen von Ports 1110 bis 1130 auf dem Host '192.168.178.57'
host_to_monitor = '192.168.178.57'
ports_to_monitor = range(1110, 1130)

check_interval = 20
monitor_ports(host_to_monitor, ports_to_monitor, check_interval)

