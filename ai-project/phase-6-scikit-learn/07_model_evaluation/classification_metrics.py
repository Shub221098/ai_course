# Classification Metrics in Scikit-learn : Confusion Matrix, Accuracy, Precision, Recall, F1, ROC-AUC

# Metrics Definitions:
# Accuracy  = (TP + TN) / (TP + TN + FP + FN)
# Precision = TP / (TP + FP)
# Recall    = TP / (TP + FN)
# F1-Score  = 2 * (Precision * Recall) / (Precision + Recall)

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report
)

actual = [1, 1, 0, 0, 1, 0, 1, 0]
predicted = [1, 0, 0, 1, 1, 0, 1, 0]
pred_probs = [0.9, 0.4, 0.2, 0.7, 0.85, 0.15, 0.95, 0.1]

cm = confusion_matrix(actual, predicted)
accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f1 = f1_score(actual, predicted)
roc_auc = roc_auc_score(actual, pred_probs)

print("--- Confusion Matrix ---")
print(cm)

print("\n--- Classification Metrics ---")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")

print("\n--- Comprehensive Classification Report ---")
print(classification_report(actual, predicted, target_names=["Class 0", "Class 1"]))

