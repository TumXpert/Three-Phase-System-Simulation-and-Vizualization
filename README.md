# Three-Phase Power System Simulation

This project is a Python-based application that simulates and visualizes a three-phase power system. It includes a graphical user interface (GUI) built with Tkinter and interactive data visualization using Plotly. The application is designed for educational purposes, allowing users to understand the behavior of three-phase systems by simulating their voltage and current waveforms.

 Features

1. Three-Phase Simulation: Simulates line and phase voltages and currents based on user inputs for parameters such as line voltage, load impedance, power factor, and frequency.
2. Interactive GUI: An easy-to-use interface for entering parameters and running simulations.
3. Unit Selection: Dropdown menus for selecting units (e.g., volts or kilovolts, ohms or kilo-ohms).
4. Interactive Plots: Generates interactive waveforms for line and phase voltages and currents using Plotly.
5. Save Results: Allows saving simulation results to a CSV file for further analysis.
6. Error Handling: Provides user-friendly error messages for invalid inputs or actions.

 Requirements

- Python 3.7+
- Required libraries:
  - `numpy`
  - `pandas`
  - `plotly`
  - `tkinter`

 Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd three_phase_simulation
   ```

3. Install the required dependencies:
   ```bash
   pip install numpy pandas plotly
   ```

 Usage

1. Run the application:
   ```bash
   python three_phase_simulation_gui.py
   ```

2. Use the GUI to input the following parameters:
   - Line Voltage: Voltage between two phases (with unit selection: V or kV).
   - Load Impedance: Impedance of the load (with unit selection: Ω or kΩ).
   - Power Factor: Power factor of the system (cosine of the phase angle).
   - Frequency: Frequency of the system in Hz.
   - Simulation Time: Total time for the simulation in seconds.

3. Click the Simulate button to generate the waveforms.

4. To save the results, click the Save Results button and choose a file location.

 File Structure

- `three_phase_simulation_gui.py`: Main script containing the simulation logic and GUI code.

 Example

1. Input parameters:
   - Line Voltage: `400 V`
   - Load Impedance: `50 Ω`
   - Power Factor: `0.8`
   - Frequency: `50 Hz`
   - Simulation Time: `0.02 s`

2. Click Simulate to generate waveforms.

3. Click Save Results to export data as a CSV file.

 Acknowledgments

This project uses the following libraries:
- [NumPy](https://numpy.org) for numerical computations.
- [Pandas](https://pandas.pydata.org) for data manipulation and storage.
- [Plotly](https://plotly.com/python/) for interactive plotting.

License

This project is licensed under the MIT License.


# Three-Phase Power System Simulation

This project is a Python-based application that simulates and visualizes a three-phase power system. It includes a graphical user interface (GUI) built with Tkinter and data visualization using Matplotlib. The application is designed for educational purposes, allowing users to understand the behavior of three-phase systems by simulating their voltage and current waveforms.

 Features

1. Three-Phase Simulation: Simulates line and phase voltages and currents based on user inputs for parameters such as line voltage, load impedance, power factor, and frequency.
2. Interactive GUI: An easy-to-use interface for entering parameters and running simulations.
3. Real-Time Visualization: Generates waveforms for line and phase voltages and currents using Matplotlib.
4. Power Analysis: Calculates and displays power factors and power consumption for each phase.
5. Error Handling: Provides user-friendly error messages for invalid inputs or actions.

 Requirements

- Python 3.7+
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `tkinter`

 Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd three_phase_simulation
   ```

3. Install the required dependencies:
   ```bash
   pip install numpy matplotlib
   ```

 Usage

1. Run the application:
   ```bash
   python three_phase_simulation_gui.py
   ```

2. Use the GUI to input the following parameters:
   - Line Voltage: Voltage between two phases (in volts).
   - Load Impedance: Impedance of the load (in ohms).
   - Power Factor: Power factor of the system (cosine of the phase angle).
   - Frequency: Frequency of the system in Hz.
   - Simulation Time: Total time for the simulation in seconds.

3. Click the Simulate button to generate the waveforms.

4. View the results and power analysis in the GUI and graphical plots.

 File Structure

- `three_phase_simulation_gui.py`: Main script containing the simulation logic and GUI code.

 Example

1. Input parameters:
   - Line Voltage: `400 V`
   - Load Impedance: `50 Ω`
   - Power Factor: `0.8`
   - Frequency: `50 Hz`
   - Simulation Time: `0.02 s`

2. Click Simulate to generate waveforms.

3. View power analysis and plots of voltages and currents.

 Acknowledgments

This project uses the following libraries:
- [NumPy](https://numpy.org) for numerical computations.
- [Matplotlib](https://matplotlib.org) for plotting waveforms.

 License

This project is licensed under the MIT License.

