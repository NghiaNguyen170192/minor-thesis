# IEEE Fraud Detection Dataset - Column Summary

This document provides a comprehensive summary of all columns in the `train_identity.csv`, `test_identity.csv`, `train_transaction.csv`, and `test_transaction.csv` files from the IEEE-CIS Fraud Detection competition.

## Overview

- **Binary Classification Problem**: Heavy class imbalance (fraud vs. legitimate transactions)
- **Train Transactions**: ~590,540 rows
- **Test Transactions**: ~506,691 rows
- **Total Columns**: 434 (after merging transaction and identity data)
- **Missing Data**: Most columns contain missing values (~88% in some cases)

---

## Transaction Dataset Columns

### Identifiers

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `TransactionID` | Integer | Unique identifier for each transaction | 2987000, 2987001, 2987002 |
| `TransactionDT` | Integer | Transaction timestamp (seconds since reference point) | 86400, 86401, 86469, 86499 |

**Note**: Train and test transaction dates don't overlap - train data predates test data. Time-based cross-validation is recommended.

### Transaction Amount

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `TransactionAmt` | Float | Transaction amount (range: $0 - $31,937) | 29.00, 50.00, 59.00, 68.50 |

### Product & Card Information

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `ProductCD` | Categorical | Product code (values: W, H, C, S, R) | W, H |
| `card1` | Integer | Card number (anonymized) | 13926, 2755, 4663, 18132 |
| `card2` | Integer | Card number (anonymized) | (anonymized integers) |
| `card3` | Integer | Card number (anonymized) | (anonymized integers) |
| `card4` | Categorical | Card issuer company | visa, mastercard, discover, american express |
| `card5` | Integer | Card number (anonymized) | (anonymized integers) |
| `card6` | Categorical | Card type (credit, debit) | credit, debit |

### Email Domain Information

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `P_emaildomain` | Categorical | Payer (purchaser) email domain | gmail.com, outlook.com, yahoo.com, hotmail.com, aol.com |
| `R_emaildomain` | Categorical | Receiver email domain | mail.com, anonymous.com, verizon.net, comcast.net |

### Address Information

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `addr1` | Integer | Billing address (anonymized) | 315, 325, 330, 476, 420 |
| `addr2` | Integer | Billing address (anonymized) | 87, 87, 87, 87, 87 |

### Binary/Categorical Flags (M1-M9)

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `M1` | Categorical | Match status | T |
| `M2` | Binary | Match status | T, F |
| `M3` | Binary | Match status | T, F |
| `M4` | Categorical | Match status codes | M0, M1, M2 |
| `M5` - `M9` | Binary | Match status flags | T, F |

**These columns appear to represent matching status between different data sources.**

### Anonymized Continuous Variables (V1-V339)

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `V1` - `V339` | Float | Anonymized numerical features (339 features) | 1.0, 0.0, (many missing) |

**Note**: These features are highly anonymized for privacy. Analysis reveals:
- Some appear to be already normalized (values between 0-1)
- High correlation with fraud detection
- Many contain missing values
- V1 sample: [1.0, NaN, 1.0, NaN, NaN]
- V337 sample: [NaN, NaN, NaN, NaN, 0.0]

### Anonymized Categorical Variables (C1-C14)

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `C1` - `C14` | Integer/Categorical | Anonymized categorical features (14 features) | 0.0, 1.0, 2.0, 5.0, 25.0 |

### Distance/Time Variables (D1-D15)

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `D1` - `D15` | Float/Integer | Distance or time-based features (15 features) | 0.0, 13.0, 14.0, 112.0, 315.0 |

**Examples**:
- `D1` sample: [14.0, 0.0, 0.0, 112.0, 0.0]
- `D15` sample: [0.0, 0.0, 315.0, 111.0, NaN]
- `D15`: Appears to be a distance or time measure with mean ~362

### Target Variable

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `isFraud` | Binary (0/1) | Target variable: 0=Legitimate, 1=Fraudulent | 0, 1 |

**Class Distribution**: Highly imbalanced (~3.5% fraud in training data)

---

## Identity Dataset Columns

### Continuous Identity Variables (id_01 to id_11)

| Column | Type | Characteristics | Example Values |
|--------|------|-----------------|-----------------|
| `id_01` | Float | 77 unique non-positive values, skewed toward 0 | -15.0, -10.0, -5.0, 0.0 |
| `id_02` | Float | Numerical identity feature | 7460.0, 31964.0, 61141.0, 70787.0 |
| `id_03` | Float | 88% missing, 98% either missing or zero | 0.0, 3.0 (mostly NaN) |
| `id_04` | Float | Numerical identity feature | 0.0, 1.0, 3.0 |
| `id_05` | Float | Numerical identity feature | 0.0, 1.0, 3.0 |
| `id_06` | Float | Numerical identity feature | -10.0, -6.0, -5.0, 0.0 |
| `id_07` | Float | Some features appear normalized (0-1 range) | (normalized values) |
| `id_08` | Float | Numerical identity feature | (various floats) |
| `id_09` | Float | Numerical identity feature | 0.0, 3.0 |
| `id_10` | Float | Numerical identity feature | 0.0 |
| `id_11` | Float | 76% missing, 22% equal to 100 | 100.0 (most common) |

