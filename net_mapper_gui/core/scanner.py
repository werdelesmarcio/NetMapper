import tkinter as tk
import socket
from net_mapper_gui.core.helpers import get_service_name, grab_banner



def scan_ports(target, initial_port, final_port, output_widget, progress_bar, status_label, total_ports):
    for count, port in enumerate(range(initial_port, final_port + 1), 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))

            # Somente exibe a porta se estiver aberta (result == 0)
            if result == 0:
                service = get_service_name(port, "tcp")
                banner = grab_banner(target, port)
                output_widget.insert(
                    tk.END,
                    f"Port {port} open - Service: {service} - Name: {banner}\n"
                )
                output_widget.update_idletasks()

        # Atualiza a barra de progresso e o rótulo com a porcentagem
        progress_bar["value"] = count
        progress_bar.update_idletasks()
        percent_complete = (count / total_ports) * 100
        status_label.config(text=f"Progress: {percent_complete:.0f}%")
        status_label.update_idletasks()


def scan_udp_ports(target, initial_port, final_port, output_widget, progress_bar, status_label, total_ports):
    for count, port in enumerate(range(initial_port, final_port + 1), 1):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))

            if result == 0:
                service = get_service_name(port, "udp")
                banner = grab_banner(target, port)
                output_widget.insert(
                    tk.END,
                    f"Port {port} open - Service: {service} - Name: {banner}\n"
                )
                output_widget.update_idletasks()

        # Atualiza a barra de progresso e o rótulo com a porcentagem
        progress_bar["value"] = count
        progress_bar.update_idletasks()
        percent_complete = (count / total_ports) * 100
        status_label.config(text=f"Progress: {percent_complete:.0f}%")
        status_label.update_idletasks()
