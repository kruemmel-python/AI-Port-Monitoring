import time
import yaml
from datetime import datetime
from utils import check_port, get_process_using_port, log_and_print
from model import PortModel

# Konfigurationsdatei laden
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

host_to_monitor = config['host']
ports_to_monitor = config['ports_to_monitor']
check_interval = config['check_interval']

def monitor_ports(host, ports, interval):
    port_model = PortModel()
    port_status = {}
    data = []
    labels = []

    while True:
        for port in ports:
            is_open = check_port(port, host)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if port not in port_status:
                port_status[port] = is_open
                log_and_print(f"{current_time}: Port {port} auf {host} ist {'offen' if is_open else 'geschlossen'}")
            elif port_status[port] != is_open:
                process_info = get_process_using_port(port) if is_open else None
                process_str = f" (genutzt von {process_info['name']} [PID: {process_info['pid']}])" if process_info else ""
                log_and_print(f"{current_time}: Statusänderung: Port {port} auf {host} ist {'offen' + process_str if is_open else 'geschlossen'}")
                port_status[port] = is_open

            data.append([port])
            labels.append(1 if is_open else 0)

        port_model.update_model(data, labels)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_ports(host_to_monitor, ports_to_monitor, check_interval)

