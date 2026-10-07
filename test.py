import matplotlib.pyplot as plt

def draw_beam(L, loads):
    """Draw the beam, supports, and loads."""
    
    fig, ax = plt.subplots(figsize=(10, 3))
    
    # --- 1. THE BEAM (horizontal line) ---
    ax.plot([0, L], [0, 0], 'k-', linewidth=4, zorder=2)
    
    # --- 2. THE SUPPORTS (triangles) ---
    ax.plot(0, 0, marker='^', color='green', markersize=18, zorder=3)
    ax.plot(L, 0, marker='^', color='green', markersize=18, zorder=3)
    ax.text(0, -0.6, 'A', ha='center', fontsize=12, fontweight='bold')
    ax.text(L, -0.6, 'B', ha='center', fontsize=12, fontweight='bold')
    
    # --- 3. THE LOADS ---
    for load in loads:
        
        # POINT LOAD (P)
        if load["type"] == "P":
            a = load["distance"]
            P = load["intensity"]
            
            # Arrow pointing down onto the beam
            ax.annotate('', xy=(a, 0), xytext=(a, 2),
                        arrowprops=dict(arrowstyle='->', color='red', lw=2.5))
            
            # Label above the arrow
            ax.text(a, 2.1, f'{P} kN', ha='center', color='red',
                    fontsize=11, fontweight='bold')
        
        # DISTRIBUTED LOAD (W)
        elif load["type"] == "W":
            start = load["start"]
            end = load["end"]
            w = load["intensity"]
            
            # Draw 6 arrows evenly spaced across the UDL region
            num_arrows = 6
            for i in range(num_arrows):
                x = start + (end - start) * i / (num_arrows - 1)
                ax.annotate('', xy=(x, 0), xytext=(x, 1.5),
                            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
            
            # Draw a horizontal line connecting the tops of the arrows
            ax.plot([start, end], [1.5, 1.5], 'b-', linewidth=1.5)
            
            # Label above
            ax.text((start + end) / 2, 1.7, f'{w} kN/m', ha='center',
                    color='blue', fontsize=11, fontweight='bold')
    
    # --- 4. CLEAN UP THE PLOT ---
    ax.set_xlim(-1, L + 1)
    ax.set_ylim(-1, 3)
    ax.set_xlabel('Position (m)', fontsize=11)
    ax.set_yticks([])                        # Hide the y-axis numbers
    ax.set_title('Beam Loading Diagram', fontsize=13, fontweight='bold')
    ax.grid(axis='x', linestyle='--', alpha=0.4)  # Faint vertical grid lines
    
    plt.tight_layout()
    plt.show()


# ==========================================
# RUN IT
# ==========================================

L = 10.0

loads = [
    {"type": "P", "intensity": 50.0, "distance": 3.0},
    {"type": "P", "intensity": 30.0, "distance": 7.0},
    {"type": "W", "intensity": 15.0, "start": 5.0, "end": 8.0},
]

draw_beam(L, loads)