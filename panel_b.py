import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load your thematic map (replace filename with the one you saved)
agreement = mpimg.imread(r"C:\Users\Mulla\Downloads\MSI_Cuddalore.png")

# Plot with title and annotations
plt.figure(figsize=(8,6))
plt.imshow(agreement)
plt.axis('off')
plt.title("(b) Pontius/Fuzzy Kappa Agreement")

# Place text below the image (outside axes)
plt.figtext(0.15, -0.05, "Allocation Disagreement: 3.2%", color='orange', fontsize=12, weight='bold')
plt.figtext(0.15, -0.10, "Quantity Disagreement: 1.6%", color='red', fontsize=12, weight='bold')

# Save the labeled panel
plt.savefig(r"C:\Users\Mulla\Downloads\Figure9b_SpatialAgreement_labeled.png", dpi=500)
plt.show()
