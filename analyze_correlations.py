import pandas as pd
import numpy as np

# Load data
print("Loading data...")
trans_df = pd.read_csv('dataset/train_transaction.csv', nrows=10000)
ident_df = pd.read_csv('dataset/train_identity.csv', nrows=10000)

# Merge datasets
df = pd.merge(trans_df, ident_df, on='TransactionID', how='left')

print(f"Dataset shape: {df.shape}")

# Calculate correlation matrix
print("Calculating correlations...")
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_cols].corr()

# Find correlations with isFraud (target)
if 'isFraud' in corr_matrix.columns:
    fraud_corr = corr_matrix['isFraud'].sort_values(ascending=False)
    print("\n=== TOP 20 FEATURES CORRELATED WITH isFraud ===")
    print(fraud_corr.head(20))
    print("\n=== BOTTOM 20 FEATURES CORRELATED WITH isFraud (NEGATIVELY) ===")
    print(fraud_corr.tail(20))

# Find highly correlated features (excluding isFraud)
print("\n=== HIGHLY CORRELATED FEATURE PAIRS (|correlation| > 0.7) ===")
high_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.7:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            if col1 != 'isFraud' and col2 != 'isFraud':
                high_corr_pairs.append((col1, col2, corr_matrix.iloc[i, j]))

high_corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
for col1, col2, corr in high_corr_pairs[:20]:
    print(f"{col1} <-> {col2}: {corr:.4f}")

# Group by column types and show correlations within groups
print("\n=== CORRELATION WITHIN V COLUMNS (Sample) ===")
v_cols = [col for col in numeric_cols if col.startswith('V')]
if v_cols:
    v_corr = df[v_cols[:10]].corr()
    print(f"Number of V columns: {len(v_cols)}")
    print("V1-V10 correlation matrix created")

print("\n=== CORRELATION WITHIN C COLUMNS ===")
c_cols = [col for col in numeric_cols if col.startswith('C')]
if c_cols:
    c_corr = df[c_cols].corr()
    print(f"Number of C columns: {len(c_cols)}")
    print("C columns correlation matrix created")

print("\n=== CORRELATION WITHIN D COLUMNS ===")
d_cols = [col for col in numeric_cols if col.startswith('D')]
if d_cols:
    d_corr = df[d_cols].corr()
    print(f"Number of D columns: {len(d_cols)}")
    high_d_corr = []
    for i in range(len(d_corr.columns)):
        for j in range(i+1, len(d_corr.columns)):
            if abs(d_corr.iloc[i, j]) > 0.5:
                col1 = d_corr.columns[i]
                col2 = d_corr.columns[j]
                high_d_corr.append((col1, col2, d_corr.iloc[i, j]))
    high_d_corr.sort(key=lambda x: abs(x[2]), reverse=True)
    print("High D column correlations:")
    for col1, col2, corr in high_d_corr[:10]:
        print(f"  {col1} <-> {col2}: {corr:.4f}")

print("\n=== CORRELATION WITH TRANSACTION AMOUNT ===")
if 'TransactionAmt' in numeric_cols:
    amt_corr = corr_matrix['TransactionAmt'].sort_values(ascending=False)
    print("Top 10 correlated with TransactionAmt:")
    print(amt_corr[1:11])

print("\n=== CORRELATION WITH TransactionDT ===")
if 'TransactionDT' in numeric_cols:
    dt_corr = corr_matrix['TransactionDT'].sort_values(ascending=False)
    print("Top 10 correlated with TransactionDT:")
    print(dt_corr[1:11])

# Identity columns correlation with target
print("\n=== IDENTITY COLUMNS CORRELATED WITH isFraud ===")
id_cols = [col for col in numeric_cols if col.startswith('id_')]
if id_cols and 'isFraud' in numeric_cols:
    id_fraud_corr = []
    for col in id_cols:
        c = corr_matrix.loc[col, 'isFraud']
        if not np.isnan(c):
            id_fraud_corr.append((col, c))
    id_fraud_corr.sort(key=lambda x: abs(x[1]), reverse=True)
    print("Top identity columns correlated with isFraud:")
    for col, c in id_fraud_corr[:15]:
        print(f"  {col}: {c:.4f}")
