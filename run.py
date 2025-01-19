import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# Circuit Simulation Functions
def simulate_three_phase_system(line_voltage, load_impedances, power_factors, load_types, frequency, time_period):
    """
    Simulate a three-phase power system with unbalanced loads.

    Parameters:
    - line_voltage: Line voltage (V)
    - load_impedances: Load impedances for each phase (Ohms)
    - power_factors: Power factors for each phase (cos(φ))
    - load_types: Load types for each phase ('resistive', 'inductive', 'capacitive')
    - frequency: Frequency of the system (Hz)
    - time_period: Total time for the simulation (s)

    Returns:
    - t: Time array
    - V_line: Line voltages (V)
    - I_line: Line currents (A)
    - V_phase: Phase voltages (V)
    - I_phase: Phase currents (A)
    - power_factors: Power factors for each phase
    - power_consumption: Power consumption for each phase
    """
    t = np.linspace(0, time_period, 1000)
    omega = 2 * np.pi * frequency

    V_line = np.array([
        line_voltage * np.sin(omega * t),
        line_voltage * np.sin(omega * t - 2 * np.pi / 3),
        line_voltage * np.sin(omega * t + 2 * np.pi / 3)
    ])

    V_phase = V_line / np.sqrt(3)

    I_phase = []
    power_factors_list = []
    power_consumption = []

    for i in range(3):
        phase_angle = np.arccos(power_factors[i])
        if load_types[i] == 'inductive':
            phase_angle = -phase_angle
        elif load_types[i] == 'capacitive':
            phase_angle = np.pi - phase_angle

        I_phase.append(V_phase[i] / load_impedances[i] * np.exp(1j * phase_angle))
        power_factors_list.append(power_factors[i])
        power_consumption.append(np.abs(V_phase[i]) * np.abs(I_phase[i]) * power_factors[i])

    I_phase = np.array(I_phase)
    I_line = I_phase

    return t, V_line, I_line, V_phase, I_phase, power_factors_list, power_consumption

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
    plt.plot(t, V_line[0].real, label='V_line1')
    plt.plot(t, V_line[1].real, label='V_line2')
    plt.plot(t, V_line[2].real, label='V_line3')
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.title('Line Voltages')
    plt.legend()
    plt.grid(True)

    # Plot Line Currents
    plt.subplot(2, 1, 2)
    plt.plot(t, I_line[0].real, label='I_line1')
    plt.plot(t, I_line[1].real, label='I_line2')
    plt.plot(t, I_line[2].real, label='I_line3')
    plt.xlabel('Time (s)')
    plt.ylabel('Current (A)')
    plt.title('Line Currents')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Graphical User Interface (GUI)
class AdvancedThreePhaseSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Three-Phase Power System Simulation")

        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=10, pady=10)

        # Line Voltage Input
        tk.Label(self.main_frame, text="Line Voltage (V):").grid(row=0, column=0, padx=5, pady=5)
        self.line_voltage_entry = tk.Entry(self.main_frame)
        self.line_voltage_entry.grid(row=0, column=1, padx=5, pady=5)

        # Frequency Input
        tk.Label(self.main_frame, text="Frequency (Hz):").grid(row=1, column=0, padx=5, pady=5)
        self.frequency_entry = tk.Entry(self.main_frame)
        self.frequency_entry.grid(row=1, column=1, padx=5, pady=5)

        # Simulation Time Input
        tk.Label(self.main_frame, text="Simulation Time (s):").grid(row=2, column=0, padx=5, pady=5)
        self.time_period_entry = tk.Entry(self.main_frame)
        self.time_period_entry.grid(row=2, column=1, padx=5, pady=5)

        # Load Parameters for Each Phase
        for i in range(3):
            phase_label = tk.Label(self.main_frame, text=f"Phase {i+1}:")
            phase_label.grid(row=3 + i * 3, column=0, padx=5, pady=5)

            tk.Label(self.main_frame, text="Load Impedance (Ω):").grid(row=3 + i * 3, column=1, padx=5, pady=5)
            entry = tk.Entry(self.main_frame)
            entry.grid(row=3 + i * 3, column=2, padx=5, pady=5)
            setattr(self, f'impedance_entry_{i}', entry)

            tk.Label(self.main_frame, text="Power Factor (cos(φ)):").grid(row=3 + i * 3 + 1, column=1, padx=5, pady=5)
            entry = tk.Entry(self.main_frame)
            entry.grid(row=3 + i * 3 + 1, column=2, padx=5, pady=5)
            setattr(self, f'power_factor_entry_{i}', entry)

            tk.Label(self.main_frame, text="Load Type:").grid(row=3 + i * 3 + 2, column=1, padx=5, pady=5)
            load_type = tk.StringVar(self.main_frame)
            load_type.set('resistive')
            dropdown = tk.OptionMenu(self.main_frame, load_type, 'resistive', 'inductive', 'capacitive')
            dropdown.grid(row=3 + i * 3 + 2, column=2, padx=5, pady=5)
            setattr(self, f'load_type_{i}', load_type)

        # Simulate Button
        simulate_button = tk.Button(self.main_frame, text="Simulate", command=self.simulate)
        simulate_button.grid(row=12, column=0, columnspan=3, pady=10)

    def simulate(self):
        try:
            line_voltage = float(self.line_voltage_entry.get())
            frequency = float(self.frequency_entry.get())
            time_period = float(self.time_period_entry.get())

            load_impedances = [float(getattr(self, f'impedance_entry_{i}').get()) for i in range(3)]
            power_factors = [float(getattr(self, f'power_factor_entry_{i}').get()) for i in range(3)]
            load_types = [getattr(self, f'load_type_{i}').get() for i in range(3)]

            t, V_line, I_line, V_phase, I_phase, power_factors, power_consumption = simulate_three_phase_system(
                line_voltage, load_impedances, power_factors, load_types, frequency, time_period
            )

            plot_waveforms(t, V_line, I_line, V_phase, I_phase)

            # Display Power Analysis
            power_analysis = f"Power Analysis:\n"
            for i in range(3):
                power_analysis += f"Phase {i+1} - Power Factor: {power_factors[i]:.2f}, Power Consumption: {power_consumption[i]:.2f} VA\n"
            messagebox.showinfo("Power Analysis", power_analysis)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedThreePhaseSystemApp(root)
    root.mainloop()