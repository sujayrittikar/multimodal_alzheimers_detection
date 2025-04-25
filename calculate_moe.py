import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv('result_files/gpt4o_results_adni.csv')

accuracies = np.array(df["Accuracy"])
f1_scores = np.array(df["wf1"])

accuracy_mean, accuracy_margin_of_error = np.mean(accuracies), np.std(accuracies, ddof=1)
f1_mean, f1_margin_of_error = np.mean(f1_scores), np.std(f1_scores, ddof=1)

print("Accuracy:")
print(f"Mean: {accuracy_mean:.2f}, Margin of Error (95%) = {accuracy_margin_of_error:.2f}")

print("\nWeighted F1 Score:")
print(f"Mean: {f1_mean:.2f}, Margin of Error (95%) = {f1_margin_of_error:.2f}")
