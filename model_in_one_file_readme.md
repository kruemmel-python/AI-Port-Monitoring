# Portüberwachungs- und Verwaltungsskript

Dieses Repository enthält ein Python-Skript zum Überwachen des Status bestimmter Ports auf einem Remote-Host. Das Skript prüft, ob die Ports geöffnet oder geschlossen sind, protokolliert die Statusänderungen, verwaltet Firewall-Regeln und verwendet ein maschinelles Lernmodell, um den Portstatus vorherzusagen.

## Merkmale

- **Portstatusüberwachung**: Überprüft kontinuierlich, ob bestimmte Ports auf einem Remote-Host offen oder geschlossen sind.
- **Protokollierung**: Protokolliert Statusänderungen und Modellgenauigkeit in einer Datei.
- **Firewall-Verwaltung**: Fügt automatisch Firewall-Regeln basierend auf dem Portstatus hinzu oder entfernt sie.
- **Maschinelles Lernen**: Verwendet einen RandomForestClassifier, um den Portstatus vorherzusagen und sein Modell im Laufe der Zeit zu verbessern.

## Anforderungen

- Python 3.x
- `numpy`
- „scikit-learn“.
- `joblib`
- `psutil`
- „Steckdose“.

Sie können die erforderlichen Pakete mit „pip“ installieren:
„Sch
pip install numpy scikit-learn joblib psutil

Skript-Erklärung
Initialisierung:

Bestimmt den Pfad des aktuellen Skripts.
Legt Pfade zum Speichern des Modells und zur Protokollierung fest.
Lädt ein vorhandenes Modell, falls verfügbar; Andernfalls wird ein neues RandomForestClassifier-Modell erstellt.
Funktionen:

check_port(port, host): Prüft, ob ein bestimmter Port auf dem Host geöffnet ist.
get_process_using_port(port): Ruft Informationen über den Prozess über einen bestimmten Port ab.
log_and_print(message): Protokolliert Nachrichten sowohl in der Konsole als auch in einer Protokolldatei.
add_firewall_rule(port): Fügt eine Firewall-Regel hinzu, um einen bestimmten Port zu blockieren.
remove_firewall_rule(port): Entfernt eine Firewall-Regel für einen bestimmten Port.
monitor_ports(host, ports_to_monitor, check_interval): Hauptfunktion, die den Portstatus überwacht, Firewall-Regeln aktualisiert und das maschinelle Lernmodell trainiert.
Überwachungsschleife:

Überprüft kontinuierlich den Status der angegebenen Ports.
Protokolliert alle Statusänderungen und verwaltet die Firewall-Regeln entsprechend.
Sammelt Daten und Labels für maschinelles Lernen.
Trainiert das Modell und bewertet seine Genauigkeit.
Speichert das trainierte Modell regelmäßig.

Aufbau
Host und Ports

host_to_monitor = '192.168.178.57'
ports_to_monitor = range(1110, 1130)
check_interval = 20 # Prüfintervall in Sekunden


Ändern Sie die oben genannten Variablen, um verschiedene Ports oder Hosts zu überwachen.

Mitwirken
Pull-Anfragen sind willkommen. Bei größeren Änderungen öffnen Sie bitte zunächst ein Problem, um zu besprechen, was Sie ändern möchten.

Danksagungen
Inspiriert durch verschiedene Netzwerküberwachungs- und maschinelle Lernprojekte.



# Port Monitoring and Management Script

This repository contains a Python script for monitoring the status of specific ports on a remote host. The script checks whether the ports are open or closed, logs the status changes, manages firewall rules, and uses a machine learning model to predict port status.

## Features

- **Port Status Monitoring**: Continuously checks if specified ports on a remote host are open or closed.
- **Logging**: Logs status changes and model accuracy to a file.
- **Firewall Management**: Automatically adds or removes firewall rules based on port status.
- **Machine Learning**: Uses a RandomForestClassifier to predict port status and improves its model over time.

## Requirements

- Python 3.x
- `numpy`
- `scikit-learn`
- `joblib`
- `psutil`
- `socket`

You can install the necessary packages using `pip`:
```sh
pip install numpy scikit-learn joblib psutil

Script Explanation
Initialization:

Determines the path of the current script.
Sets paths for saving the model and logging.
Loads an existing model if available; otherwise, creates a new RandomForestClassifier model.
Functions:

check_port(port, host): Checks if a specific port on the host is open.
get_process_using_port(port): Retrieves information about the process using a specific port.
log_and_print(message): Logs messages to both the console and a log file.
add_firewall_rule(port): Adds a firewall rule to block a specific port.
remove_firewall_rule(port): Removes a firewall rule for a specific port.
monitor_ports(host, ports_to_monitor, check_interval): Main function that monitors port status, updates firewall rules, and trains the machine learning model.
Monitoring Loop:

Continuously checks the status of specified ports.
Logs any status changes and manages firewall rules accordingly.
Collects data and labels for machine learning.
Trains the model and evaluates its accuracy.
Saves the trained model periodically.

Configuration
Host and Ports

host_to_monitor = '192.168.178.57'
ports_to_monitor = range(1110, 1130)
check_interval = 20  # Check interval in seconds


Modify the above variables to monitor different ports or hosts.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Acknowledgments
Inspired by various network monitoring and machine learning projects.


