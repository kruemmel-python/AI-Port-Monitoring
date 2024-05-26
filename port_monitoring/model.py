import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
from utils import log_and_print

class PortModel:
    def __init__(self, model_path='port_model.pkl'):
        self.model_path = model_path
        if os.path.exists(self.model_path):
            self.model = load(self.model_path)
            log_and_print("Modell geladen und bereit für weiteres Training.")
        else:
            self.model = RandomForestClassifier(n_estimators=100)
            log_and_print("Neues Modell erstellt.")

    def update_model(self, data, labels):
        data_array = np.array(data)
        labels_array = np.array(labels)

        if len(data_array) > 1:
            train_data, test_data, train_labels, test_labels = train_test_split(data_array, labels_array, test_size=0.2)
            self.model.fit(train_data, train_labels)
            accuracy = self.model.score(test_data, test_labels)
            log_and_print(f"Modellgenauigkeit: {accuracy}")
            dump(self.model, self.model_path)
            log_and_print(f"Modell gespeichert unter: {self.model_path}")
