import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Circuit Simulation Functions
def simulate_three_phase_system(line_voltage, load_impedance, power_factor, frequency, time_period):
    """
    Simulate a three-phase power system.

    Parameters:
    - line_voltage: Line voltage (V)
    - load_impedance: Load impedance (Ohms)
    - power_factor: Power factor (cos(φ))
    - frequency: Frequency of the system (Hz)
    - time_period: Total time for the simulation (s)

    Returns:
    - t: Time array
    - V_line: Line voltages (V)
    - I_line: Line currents (A)
    - V_phase: Phase voltages (V)
    - I_phase: Phase currents (A)
    """
    t = np.linspace(0, time_period, 1000)
    omega = 2 * np.pi * frequency
    phase_angle = np.arccos(power_factor)

    V_line = np.array([
        line_voltage * np.sin(omega * t),
        line_voltage * np.sin(omega * t - 2 * np.pi / 3),
        line_voltage * np.sin(omega * t + 2 * np.pi / 3)
    ])

    V_phase = V_line / np.sqrt(3)

    I_phase = V_phase / load_impedance
    I_line = I_phase

    return t, V_line, I_line, V_phase, I_phase

# Data Visualization Functions
def plot_waveforms(t, V_line, I_line, V_phase, I_phase):
    """
    Plot the waveforms of the line and phase voltages and currents.

    Parameters:
    - t: Time array
    - V_line: Line voltages (V)
    - I_line: Line currents (A)
    - V_phase: Phase voltages (V)
    - I_phase: Phase currents (A)
    """
    plt.figure(figsize=(14, 10))

    # Plot Line Voltages
    plt.subplot(2, 1, 1)
    plt.plot(t, V_line[0], label='V_line1')
    plt.plot(t, V_line[1], label='V_line2')
    plt.plot(t, V_line[2], label='V_line3')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title('Line Voltages')
    plt.legend()
    plt.grid(True)

    # Plot Line Currents
    plt.subplot(2, 1, 2)
    plt.plot(t, I_line[0], label='I_line1')
    plt.plot(t, I_line[1], label='I_line2')
    plt.plot(t, I_line[2], label='I_line3')
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.title('Line Currents')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Graphical User Interface (GUI)
class ThreePhaseSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Three-Phase Power System Simulation")

        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        # Line Voltage Input
        tk.Label(self.main_frame, text="Line Voltage (V):").grid(row=0, column=0, padx=5, pady=5)
        self.line_voltage_entry = tk.Entry(self.main_frame)
        self.line_voltage_entry.grid(row=0, column=1, padx=5, pady=5)

        # Load Impedance Input
        tk.Label(self.main_frame, text="Load Impedance (Ω):").grid(row=1, column=0, padx=5, pady=5)
        self.load_impedance_entry = tk.Entry(self.main_frame)
        self.load_impedance_entry.grid(row=1, column=1, padx=5, pady=5)

        # Power Factor Input
        tk.Label(self.main_frame, text="Power Factor (cos(φ)):").grid(row=2, column=0, padx=5, pady=5)
        self.power_factor_entry = tk.Entry(self.main_frame)
        self.power_factor_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frequency Input
        tk.Label(self.main_frame, text="Frequency (Hz):").grid(row=3, column=0, padx=5, pady=5)
        self.frequency_entry = tk.Entry(self.main_frame)
        self.frequency_entry.grid(row=3, column=1, padx=5, pady=5)

        # Simulation Time Input
        tk.Label(self.main_frame, text="Simulation Time (s):").grid(row=4, column=0, padx=5, pady=5)
        self.time_period_entry = tk.Entry(self.main_frame)
        self.time_period_entry.grid(row=4, column=1, padx=5, pady=5)

        # Simulate Button
        simulate_button = tk.Button(self.main_frame, text="Simulate", command=self.simulate)
        simulate_button.grid(row=5, column=0, columnspan=2, pady=10)

    def simulate(self):
        try:
            line_voltage = float(self.line_voltage_entry.get())
            load_impedance = float(self.load_impedance_entry.get())
            power_factor = float(self.power_factor_entry.get())
            frequency = float(self.frequency_entry.get())
            time_period = float(self.time_period_entry.get())

            t, V_line, I_line, V_phase, I_phase = simulate_three_phase_system(line_voltage, load_impedance, power_factor, frequency, time_period)
            plot_waveforms(t, V_line, I_line, V_phase, I_phase)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ThreePhaseSystemApp(root)
    root.mainloop()