# Leaky Integrate-and-Fire (LIF) Neuron Simulation

## Overview

This project simulates a basic **Leaky Integrate-and-Fire (LIF)** neuron model using Euler's method. It computes the membrane potential of a neuron over discrete time steps and generates a line graph visualizing the potential over time.

## Model Description

The LIF model is a commonly used spiking neuron model in computational neuroscience. It integrates input current over time and fires a spike when the membrane potential crosses a threshold.

### Equation:

The membrane potential `V` is updated using the following discretized form of the LIF model:

```
V(t+1) = V(t) + (dt/tau) * (-(V(t) - V_rest) + R * I(t))
```

Where:

* `V_rest` = resting membrane potential
* `V_th` = spike threshold potential
* `V_reset` = reset potential after spike
* `R` = membrane resistance
* `tau` = membrane time constant
* `I(t)` = input current (assumed constant)
* `dt` = time step (in this case, implicitly taken as iteration count)

If `V(t)` exceeds `V_th`, a spike is said to have occurred.

## File Structure

* `LIF.py`: Contains the simulation logic and plotting code.
* Output: A matplotlib line plot showing the evolution of membrane potential over time.

## Simulation Parameters

* Resting potential (`V_rest`): -65 mV
* Threshold potential (`V_th`): -50 mV
* Reset potential (`V_reset`): -65 mV
* Resistance (`R`): 10 MΩ
* Time constant (`tau`): 10 ms
* Input current (`I_t`): 1.5 nA
* Simulation duration: 10 steps (with 11 time points)

## Output

The program prints a step-wise update of the membrane potential and indicates whether a spike occurred. It also generates a line plot of voltage versus time.

## Plot Details

* **X-axis**: Time in milliseconds
* **Y-axis**: Membrane potential in millivolts (mV)
* **Color**: Deep pink
* **Markers**: Circular markers at each time step

## Requirements

* Python 3.x
* NumPy
* Matplotlib

## How to Run

1. Ensure you have Python and required packages installed:

   ```bash
   pip install numpy matplotlib
   ```
2. Run the script:

   ```bash
   python LIF.py
   ```

## License

This project is for educational and academic purposes.

## Author

Nippani Meghana

---

For inquiries or suggestions, feel free to reach out.
