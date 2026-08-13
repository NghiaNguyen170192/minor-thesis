
XGBoost - Baseline
Features: 437
Accuracy           : 0.9116
Precision          : 0.2374
Recall             : 0.7096
F1 Score           : 0.3558
ROC-AUC            : 0.9007
PR-AUC             : 0.5151
Balanced Accuracy  : 0.8142
MCC                : 0.3771

Confusion Matrix:
[[104780   9264]
 [  1180   2884]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9889    0.9188    0.9525    114044
       Fraud     0.2374    0.7096    0.3558      4064

    accuracy                         0.9116    118108
   macro avg     0.6131    0.8142    0.6542    118108
weighted avg     0.9630    0.9116    0.9320    118108

XGBoost - Feature Engineering
Features: 439
Accuracy           : 0.9116
Precision          : 0.2384
Recall             : 0.7158
F1 Score           : 0.3577
ROC-AUC            : 0.9039
PR-AUC             : 0.5243
Balanced Accuracy  : 0.8172
MCC                : 0.3799

Confusion Matrix:
[[104753   9291]
 [  1155   2909]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9891    0.9185    0.9525    114044
       Fraud     0.2384    0.7158    0.3577      4064

    accuracy                         0.9116    118108
   macro avg     0.6138    0.8172    0.6551    118108
weighted avg     0.9633    0.9116    0.9320    118108

XGBoost - Remove C

Features: 423
Accuracy           : 0.8947
Precision          : 0.2039
Recall             : 0.7096
F1 Score           : 0.3167
ROC-AUC            : 0.8926
PR-AUC             : 0.4777
Balanced Accuracy  : 0.8054
MCC                : 0.3429

Confusion Matrix:
[[102782  11262]
 [  1180   2884]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9886    0.9012    0.9429    114044
       Fraud     0.2039    0.7096    0.3167      4064

    accuracy                         0.8947    118108
   macro avg     0.5963    0.8054    0.6298    118108
weighted avg     0.9616    0.8947    0.9214    118108

XGBoost - Remove D

Features: 415
Accuracy           : 0.9081
Precision          : 0.2292
Recall             : 0.7074
F1 Score           : 0.3462
ROC-AUC            : 0.8972
PR-AUC             : 0.5166
Balanced Accuracy  : 0.8113
MCC                : 0.3684

Confusion Matrix:
[[104376   9668]
 [  1189   2875]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9887    0.9152    0.9506    114044
       Fraud     0.2292    0.7074    0.3462      4064

    accuracy                         0.9081    118108
   macro avg     0.6090    0.8113    0.6484    118108
weighted avg     0.9626    0.9081    0.9298    118108

XGBoost - Remove M

Features: 428
Accuracy           : 0.9085
Precision          : 0.2306
Recall             : 0.7099
F1 Score           : 0.3481
ROC-AUC            : 0.8984
PR-AUC             : 0.5145
Balanced Accuracy  : 0.8127
MCC                : 0.3705

Confusion Matrix:
[[104419   9625]
 [  1179   2885]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9888    0.9156    0.9508    114044
       Fraud     0.2306    0.7099    0.3481      4064

    accuracy                         0.9085    118108
   macro avg     0.6097    0.8127    0.6495    118108
weighted avg     0.9627    0.9085    0.9301    118108

XGBoost - Remove id

Features: 399
Accuracy           : 0.9114
Precision          : 0.2362
Recall             : 0.7047
F1 Score           : 0.3539
ROC-AUC            : 0.9038
PR-AUC             : 0.5169
Balanced Accuracy  : 0.8118
MCC                : 0.3745

Confusion Matrix:
[[104785   9259]
 [  1200   2864]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9887    0.9188    0.9525    114044
       Fraud     0.2362    0.7047    0.3539      4064

    accuracy                         0.9114    118108
   macro avg     0.6125    0.8118    0.6532    118108
weighted avg     0.9628    0.9114    0.9319    118108

XGBoost - Remove V

Features: 98
Accuracy           : 0.9003
Precision          : 0.2171
Recall             : 0.7281
F1 Score           : 0.3344
ROC-AUC            : 0.9053
PR-AUC             : 0.5072
Balanced Accuracy  : 0.8173
MCC                : 0.3620

Confusion Matrix:
[[103371  10673]
 [  1105   2959]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9894    0.9064    0.9461    114044
       Fraud     0.2171    0.7281    0.3344      4064

    accuracy                         0.9003    118108
   macro avg     0.6032    0.8173    0.6403    118108
weighted avg     0.9628    0.9003    0.9251    118108

XGBoost - Remove C + D

Features: 401
Accuracy           : 0.8934
Precision          : 0.2001
Recall             : 0.6998
F1 Score           : 0.3112
ROC-AUC            : 0.8824
PR-AUC             : 0.4760
Balanced Accuracy  : 0.8000
MCC                : 0.3362

Confusion Matrix:
[[102672  11372]
 [  1220   2844]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9883    0.9003    0.9422    114044
       Fraud     0.2001    0.6998    0.3112      4064

    accuracy                         0.8934    118108
   macro avg     0.5942    0.8000    0.6267    118108
weighted avg     0.9611    0.8934    0.9205    118108

XGBoost - Remove C + M

Features: 414
Accuracy           : 0.8950
Precision          : 0.2027
Recall             : 0.6991
F1 Score           : 0.3143
ROC-AUC            : 0.8882
PR-AUC             : 0.4694
Balanced Accuracy  : 0.8005
MCC                : 0.3388

Confusion Matrix:
[[102871  11173]
 [  1223   2841]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9883    0.9020    0.9432    114044
       Fraud     0.2027    0.6991    0.3143      4064

    accuracy                         0.8950    118108
   macro avg     0.5955    0.8005    0.6287    118108
weighted avg     0.9612    0.8950    0.9215    118108

XGBoost - Remove C + id

Features: 385
Accuracy           : 0.8920
Precision          : 0.1991
Recall             : 0.7069
F1 Score           : 0.3107
ROC-AUC            : 0.8916
PR-AUC             : 0.4700
Balanced Accuracy  : 0.8028
MCC                : 0.3370

Confusion Matrix:
[[102485  11559]
 [  1191   2873]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9885    0.8986    0.9414    114044
       Fraud     0.1991    0.7069    0.3107      4064

    accuracy                         0.8920    118108
   macro avg     0.5938    0.8028    0.6261    118108
weighted avg     0.9613    0.8920    0.9197    118108

XGBoost - Remove C + V

Features: 84
Accuracy           : 0.8801
Precision          : 0.1801
Recall             : 0.6988
F1 Score           : 0.2863
ROC-AUC            : 0.8798
PR-AUC             : 0.3753
Balanced Accuracy  : 0.7927
MCC                : 0.3137

Confusion Matrix:
[[101112  12932]
 [  1224   2840]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9880    0.8866    0.9346    114044
       Fraud     0.1801    0.6988    0.2863      4064

    accuracy                         0.8801    118108
   macro avg     0.5841    0.7927    0.6105    118108
weighted avg     0.9602    0.8801    0.9123    118108

XGBoost - Remove D + M

Features: 406
Accuracy           : 0.9072
Precision          : 0.2269
Recall             : 0.7047
F1 Score           : 0.3433
ROC-AUC            : 0.8921
PR-AUC             : 0.5136
Balanced Accuracy  : 0.8096
MCC                : 0.3653

Confusion Matrix:
[[104287   9757]
 [  1200   2864]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9886    0.9144    0.9501    114044
       Fraud     0.2269    0.7047    0.3433      4064

    accuracy                         0.9072    118108
   macro avg     0.6078    0.8096    0.6467    118108
weighted avg     0.9624    0.9072    0.9292    118108

XGBoost - Remove D + id

Features: 377
Accuracy           : 0.9068
Precision          : 0.2278
Recall             : 0.7148
F1 Score           : 0.3455
ROC-AUC            : 0.8969
PR-AUC             : 0.5126
Balanced Accuracy  : 0.8142
MCC                : 0.3691

Confusion Matrix:
[[104197   9847]
 [  1159   2905]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9890    0.9137    0.9498    114044
       Fraud     0.2278    0.7148    0.3455      4064

    accuracy                         0.9068    118108
   macro avg     0.6084    0.8142    0.6477    118108
weighted avg     0.9628    0.9068    0.9290    118108

XGBoost - Remove D + V

Features: 76
Accuracy           : 0.9122
Precision          : 0.2332
Recall             : 0.6784
F1 Score           : 0.3471
ROC-AUC            : 0.8916
PR-AUC             : 0.4988
Balanced Accuracy  : 0.7995
MCC                : 0.3638

Confusion Matrix:
[[104980   9064]
 [  1307   2757]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9877    0.9205    0.9529    114044
       Fraud     0.2332    0.6784    0.3471      4064

    accuracy                         0.9122    118108
   macro avg     0.6105    0.7995    0.6500    118108
weighted avg     0.9617    0.9122    0.9321    118108

XGBoost - Remove M + id

Features: 390
Accuracy           : 0.9068
Precision          : 0.2277
Recall             : 0.7146
F1 Score           : 0.3454
ROC-AUC            : 0.9052
PR-AUC             : 0.5144
Balanced Accuracy  : 0.8141
MCC                : 0.3690

Confusion Matrix:
[[104197   9847]
 [  1160   2904]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9890    0.9137    0.9498    114044
       Fraud     0.2277    0.7146    0.3454      4064

    accuracy                         0.9068    118108
   macro avg     0.6084    0.8141    0.6476    118108
weighted avg     0.9628    0.9068    0.9290    118108

XGBoost - Remove M + V

Features: 89
Accuracy           : 0.9022
Precision          : 0.2191
Recall             : 0.7188
F1 Score           : 0.3358
ROC-AUC            : 0.9033
PR-AUC             : 0.5031
Balanced Accuracy  : 0.8137
MCC                : 0.3614

Confusion Matrix:
[[103632  10412]
 [  1143   2921]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9891    0.9087    0.9472    114044
       Fraud     0.2191    0.7188    0.3358      4064

    accuracy                         0.9022    118108
   macro avg     0.6041    0.8137    0.6415    118108
weighted avg     0.9626    0.9022    0.9262    118108

XGBoost - Remove id + V

Features: 60
Accuracy           : 0.9014
Precision          : 0.2185
Recall             : 0.7237
F1 Score           : 0.3356
ROC-AUC            : 0.9052
PR-AUC             : 0.4973
Balanced Accuracy  : 0.8157
MCC                : 0.3622

Confusion Matrix:
[[103523  10521]
 [  1123   2941]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9893    0.9077    0.9468    114044
       Fraud     0.2185    0.7237    0.3356      4064

    accuracy                         0.9014    118108
   macro avg     0.6039    0.8157    0.6412    118108
weighted avg     0.9627    0.9014    0.9257    118108

XGBoost - Remove C + D + M

Features: 392
Accuracy           : 0.8897
Precision          : 0.1939
Recall             : 0.6983
F1 Score           : 0.3035
ROC-AUC            : 0.8814
PR-AUC             : 0.4739
Balanced Accuracy  : 0.7974
MCC                : 0.3291

Confusion Matrix:
[[102244  11800]
 [  1226   2838]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9882    0.8965    0.9401    114044
       Fraud     0.1939    0.6983    0.3035      4064

    accuracy                         0.8897    118108
   macro avg     0.5910    0.7974    0.6218    118108
weighted avg     0.9608    0.8897    0.9182    118108

XGBoost - Remove C + D + id

Features: 363
Accuracy           : 0.8900
Precision          : 0.1955
Recall             : 0.7055
F1 Score           : 0.3062
ROC-AUC            : 0.8829
PR-AUC             : 0.4681
Balanced Accuracy  : 0.8010
MCC                : 0.3328

Confusion Matrix:
[[102248  11796]
 [  1197   2867]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9884    0.8966    0.9403    114044
       Fraud     0.1955    0.7055    0.3062      4064

    accuracy                         0.8900    118108
   macro avg     0.5920    0.8010    0.6232    118108
weighted avg     0.9611    0.8900    0.9184    118108

XGBoost - Remove C + D + V

Features: 62
Accuracy           : 0.8638
Precision          : 0.1524
Recall             : 0.6486
F1 Score           : 0.2468
ROC-AUC            : 0.8435
PR-AUC             : 0.3103
Balanced Accuracy  : 0.7600
MCC                : 0.2682

Confusion Matrix:
[[99386 14658]
 [ 1428  2636]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9858    0.8715    0.9251    114044
       Fraud     0.1524    0.6486    0.2468      4064

    accuracy                         0.8638    118108
   macro avg     0.5691    0.7600    0.5860    118108
weighted avg     0.9572    0.8638    0.9018    118108

XGBoost - Remove C + M + id

Features: 376
Accuracy           : 0.8930
Precision          : 0.1991
Recall             : 0.6981
F1 Score           : 0.3098
ROC-AUC            : 0.8897
PR-AUC             : 0.4656
Balanced Accuracy  : 0.7990
MCC                : 0.3346

Confusion Matrix:
[[102629  11415]
 [  1227   2837]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9882    0.8999    0.9420    114044
       Fraud     0.1991    0.6981    0.3098      4064

    accuracy                         0.8930    118108
   macro avg     0.5936    0.7990    0.6259    118108
weighted avg     0.9610    0.8930    0.9202    118108

XGBoost - Remove C + M + V

Features: 75
Accuracy           : 0.8730
Precision          : 0.1667
Recall             : 0.6730
F1 Score           : 0.2672
ROC-AUC            : 0.8679
PR-AUC             : 0.3752
Balanced Accuracy  : 0.7766
MCC                : 0.2915

Confusion Matrix:
[[100373  13671]
 [  1329   2735]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9869    0.8801    0.9305    114044
       Fraud     0.1667    0.6730    0.2672      4064

    accuracy                         0.8730    118108
   macro avg     0.5768    0.7766    0.5988    118108
weighted avg     0.9587    0.8730    0.9077    118108

XGBoost - Remove C + id + V

Features: 46
Accuracy           : 0.8853
Precision          : 0.1840
Recall             : 0.6794
F1 Score           : 0.2895
ROC-AUC            : 0.8802
PR-AUC             : 0.3391
Balanced Accuracy  : 0.7860
MCC                : 0.3131

Confusion Matrix:
[[101798  12246]
 [  1303   2761]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9874    0.8926    0.9376    114044
       Fraud     0.1840    0.6794    0.2895      4064

    accuracy                         0.8853    118108
   macro avg     0.5857    0.7860    0.6136    118108
weighted avg     0.9597    0.8853    0.9153    118108

XGBoost - Remove D + M + id

Features: 368
Accuracy           : 0.9036
Precision          : 0.2201
Recall             : 0.7077
F1 Score           : 0.3357
ROC-AUC            : 0.8927
PR-AUC             : 0.5086
Balanced Accuracy  : 0.8092
MCC                : 0.3593

Confusion Matrix:
[[103852  10192]
 [  1188   2876]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9887    0.9106    0.9481    114044
       Fraud     0.2201    0.7077    0.3357      4064

    accuracy                         0.9036    118108
   macro avg     0.6044    0.8092    0.6419    118108
weighted avg     0.9622    0.9036    0.9270    118108

XGBoost - Remove D + M + V

Features: 67
Accuracy           : 0.9063
Precision          : 0.2178
Recall             : 0.6651
F1 Score           : 0.3282
ROC-AUC            : 0.8872
PR-AUC             : 0.4928
Balanced Accuracy  : 0.7900
MCC                : 0.3448

Confusion Matrix:
[[104337   9707]
 [  1361   2703]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9871    0.9149    0.9496    114044
       Fraud     0.2178    0.6651    0.3282      4064

    accuracy                         0.9063    118108
   macro avg     0.6025    0.7900    0.6389    118108
weighted avg     0.9607    0.9063    0.9282    118108

XGBoost - Remove D + id + V

Features: 38
Accuracy           : 0.9101
Precision          : 0.2281
Recall             : 0.6764
F1 Score           : 0.3412
ROC-AUC            : 0.8913
PR-AUC             : 0.4809
Balanced Accuracy  : 0.7974
MCC                : 0.3582

Confusion Matrix:
[[104742   9302]
 [  1315   2749]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9876    0.9184    0.9518    114044
       Fraud     0.2281    0.6764    0.3412      4064

    accuracy                         0.9101    118108
   macro avg     0.6079    0.7974    0.6465    118108
weighted avg     0.9615    0.9101    0.9308    118108

XGBoost - Remove M + id + V

Features: 51
Accuracy           : 0.8999
Precision          : 0.2155
Recall             : 0.7224
F1 Score           : 0.3319
ROC-AUC            : 0.9048
PR-AUC             : 0.4954
Balanced Accuracy  : 0.8143
MCC                : 0.3587

Confusion Matrix:
[[103353  10691]
 [  1128   2936]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9892    0.9063    0.9459    114044
       Fraud     0.2155    0.7224    0.3319      4064

    accuracy                         0.8999    118108
   macro avg     0.6023    0.8143    0.6389    118108
weighted avg     0.9626    0.8999    0.9248    118108

XGBoost - Remove C + D + M + id

Features: 354
Accuracy           : 0.8823
Precision          : 0.1814
Recall             : 0.6892
F1 Score           : 0.2872
ROC-AUC            : 0.8751
PR-AUC             : 0.4603
Balanced Accuracy  : 0.7892
MCC                : 0.3127

Confusion Matrix:
[[101404  12640]
 [  1263   2801]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9877    0.8892    0.9358    114044
       Fraud     0.1814    0.6892    0.2872      4064

    accuracy                         0.8823    118108
   macro avg     0.5845    0.7892    0.6115    118108
weighted avg     0.9600    0.8823    0.9135    118108

XGBoost - Remove C + D + M + V

Features: 53
Accuracy           : 0.8786
Precision          : 0.1558
Recall             : 0.5723
F1 Score           : 0.2449
ROC-AUC            : 0.8137
PR-AUC             : 0.2873
Balanced Accuracy  : 0.7309
MCC                : 0.2533

Confusion Matrix:
[[101440  12604]
 [  1738   2326]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9832    0.8895    0.9340    114044
       Fraud     0.1558    0.5723    0.2449      4064

    accuracy                         0.8786    118108
   macro avg     0.5695    0.7309    0.5894    118108
weighted avg     0.9547    0.8786    0.9103    118108

XGBoost - Remove C + D + id + V

Features: 24
Accuracy           : 0.8734
Precision          : 0.1592
Recall             : 0.6255
F1 Score           : 0.2537
ROC-AUC            : 0.8398
PR-AUC             : 0.2339
Balanced Accuracy  : 0.7539
MCC                : 0.2706

Confusion Matrix:
[[100614  13430]
 [  1522   2542]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9851    0.8822    0.9308    114044
       Fraud     0.1592    0.6255    0.2537      4064

    accuracy                         0.8734    118108
   macro avg     0.5721    0.7539    0.5923    118108
weighted avg     0.9567    0.8734    0.9075    118108

XGBoost - Remove C + M + id + V

Features: 37
Accuracy           : 0.8772
Precision          : 0.1703
Recall             : 0.6631
F1 Score           : 0.2710
ROC-AUC            : 0.8690
PR-AUC             : 0.3444
Balanced Accuracy  : 0.7740
MCC                : 0.2932

Confusion Matrix:
[[100911  13133]
 [  1369   2695]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9866    0.8848    0.9330    114044
       Fraud     0.1703    0.6631    0.2710      4064

    accuracy                         0.8772    118108
   macro avg     0.5784    0.7740    0.6020    118108
weighted avg     0.9585    0.8772    0.9102    118108

XGBoost - Remove D + M + id + V

Features: 29
Accuracy           : 0.9136
Precision          : 0.2299
Recall             : 0.6425
F1 Score           : 0.3386
ROC-AUC            : 0.8842
PR-AUC             : 0.4772
Balanced Accuracy  : 0.7829
MCC                : 0.3498

Confusion Matrix:
[[105298   8746]
 [  1453   2611]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9864    0.9233    0.9538    114044
       Fraud     0.2299    0.6425    0.3386      4064

    accuracy                         0.9136    118108
   macro avg     0.6081    0.7829    0.6462    118108
weighted avg     0.9604    0.9136    0.9326    118108

XGBoost - Remove C + D + M + id + V

Features: 15
Accuracy           : 0.8866
Precision          : 0.1631
Recall             : 0.5556
F1 Score           : 0.2522
ROC-AUC            : 0.8156
PR-AUC             : 0.2250
Balanced Accuracy  : 0.7270
MCC                : 0.2573

Confusion Matrix:
[[102457  11587]
 [  1806   2258]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9827    0.8984    0.9387    114044
       Fraud     0.1631    0.5556    0.2522      4064

    accuracy                         0.8866    118108
   macro avg     0.5729    0.7270    0.5954    118108
weighted avg     0.9545    0.8866    0.9150    118108

