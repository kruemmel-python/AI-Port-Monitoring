# Python-Skript zum Generieren der YAML-Konfiguration für ports_to_monitor
with open('config.yaml', 'w') as file:
    file.write("host: \"192.168.178.57\"\n")
    file.write("ports_to_monitor:\n")
    for port in range(65536):
        file.write(f"  - {port}\n")
    file.write("check_interval: 60\n")
