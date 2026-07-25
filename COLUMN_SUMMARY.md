# IEEE Fraud Detection Dataset - Concise Column Summary

## Dataset Overview
- **Problem**: Binary classification (fraud detection) with 3.5% class imbalance
- **Size**: Train: 590,540 rows | Test: 506,691 rows
- **Columns**: 434 total (393 transaction + 41 identity features)
- **Missing Data**: Heavy missingness across features (up to 88%)
- **Time Structure**: Train and test periods don't overlap (sequential split)

---

## Column Categories

| Category | Columns | Type | Key Characteristics |
|----------|---------|------|---------------------|
| **Identifiers** | TransactionID, TransactionDT | Integer | Unique ID and timestamp (seconds) |
| **Amount** | TransactionAmt | Float | $0-$31,937 range |
| **Product/Card** | ProductCD, card1-6 | Mixed | Product code (W/H/C/S/R), card details |
| **Email/Address** | P_emaildomain, R_emaildomain, addr1-2 | Mixed | Payer/Receiver domains, billing addresses |
| **Match Flags** | M1-M9 | Categorical | Verification status (T/F, M0/M1/M2) |
| **Anonymous Features** | V1-V339 | Float | 339 anonymized numerical features |
| **Count Features** | C1-C14 | Integer | 14 anonymized count features |
| **Distance/Time** | D1-D15 | Float | 15 distance/time-based features |
| **Identity** | id_01-id_38 | Mixed | 11 continuous + 27 categorical identity features |
| **Device** | DeviceType, DeviceInfo | Categorical | Device fingerprints (high cardinality) |
| **Target** | isFraud | Binary | 0=Legitimate, 1=Fraudulent |

---

## Key Feature Groups

### Transaction Features (53 columns)

- **ProductCD**: 5 product types (W, H, C, S, R)
- **card1-card6**: Card identifiers + issuer (visa, mastercard, discover, amex) + type (credit/debit)
- **addr1-addr2**: Anonymized billing addresses
- **P/R_emaildomain**: Payer/Receiver email domains (gmail, yahoo, outlook, etc.)
- **TransactionAmt**: Dollar amounts ($0-$31,937)

### Match Flags - M1-M9 (9 columns)
- **M1-M3**: Correlated match status (T/F) - **highly redundant**
- **M4**: 3-level status (M0/M1/M2)
- **M5-M9**: Binary match flags - **M8-M9 redundant**

### Anonymous V Features - V1-V339 (339 columns)
**Most redundant category - 62% can be reduced**

**NAN Structure Groups**:
- **V1-V11**: Related to D11 (279K missing)
- **V12-V34**: 76K missing
- **V35-V52**: 169K missing
- **V53-V74**: 77K missing
- **V75-V94**: 89K missing
- **V95-V137**: Only 314 missing - **different pattern**
- **V138-V166**: 508K+ missing (two sub-groups)
- **V167-V278**: 450K+ missing (multiple sub-groups)
- **V279-V321**: Only 12 missing - **highly complete**
- **V281-V315**: Related to D1 (1,269 missing)
- **V322-V339**: 508K missing

**Key Insight**: V1-V100 don't correlate with V101-V339 (capture different fraud patterns)

### Count Features - C1-C14 (14 columns)
- Anonymized count/categorical features
- **Mostly independent** - low internal correlation
- All are integer-valued

### Distance/Time - D1-D15 (15 columns)
- Time/distance measurements
- **D1**: Related to V281-V315 group
- **D11**: Related to V1-V11 group
- **D15**: Distance measure (mean ~362)
- D2-D8, D3-D13, D5-D14 show moderate correlations

### Identity Features - id_01-id_38 (38 columns)

**Continuous (id_01-id_11)**:
- id_01, id_06: Non-positive skewed values
- id_02: Wide range numerical feature
- id_03: 88% missing, mostly zero
- id_11: 76% missing, 22% equals 100

**Categorical (id_12-id_38)**:
- id_12-id_29: Verification status (Found/NotFound/New)
- id_30-id_33: **Device info** (OS, browser, screen resolution)
- id_34-id_38: Binary match flags (T/F)

**Device Features**:
- **DeviceType**: mobile/desktop
- **DeviceInfo**: High cardinality device fingerprints


---

## Data Quality Summary

### Missing Values by Feature Type
- **V columns**: 314 to 508K missing (varies dramatically by group)
- **D columns**: D1 (1,269), D11 (279K), others vary
- **ID columns**: id_03 (88%), id_11 (76%), others moderate
- **C, M columns**: Minimal to moderate missing

### High Cardinality Features
- **DeviceInfo**: Thousands of unique fingerprints
- **Email domains**: Hundreds of unique values
- **Device features** (id_30, id_31, id_33): High diversity

### Dropped Features Criteria
- >90% missing values
- Single unique value (no variance)
- Top value represents >90% of data

---

## Feature Engineering Insights

### Recommended Transformations
1. **Ratio features**: TransactionAmt/id_02 by card1, card4, addr1
2. **Domain parsing**: Split email domains into hierarchical parts
3. **Aggregations**: Group-wise mean/std for numerical features
4. **Time features**: Extract from TransactionDT (day, hour, etc.)

### Dimensionality Reduction Potential
- **V columns**: 339 → 130 columns (62% reduction) using correlation analysis
- **M columns**: 9 → 6-7 columns (remove M1-M3 redundancy, M8-M9 redundancy)
- **ID columns**: 38 → 35 columns (minor reductions in match flags)
- **Total**: 434 → ~300 columns with 95%+ information retention

---

## Quick Reference Table

| Feature Type | Count | Missing % Range | Redundancy | Keep |
|--------------|-------|-----------------|------------|------|
| Transaction basics | 3 | 0% | None | All |
| Product/Card/Email | 10 | 0-40% | Low | All |
| M flags | 9 | 30-60% | **High** | 6-7 |
| V features | 339 | 0-88% | **Very High** | ~130 |
| C features | 14 | 0-20% | Low | 12-13 |
| D features | 15 | 0-50% | Low | 13-14 |
| ID features | 38 | 0-88% | Medium | 35 |
| Device | 2 | 30-40% | None | All |
| **Total** | **434** | - | **52%** | **~300** |

---

## Target Variable: isFraud

- **Type**: Binary (0=Legitimate, 1=Fraudulent)
- **Distribution**: 96.5% legitimate, 3.5% fraud
- **Class Imbalance**: ~28:1 ratio
- **Modeling Challenge**: Requires imbalanced learning techniques (SMOTE, class weights, focal loss)

---

## Sample Data Patterns

**Transaction Sample**:
```
TransactionID: 2987000 | DT: 86400 | Amt: $68.50 | Product: W
card1: 13926 | card4: discover | card6: credit | isFraud: 0
```

**V Features**: Range 0-1 (normalized) or wider ranges, many NaN
**C Features**: Integer counts (0-25+ range)
**D Features**: Time/distance (0-500+ range)
**ID Features**: Mixed continuous and categorical identity markers

---

## Key Takeaways

1. **Heavy anonymization**: Most features (V, C, D) lack interpretable meaning
2. **Extreme missingness**: 88% missing in some features requires imputation strategy
3. **High redundancy**: V columns contain 62% redundant information
4. **Time structure**: Sequential train/test split enables time-based validation
5. **Class imbalance**: 3.5% fraud rate requires specialized handling
6. **Device diversity**: High cardinality in device fingerprints (generalization risk)

---

*Generated from IEEE-CIS Fraud Detection competition notebooks (ieee-transaction-columns-reference.ipynb, eda-for-columns-v-and-id.ipynb)*

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
