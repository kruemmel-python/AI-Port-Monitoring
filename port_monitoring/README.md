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
