# AI Port Monitoring

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

AI Port Monitoring ist ein Machine-Learning-Projekt, das den Status von Netzwerk-Ports überwacht und lernt, wie sich der Status über die Zeit verändert. Dieses Tool verwendet einen RandomForest-Klassifikator, um Muster zu erkennen und zukünftige Zustandsänderungen von Ports vorherzusagen.

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Projektstruktur](#projektstruktur)
- [Konfiguration](#konfiguration)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)

## Installation

Um das Projekt zu nutzen, klone dieses Repository und installiere die benötigten Abhängigkeiten.

```bash
git clone https://github.com/kruemmel-python/AI-Port-Monitoring.git
cd AI-Port-Monitoring
pip install -r requirements.txt
```

### Abhängigkeiten

- `scikit-learn`
- `numpy`
- `psutil`
- `pyyaml`
- `joblib`

Diese Pakete können durch das Ausführen des folgenden Befehls installiert werden:

```bash
pip install -r requirements.txt
```

## Verwendung

1. **Konfigurationsdatei erstellen**: Erstelle eine `config.yaml` Datei oder benutze das bereitgestellte Skript `create_config_yaml.py`, um eine Beispiel-Konfiguration zu generieren.

```bash
python create_config_yaml.py
```

2. **Ports überwachen**: Starte das Überwachungsskript `monitor.py`, um die Ports zu überwachen.

```bash
python monitor.py
```

### Beispielkonfiguration (`config.yaml`):

```yaml
host: "192.168.178.57"
ports_to_monitor:
  - 80
  - 443
  - 8080
check_interval: 60
```

- **host**: IP-Adresse oder Hostname des zu überwachenden Systems.
- **ports_to_monitor**: Liste von Ports, die überwacht werden sollen.
- **check_interval**: Zeitintervall (in Sekunden) zwischen den Überprüfungen.

## Projektstruktur

```bash
├── monitor.py           # Hauptskript zur Portüberwachung
├── model.py             # Machine-Learning-Model für das Port-Monitoring
├── utils.py             # Hilfsfunktionen für Portüberprüfung und Logging
├── create_config_yaml.py# Skript zum Generieren der Konfigurationsdatei
├── config.yaml          # Beispiel-Konfigurationsdatei
├── requirements.txt     # Python-Abhängigkeiten
└── README.md            # Diese Datei
```

### Erklärung der wichtigsten Dateien:

- `monitor.py`: Das Hauptskript, das die Ports in regelmäßigen Abständen überwacht und den Status der Ports loggt. Es verwendet das Machine-Learning-Modell, um den Portstatus zu analysieren.
- `model.py`: Beinhaltet die Logik zur Erstellung, Aktualisierung und Speicherung des RandomForest-Klassifikators.
- `utils.py`: Enthält Hilfsfunktionen wie das Überprüfen von Ports, das Abrufen von Prozessen, die einen bestimmten Port verwenden, und das Logging.
- `create_config_yaml.py`: Ein einfaches Skript zur automatischen Erstellung einer Konfigurationsdatei.

## Mitwirken

Beiträge zu diesem Projekt sind willkommen! Um mitzuhelfen:

1. Forke das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/neue-funktion`)
3. Commite deine Änderungen (`git commit -m 'Füge neue Funktion hinzu'`)
4. Pushe auf den Branch (`git push origin feature/neue-funktion`)
5. Erstelle einen Pull-Request

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz – siehe die [LICENSE](LICENSE)-Datei für Details.

---

### Autor

**Ralf Krümmel**  
GitHub: [kruemmel-python](https://github.com/kruemmel-python)

