import matplotlib.pyplot as plt
import numpy as np
#Leaky Integrate and Fire Model
V_rest = -65
V_th = -50
V_reset = -65
V_collections = []
V_collections.append(V_rest)
def leaky_integragte_and_fire_model(Vnew,t):
    #Using Euler's method
    I_t = 1.5
    tau = 10
    V_r = -65
    R = 10
    V = Vnew + (t/tau)*(-(Vnew - V_r) + (R*I_t))
    return V

print(f"{'Step':<6} {'Voltage (V)':<18} {'Spike?'}")
print("-" * 40)
for _ in range(1,11):
    V_new = leaky_integragte_and_fire_model(V_rest,_)
    V_rest = V_new
    V_collections.append(V_new)
    if V_new>=V_th:
        print("{:<6} {:<20.5f} {:<6}".format(_, V_new,"Yes"))
    else:
        print("{:<6} {:<20.5f} {:<6}".format(_, V_new,"No"))

t = np.linspace(0,10,11)
plt.plot(t,V_collections ,marker='o', linestyle='-', color='deeppink',linewidth=2.0)
plt.xlabel('Time in milliseconds')  
plt.ylabel('Voltage')  
plt.title('Leaky Integrate and Fire Model')
plt.grid(True)
plt.show()
