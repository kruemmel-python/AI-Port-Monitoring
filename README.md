# Modell für Hafenüberwachung und Klassifizierung

## Überblick
Dieses Repository enthält ein Python-Skript zur Überwachung von Netzwerk-Ports auf einem entfernten Host und zum Trainieren eines maschinellen Lernmodells zur Klassifizierung des Status dieser Ports. Das verwendete Modell ist ein `RandomForestClassifier` aus `sklearn`.

## Merkmale
- Überwacht den Status bestimmter Netzwerk-Ports auf einem Remote-Host.
- Protokollierung von Änderungen des Portstatus und der Prozesse, die diese Ports benutzen.
- Trainieren und Aktualisieren eines maschinellen Lernmodells basierend auf den gesammelten Daten.
- Speichern und Laden des trainierten Modells zur späteren Verwendung.

## Anforderungen
- Python 3.x
- `numpy`
- `scikit-learn`
- `psutil`
- `joblib`
- `pyyaml`

## Installation
Installieren Sie die benötigten Pakete mit pip:
``sh
pip install -r anforderungen.txt

Übersetzt mit DeepL.com (kostenlose Version)





# Port Monitoring and Classification Model

## Overview
This repository contains a Python script for monitoring network ports on a remote host and training a machine learning model to classify the status of these ports. The model used is a `RandomForestClassifier` from `sklearn`.

## Features
- Monitor the status of specified network ports on a remote host.
- Log changes in port status and the processes using those ports.
- Train and update a machine learning model based on the collected data.
- Save and load the trained model for future use.

## Requirements
- Python 3.x
- `numpy`
- `scikit-learn`
- `psutil`
- `joblib`
- `pyyaml`

## Installation
Install the required packages using pip:
```sh
pip install -r requirements.txt
