
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from qiskit.quantum_info import Statevector
from qiskit.circuit.library import RYGate

# Function for finding orthonoal vector of a given vector
def ortho(vector):
  return np.array([np.conj(vector[1]), -np.conj(vector[0])])

# Define computation basis vectors
zero_ket = np.array([1, 0])
one_ket = np.array([0, 1])

# Define signla states (only psi_1 outside loop) 
psi_1 = zero_ket


# Variable initialization
theta_skr_b92_neg = 0
theta_100 = 0
theta_s = np.linspace(0,0.999999*np.pi/2,10000)
coverage_s = np.zeros_like(theta_s)
opt_phi_s = np.zeros_like(theta_s)
h_skr_s = np.zeros_like(theta_s)
skr_b92_s = np.zeros_like(theta_s)
difference_s = np.zeros_like(theta_s)
improvement_s = np.zeros_like(theta_s)
remaining_phiQKD_bit_s = np.zeros_like(theta_s)
remaining_b92_bit_s = np.zeros_like(theta_s)

# Start loop for all possible theta between range
for i,v in enumerate(theta_s):
  # Overlap angle theta
  theta = v       

  # Define second signal state (psi_2)
  psi_2 = Statevector([1, 0]).evolve(RYGate(theta * 2)).data
  
  phi_helstrom = (np.pi / 2 - theta) / 2

  phi = np.linspace(0.000001, phi_helstrom, 10000)

  # Numerical probabilities of correct(P_s), incorrect(P_e) and inconclusive(P_q) events 
  P_s = (np.sin(theta + phi)**2) / (1 + np.cos(theta + 2*phi))
  P_e = (np.sin(phi)**2) / (1 + np.cos(theta + 2*phi))
  P_q = ((np.cos(theta + 2*phi)) * (np.cos(phi) + np.cos(theta + phi))**2) / ((1 + np.cos(theta + 2*phi))**2)

  # Calculate asymptotic key rate (akr)

  eta = 1 - P_q
  Q = P_e / eta
  h_xy = -Q * np.log2(Q) - (1-Q) * np.log2(1-Q)
  c = (psi_1.conj().T @ psi_2).real**2
  h_xe = np.log2(1/c) - h_xy
  akr = eta * (h_xe - h_xy)

  # Calculate delta from Hoeffding's inequality

  n = 10**5           # Sample qubits for paramete estimation
  N = 10**6           # Total number of qubits
  eps_pe = 10**(-10)  # Failure probabilty of parameter estimation
  delta = np.sqrt(np.log(2/eps_pe)/(2*n))

  # Calculate finite key rate (fkr)

  Q_w = Q + delta
  h_q_w = -Q_w * np.log2(Q_w) - (1-Q_w) * np.log2(1-Q_w)
  # fkr = (eta) * (np.log2(c) - 2*h_q_w)
  fkr = (eta-(n/N)) * (np.log2(c) - 2*h_q_w)


  psi_1_ortho = ortho(psi_1)
  psi_2_ortho = ortho(psi_2)
  numerator = ((psi_1_ortho.conj().T @ psi_2)**2 + (psi_2_ortho.conj().T @ psi_1)**2)
  ps = numerator/(2*(1+np.abs(psi_2.conj().T @ psi_1)))
  ps = ps.real.round(6)
  
  # Calculate Qworst
  Q_w = (P_e / eta) + 0.01089
  # set parameter values
  eps_sec = 10**(-10)
  eps_cor = 10**(-10)
  # Calculate composable secure key rate
  h_Q = -Q_w * np.log2(Q_w) - (1-Q_w) * np.log2(1-Q_w)
  skr = (eta-(n/N)) * (np.log2(1/c) - (2.15)*h_Q) - np.log2(2/(eps_sec**2)*eps_cor)/N

  Q_bw = delta
  h_q_bw = -Q_bw * np.log2(Q_bw) - (1-Q_bw) * np.log2(1-Q_bw)
  skr_b92 = (ps-n/N) * (np.log2(1/c) - 2.15*h_q_bw) - np.log2(2/(eps_sec**2)*eps_cor)/N
  skr_b92_s[i] = skr_b92


  opt_phi_s[i] = phi[np.argmax(skr)]
  
  h_skr_s[i] = np.max(skr)

  difference_s[i] = skr[np.argmax(skr)]-skr_b92
  
  improvement_s[i] = ((skr[np.argmax(skr)]-skr_b92)*100)/(skr_b92)

  phi_bound = 0
  for (j,k) in enumerate(skr):
    if k > skr_b92 and k > 0:
      phi_bound = phi[j]
  phi_1 = 0
  coverage = phi_bound*100/phi_helstrom
  coverage_s[i] = coverage

  remaining_phiQKD_bit_s[i] = eta[np.argmax(skr)]*N - n
  remaining_b92_bit_s[i] = ps*N - n

  if coverage < 99.999999:
    theta_100 = v # The value of theta for which the coverage becomes 100 and stay constant

  if skr_b92 < 0:
    theta_skr_b92_neg = v # The value of theta for which the key rate of b92 becomes negative

df = pd.DataFrame({"phi_optimal": opt_phi_s, "highest_key_rate": h_skr_s, "b92_key_rate": skr_b92_s, "improvement": improvement_s,'coverage': coverage_s, "difference": difference_s, "remaining_phiQKD_bits": remaining_phiQKD_bit_s, "remaining_b92_bits": remaining_b92_bit_s}, index=pd.Index(theta_s,name='theta'))
df.to_csv("./percentages.csv")

print(f'theta_skr_b92_neg = {theta_skr_b92_neg}')
print(f'theta_coverage_100 = {theta_100}')