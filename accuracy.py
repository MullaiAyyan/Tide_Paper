import matplotlib.pyplot as plt

# Metrics and values (replace with your actual results if needed)
metrics = ["Overall Accuracy", "Kappa", "F1-score"]
values = [0.57, 0.14, 0.57]   # example values from your confusion matrix
errors = [0.05, 0.02, 0.03]   # approximate error bars

# Plot
plt.figure(figsize=(6,6))
bars = plt.bar(metrics, values, yerr=errors, color=['blue','orange','green'], capsize=5)

# Add labels on top of bars
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
             f"{val:.2f}", ha='center', fontsize=11, weight='bold')

plt.ylim(0,1)
plt.ylabel("Score")
plt.title("(a) Statistical Validation")
plt.savefig(r"C:\Users\Mulla\Downloads\Figure9a_Stats.png", dpi=300)
plt.show()
