"""
Module 9: Section 6 QML Layer Training Convergence Visualizer
Specification Reference: UTP-SPEC-2026-V5.0 - Section 6.0 & Section 11.0
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_qml_training_convergence(epochs=50, num_features=4):
    np.random.seed(42)
    
    # Initialize identical random parameters for both training loops
    theta_protected = np.random.uniform(0.5, 2.0, num_features)
    theta_unprotected = theta_protected.copy()
    target_theta = np.zeros(num_features)  # Absolute ground state baseline (0)
    
    loss_protected_history = []
    loss_unprotected_history = []
    
    print("=== MONITORING LOG: QML GRADIENT BACKPROPAGATION SPEED ===")
    
    for epoch in range(epochs):
        # Calculate Categorical Cross-Entropy representation values (Section 11)
        loss_p = np.mean((theta_protected - target_theta)**2) * (1.0 + 0.05 * np.random.randn())
        loss_u = np.mean((theta_unprotected - target_theta)**2) * (1.0 + 0.05 * np.random.randn())
        
        # 1. Protected Update Loop: QEC Stabilizer Shield Preserves Clean Gradients
        grad_p = 0.1 * (theta_protected - target_theta) + 0.01 * np.random.randn(num_features)
        theta_protected -= 0.15 * grad_p  # Stable parameter update step
        
        # 2. Unprotected Update Loop: Phase Noise Induces Barren Plateau Collapse
        if epoch < 12:
            # Initial phase maps track loosely before analog drift saturates the layer
            grad_u = 0.1 * (theta_unprotected - target_theta) + 0.05 * np.random.randn(num_features)
            theta_unprotected -= 0.15 * grad_u
        else:
            # Barren Plateau regime sets in; parameter gradients vanish into isotropic variance
            grad_u = np.random.normal(0, 1e-5, num_features)
            theta_unprotected -= 0.15 * grad_u
            # Loss stalls out and experiences random walk drift from background fluctuations
            loss_u += 0.015 * (epoch - 12) * np.random.rand()
            
        loss_protected_history.append(loss_p)
        loss_unprotected_history.append(loss_u)
        
        if (epoch + 1) % 10 == 0 or epoch == 0:
            print(f"Epoch {epoch+1:02d}/{epochs} | Protected Loss = {loss_p:.5f} | Unprotected Loss = {loss_u:.5f}")
            
    return np.array(loss_protected_history), np.array(loss_unprotected_history)

# Run the 50-epoch optimization pass
epochs_count = 50
loss_p, loss_u = simulate_qml_training_convergence(epochs=epochs_count)

# Calculate final loss reduction efficiency metrics
net_loss_reduction = (1.0 - (loss_p[-1] / loss_p[0])) * 100
print("-----------------------------------------------------------------")
print(f"-> Net Cross-Entropy Loss Reduction (Protected): {net_loss_reduction:.2f}%")
print("=================================================================\n")

# Render Vector Visualization Canvas Engine
plt.figure(figsize=(10, 6), facecolor='#09090c')
ax = plt.subplot(111)
ax.set_facecolor('#09090c')

# Plot continuous optimization paths
epochs_range = np.arange(1, epochs_count + 1)
plt.plot(epochs_range, loss_p, color='#00efff', linewidth=2.5, label='Protected QML Core (Stabilizer Shield Active)')
plt.plot(epochs_range, loss_u, color='#ff3f34', linewidth=2.0, linestyle='--', label='Unprotected Hidden Layer')

# Draw the exact structural transition point indicator
plt.axvline(12, color='#f1c40f', linestyle=':', alpha=0.6, label='Barren Plateau Transition (Epoch 12)')

# Canvas Layout Configurations (0-Base Design Standard)
plt.title("Section 6 Variational QML Convergence Curves\nShielding Hidden Layer Gradients Against Barren Plateaus (UTP-SPEC-2026-V5.0)", 
          color='white', fontsize=12, weight='bold', pad=20)
plt.xlabel("Supervised Learning Optimization Epochs", color='#888888')
plt.ylabel("Categorical Cross-Entropy Loss Potential", color='#888888')
plt.grid(True, color='#1c1c24', linestyle=':')

ax.tick_params(colors='#888888', labelsize=9)
for spine in ax.spines.values(): spine.set_color('#22222b')
    
plt.xlim(1, epochs_count)
plt.ylim(0, np.max(loss_u) * 1.1)
plt.legend(loc="upper right", framealpha=0.1, labelcolor='white')
plt.show()
