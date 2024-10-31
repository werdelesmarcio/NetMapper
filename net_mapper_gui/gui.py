from net_mapper_gui.core.scanner import scan_ports, scan_udp_ports
import tkinter as tk
from tkinter import ttk, scrolledtext


class PortScannerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Port Scanner")
        self.root.geometry("600x600")
        self.root.configure(bg="#2e2e2e")
        self.create_styles()
        self.create_widgets()

    def create_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background="#2e2e2e")
        style.configure("TLabel", background="#2e2e2e", foreground="#ffffff", font=("Arial", 10))
        style.configure("TEntry", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10, "bold"), foreground="#ffffff", background="#007acc")
        style.map("TButton", background=[("active", "#005f8c")])
        style.configure("TProgressbar", thickness=10, troughcolor="#404040", background="#4CAF50")

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        title_label = ttk.Label(main_frame, text="Port Scanner Tool", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Label(main_frame, text="Target (IP or Hostname):").grid(row=1, column=0, sticky="w", pady=2)
        self.target_entry = ttk.Entry(main_frame)
        self.target_entry.grid(row=1, column=1, sticky="we", pady=2)

        ttk.Label(main_frame, text="Initial Port:").grid(row=2, column=0, sticky="w", pady=2)
        self.initial_port_entry = ttk.Entry(main_frame)
        self.initial_port_entry.grid(row=2, column=1, sticky="we", pady=2)

        ttk.Label(main_frame, text="Final Port:").grid(row=3, column=0, sticky="w", pady=2)
        self.final_port_entry = ttk.Entry(main_frame)
        self.final_port_entry.grid(row=3, column=1, sticky="we", pady=2)

        ttk.Label(main_frame, text="Protocol:").grid(row=4, column=0, sticky="w", pady=2)
        self.protocol_choice = ttk.Combobox(main_frame, values=["TCP", "UDP"], state="readonly")
        self.protocol_choice.grid(row=4, column=1, sticky="we", pady=2)
        self.protocol_choice.set("TCP")

        scan_button = ttk.Button(main_frame, text="Start Scan", command=self.start_scan)
        scan_button.grid(row=5, column=1, sticky="we", pady=10)

        self.results_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=60, height=15, font=("Arial", 9), bg="#1c1c1c", fg="#ffffff")
        self.results_text.grid(row=6, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

        self.status_bar = ttk.LabelFrame(self.root, text="Status", padding="5 5 5 5", style="TFrame")
        self.status_bar.grid(row=1, column=0, sticky="we", padx=10, pady=(5, 10))

        self.progress_bar = ttk.Progressbar(self.status_bar, orient="horizontal", mode="determinate")
        self.progress_bar.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        self.status_label = ttk.Label(self.status_bar, text="Progress: 0%")
        self.status_label.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        main_frame.columnconfigure(1, weight=1)
        self.status_bar.columnconfigure(0, weight=1)

    def start_scan(self):
        target = self.target_entry.get()
        initial_port = int(self.initial_port_entry.get())
        final_port = int(self.final_port_entry.get())
        protocol = self.protocol_choice.get()

        total_ports = final_port - initial_port + 1
        self.progress_bar["maximum"] = total_ports
        self.progress_bar["value"] = 0
        self.status_label.config(text="Progress: 0%")

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Scanning {protocol} ports on {target}...\n")

        if protocol == "TCP":
            scan_ports(target, initial_port, final_port, self.results_text, self.progress_bar, self.status_label, total_ports, self.on_scan_complete)
        elif protocol == "UDP":
            scan_udp_ports(target, initial_port, final_port, self.results_text, self.progress_bar, self.status_label, total_ports, self.on_scan_complete)

    def on_scan_complete(self):
        self.progress_bar["value"] = self.progress_bar["maximum"]
        self.status_label.config(text="Progress: 100%.")
        self.results_text.insert(tk.END, "\nScanner concluído com sucesso.\n")


    def run(self):
        self.root.mainloop()