### Categorical Identity Variables (id_12 to id_38)

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `id_12` - `id_27` | Categorical | Customer verification/identity categorical features | Found, NotFound |
| `id_28` | Categorical | Binary/categorical status flag | New, Found, NotFound |
| `id_29` | Categorical | Binary/categorical status flag | Found, NotFound |
| `id_30` | Categorical | Operating system or device type information | Android 7.0, Windows 10, iOS 11.1.2, Mac OS X 10_11_6 |
| `id_31` | Categorical | Device manufacturer or model information | chrome 62.0, mobile safari 11.0, samsung browser 6.2, edge 15.0 |
| `id_32` | Categorical | Device status or information | 24.0, 32.0 |
| `id_33` | Categorical | Device-related categorical information | 1920x1080, 1334x750, 1280x800, 1366x768 |
| `id_34` | Categorical | Match status (Found/Not Found) | Found, NotFound |
| `id_35` | Binary | Match/verification flag | T, F |
| `id_36` | Binary | Match/verification flag | T, F |
| `id_37` | Binary | Match/verification flag | T, F |
| `id_38` | Binary | Match/verification flag | T, F |

**Feature Groups**:
- **id_12-id_27**: General categorical identity features
- **id_28-id_33**: Device-related information (OS, manufacturer, status)
- **id_34-id_38**: Binary match/verification flags

### Device Information

| Column | Type | Description | Example Values |
|--------|------|-------------|-----------------|
| `DeviceType` | Categorical | Type of device used (e.g., desktop, mobile) | mobile, desktop |
| `DeviceInfo` | Categorical | Device information/fingerprint (highly diverse values) | SAMSUNG SM-G892A Build/NRD90M, iOS Device, Windows, MacOS |

**Note**: High cardinality - many unique device fingerprints. Some device info may be absent from test data due to old/obsolete devices.

---

## Data Quality Issues

### Missing Values
- Most columns contain missing data (up to 88% in `id_03`)
- Distribution of missing values varies significantly between columns
- Columns dropped during analysis: 140+ columns with >90% missing or single unique value

### High Cardinality Columns
- `DeviceInfo`: Thousands of unique values
- `P_emaildomain`, `R_emaildomain`: Hundreds of unique values
- `id_30`, `id_31`: Many unique values representing device/OS types

### Columns Dropped During Analysis
- Columns with >90% missing values
- Columns with single unique value (no variance)
- Columns where top value represents >90% of data

---

## Feature Engineering Opportunities

Based on the EDA notebooks, the following feature engineering approaches were explored:

### Ratio Features
- `TransactionAmt` to mean/std by `card1`, `card4`
- `id_02` to mean/std by `card1`, `card4`
- `D15` to mean/std by `card1`, `card4`, `addr1`, `addr2`

### Domain Decomposition
- Email domains split into parts: `P_emaildomain_1`, `P_emaildomain_2`, `P_emaildomain_3`
- Similarly for `R_emaildomain`

### Aggregation Features
- Group-wise statistics (mean, std) for numerical features by categorical identifiers

---

## Model Performance Notes

- **Best Model**: LightGBM with parameters:
  - `num_leaves`: 256
  - `max_depth`: 13
  - `learning_rate`: 0.03
  - Optimized for AUC metric
  - 5-fold cross-validation

- **Key Features**: Top 50 features identified through feature importance analysis
- **Imbalanced Learning**: Handles class imbalance inherent in fraud detection problems

---

## Dataset Statistics

| Metric | Train | Test (Combined) |
|--------|-------|-----------------|
| Total Rows | 590,540 | 506,691 |
| Total Columns | 434 | 434 |
| Fraud Cases | ~20,663 (3.5%) | Unknown |
| Legitimate Cases | ~569,877 (96.5%) | Unknown |
| Columns with Missing Data | 394 | 394 |

---

## Column Categories Summary

| Category | Count | Type |
|----------|-------|------|
| Transaction Basics | 3 | ID, Date, Amount |
| Product & Card | 6 | Categorical/Integer |
| Email & Address | 4 | Categorical/Integer |
| Match Flags (M1-M9) | 9 | Categorical/Binary |
| Anonymous Continuous (V1-V339) | 339 | Float |
| Anonymous Categorical (C1-C14) | 14 | Integer/Categorical |
| Distance/Time (D1-D15) | 15 | Float/Integer |
| Identity Continuous (id_01-id_11) | 11 | Float |
| Identity Categorical (id_12-id_38) | 27 | Categorical |
| Device Info | 2 | Categorical |
| Target | 1 | Binary |
| **Total** | **~434** | |

---

---

## Sample Data

### Transaction Data Sample (First 5 Rows)

