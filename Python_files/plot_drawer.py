
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# counts = {'10': 703, '00': 297}
# phi_s = np.linspace(0,np.pi/8,1000)
# ps = np.zeros_like(phi_s)
# pe = np.zeros_like(phi_s)
# pq = np.zeros_like(phi_s)
# # print(asd)
# for i,v in enumerate(phi_s):
#     ps[i] = v + 1
#     pe[i] = v + 2
#     pq[i] = v + 3
# df = pd.DataFrame({"Ps":ps, "Pe":pe, "Pq":pq}, index=pd.Index(phi_s,name='phi'))
# df.to_csv("./Probabilities.csv")

df = pd.read_csv("./Percentages.csv", index_col='theta')
# print(df['b92_key_rate']>0)
# df = df.loc[df['b92_key_rate']>0.01]
# df = df.loc[df['highest_key_rate']>0]
df1 = df.loc[df['remaining_phiQKD_bits']>2100]
print(df1.index[0])
df2 = df.loc[df['remaining_b92_bits']>7379]
# df2 = df.loc[df['remaining_b92_bits']>339]
print(df2.index[0])
max_iddx = np.argmax(df2['difference'])
print(f"Highest difference = {df2['difference'].iloc[max_iddx]:.6f} at theta = {df2.index[max_iddx]:.6f}")
max_idix = np.argmax(df2['improvement'])
print(f"Highest improvement = {df2['improvement'].iloc[max_idix]:.6f} at theta = {df2.index[max_idix]:.6f}")

# Plot phi_optimal vs theta
plt.figure()
plt.plot(df1['phi_optimal'])
max_idx = np.argmax(df['phi_optimal'])
max_phi = df['phi_optimal'].iloc[max_idx]
print(f'Maximum value of phi_opt = {max_phi}')
plt.xlabel(r'Overlap angle, $\Theta~(rad)$')
plt.ylabel(r'Optimal tilting angle, $\phi_{OPT}~(rad)$')
# plt.title(r'$\phi_{OPT}$ vs $\Theta$')
plt.grid(True)
plt.savefig('phi_optimal_vs_theta.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot coverage vs theta
plt.figure()
plt.plot(df2['coverage'], color='red')
plt.xlabel(r'Overlap angle, $\Theta~(rad)$')
plt.ylabel('Coverage (%)')
# plt.title(r'Coverage vs $\Theta$')
plt.grid(True)
plt.savefig('percentage_vs_theta.png', dpi=300, bbox_inches='tight')
plt.show()


# Plot composable secure rates in phiQKD and B92 vs theta
plt.figure()
plt.plot(df1['highest_key_rate'], color='royalblue', label='Highest secure key rate in phiQKD protocol')
plt.plot(df2['b92_key_rate'], color='crimson', label='Highest secure key rate in B92 protocol')
# plt.plot(df[['highest_key_rate','b92_key_rate']])
plt.xlabel(r'Overlap angle, $\Theta~(rad)$')
plt.ylabel(r'Secure key rates')
# plt.title(r'Secure key rates vs $\Theta$')
plt.legend()
plt.grid(True)
plt.savefig('skr_vs_theta.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot difference vs theta
plt.figure()
plt.plot(df2['difference'], color='red')
plt.xlabel(r'Overlap angle, $\Theta~(rad)$')
plt.ylabel('Difference')
# plt.title(r'Difference vs $\Theta$')
plt.grid(True)
plt.savefig('difference_vs_theta.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot improvement vs theta
plt.figure()
plt.plot(df2['improvement'], color='green')
plt.xlabel(r'Overlap angle, $\Theta~(rad)$')
plt.ylabel('Improvement in secure key rate (%)')
# plt.title(r'Improvement vs $\Theta$')
plt.grid(True)
plt.savefig('Improvement_vs_theta.png', dpi=300, bbox_inches='tight')
plt.show()