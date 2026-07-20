import pandas as pd
import numpy as np

# Read sample data from transaction file
print("=== TRANSACTION DATA SAMPLE ===")
trans_df = pd.read_csv('dataset/train_transaction.csv', nrows=5)
print(trans_df[['TransactionID', 'TransactionDT', 'TransactionAmt', 'ProductCD', 'card1', 'card4', 'card6', 'P_emaildomain', 'R_emaildomain', 'addr1', 'addr2', 'M1', 'M4', 'isFraud']].to_string())

print("\n=== SAMPLE V COLUMNS ===")
print(trans_df[['V1', 'V2', 'V3', 'V337', 'V338', 'V339']].to_string())

print("\n=== SAMPLE C COLUMNS ===")
print(trans_df[['C1', 'C2', 'C3', 'C12', 'C13', 'C14']].to_string())

print("\n=== SAMPLE D COLUMNS ===")
print(trans_df[['D1', 'D2', 'D3', 'D13', 'D14', 'D15']].to_string())

# Get some statistics
print("\n=== COLUMN VALUE RANGES ===")
print(f"TransactionAmt min/max: {trans_df['TransactionAmt'].min():.2f} / {trans_df['TransactionAmt'].max():.2f}")
print(f"ProductCD values: {trans_df['ProductCD'].unique().tolist()}")
print(f"M1 values: {trans_df['M1'].dropna().unique().tolist()}")
print(f"M4 values: {trans_df['M4'].dropna().unique().tolist()}")
print(f"isFraud values: {trans_df['isFraud'].unique().tolist()}")

print("\n=== CARD COMPANIES ===")
card4_vals = pd.read_csv('dataset/train_transaction.csv', usecols=['card4'], nrows=100)
print(f"Card4 values: {card4_vals['card4'].dropna().unique().tolist()[:10]}")

card6_vals = pd.read_csv('dataset/train_transaction.csv', usecols=['card6'], nrows=100)
print(f"Card6 values: {card6_vals['card6'].dropna().unique().tolist()}")

print("\n=== IDENTITY DATA ===")
ident_df = pd.read_csv('dataset/train_identity.csv', nrows=5)
print(ident_df[['TransactionID', 'id_01', 'id_02', 'id_03', 'id_11', 'id_12', 'id_30', 'id_31', 'DeviceType', 'DeviceInfo']].to_string())