| TransactionID | TransactionDT | TransactionAmt | ProductCD | card1 | card4 | card6 | P_emaildomain | M1 | M4 | isFraud |
|---|---|---|---|---|---|---|---|---|---|---|
| 2987000 | 86400 | 68.5 | W | 13926 | discover | credit | (missing) | T | M2 | 0 |
| 2987001 | 86401 | 29.0 | W | 2755 | mastercard | credit | gmail.com | (missing) | M0 | 0 |
| 2987002 | 86469 | 59.0 | W | 4663 | visa | debit | outlook.com | T | M0 | 0 |
| 2987003 | 86499 | 50.0 | W | 18132 | mastercard | debit | yahoo.com | (missing) | M0 | 0 |
| 2987004 | 86506 | 50.0 | H | 4497 | mastercard | credit | gmail.com | (missing) | (missing) | 0 |

### V Variables Sample (V1, V2, V3, V337, V338, V339)

| V1 | V2 | V3 | V337 | V338 | V339 |
|---|---|---|---|---|---|
| 1.0 | 1.0 | 1.0 | (missing) | (missing) | (missing) |
| (missing) | (missing) | (missing) | (missing) | (missing) | (missing) |
| 1.0 | 1.0 | 1.0 | (missing) | (missing) | (missing) |
| (missing) | (missing) | (missing) | (missing) | (missing) | (missing) |
| (missing) | (missing) | (missing) | 0.0 | 0.0 | 0.0 |

### C Variables Sample (C1-C14)

| C1 | C2 | C3 | C4 | C5 | C12 | C13 | C14 |
|---|---|---|---|---|---|---|---|
| 1.0 | 1.0 | 0.0 | 0.0 | 1.0 | 0.0 | 1.0 | 1.0 |
| 1.0 | 1.0 | 0.0 | 0.0 | 1.0 | 0.0 | 1.0 | 1.0 |
| 1.0 | 1.0 | 0.0 | 0.0 | 1.0 | 0.0 | 1.0 | 1.0 |
| 2.0 | 5.0 | 0.0 | 0.0 | 25.0 | 0.0 | 1.0 | 1.0 |
| 1.0 | 1.0 | 0.0 | 0.0 | 1.0 | 0.0 | 1.0 | 1.0 |

### D Variables Sample (D1-D15)

| D1 | D2 | D3 | D13 | D14 | D15 |
|---|---|---|---|---|---|
| 14.0 | (missing) | 13.0 | (missing) | (missing) | 0.0 |
| 0.0 | (missing) | (missing) | (missing) | (missing) | 0.0 |
| 0.0 | (missing) | (missing) | (missing) | (missing) | 315.0 |
| 112.0 | 112.0 | 0.0 | (missing) | (missing) | 111.0 |
| 0.0 | (missing) | (missing) | (missing) | (missing) | (missing) |

### Identity Data Sample (First 5 Rows)

| TransactionID | id_01 | id_02 | id_03 | id_11 | id_12 | id_30 | id_31 | DeviceType | DeviceInfo |
|---|---|---|---|---|---|---|---|---|---|
| 2987004 | 0.0 | 70787.0 | (missing) | 100.0 | NotFound | Android 7.0 | samsung browser 6.2 | mobile | SAMSUNG SM-G892A Build/NRD90M |
| 2987008 | -5.0 | 98945.0 | (missing) | 100.0 | NotFound | iOS 11.1.2 | mobile safari 11.0 | mobile | iOS Device |
| 2987010 | -5.0 | 191631.0 | 0.0 | 100.0 | NotFound | (missing) | chrome 62.0 | desktop | Windows |
| 2987011 | -5.0 | 221832.0 | (missing) | 100.0 | NotFound | (missing) | chrome 62.0 | desktop | (missing) |
| 2987016 | 0.0 | 7460.0 | 0.0 | 100.0 | NotFound | Mac OS X 10_11_6 | chrome 62.0 | desktop | MacOS |

### Common Categorical Values

**Email Domains (P_emaildomain)**:
- gmail.com, outlook.com, yahoo.com, hotmail.com, aol.com, mail.com, anonymous.com, verizon.net, comcast.net, cox.net, optonline.net, rocketmail.com

**Operating Systems (id_30)**:
- Android 7.0, iOS 11.1.2, Windows 10, Mac OS X 10_11_6, Android, Linux, iOS 11.0.3, Mac OS X 10_7_5, Mac OS X 10_12_6

**Browsers (id_31)**:
- chrome 62.0, mobile safari 11.0, samsung browser 6.2, edge 15.0, chrome 49.0, chrome 61.0, safari generic, mobile safari generic

**Match Flags**:
- M1: T
- M2, M3, M5-M9: T, F
- M4: M0, M1, M2

---

## References

- Source: IEEE-CIS Fraud Detection Competition
- Data obtained from: https://www.kaggle.com/competitions/ieee-fraud-detection
- Imbalanced learning approach recommended for modeling
