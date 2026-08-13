Streaming output truncated to the last 5000 lines.
[[99369 14675]
 [ 1048  3016]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9896    0.8713    0.9267    114044
       Fraud     0.1705    0.7421    0.2773      4064

    accuracy                         0.8669    118108
   macro avg     0.5800    0.8067    0.6020    118108
weighted avg     0.9614    0.8669    0.9043    118108

XGBoost - Remove C + D + id - Undersampling

Features: 363
Accuracy           : 0.8640
Precision          : 0.1661
Recall             : 0.7345
F1 Score           : 0.2709
ROC-AUC            : 0.8876
PR-AUC             : 0.4570
Balanced Accuracy  : 0.8015
MCC                : 0.3061

Confusion Matrix:
[[99057 14987]
 [ 1079  2985]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9892    0.8686    0.9250    114044
       Fraud     0.1661    0.7345    0.2709      4064

    accuracy                         0.8640    118108
   macro avg     0.5777    0.8015    0.5980    118108
weighted avg     0.9609    0.8640    0.9025    118108


===== Remove C + D + id - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + D + id - SMOTE + Undersampling

Features: 363
Accuracy           : 0.9706
Precision          : 0.6278
Recall             : 0.3602
F1 Score           : 0.4578
ROC-AUC            : 0.8743
PR-AUC             : 0.4568
Balanced Accuracy  : 0.6763
MCC                : 0.4620

Confusion Matrix:
[[113176    868]
 [  2600   1464]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9775    0.9924    0.9849    114044
       Fraud     0.6278    0.3602    0.4578      4064

    accuracy                         0.9706    118108
   macro avg     0.8027    0.6763    0.7213    118108
weighted avg     0.9655    0.9706    0.9668    118108
LightGBM - Remove C + D + id - SMOTE + Undersampling

Features: 363
Accuracy           : 0.9589
Precision          : 0.4148
Recall             : 0.4769
F1 Score           : 0.4437
ROC-AUC            : 0.8831
PR-AUC             : 0.4656
Balanced Accuracy  : 0.7264
MCC                : 0.4235

Confusion Matrix:
[[111310   2734]
 [  2126   1938]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9813    0.9760    0.9786    114044
       Fraud     0.4148    0.4769    0.4437      4064

    accuracy                         0.9589    118108
   macro avg     0.6980    0.7264    0.7112    118108
weighted avg     0.9618    0.9589    0.9602    118108
XGBoost - Remove C + D + id - SMOTE + Undersampling

Features: 363
Accuracy           : 0.9581
Precision          : 0.4065
Recall             : 0.4705
F1 Score           : 0.4362
ROC-AUC            : 0.8820
PR-AUC             : 0.4610
Balanced Accuracy  : 0.7230
MCC                : 0.4158

Confusion Matrix:
[[111253   2791]
 [  2152   1912]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9810    0.9755    0.9783    114044
       Fraud     0.4065    0.4705    0.4362      4064

    accuracy                         0.9581    118108
   macro avg     0.6938    0.7230    0.7072    118108
weighted avg     0.9613    0.9581    0.9596    118108


===== Remove C + D + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + D + V - Original

Features: 62
Accuracy           : 0.9681
Precision          : 0.9518
Recall             : 0.0778
F1 Score           : 0.1438
ROC-AUC            : 0.8633
PR-AUC             : 0.3982
Balanced Accuracy  : 0.5388
MCC                : 0.2672

Confusion Matrix:
[[114028     16]
 [  3748    316]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9682    0.9999    0.9838    114044
       Fraud     0.9518    0.0778    0.1438      4064

    accuracy                         0.9681    118108
   macro avg     0.9600    0.5388    0.5638    118108
weighted avg     0.9676    0.9681    0.9549    118108
LightGBM - Remove C + D + V - Original

Features: 62
Accuracy           : 0.8436
Precision          : 0.1426
Recall             : 0.7072
F1 Score           : 0.2374
ROC-AUC            : 0.8575
PR-AUC             : 0.3201
Balanced Accuracy  : 0.7778
MCC                : 0.2693

Confusion Matrix:
[[96766 17278]
 [ 1190  2874]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9879    0.8485    0.9129    114044
       Fraud     0.1426    0.7072    0.2374      4064

    accuracy                         0.8436    118108
   macro avg     0.5652    0.7778    0.5751    118108
weighted avg     0.9588    0.8436    0.8896    118108
XGBoost - Remove C + D + V - Original

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


===== Remove C + D + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + D + V - SMOTE

Features: 62
Accuracy           : 0.9667
Precision          : 0.5430
Recall             : 0.2037
F1 Score           : 0.2963
ROC-AUC            : 0.8456
PR-AUC             : 0.3253
Balanced Accuracy  : 0.5988
MCC                : 0.3191

Confusion Matrix:
[[113347    697]
 [  3236    828]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9722    0.9939    0.9829    114044
       Fraud     0.5430    0.2037    0.2963      4064

    accuracy                         0.9667    118108
   macro avg     0.7576    0.5988    0.6396    118108
weighted avg     0.9575    0.9667    0.9593    118108
LightGBM - Remove C + D + V - SMOTE

Features: 62
Accuracy           : 0.9576
Precision          : 0.3362
Recall             : 0.2372
F1 Score           : 0.2782
ROC-AUC            : 0.8216
PR-AUC             : 0.2445
Balanced Accuracy  : 0.6103
MCC                : 0.2612

Confusion Matrix:
[[112141   1903]
 [  3100    964]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9731    0.9833    0.9782    114044
       Fraud     0.3362    0.2372    0.2782      4064

    accuracy                         0.9576    118108
   macro avg     0.6547    0.6103    0.6282    118108
weighted avg     0.9512    0.9576    0.9541    118108
XGBoost - Remove C + D + V - SMOTE

Features: 62
Accuracy           : 0.9581
Precision          : 0.3385
Recall             : 0.2296
F1 Score           : 0.2736
ROC-AUC            : 0.8191
PR-AUC             : 0.2393
Balanced Accuracy  : 0.6068
MCC                : 0.2579

Confusion Matrix:
[[112221   1823]
 [  3131    933]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9729    0.9840    0.9784    114044
       Fraud     0.3385    0.2296    0.2736      4064

    accuracy                         0.9581    118108
   macro avg     0.6557    0.6068    0.6260    118108
weighted avg     0.9510    0.9581    0.9542    118108


===== Remove C + D + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + D + V - Undersampling

Features: 62
Accuracy           : 0.8528
Precision          : 0.1481
Recall             : 0.6897
F1 Score           : 0.2439
ROC-AUC            : 0.8602
PR-AUC             : 0.3316
Balanced Accuracy  : 0.7742
MCC                : 0.2725

Confusion Matrix:
[[97924 16120]
 [ 1261  2803]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9873    0.8587    0.9185    114044
       Fraud     0.1481    0.6897    0.2439      4064

    accuracy                         0.8528    118108
   macro avg     0.5677    0.7742    0.5812    118108
weighted avg     0.9584    0.8528    0.8953    118108
LightGBM - Remove C + D + V - Undersampling

Features: 62
Accuracy           : 0.8337
Precision          : 0.1331
Recall             : 0.6951
F1 Score           : 0.2234
ROC-AUC            : 0.8507
PR-AUC             : 0.3028
Balanced Accuracy  : 0.7669
MCC                : 0.2534

Confusion Matrix:
[[95642 18402]
 [ 1239  2825]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9872    0.8386    0.9069    114044
       Fraud     0.1331    0.6951    0.2234      4064

    accuracy                         0.8337    118108
   macro avg     0.5601    0.7669    0.5651    118108
weighted avg     0.9578    0.8337    0.8834    118108
XGBoost - Remove C + D + V - Undersampling

Features: 62
Accuracy           : 0.8272
Precision          : 0.1283
Recall             : 0.6939
F1 Score           : 0.2165
ROC-AUC            : 0.8442
PR-AUC             : 0.2810
Balanced Accuracy  : 0.7629
MCC                : 0.2463

Confusion Matrix:
[[94879 19165]
 [ 1244  2820]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9871    0.8320    0.9029    114044
       Fraud     0.1283    0.6939    0.2165      4064

    accuracy                         0.8272    118108
   macro avg     0.5577    0.7629    0.5597    118108
weighted avg     0.9575    0.8272    0.8793    118108


===== Remove C + D + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + D + V - SMOTE + Undersampling

Features: 62
Accuracy           : 0.9648
Precision          : 0.4801
Recall             : 0.2874
F1 Score           : 0.3596
ROC-AUC            : 0.8540
PR-AUC             : 0.3411
Balanced Accuracy  : 0.6382
MCC                : 0.3546

Confusion Matrix:
[[112779   1265]
 [  2896   1168]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9750    0.9889    0.9819    114044
       Fraud     0.4801    0.2874    0.3596      4064

    accuracy                         0.9648    118108
   macro avg     0.7275    0.6382    0.6707    118108
weighted avg     0.9579    0.9648    0.9605    118108
LightGBM - Remove C + D + V - SMOTE + Undersampling

Features: 62
Accuracy           : 0.9293
Precision          : 0.2277
Recall             : 0.4417
F1 Score           : 0.3005
ROC-AUC            : 0.8388
PR-AUC             : 0.2891
Balanced Accuracy  : 0.6942
MCC                : 0.2836

Confusion Matrix:
[[107957   6087]
 [  2269   1795]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9794    0.9466    0.9627    114044
       Fraud     0.2277    0.4417    0.3005      4064

    accuracy                         0.9293    118108
   macro avg     0.6036    0.6942    0.6316    118108
weighted avg     0.9536    0.9293    0.9400    118108
XGBoost - Remove C + D + V - SMOTE + Undersampling

Features: 62
Accuracy           : 0.9342
Precision          : 0.2346
Recall             : 0.4028
F1 Score           : 0.2965
ROC-AUC            : 0.8362
PR-AUC             : 0.2809
Balanced Accuracy  : 0.6780
MCC                : 0.2752

Confusion Matrix:
[[108703   5341]
 [  2427   1637]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9782    0.9532    0.9655    114044
       Fraud     0.2346    0.4028    0.2965      4064

    accuracy                         0.9342    118108
   macro avg     0.6064    0.6780    0.6310    118108
weighted avg     0.9526    0.9342    0.9425    118108


===== Remove C + M + id - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + M + id - Original

Features: 376
Accuracy           : 0.9719
Precision          : 0.8855
Recall             : 0.2094
F1 Score           : 0.3387
ROC-AUC            : 0.8797
PR-AUC             : 0.4796
Balanced Accuracy  : 0.6042
MCC                : 0.4229

Confusion Matrix:
[[113934    110]
 [  3213    851]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9726    0.9990    0.9856    114044
       Fraud     0.8855    0.2094    0.3387      4064

    accuracy                         0.9719    118108
   macro avg     0.9291    0.6042    0.6622    118108
weighted avg     0.9696    0.9719    0.9634    118108
LightGBM - Remove C + M + id - Original

Features: 376
Accuracy           : 0.8834
Precision          : 0.1867
Recall             : 0.7116
F1 Score           : 0.2958
ROC-AUC            : 0.8909
PR-AUC             : 0.4668
Balanced Accuracy  : 0.8006
MCC                : 0.3246

Confusion Matrix:
[[101448  12596]
 [  1172   2892]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9886    0.8896    0.9365    114044
       Fraud     0.1867    0.7116    0.2958      4064

    accuracy                         0.8834    118108
   macro avg     0.5877    0.8006    0.6161    118108
weighted avg     0.9610    0.8834    0.9144    118108
XGBoost - Remove C + M + id - Original

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


===== Remove C + M + id - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + M + id - SMOTE

Features: 376
Accuracy           : 0.9728
Precision          : 0.8046
Recall             : 0.2766
F1 Score           : 0.4116
ROC-AUC            : 0.8692
PR-AUC             : 0.4492
Balanced Accuracy  : 0.6371
MCC                : 0.4623

Confusion Matrix:
[[113771    273]
 [  2940   1124]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9748    0.9976    0.9861    114044
       Fraud     0.8046    0.2766    0.4116      4064

    accuracy                         0.9728    118108
   macro avg     0.8897    0.6371    0.6989    118108
weighted avg     0.9690    0.9728    0.9663    118108
LightGBM - Remove C + M + id - SMOTE

Features: 376
Accuracy           : 0.9722
Precision          : 0.7347
Recall             : 0.3012
F1 Score           : 0.4272
ROC-AUC            : 0.8827
PR-AUC             : 0.4640
Balanced Accuracy  : 0.6487
MCC                : 0.4595

Confusion Matrix:
[[113602    442]
 [  2840   1224]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9756    0.9961    0.9858    114044
       Fraud     0.7347    0.3012    0.4272      4064

    accuracy                         0.9722    118108
   macro avg     0.8552    0.6487    0.7065    118108
weighted avg     0.9673    0.9722    0.9665    118108
XGBoost - Remove C + M + id - SMOTE

Features: 376
Accuracy           : 0.9720
Precision          : 0.7280
Recall             : 0.2990
F1 Score           : 0.4239
ROC-AUC            : 0.8726
PR-AUC             : 0.4486
Balanced Accuracy  : 0.6475
MCC                : 0.4556

Confusion Matrix:
[[113590    454]
 [  2849   1215]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9755    0.9960    0.9857    114044
       Fraud     0.7280    0.2990    0.4239      4064

    accuracy                         0.9720    118108
   macro avg     0.8518    0.6475    0.7048    118108
weighted avg     0.9670    0.9720    0.9663    118108


===== Remove C + M + id - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + M + id - Undersampling

Features: 376
Accuracy           : 0.8534
Precision          : 0.1555
Recall             : 0.7362
F1 Score           : 0.2568
ROC-AUC            : 0.8794
PR-AUC             : 0.4173
Balanced Accuracy  : 0.7969
MCC                : 0.2931

Confusion Matrix:
[[97797 16247]
 [ 1072  2992]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9892    0.8575    0.9187    114044
       Fraud     0.1555    0.7362    0.2568      4064

    accuracy                         0.8534    118108
   macro avg     0.5723    0.7969    0.5877    118108
weighted avg     0.9605    0.8534    0.8959    118108
LightGBM - Remove C + M + id - Undersampling

Features: 376
Accuracy           : 0.8652
Precision          : 0.1696
Recall             : 0.7488
F1 Score           : 0.2766
ROC-AUC            : 0.8937
PR-AUC             : 0.4608
Balanced Accuracy  : 0.8091
MCC                : 0.3139

Confusion Matrix:
[[99149 14895]
 [ 1021  3043]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9898    0.8694    0.9257    114044
       Fraud     0.1696    0.7488    0.2766      4064

    accuracy                         0.8652    118108
   macro avg     0.5797    0.8091    0.6012    118108
weighted avg     0.9616    0.8652    0.9034    118108
XGBoost - Remove C + M + id - Undersampling

Features: 376
Accuracy           : 0.8643
Precision          : 0.1692
Recall             : 0.7530
F1 Score           : 0.2763
ROC-AUC            : 0.8925
PR-AUC             : 0.4600
Balanced Accuracy  : 0.8106
MCC                : 0.3144

Confusion Matrix:
[[99019 15025]
 [ 1004  3060]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9900    0.8683    0.9251    114044
       Fraud     0.1692    0.7530    0.2763      4064

    accuracy                         0.8643    118108
   macro avg     0.5796    0.8106    0.6007    118108
weighted avg     0.9617    0.8643    0.9028    118108


===== Remove C + M + id - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + M + id - SMOTE + Undersampling

Features: 376
Accuracy           : 0.9715
Precision          : 0.6611
Recall             : 0.3509
F1 Score           : 0.4584
ROC-AUC            : 0.8756
PR-AUC             : 0.4587
Balanced Accuracy  : 0.6722
MCC                : 0.4689

Confusion Matrix:
[[113313    731]
 [  2638   1426]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9772    0.9936    0.9854    114044
       Fraud     0.6611    0.3509    0.4584      4064

    accuracy                         0.9715    118108
   macro avg     0.8192    0.6722    0.7219    118108
weighted avg     0.9664    0.9715    0.9672    118108
LightGBM - Remove C + M + id - SMOTE + Undersampling

Features: 376
Accuracy           : 0.9600
Precision          : 0.4279
Recall             : 0.4813
F1 Score           : 0.4530
ROC-AUC            : 0.8923
PR-AUC             : 0.4749
Balanced Accuracy  : 0.7292
MCC                : 0.4332

Confusion Matrix:
[[111429   2615]
 [  2108   1956]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9814    0.9771    0.9792    114044
       Fraud     0.4279    0.4813    0.4530      4064

    accuracy                         0.9600    118108
   macro avg     0.7047    0.7292    0.7161    118108
weighted avg     0.9624    0.9600    0.9611    118108
XGBoost - Remove C + M + id - SMOTE + Undersampling

Features: 376
Accuracy           : 0.9607
Precision          : 0.4336
Recall             : 0.4656
F1 Score           : 0.4490
ROC-AUC            : 0.8871
PR-AUC             : 0.4682
Balanced Accuracy  : 0.7219
MCC                : 0.4290

Confusion Matrix:
[[111573   2471]
 [  2172   1892]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9809    0.9783    0.9796    114044
       Fraud     0.4336    0.4656    0.4490      4064

    accuracy                         0.9607    118108
   macro avg     0.7073    0.7219    0.7143    118108
weighted avg     0.9621    0.9607    0.9614    118108


===== Remove C + M + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + M + V - Original

Features: 75
Accuracy           : 0.9660
Precision          : 0.8125
Recall             : 0.0160
F1 Score           : 0.0314
ROC-AUC            : 0.8658
PR-AUC             : 0.3781
Balanced Accuracy  : 0.5079
MCC                : 0.1111

Confusion Matrix:
[[114029     15]
 [  3999     65]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9661    0.9999    0.9827    114044
       Fraud     0.8125    0.0160    0.0314      4064

    accuracy                         0.9660    118108
   macro avg     0.8893    0.5079    0.5070    118108
weighted avg     0.9608    0.9660    0.9500    118108
LightGBM - Remove C + M + V - Original

Features: 75
Accuracy           : 0.8630
Precision          : 0.1593
Recall             : 0.6969
F1 Score           : 0.2593
ROC-AUC            : 0.8753
PR-AUC             : 0.3799
Balanced Accuracy  : 0.7829
MCC                : 0.2884

Confusion Matrix:
[[99098 14946]
 [ 1232  2832]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9877    0.8689    0.9245    114044
       Fraud     0.1593    0.6969    0.2593      4064

    accuracy                         0.8630    118108
   macro avg     0.5735    0.7829    0.5919    118108
weighted avg     0.9592    0.8630    0.9016    118108
XGBoost - Remove C + M + V - Original

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


===== Remove C + M + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + M + V - SMOTE

Features: 75
Accuracy           : 0.9689
Precision          : 0.7014
Recall             : 0.1658
F1 Score           : 0.2683
ROC-AUC            : 0.8530
PR-AUC             : 0.3648
Balanced Accuracy  : 0.5817
MCC                : 0.3314

Confusion Matrix:
[[113757    287]
 [  3390    674]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9711    0.9975    0.9841    114044
       Fraud     0.7014    0.1658    0.2683      4064

    accuracy                         0.9689    118108
   macro avg     0.8362    0.5817    0.6262    118108
weighted avg     0.9618    0.9689    0.9595    118108
LightGBM - Remove C + M + V - SMOTE

Features: 75
Accuracy           : 0.9661
Precision          : 0.5138
Recall             : 0.2566
F1 Score           : 0.3423
ROC-AUC            : 0.8486
PR-AUC             : 0.3465
Balanced Accuracy  : 0.6240
MCC                : 0.3478

Confusion Matrix:
[[113057    987]
 [  3021   1043]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9740    0.9913    0.9826    114044
       Fraud     0.5138    0.2566    0.3423      4064

    accuracy                         0.9661    118108
   macro avg     0.7439    0.6240    0.6624    118108
weighted avg     0.9581    0.9661    0.9606    118108
XGBoost - Remove C + M + V - SMOTE

Features: 75
Accuracy           : 0.9656
Precision          : 0.4995
Recall             : 0.2682
F1 Score           : 0.3490
ROC-AUC            : 0.8471
PR-AUC             : 0.3387
Balanced Accuracy  : 0.6293
MCC                : 0.3501

Confusion Matrix:
[[112952   1092]
 [  2974   1090]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9743    0.9904    0.9823    114044
       Fraud     0.4995    0.2682    0.3490      4064

    accuracy                         0.9656    118108
   macro avg     0.7369    0.6293    0.6657    118108
weighted avg     0.9580    0.9656    0.9605    118108


===== Remove C + M + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + M + V - Undersampling

Features: 75
Accuracy           : 0.8610
Precision          : 0.1538
Recall             : 0.6752
F1 Score           : 0.2506
ROC-AUC            : 0.8601
PR-AUC             : 0.3203
Balanced Accuracy  : 0.7714
MCC                : 0.2764

Confusion Matrix:
[[98952 15092]
 [ 1320  2744]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9868    0.8677    0.9234    114044
       Fraud     0.1538    0.6752    0.2506      4064

    accuracy                         0.8610    118108
   macro avg     0.5703    0.7714    0.5870    118108
weighted avg     0.9582    0.8610    0.9003    118108
LightGBM - Remove C + M + V - Undersampling

Features: 75
Accuracy           : 0.8373
Precision          : 0.1415
Recall             : 0.7355
F1 Score           : 0.2373
ROC-AUC            : 0.8736
PR-AUC             : 0.3714
Balanced Accuracy  : 0.7882
MCC                : 0.2742

Confusion Matrix:
[[95906 18138]
 [ 1075  2989]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9889    0.8410    0.9090    114044
       Fraud     0.1415    0.7355    0.2373      4064

    accuracy                         0.8373    118108
   macro avg     0.5652    0.7882    0.5731    118108
weighted avg     0.9598    0.8373    0.8858    118108
XGBoost - Remove C + M + V - Undersampling

Features: 75
Accuracy           : 0.8289
Precision          : 0.1353
Recall             : 0.7367
F1 Score           : 0.2286
ROC-AUC            : 0.8704
PR-AUC             : 0.3670
Balanced Accuracy  : 0.7845
MCC                : 0.2658

Confusion Matrix:
[[94908 19136]
 [ 1070  2994]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9889    0.8322    0.9038    114044
       Fraud     0.1353    0.7367    0.2286      4064

    accuracy                         0.8289    118108
   macro avg     0.5621    0.7845    0.5662    118108
weighted avg     0.9595    0.8289    0.8806    118108


===== Remove C + M + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + M + V - SMOTE + Undersampling

Features: 75
Accuracy           : 0.9687
Precision          : 0.6074
Recall             : 0.2554
F1 Score           : 0.3596
ROC-AUC            : 0.8645
PR-AUC             : 0.3742
Balanced Accuracy  : 0.6248
MCC                : 0.3809

Confusion Matrix:
[[113373    671]
 [  3026   1038]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9740    0.9941    0.9840    114044
       Fraud     0.6074    0.2554    0.3596      4064

    accuracy                         0.9687    118108
   macro avg     0.7907    0.6248    0.6718    118108
weighted avg     0.9614    0.9687    0.9625    118108
LightGBM - Remove C + M + V - SMOTE + Undersampling

Features: 75
Accuracy           : 0.9513
Precision          : 0.3422
Recall             : 0.4513
F1 Score           : 0.3892
ROC-AUC            : 0.8657
PR-AUC             : 0.3769
Balanced Accuracy  : 0.7102
MCC                : 0.3681

Confusion Matrix:
[[110518   3526]
 [  2230   1834]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9802    0.9691    0.9746    114044
       Fraud     0.3422    0.4513    0.3892      4064

    accuracy                         0.9513    118108
   macro avg     0.6612    0.7102    0.6819    118108
weighted avg     0.9583    0.9513    0.9545    118108
XGBoost - Remove C + M + V - SMOTE + Undersampling

Features: 75
Accuracy           : 0.9515
Precision          : 0.3439
Recall             : 0.4520
F1 Score           : 0.3906
ROC-AUC            : 0.8673
PR-AUC             : 0.3799
Balanced Accuracy  : 0.7106
MCC                : 0.3695

Confusion Matrix:
[[110539   3505]
 [  2227   1837]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9803    0.9693    0.9747    114044
       Fraud     0.3439    0.4520    0.3906      4064

    accuracy                         0.9515    118108
   macro avg     0.6621    0.7106    0.6827    118108
weighted avg     0.9584    0.9515    0.9546    118108


===== Remove C + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + id + V - Original

Features: 46
Accuracy           : 0.9660
Precision          : 0.8732
Recall             : 0.0153
F1 Score           : 0.0300
ROC-AUC            : 0.8772
PR-AUC             : 0.3883
Balanced Accuracy  : 0.5076
MCC                : 0.1129

Confusion Matrix:
[[114035      9]
 [  4002     62]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9661    0.9999    0.9827    114044
       Fraud     0.8732    0.0153    0.0300      4064

    accuracy                         0.9660    118108
   macro avg     0.9197    0.5076    0.5064    118108
weighted avg     0.9629    0.9660    0.9499    118108
LightGBM - Remove C + id + V - Original

Features: 46
Accuracy           : 0.8668
Precision          : 0.1668
Recall             : 0.7188
F1 Score           : 0.2708
ROC-AUC            : 0.8848
PR-AUC             : 0.3519
Balanced Accuracy  : 0.7954
MCC                : 0.3030

Confusion Matrix:
[[99452 14592]
 [ 1143  2921]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9886    0.8720    0.9267    114044
       Fraud     0.1668    0.7188    0.2708      4064

    accuracy                         0.8668    118108
   macro avg     0.5777    0.7954    0.5987    118108
weighted avg     0.9604    0.8668    0.9041    118108
XGBoost - Remove C + id + V - Original

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


===== Remove C + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + id + V - SMOTE

Features: 46
Accuracy           : 0.9685
Precision          : 0.6787
Recall             : 0.1622
F1 Score           : 0.2618
ROC-AUC            : 0.8572
PR-AUC             : 0.3506
Balanced Accuracy  : 0.5797
MCC                : 0.3218

Confusion Matrix:
[[113732    312]
 [  3405    659]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9709    0.9973    0.9839    114044
       Fraud     0.6787    0.1622    0.2618      4064

    accuracy                         0.9685    118108
   macro avg     0.8248    0.5797    0.6228    118108
weighted avg     0.9609    0.9685    0.9591    118108
LightGBM - Remove C + id + V - SMOTE

Features: 46
Accuracy           : 0.9632
Precision          : 0.4452
Recall             : 0.2808
F1 Score           : 0.3443
ROC-AUC            : 0.8575
PR-AUC             : 0.3217
Balanced Accuracy  : 0.6341
MCC                : 0.3356

Confusion Matrix:
[[112622   1422]
 [  2923   1141]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9747    0.9875    0.9811    114044
       Fraud     0.4452    0.2808    0.3443      4064

    accuracy                         0.9632    118108
   macro avg     0.7099    0.6341    0.6627    118108
weighted avg     0.9565    0.9632    0.9592    118108
XGBoost - Remove C + id + V - SMOTE

Features: 46
Accuracy           : 0.9640
Precision          : 0.4610
Recall             : 0.2675
F1 Score           : 0.3385
ROC-AUC            : 0.8589
PR-AUC             : 0.3228
Balanced Accuracy  : 0.6282
MCC                : 0.3340

Confusion Matrix:
[[112773   1271]
 [  2977   1087]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9743    0.9889    0.9815    114044
       Fraud     0.4610    0.2675    0.3385      4064

    accuracy                         0.9640    118108
   macro avg     0.7176    0.6282    0.6600    118108
weighted avg     0.9566    0.9640    0.9594    118108


===== Remove C + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + id + V - Undersampling

Features: 46
Accuracy           : 0.8629
Precision          : 0.1605
Recall             : 0.7057
F1 Score           : 0.2615
ROC-AUC            : 0.8736
PR-AUC             : 0.3232
Balanced Accuracy  : 0.7871
MCC                : 0.2921

Confusion Matrix:
[[99042 15002]
 [ 1196  2868]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9881    0.8685    0.9244    114044
       Fraud     0.1605    0.7057    0.2615      4064

    accuracy                         0.8629    118108
   macro avg     0.5743    0.7871    0.5930    118108
weighted avg     0.9596    0.8629    0.9016    118108
LightGBM - Remove C + id + V - Undersampling

Features: 46
Accuracy           : 0.8409
Precision          : 0.1466
Recall             : 0.7512
F1 Score           : 0.2453
ROC-AUC            : 0.8795
PR-AUC             : 0.3275
Balanced Accuracy  : 0.7977
MCC                : 0.2847

Confusion Matrix:
[[96265 17779]
 [ 1011  3053]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9896    0.8441    0.9111    114044
       Fraud     0.1466    0.7512    0.2453      4064

    accuracy                         0.8409    118108
   macro avg     0.5681    0.7977    0.5782    118108
weighted avg     0.9606    0.8409    0.8882    118108
XGBoost - Remove C + id + V - Undersampling

Features: 46
Accuracy           : 0.8373
Precision          : 0.1443
Recall             : 0.7562
F1 Score           : 0.2423
ROC-AUC            : 0.8816
PR-AUC             : 0.3411
Balanced Accuracy  : 0.7982
MCC                : 0.2827

Confusion Matrix:
[[95817 18227]
 [  991  3073]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9898    0.8402    0.9089    114044
       Fraud     0.1443    0.7562    0.2423      4064

    accuracy                         0.8373    118108
   macro avg     0.5670    0.7982    0.5756    118108
weighted avg     0.9607    0.8373    0.8859    118108


===== Remove C + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + id + V - SMOTE + Undersampling

Features: 46
Accuracy           : 0.9680
Precision          : 0.5797
Recall             : 0.2532
F1 Score           : 0.3525
ROC-AUC            : 0.8682
PR-AUC             : 0.3632
Balanced Accuracy  : 0.6233
MCC                : 0.3695

Confusion Matrix:
[[113298    746]
 [  3035   1029]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9739    0.9935    0.9836    114044
       Fraud     0.5797    0.2532    0.3525      4064

    accuracy                         0.9680    118108
   macro avg     0.7768    0.6233    0.6680    118108
weighted avg     0.9603    0.9680    0.9619    118108
LightGBM - Remove C + id + V - SMOTE + Undersampling

Features: 46
Accuracy           : 0.9454
Precision          : 0.3076
Recall             : 0.4690
F1 Score           : 0.3715
ROC-AUC            : 0.8764
PR-AUC             : 0.3482
Balanced Accuracy  : 0.7157
MCC                : 0.3527

Confusion Matrix:
[[109754   4290]
 [  2158   1906]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9807    0.9624    0.9715    114044
       Fraud     0.3076    0.4690    0.3715      4064

    accuracy                         0.9454    118108
   macro avg     0.6442    0.7157    0.6715    118108
weighted avg     0.9576    0.9454    0.9508    118108
XGBoost - Remove C + id + V - SMOTE + Undersampling

Features: 46
Accuracy           : 0.9515
Precision          : 0.3389
Recall             : 0.4311
F1 Score           : 0.3795
ROC-AUC            : 0.8730
PR-AUC             : 0.3567
Balanced Accuracy  : 0.7006
MCC                : 0.3574

Confusion Matrix:
[[110627   3417]
 [  2312   1752]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9795    0.9700    0.9748    114044
       Fraud     0.3389    0.4311    0.3795      4064

    accuracy                         0.9515    118108
   macro avg     0.6592    0.7006    0.6771    118108
weighted avg     0.9575    0.9515    0.9543    118108


===== Remove D + M + id - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove D + M + id - Original

Features: 368
Accuracy           : 0.9730
Precision          : 0.8729
Recall             : 0.2517
F1 Score           : 0.3908
ROC-AUC            : 0.8881
PR-AUC             : 0.5096
Balanced Accuracy  : 0.6252
MCC                : 0.4605

Confusion Matrix:
[[113895    149]
 [  3041   1023]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9740    0.9987    0.9862    114044
       Fraud     0.8729    0.2517    0.3908      4064

    accuracy                         0.9730    118108
   macro avg     0.9234    0.6252    0.6885    118108
weighted avg     0.9705    0.9730    0.9657    118108
LightGBM - Remove D + M + id - Original

Features: 368
Accuracy           : 0.8988
Precision          : 0.2118
Recall             : 0.7136
F1 Score           : 0.3267
ROC-AUC            : 0.8943
PR-AUC             : 0.5076
Balanced Accuracy  : 0.8095
MCC                : 0.3525

Confusion Matrix:
[[103255  10789]
 [  1164   2900]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9889    0.9054    0.9453    114044
       Fraud     0.2118    0.7136    0.3267      4064

    accuracy                         0.8988    118108
   macro avg     0.6004    0.8095    0.6360    118108
weighted avg     0.9621    0.8988    0.9240    118108
XGBoost - Remove D + M + id - Original

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


===== Remove D + M + id - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove D + M + id - SMOTE

Features: 368
Accuracy           : 0.9740
Precision          : 0.8040
Recall             : 0.3250
F1 Score           : 0.4629
ROC-AUC            : 0.8814
PR-AUC             : 0.4841
Balanced Accuracy  : 0.6611
MCC                : 0.5015

Confusion Matrix:
[[113722    322]
 [  2743   1321]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9764    0.9972    0.9867    114044
       Fraud     0.8040    0.3250    0.4629      4064

    accuracy                         0.9740    118108
   macro avg     0.8902    0.6611    0.7248    118108
weighted avg     0.9705    0.9740    0.9687    118108
LightGBM - Remove D + M + id - SMOTE

Features: 368
Accuracy           : 0.9735
Precision          : 0.7435
Recall             : 0.3494
F1 Score           : 0.4754
ROC-AUC            : 0.8904
PR-AUC             : 0.5046
Balanced Accuracy  : 0.6726
MCC                : 0.4987

Confusion Matrix:
[[113554    490]
 [  2644   1420]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9772    0.9957    0.9864    114044
       Fraud     0.7435    0.3494    0.4754      4064

    accuracy                         0.9735    118108
   macro avg     0.8604    0.6726    0.7309    118108
weighted avg     0.9692    0.9735    0.9688    118108
XGBoost - Remove D + M + id - SMOTE

Features: 368
Accuracy           : 0.9733
Precision          : 0.7428
Recall             : 0.3425
F1 Score           : 0.4688
ROC-AUC            : 0.8805
PR-AUC             : 0.4715
Balanced Accuracy  : 0.6691
MCC                : 0.4935

Confusion Matrix:
[[113562    482]
 [  2672   1392]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9770    0.9958    0.9863    114044
       Fraud     0.7428    0.3425    0.4688      4064

    accuracy                         0.9733    118108
   macro avg     0.8599    0.6691    0.7276    118108
weighted avg     0.9690    0.9733    0.9685    118108


===== Remove D + M + id - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove D + M + id - Undersampling

Features: 368
Accuracy           : 0.8576
Precision          : 0.1617
Recall             : 0.7498
F1 Score           : 0.2660
ROC-AUC            : 0.8880
PR-AUC             : 0.4564
Balanced Accuracy  : 0.8056
MCC                : 0.3042

Confusion Matrix:
[[98246 15798]
 [ 1017  3047]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9898    0.8615    0.9212    114044
       Fraud     0.1617    0.7498    0.2660      4064

    accuracy                         0.8576    118108
   macro avg     0.5757    0.8056    0.5936    118108
weighted avg     0.9613    0.8576    0.8986    118108
LightGBM - Remove D + M + id - Undersampling

Features: 368
Accuracy           : 0.8779
Precision          : 0.1860
Recall             : 0.7547
F1 Score           : 0.2984
ROC-AUC            : 0.9009
PR-AUC             : 0.4992
Balanced Accuracy  : 0.8185
MCC                : 0.3350

Confusion Matrix:
[[100619  13425]
 [   997   3067]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9902    0.8823    0.9331    114044
       Fraud     0.1860    0.7547    0.2984      4064

    accuracy                         0.8779    118108
   macro avg     0.5881    0.8185    0.6158    118108
weighted avg     0.9625    0.8779    0.9113    118108
XGBoost - Remove D + M + id - Undersampling

Features: 368
Accuracy           : 0.8811
Precision          : 0.1899
Recall             : 0.7520
F1 Score           : 0.3032
ROC-AUC            : 0.8980
PR-AUC             : 0.4894
Balanced Accuracy  : 0.8188
MCC                : 0.3388

Confusion Matrix:
[[101009  13035]
 [  1008   3056]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9901    0.8857    0.9350    114044
       Fraud     0.1899    0.7520    0.3032      4064

    accuracy                         0.8811    118108
   macro avg     0.5900    0.8188    0.6191    118108
weighted avg     0.9626    0.8811    0.9133    118108


===== Remove D + M + id - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove D + M + id - SMOTE + Undersampling

Features: 368
Accuracy           : 0.9720
Precision          : 0.6562
Recall             : 0.3927
F1 Score           : 0.4914
ROC-AUC            : 0.8891
PR-AUC             : 0.4921
Balanced Accuracy  : 0.6927
MCC                : 0.4947

Confusion Matrix:
[[113208    836]
 [  2468   1596]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9787    0.9927    0.9856    114044
       Fraud     0.6562    0.3927    0.4914      4064

    accuracy                         0.9720    118108
   macro avg     0.8175    0.6927    0.7385    118108
weighted avg     0.9676    0.9720    0.9686    118108
LightGBM - Remove D + M + id - SMOTE + Undersampling

Features: 368
Accuracy           : 0.9627
Precision          : 0.4628
Recall             : 0.5244
F1 Score           : 0.4916
ROC-AUC            : 0.8950
PR-AUC             : 0.5156
Balanced Accuracy  : 0.7513
MCC                : 0.4733

Confusion Matrix:
[[111570   2474]
 [  1933   2131]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9830    0.9783    0.9806    114044
       Fraud     0.4628    0.5244    0.4916      4064

    accuracy                         0.9627    118108
   macro avg     0.7229    0.7513    0.7361    118108
weighted avg     0.9651    0.9627    0.9638    118108
XGBoost - Remove D + M + id - SMOTE + Undersampling

Features: 368
Accuracy           : 0.9624
Precision          : 0.4575
Recall             : 0.5010
F1 Score           : 0.4783
ROC-AUC            : 0.8926
PR-AUC             : 0.5138
Balanced Accuracy  : 0.7399
MCC                : 0.4593

Confusion Matrix:
[[111630   2414]
 [  2028   2036]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9822    0.9788    0.9805    114044
       Fraud     0.4575    0.5010    0.4783      4064

    accuracy                         0.9624    118108
   macro avg     0.7198    0.7399    0.7294    118108
weighted avg     0.9641    0.9624    0.9632    118108


===== Remove D + M + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove D + M + V - Original

Features: 67
Accuracy           : 0.9727
Precision          : 0.9152
Recall             : 0.2283
F1 Score           : 0.3655
ROC-AUC            : 0.9020
PR-AUC             : 0.5709
Balanced Accuracy  : 0.6138
MCC                : 0.4497

Confusion Matrix:
[[113958     86]
 [  3136    928]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9732    0.9992    0.9861    114044
       Fraud     0.9152    0.2283    0.3655      4064

    accuracy                         0.9727    118108
   macro avg     0.9442    0.6138    0.6758    118108
weighted avg     0.9712    0.9727    0.9647    118108
LightGBM - Remove D + M + V - Original

Features: 67
Accuracy           : 0.8880
Precision          : 0.1913
Recall             : 0.6991
F1 Score           : 0.3004
ROC-AUC            : 0.8892
PR-AUC             : 0.4894
Balanced Accuracy  : 0.7969
MCC                : 0.3265

Confusion Matrix:
[[102036  12008]
 [  1223   2841]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9882    0.8947    0.9391    114044
       Fraud     0.1913    0.6991    0.3004      4064

    accuracy                         0.8880    118108
   macro avg     0.5897    0.7969    0.6198    118108
weighted avg     0.9607    0.8880    0.9171    118108
XGBoost - Remove D + M + V - Original

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


===== Remove D + M + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove D + M + V - SMOTE

Features: 67
Accuracy           : 0.9754
Precision          : 0.8001
Recall             : 0.3802
F1 Score           : 0.5154
ROC-AUC            : 0.8869
PR-AUC             : 0.5260
Balanced Accuracy  : 0.6884
MCC                : 0.5416

Confusion Matrix:
[[113658    386]
 [  2519   1545]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9783    0.9966    0.9874    114044
       Fraud     0.8001    0.3802    0.5154      4064

    accuracy                         0.9754    118108
   macro avg     0.8892    0.6884    0.7514    118108
weighted avg     0.9722    0.9754    0.9711    118108
LightGBM - Remove D + M + V - SMOTE

Features: 67
Accuracy           : 0.9708
Precision          : 0.6241
Recall             : 0.3792
F1 Score           : 0.4718
ROC-AUC            : 0.8668
PR-AUC             : 0.4609
Balanced Accuracy  : 0.6855
MCC                : 0.4727

Confusion Matrix:
[[113116    928]
 [  2523   1541]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9782    0.9919    0.9850    114044
       Fraud     0.6241    0.3792    0.4718      4064

    accuracy                         0.9708    118108
   macro avg     0.8012    0.6855    0.7284    118108
weighted avg     0.9660    0.9708    0.9673    118108
XGBoost - Remove D + M + V - SMOTE

Features: 67
Accuracy           : 0.9709
Precision          : 0.6303
Recall             : 0.3708
F1 Score           : 0.4669
ROC-AUC            : 0.8638
PR-AUC             : 0.4525
Balanced Accuracy  : 0.6815
MCC                : 0.4699

Confusion Matrix:
[[113160    884]
 [  2557   1507]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9779    0.9922    0.9850    114044
       Fraud     0.6303    0.3708    0.4669      4064

    accuracy                         0.9709    118108
   macro avg     0.8041    0.6815    0.7260    118108
weighted avg     0.9659    0.9709    0.9672    118108


===== Remove D + M + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove D + M + V - Undersampling

Features: 67
Accuracy           : 0.8958
Precision          : 0.2045
Recall             : 0.7015
F1 Score           : 0.3166
ROC-AUC            : 0.8979
PR-AUC             : 0.4778
Balanced Accuracy  : 0.8021
MCC                : 0.3413

Confusion Matrix:
[[102951  11093]
 [  1213   2851]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9884    0.9027    0.9436    114044
       Fraud     0.2045    0.7015    0.3166      4064

    accuracy                         0.8958    118108
   macro avg     0.5964    0.8021    0.6301    118108
weighted avg     0.9614    0.8958    0.9220    118108
LightGBM - Remove D + M + V - Undersampling

Features: 67
Accuracy           : 0.8722
Precision          : 0.1722
Recall             : 0.7126
F1 Score           : 0.2774
ROC-AUC            : 0.8853
PR-AUC             : 0.4692
Balanced Accuracy  : 0.7953
MCC                : 0.3080

Confusion Matrix:
[[100121  13923]
 [  1168   2896]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9885    0.8779    0.9299    114044
       Fraud     0.1722    0.7126    0.2774      4064

    accuracy                         0.8722    118108
   macro avg     0.5803    0.7953    0.6036    118108
weighted avg     0.9604    0.8722    0.9075    118108
XGBoost - Remove D + M + V - Undersampling

Features: 67
Accuracy           : 0.8837
Precision          : 0.1857
Recall             : 0.7028
F1 Score           : 0.2937
ROC-AUC            : 0.8850
PR-AUC             : 0.4702
Balanced Accuracy  : 0.7965
MCC                : 0.3211

Confusion Matrix:
[[101517  12527]
 [  1208   2856]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9882    0.8902    0.9366    114044
       Fraud     0.1857    0.7028    0.2937      4064

    accuracy                         0.8837    118108
   macro avg     0.5869    0.7965    0.6152    118108
weighted avg     0.9606    0.8837    0.9145    118108


===== Remove D + M + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove D + M + V - SMOTE + Undersampling

Features: 67
Accuracy           : 0.9744
Precision          : 0.7022
Recall             : 0.4439
F1 Score           : 0.5439
ROC-AUC            : 0.8955
PR-AUC             : 0.5249
Balanced Accuracy  : 0.7186
MCC                : 0.5463

Confusion Matrix:
[[113279    765]
 [  2260   1804]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9804    0.9933    0.9868    114044
       Fraud     0.7022    0.4439    0.5439      4064

    accuracy                         0.9744    118108
   macro avg     0.8413    0.7186    0.7654    118108
weighted avg     0.9709    0.9744    0.9716    118108
LightGBM - Remove D + M + V - SMOTE + Undersampling

Features: 67
Accuracy           : 0.9587
Precision          : 0.4181
Recall             : 0.5148
F1 Score           : 0.4615
ROC-AUC            : 0.8810
PR-AUC             : 0.4838
Balanced Accuracy  : 0.7446
MCC                : 0.4428

Confusion Matrix:
[[111133   2911]
 [  1972   2092]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9826    0.9745    0.9785    114044
       Fraud     0.4181    0.5148    0.4615      4064

    accuracy                         0.9587    118108
   macro avg     0.7004    0.7446    0.7200    118108
weighted avg     0.9631    0.9587    0.9607    118108
XGBoost - Remove D + M + V - SMOTE + Undersampling

Features: 67
Accuracy           : 0.9616
Precision          : 0.4467
Recall             : 0.4857
F1 Score           : 0.4654
ROC-AUC            : 0.8760
PR-AUC             : 0.4712
Balanced Accuracy  : 0.7321
MCC                : 0.4459

Confusion Matrix:
[[111599   2445]
 [  2090   1974]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9816    0.9786    0.9801    114044
       Fraud     0.4467    0.4857    0.4654      4064

    accuracy                         0.9616    118108
   macro avg     0.7142    0.7321    0.7227    118108
weighted avg     0.9632    0.9616    0.9624    118108


===== Remove D + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove D + id + V - Original

Features: 38
Accuracy           : 0.9729
Precision          : 0.8916
Recall             : 0.2409
F1 Score           : 0.3793
ROC-AUC            : 0.9005
PR-AUC             : 0.5686
Balanced Accuracy  : 0.6199
MCC                : 0.4556

Confusion Matrix:
[[113925    119]
 [  3085    979]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9736    0.9990    0.9861    114044
       Fraud     0.8916    0.2409    0.3793      4064

    accuracy                         0.9729    118108
   macro avg     0.9326    0.6199    0.6827    118108
weighted avg     0.9708    0.9729    0.9653    118108
LightGBM - Remove D + id + V - Original

Features: 38
Accuracy           : 0.8936
Precision          : 0.2052
Recall             : 0.7281
F1 Score           : 0.3201
ROC-AUC            : 0.8971
PR-AUC             : 0.4912
Balanced Accuracy  : 0.8138
MCC                : 0.3494

Confusion Matrix:
[[102581  11463]
 [  1105   2959]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9893    0.8995    0.9423    114044
       Fraud     0.2052    0.7281    0.3201      4064

    accuracy                         0.8936    118108
   macro avg     0.5973    0.8138    0.6312    118108
weighted avg     0.9624    0.8936    0.9209    118108
XGBoost - Remove D + id + V - Original

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


===== Remove D + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove D + id + V - SMOTE

Features: 38
Accuracy           : 0.9754
Precision          : 0.7958
Recall             : 0.3826
F1 Score           : 0.5168
ROC-AUC            : 0.8876
PR-AUC             : 0.5210
Balanced Accuracy  : 0.6896
MCC                : 0.5418

Confusion Matrix:
[[113645    399]
 [  2509   1555]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9784    0.9965    0.9874    114044
       Fraud     0.7958    0.3826    0.5168      4064

    accuracy                         0.9754    118108
   macro avg     0.8871    0.6896    0.7521    118108
weighted avg     0.9721    0.9754    0.9712    118108
LightGBM - Remove D + id + V - SMOTE

Features: 38
Accuracy           : 0.9704
Precision          : 0.6084
Recall             : 0.3903
F1 Score           : 0.4755
ROC-AUC            : 0.8759
PR-AUC             : 0.4635
Balanced Accuracy  : 0.6907
MCC                : 0.4731

Confusion Matrix:
[[113023   1021]
 [  2478   1586]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9785    0.9910    0.9848    114044
       Fraud     0.6084    0.3903    0.4755      4064

    accuracy                         0.9704    118108
   macro avg     0.7935    0.6907    0.7301    118108
weighted avg     0.9658    0.9704    0.9672    118108
XGBoost - Remove D + id + V - SMOTE

Features: 38
Accuracy           : 0.9710
Precision          : 0.6347
Recall             : 0.3669
F1 Score           : 0.4650
ROC-AUC            : 0.8731
PR-AUC             : 0.4654
Balanced Accuracy  : 0.6797
MCC                : 0.4692

Confusion Matrix:
[[113186    858]
 [  2573   1491]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9778    0.9925    0.9851    114044
       Fraud     0.6347    0.3669    0.4650      4064

    accuracy                         0.9710    118108
   macro avg     0.8063    0.6797    0.7250    118108
weighted avg     0.9660    0.9710    0.9672    118108


===== Remove D + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove D + id + V - Undersampling

Features: 38
Accuracy           : 0.8978
Precision          : 0.2111
Recall             : 0.7202
F1 Score           : 0.3265
ROC-AUC            : 0.8992
PR-AUC             : 0.4567
Balanced Accuracy  : 0.8122
MCC                : 0.3536

Confusion Matrix:
[[103108  10936]
 [  1137   2927]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9891    0.9041    0.9447    114044
       Fraud     0.2111    0.7202    0.3265      4064

    accuracy                         0.8978    118108
   macro avg     0.6001    0.8122    0.6356    118108
weighted avg     0.9623    0.8978    0.9234    118108
LightGBM - Remove D + id + V - Undersampling

Features: 38
Accuracy           : 0.8796
Precision          : 0.1838
Recall             : 0.7264
F1 Score           : 0.2934
ROC-AUC            : 0.8875
PR-AUC             : 0.4583
Balanced Accuracy  : 0.8057
MCC                : 0.3251

Confusion Matrix:
[[100934  13110]
 [  1112   2952]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9891    0.8850    0.9342    114044
       Fraud     0.1838    0.7264    0.2934      4064

    accuracy                         0.8796    118108
   macro avg     0.5864    0.8057    0.6138    118108
weighted avg     0.9614    0.8796    0.9121    118108
XGBoost - Remove D + id + V - Undersampling

Features: 38
Accuracy           : 0.8801
Precision          : 0.1826
Recall             : 0.7148
F1 Score           : 0.2909
ROC-AUC            : 0.8841
PR-AUC             : 0.4599
Balanced Accuracy  : 0.8004
MCC                : 0.3208

Confusion Matrix:
[[101041  13003]
 [  1159   2905]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9887    0.8860    0.9345    114044
       Fraud     0.1826    0.7148    0.2909      4064

    accuracy                         0.8801    118108
   macro avg     0.5856    0.8004    0.6127    118108
weighted avg     0.9609    0.8801    0.9124    118108


===== Remove D + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove D + id + V - SMOTE + Undersampling

Features: 38
Accuracy           : 0.9740
Precision          : 0.6874
Recall             : 0.4486
F1 Score           : 0.5429
ROC-AUC            : 0.8920
PR-AUC             : 0.5181
Balanced Accuracy  : 0.7207
MCC                : 0.5429

Confusion Matrix:
[[113215    829]
 [  2241   1823]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9806    0.9927    0.9866    114044
       Fraud     0.6874    0.4486    0.5429      4064

    accuracy                         0.9740    118108
   macro avg     0.8340    0.7207    0.7648    118108
weighted avg     0.9705    0.9740    0.9714    118108
LightGBM - Remove D + id + V - SMOTE + Undersampling

Features: 38
Accuracy           : 0.9549
Precision          : 0.3878
Recall             : 0.5364
F1 Score           : 0.4502
ROC-AUC            : 0.8889
PR-AUC             : 0.4908
Balanced Accuracy  : 0.7531
MCC                : 0.4334

Confusion Matrix:
[[110603   3441]
 [  1884   2180]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9833    0.9698    0.9765    114044
       Fraud     0.3878    0.5364    0.4502      4064

    accuracy                         0.9549    118108
   macro avg     0.6855    0.7531    0.7133    118108
weighted avg     0.9628    0.9549    0.9584    118108
XGBoost - Remove D + id + V - SMOTE + Undersampling

Features: 38
Accuracy           : 0.9603
Precision          : 0.4323
Recall             : 0.4921
F1 Score           : 0.4603
ROC-AUC            : 0.8835
PR-AUC             : 0.4721
Balanced Accuracy  : 0.7345
MCC                : 0.4408

Confusion Matrix:
[[111418   2626]
 [  2064   2000]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9818    0.9770    0.9794    114044
       Fraud     0.4323    0.4921    0.4603      4064

    accuracy                         0.9603    118108
   macro avg     0.7071    0.7345    0.7198    118108
weighted avg     0.9629    0.9603    0.9615    118108


===== Remove M + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove M + id + V - Original

Features: 51
Accuracy           : 0.9711
Precision          : 0.8900
Recall             : 0.1811
F1 Score           : 0.3010
ROC-AUC            : 0.9000
PR-AUC             : 0.5399
Balanced Accuracy  : 0.5902
MCC                : 0.3941

Confusion Matrix:
[[113953     91]
 [  3328    736]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9716    0.9992    0.9852    114044
       Fraud     0.8900    0.1811    0.3010      4064

    accuracy                         0.9711    118108
   macro avg     0.9308    0.5902    0.6431    118108
weighted avg     0.9688    0.9711    0.9617    118108
LightGBM - Remove M + id + V - Original

Features: 51
Accuracy           : 0.8879
Precision          : 0.1992
Recall             : 0.7475
F1 Score           : 0.3146
ROC-AUC            : 0.9069
PR-AUC             : 0.5002
Balanced Accuracy  : 0.8202
MCC                : 0.3482

Confusion Matrix:
[[101834  12210]
 [  1026   3038]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9900    0.8929    0.9390    114044
       Fraud     0.1992    0.7475    0.3146      4064

    accuracy                         0.8879    118108
   macro avg     0.5946    0.8202    0.6268    118108
weighted avg     0.9628    0.8879    0.9175    118108
XGBoost - Remove M + id + V - Original

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


===== Remove M + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove M + id + V - SMOTE

Features: 51
Accuracy           : 0.9739
Precision          : 0.7976
Recall             : 0.3238
F1 Score           : 0.4606
ROC-AUC            : 0.8920
PR-AUC             : 0.5231
Balanced Accuracy  : 0.6604
MCC                : 0.4984

Confusion Matrix:
[[113710    334]
 [  2748   1316]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9764    0.9971    0.9866    114044
       Fraud     0.7976    0.3238    0.4606      4064

    accuracy                         0.9739    118108
   macro avg     0.8870    0.6604    0.7236    118108
weighted avg     0.9703    0.9739    0.9685    118108
LightGBM - Remove M + id + V - SMOTE

Features: 51
Accuracy           : 0.9714
Precision          : 0.6358
Recall             : 0.3935
F1 Score           : 0.4861
ROC-AUC            : 0.8932
PR-AUC             : 0.4943
Balanced Accuracy  : 0.6927
MCC                : 0.4866

Confusion Matrix:
[[113128    916]
 [  2465   1599]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9787    0.9920    0.9853    114044
       Fraud     0.6358    0.3935    0.4861      4064

    accuracy                         0.9714    118108
   macro avg     0.8072    0.6927    0.7357    118108
weighted avg     0.9669    0.9714    0.9681    118108
XGBoost - Remove M + id + V - SMOTE

Features: 51
Accuracy           : 0.9703
Precision          : 0.6098
Recall             : 0.3834
F1 Score           : 0.4708
ROC-AUC            : 0.8881
PR-AUC             : 0.4830
Balanced Accuracy  : 0.6873
MCC                : 0.4694

Confusion Matrix:
[[113047    997]
 [  2506   1558]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9783    0.9913    0.9847    114044
       Fraud     0.6098    0.3834    0.4708      4064

    accuracy                         0.9703    118108
   macro avg     0.7940    0.6873    0.7278    118108
weighted avg     0.9656    0.9703    0.9671    118108


===== Remove M + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove M + id + V - Undersampling

Features: 51
Accuracy           : 0.8964
Precision          : 0.2082
Recall             : 0.7173
F1 Score           : 0.3227
ROC-AUC            : 0.8951
PR-AUC             : 0.4548
Balanced Accuracy  : 0.8100
MCC                : 0.3496

Confusion Matrix:
[[102957  11087]
 [  1149   2915]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9890    0.9028    0.9439    114044
       Fraud     0.2082    0.7173    0.3227      4064

    accuracy                         0.8964    118108
   macro avg     0.5986    0.8100    0.6333    118108
weighted avg     0.9621    0.8964    0.9225    118108
LightGBM - Remove M + id + V - Undersampling

Features: 51
Accuracy           : 0.8671
Precision          : 0.1718
Recall             : 0.7493
F1 Score           : 0.2796
ROC-AUC            : 0.8992
PR-AUC             : 0.4708
Balanced Accuracy  : 0.8103
MCC                : 0.3168

Confusion Matrix:
[[99370 14674]
 [ 1019  3045]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9898    0.8713    0.9268    114044
       Fraud     0.1718    0.7493    0.2796      4064

    accuracy                         0.8671    118108
   macro avg     0.5808    0.8103    0.6032    118108
weighted avg     0.9617    0.8671    0.9045    118108
XGBoost - Remove M + id + V - Undersampling

Features: 51
Accuracy           : 0.8757
Precision          : 0.1827
Recall             : 0.7520
F1 Score           : 0.2939
ROC-AUC            : 0.9020
PR-AUC             : 0.4847
Balanced Accuracy  : 0.8160
MCC                : 0.3304

Confusion Matrix:
[[100369  13675]
 [  1008   3056]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9901    0.8801    0.9318    114044
       Fraud     0.1827    0.7520    0.2939      4064

    accuracy                         0.8757    118108
   macro avg     0.5864    0.8160    0.6129    118108
weighted avg     0.9623    0.8757    0.9099    118108


===== Remove M + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove M + id + V - SMOTE + Undersampling

Features: 51
Accuracy           : 0.9731
Precision          : 0.6915
Recall             : 0.3954
F1 Score           : 0.5031
ROC-AUC            : 0.9002
PR-AUC             : 0.5198
Balanced Accuracy  : 0.6946
MCC                : 0.5107

Confusion Matrix:
[[113327    717]
 [  2457   1607]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9788    0.9937    0.9862    114044
       Fraud     0.6915    0.3954    0.5031      4064

    accuracy                         0.9731    118108
   macro avg     0.8351    0.6946    0.7447    118108
weighted avg     0.9689    0.9731    0.9696    118108
LightGBM - Remove M + id + V - SMOTE + Undersampling

Features: 51
Accuracy           : 0.9581
Precision          : 0.4170
Recall             : 0.5497
F1 Score           : 0.4743
ROC-AUC            : 0.9022
PR-AUC             : 0.5081
Balanced Accuracy  : 0.7612
MCC                : 0.4575

Confusion Matrix:
[[110921   3123]
 [  1830   2234]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9838    0.9726    0.9782    114044
       Fraud     0.4170    0.5497    0.4743      4064

    accuracy                         0.9581    118108
   macro avg     0.7004    0.7612    0.7262    118108
weighted avg     0.9643    0.9581    0.9608    118108
XGBoost - Remove M + id + V - SMOTE + Undersampling

Features: 51
Accuracy           : 0.9598
Precision          : 0.4321
Recall             : 0.5354
F1 Score           : 0.4782
ROC-AUC            : 0.9005
PR-AUC             : 0.5029
Balanced Accuracy  : 0.7552
MCC                : 0.4604

Confusion Matrix:
[[111184   2860]
 [  1888   2176]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9833    0.9749    0.9791    114044
       Fraud     0.4321    0.5354    0.4782      4064

    accuracy                         0.9598    118108
   macro avg     0.7077    0.7552    0.7287    118108
weighted avg     0.9643    0.9598    0.9619    118108


===== Remove C + D + M + id - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + D + M + id - Original

Features: 354
Accuracy           : 0.9720
Precision          : 0.8684
Recall             : 0.2192
F1 Score           : 0.3501
ROC-AUC            : 0.8725
PR-AUC             : 0.4664
Balanced Accuracy  : 0.6090
MCC                : 0.4283

Confusion Matrix:
[[113909    135]
 [  3173    891]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9729    0.9988    0.9857    114044
       Fraud     0.8684    0.2192    0.3501      4064

    accuracy                         0.9720    118108
   macro avg     0.9207    0.6090    0.6679    118108
weighted avg     0.9693    0.9720    0.9638    118108
LightGBM - Remove C + D + M + id - Original

Features: 354
Accuracy           : 0.8867
Precision          : 0.1883
Recall             : 0.6924
F1 Score           : 0.2960
ROC-AUC            : 0.8822
PR-AUC             : 0.4639
Balanced Accuracy  : 0.7930
MCC                : 0.3213

Confusion Matrix:
[[101910  12134]
 [  1250   2814]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9879    0.8936    0.9384    114044
       Fraud     0.1883    0.6924    0.2960      4064

    accuracy                         0.8867    118108
   macro avg     0.5881    0.7930    0.6172    118108
weighted avg     0.9604    0.8867    0.9163    118108
XGBoost - Remove C + D + M + id - Original

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


===== Remove C + D + M + id - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + D + M + id - SMOTE

Features: 354
Accuracy           : 0.9727
Precision          : 0.7854
Recall             : 0.2827
F1 Score           : 0.4158
ROC-AUC            : 0.8635
PR-AUC             : 0.4437
Balanced Accuracy  : 0.6400
MCC                : 0.4614

Confusion Matrix:
[[113730    314]
 [  2915   1149]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9750    0.9972    0.9860    114044
       Fraud     0.7854    0.2827    0.4158      4064

    accuracy                         0.9727    118108
   macro avg     0.8802    0.6400    0.7009    118108
weighted avg     0.9685    0.9727    0.9664    118108
LightGBM - Remove C + D + M + id - SMOTE

Features: 354
Accuracy           : 0.9719
Precision          : 0.7175
Recall             : 0.3012
F1 Score           : 0.4243
ROC-AUC            : 0.8757
PR-AUC             : 0.4584
Balanced Accuracy  : 0.6485
MCC                : 0.4537

Confusion Matrix:
[[113562    482]
 [  2840   1224]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9756    0.9958    0.9856    114044
       Fraud     0.7175    0.3012    0.4243      4064

    accuracy                         0.9719    118108
   macro avg     0.8465    0.6485    0.7049    118108
weighted avg     0.9667    0.9719    0.9663    118108
XGBoost - Remove C + D + M + id - SMOTE

Features: 354
Accuracy           : 0.9717
Precision          : 0.7162
Recall             : 0.2950
F1 Score           : 0.4179
ROC-AUC            : 0.8651
PR-AUC             : 0.4321
Balanced Accuracy  : 0.6454
MCC                : 0.4485

Confusion Matrix:
[[113569    475]
 [  2865   1199]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9754    0.9958    0.9855    114044
       Fraud     0.7162    0.2950    0.4179      4064

    accuracy                         0.9717    118108
   macro avg     0.8458    0.6454    0.7017    118108
weighted avg     0.9665    0.9717    0.9660    118108


===== Remove C + D + M + id - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + D + M + id - Undersampling

Features: 354
Accuracy           : 0.8400
Precision          : 0.1435
Recall             : 0.7345
F1 Score           : 0.2401
ROC-AUC            : 0.8719
PR-AUC             : 0.4151
Balanced Accuracy  : 0.7891
MCC                : 0.2767

Confusion Matrix:
[[96230 17814]
 [ 1079  2985]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9889    0.8438    0.9106    114044
       Fraud     0.1435    0.7345    0.2401      4064

    accuracy                         0.8400    118108
   macro avg     0.5662    0.7891    0.5754    118108
weighted avg     0.9598    0.8400    0.8875    118108
LightGBM - Remove C + D + M + id - Undersampling

Features: 354
Accuracy           : 0.8676
Precision          : 0.1692
Recall             : 0.7286
F1 Score           : 0.2747
ROC-AUC            : 0.8856
PR-AUC             : 0.4536
Balanced Accuracy  : 0.8006
MCC                : 0.3085

Confusion Matrix:
[[99510 14534]
 [ 1103  2961]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9890    0.8726    0.9272    114044
       Fraud     0.1692    0.7286    0.2747      4064

    accuracy                         0.8676    118108
   macro avg     0.5791    0.8006    0.6009    118108
weighted avg     0.9608    0.8676    0.9047    118108
XGBoost - Remove C + D + M + id - Undersampling

Features: 354
Accuracy           : 0.8638
Precision          : 0.1652
Recall             : 0.7298
F1 Score           : 0.2694
ROC-AUC            : 0.8837
PR-AUC             : 0.4483
Balanced Accuracy  : 0.7992
MCC                : 0.3038

Confusion Matrix:
[[99057 14987]
 [ 1098  2966]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9890    0.8686    0.9249    114044
       Fraud     0.1652    0.7298    0.2694      4064

    accuracy                         0.8638    118108
   macro avg     0.5771    0.7992    0.5972    118108
weighted avg     0.9607    0.8638    0.9024    118108


===== Remove C + D + M + id - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + D + M + id - SMOTE + Undersampling

Features: 354
Accuracy           : 0.9704
Precision          : 0.6219
Recall             : 0.3597
F1 Score           : 0.4558
ROC-AUC            : 0.8695
PR-AUC             : 0.4492
Balanced Accuracy  : 0.6760
MCC                : 0.4593

Confusion Matrix:
[[113155    889]
 [  2602   1462]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9775    0.9922    0.9848    114044
       Fraud     0.6219    0.3597    0.4558      4064

    accuracy                         0.9704    118108
   macro avg     0.7997    0.6760    0.7203    118108
weighted avg     0.9653    0.9704    0.9666    118108
LightGBM - Remove C + D + M + id - SMOTE + Undersampling

Features: 354
Accuracy           : 0.9586
Precision          : 0.4113
Recall             : 0.4734
F1 Score           : 0.4402
ROC-AUC            : 0.8838
PR-AUC             : 0.4633
Balanced Accuracy  : 0.7246
MCC                : 0.4199

Confusion Matrix:
[[111290   2754]
 [  2140   1924]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9811    0.9759    0.9785    114044
       Fraud     0.4113    0.4734    0.4402      4064

    accuracy                         0.9586    118108
   macro avg     0.6962    0.7246    0.7093    118108
weighted avg     0.9615    0.9586    0.9600    118108
XGBoost - Remove C + D + M + id - SMOTE + Undersampling

Features: 354
Accuracy           : 0.9607
Precision          : 0.4328
Recall             : 0.4616
F1 Score           : 0.4467
ROC-AUC            : 0.8769
PR-AUC             : 0.4556
Balanced Accuracy  : 0.7200
MCC                : 0.4266

Confusion Matrix:
[[111585   2459]
 [  2188   1876]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9808    0.9784    0.9796    114044
       Fraud     0.4328    0.4616    0.4467      4064

    accuracy                         0.9607    118108
   macro avg     0.7068    0.7200    0.7132    118108
weighted avg     0.9619    0.9607    0.9613    118108


===== Remove C + D + M + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + D + M + V - Original

Features: 53
Accuracy           : 0.9677
Precision          : 0.9536
Recall             : 0.0657
F1 Score           : 0.1229
ROC-AUC            : 0.8441
PR-AUC             : 0.3689
Balanced Accuracy  : 0.5328
MCC                : 0.2458

Confusion Matrix:
[[114031     13]
 [  3797    267]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9678    0.9999    0.9836    114044
       Fraud     0.9536    0.0657    0.1229      4064

    accuracy                         0.9677    118108
   macro avg     0.9607    0.5328    0.5532    118108
weighted avg     0.9673    0.9677    0.9540    118108
LightGBM - Remove C + D + M + V - Original

Features: 53
Accuracy           : 0.8647
Precision          : 0.1495
Recall             : 0.6252
F1 Score           : 0.2413
ROC-AUC            : 0.8332
PR-AUC             : 0.2989
Balanced Accuracy  : 0.7492
MCC                : 0.2588

Confusion Matrix:
[[99585 14459]
 [ 1523  2541]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9849    0.8732    0.9257    114044
       Fraud     0.1495    0.6252    0.2413      4064

    accuracy                         0.8647    118108
   macro avg     0.5672    0.7492    0.5835    118108
weighted avg     0.9562    0.8647    0.9022    118108
XGBoost - Remove C + D + M + V - Original

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


===== Remove C + D + M + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + D + M + V - SMOTE

Features: 53
Accuracy           : 0.9676
Precision          : 0.5958
Recall             : 0.1836
F1 Score           : 0.2807
ROC-AUC            : 0.8248
PR-AUC             : 0.3159
Balanced Accuracy  : 0.5896
MCC                : 0.3188

Confusion Matrix:
[[113538    506]
 [  3318    746]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9716    0.9956    0.9834    114044
       Fraud     0.5958    0.1836    0.2807      4064

    accuracy                         0.9676    118108
   macro avg     0.7837    0.5896    0.6321    118108
weighted avg     0.9587    0.9676    0.9593    118108
LightGBM - Remove C + D + M + V - SMOTE

Features: 53
Accuracy           : 0.9539
Precision          : 0.2906
Recall             : 0.2362
F1 Score           : 0.2606
ROC-AUC            : 0.7879
PR-AUC             : 0.2376
Balanced Accuracy  : 0.6078
MCC                : 0.2384

Confusion Matrix:
[[111701   2343]
 [  3104    960]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9730    0.9795    0.9762    114044
       Fraud     0.2906    0.2362    0.2606      4064

    accuracy                         0.9539    118108
   macro avg     0.6318    0.6078    0.6184    118108
weighted avg     0.9495    0.9539    0.9516    118108
XGBoost - Remove C + D + M + V - SMOTE

Features: 53
Accuracy           : 0.9618
Precision          : 0.4009
Recall             : 0.2234
F1 Score           : 0.2869
ROC-AUC            : 0.7780
PR-AUC             : 0.2373
Balanced Accuracy  : 0.6058
MCC                : 0.2811

Confusion Matrix:
[[112687   1357]
 [  3156    908]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9728    0.9881    0.9804    114044
       Fraud     0.4009    0.2234    0.2869      4064

    accuracy                         0.9618    118108
   macro avg     0.6868    0.6058    0.6337    118108
weighted avg     0.9531    0.9618    0.9565    118108


===== Remove C + D + M + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + D + M + V - Undersampling

Features: 53
Accuracy           : 0.8604
Precision          : 0.1484
Recall             : 0.6449
F1 Score           : 0.2412
ROC-AUC            : 0.8420
PR-AUC             : 0.3089
Balanced Accuracy  : 0.7565
MCC                : 0.2622

Confusion Matrix:
[[98999 15045]
 [ 1443  2621]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9856    0.8681    0.9231    114044
       Fraud     0.1484    0.6449    0.2412      4064

    accuracy                         0.8604    118108
   macro avg     0.5670    0.7565    0.5822    118108
weighted avg     0.9568    0.8604    0.8997    118108
LightGBM - Remove C + D + M + V - Undersampling

Features: 53
Accuracy           : 0.8385
Precision          : 0.1294
Recall             : 0.6447
F1 Score           : 0.2155
ROC-AUC            : 0.8269
PR-AUC             : 0.2814
Balanced Accuracy  : 0.7450
MCC                : 0.2370

Confusion Matrix:
[[96414 17630]
 [ 1444  2620]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9852    0.8454    0.9100    114044
       Fraud     0.1294    0.6447    0.2155      4064

    accuracy                         0.8385    118108
   macro avg     0.5573    0.7450    0.5628    118108
weighted avg     0.9558    0.8385    0.8861    118108
XGBoost - Remove C + D + M + V - Undersampling

Features: 53
Accuracy           : 0.8378
Precision          : 0.1292
Recall             : 0.6474
F1 Score           : 0.2154
ROC-AUC            : 0.8240
PR-AUC             : 0.2808
Balanced Accuracy  : 0.7460
MCC                : 0.2374

Confusion Matrix:
[[96314 17730]
 [ 1433  2631]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9853    0.8445    0.9095    114044
       Fraud     0.1292    0.6474    0.2154      4064

    accuracy                         0.8378    118108
   macro avg     0.5573    0.7460    0.5625    118108
weighted avg     0.9559    0.8378    0.8856    118108


===== Remove C + D + M + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + D + M + V - SMOTE + Undersampling

Features: 53
Accuracy           : 0.9662
Precision          : 0.5162
Recall             : 0.2704
F1 Score           : 0.3549
ROC-AUC            : 0.8374
PR-AUC             : 0.3299
Balanced Accuracy  : 0.6307
MCC                : 0.3581

Confusion Matrix:
[[113014   1030]
 [  2965   1099]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9744    0.9910    0.9826    114044
       Fraud     0.5162    0.2704    0.3549      4064

    accuracy                         0.9662    118108
   macro avg     0.7453    0.6307    0.6688    118108
weighted avg     0.9587    0.9662    0.9610    118108
LightGBM - Remove C + D + M + V - SMOTE + Undersampling

Features: 53
Accuracy           : 0.9372
Precision          : 0.2396
Recall             : 0.3797
F1 Score           : 0.2938
ROC-AUC            : 0.8113
PR-AUC             : 0.2748
Balanced Accuracy  : 0.6684
MCC                : 0.2704

Confusion Matrix:
[[109148   4896]
 [  2521   1543]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9774    0.9571    0.9671    114044
       Fraud     0.2396    0.3797    0.2938      4064

    accuracy                         0.9372    118108
   macro avg     0.6085    0.6684    0.6305    118108
weighted avg     0.9520    0.9372    0.9440    118108
XGBoost - Remove C + D + M + V - SMOTE + Undersampling

Features: 53
Accuracy           : 0.9464
Precision          : 0.2799
Recall             : 0.3543
F1 Score           : 0.3128
ROC-AUC            : 0.8084
PR-AUC             : 0.2800
Balanced Accuracy  : 0.6609
MCC                : 0.2874

Confusion Matrix:
[[110340   3704]
 [  2624   1440]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9768    0.9675    0.9721    114044
       Fraud     0.2799    0.3543    0.3128      4064

    accuracy                         0.9464    118108
   macro avg     0.6284    0.6609    0.6424    118108
weighted avg     0.9528    0.9464    0.9494    118108


===== Remove C + D + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + D + id + V - Original

Features: 24
Accuracy           : 0.9677
Precision          : 0.8048
Recall             : 0.0822
F1 Score           : 0.1491
ROC-AUC            : 0.8390
PR-AUC             : 0.3208
Balanced Accuracy  : 0.5407
MCC                : 0.2510

Confusion Matrix:
[[113963     81]
 [  3730    334]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9683    0.9993    0.9836    114044
       Fraud     0.8048    0.0822    0.1491      4064

    accuracy                         0.9677    118108
   macro avg     0.8866    0.5407    0.5663    118108
weighted avg     0.9627    0.9677    0.9548    118108
LightGBM - Remove C + D + id + V - Original

Features: 24
Accuracy           : 0.8451
Precision          : 0.1386
Recall             : 0.6715
F1 Score           : 0.2298
ROC-AUC            : 0.8452
PR-AUC             : 0.2293
Balanced Accuracy  : 0.7614
MCC                : 0.2557

Confusion Matrix:
[[97085 16959]
 [ 1335  2729]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9864    0.8513    0.9139    114044
       Fraud     0.1386    0.6715    0.2298      4064

    accuracy                         0.8451    118108
   macro avg     0.5625    0.7614    0.5718    118108
weighted avg     0.9573    0.8451    0.8904    118108
XGBoost - Remove C + D + id + V - Original

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


===== Remove C + D + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + D + id + V - SMOTE

Features: 24
Accuracy           : 0.9632
Precision          : 0.4191
Recall             : 0.1784
F1 Score           : 0.2503
ROC-AUC            : 0.8206
PR-AUC             : 0.2560
Balanced Accuracy  : 0.5848
MCC                : 0.2573

Confusion Matrix:
[[113039   1005]
 [  3339    725]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9713    0.9912    0.9811    114044
       Fraud     0.4191    0.1784    0.2503      4064

    accuracy                         0.9632    118108
   macro avg     0.6952    0.5848    0.6157    118108
weighted avg     0.9523    0.9632    0.9560    118108
LightGBM - Remove C + D + id + V - SMOTE

Features: 24
Accuracy           : 0.9534
Precision          : 0.2777
Recall             : 0.2212
F1 Score           : 0.2463
ROC-AUC            : 0.8162
PR-AUC             : 0.1862
Balanced Accuracy  : 0.6004
MCC                : 0.2241

Confusion Matrix:
[[111706   2338]
 [  3165    899]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9724    0.9795    0.9760    114044
       Fraud     0.2777    0.2212    0.2463      4064

    accuracy                         0.9534    118108
   macro avg     0.6251    0.6004    0.6111    118108
weighted avg     0.9485    0.9534    0.9509    118108
XGBoost - Remove C + D + id + V - SMOTE

Features: 24
Accuracy           : 0.9571
Precision          : 0.3028
Recall             : 0.1897
F1 Score           : 0.2333
ROC-AUC            : 0.8127
PR-AUC             : 0.1857
Balanced Accuracy  : 0.5871
MCC                : 0.2186

Confusion Matrix:
[[112269   1775]
 [  3293    771]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9715    0.9844    0.9779    114044
       Fraud     0.3028    0.1897    0.2333      4064

    accuracy                         0.9571    118108
   macro avg     0.6372    0.5871    0.6056    118108
weighted avg     0.9485    0.9571    0.9523    118108


===== Remove C + D + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + D + id + V - Undersampling

Features: 24
Accuracy           : 0.8561
Precision          : 0.1446
Recall             : 0.6476
F1 Score           : 0.2365
ROC-AUC            : 0.8484
PR-AUC             : 0.2535
Balanced Accuracy  : 0.7556
MCC                : 0.2581

Confusion Matrix:
[[98479 15565]
 [ 1432  2632]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9857    0.8635    0.9206    114044
       Fraud     0.1446    0.6476    0.2365      4064

    accuracy                         0.8561    118108
   macro avg     0.5652    0.7556    0.5785    118108
weighted avg     0.9567    0.8561    0.8970    118108
LightGBM - Remove C + D + id + V - Undersampling

Features: 24
Accuracy           : 0.8319
Precision          : 0.1288
Recall             : 0.6742
F1 Score           : 0.2163
ROC-AUC            : 0.8376
PR-AUC             : 0.2156
Balanced Accuracy  : 0.7559
MCC                : 0.2428

Confusion Matrix:
[[95518 18526]
 [ 1324  2740]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9863    0.8376    0.9059    114044
       Fraud     0.1288    0.6742    0.2163      4064

    accuracy                         0.8319    118108
   macro avg     0.5576    0.7559    0.5611    118108
weighted avg     0.9568    0.8319    0.8821    118108
XGBoost - Remove C + D + id + V - Undersampling

Features: 24
Accuracy           : 0.8247
Precision          : 0.1212
Recall             : 0.6545
F1 Score           : 0.2045
ROC-AUC            : 0.8237
PR-AUC             : 0.1948
Balanced Accuracy  : 0.7427
MCC                : 0.2274

Confusion Matrix:
[[94749 19295]
 [ 1404  2660]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9854    0.8308    0.9015    114044
       Fraud     0.1212    0.6545    0.2045      4064

    accuracy                         0.8247    118108
   macro avg     0.5533    0.7427    0.5530    118108
weighted avg     0.9557    0.8247    0.8775    118108


===== Remove C + D + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + D + id + V - SMOTE + Undersampling

Features: 24
Accuracy           : 0.9615
Precision          : 0.4013
Recall             : 0.2411
F1 Score           : 0.3013
ROC-AUC            : 0.8331
PR-AUC             : 0.2698
Balanced Accuracy  : 0.6142
MCC                : 0.2925

Confusion Matrix:
[[112582   1462]
 [  3084    980]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9733    0.9872    0.9802    114044
       Fraud     0.4013    0.2411    0.3013      4064

    accuracy                         0.9615    118108
   macro avg     0.6873    0.6142    0.6407    118108
weighted avg     0.9537    0.9615    0.9568    118108
LightGBM - Remove C + D + id + V - SMOTE + Undersampling

Features: 24
Accuracy           : 0.9321
Precision          : 0.2228
Recall             : 0.3910
F1 Score           : 0.2839
ROC-AUC            : 0.8301
PR-AUC             : 0.2120
Balanced Accuracy  : 0.6712
MCC                : 0.2620

Confusion Matrix:
[[108501   5543]
 [  2475   1589]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9777    0.9514    0.9644    114044
       Fraud     0.2228    0.3910    0.2839      4064

    accuracy                         0.9321    118108
   macro avg     0.6002    0.6712    0.6241    118108
weighted avg     0.9517    0.9321    0.9410    118108
XGBoost - Remove C + D + id + V - SMOTE + Undersampling

Features: 24
Accuracy           : 0.9420
Precision          : 0.2480
Recall             : 0.3381
F1 Score           : 0.2861
ROC-AUC            : 0.8252
PR-AUC             : 0.2126
Balanced Accuracy  : 0.6508
MCC                : 0.2600

Confusion Matrix:
[[109878   4166]
 [  2690   1374]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9761    0.9635    0.9697    114044
       Fraud     0.2480    0.3381    0.2861      4064

    accuracy                         0.9420    118108
   macro avg     0.6121    0.6508    0.6279    118108
weighted avg     0.9511    0.9420    0.9462    118108


===== Remove C + M + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + M + id + V - Original

Features: 37
Accuracy           : 0.9658
Precision          : 0.8537
Recall             : 0.0086
F1 Score           : 0.0171
ROC-AUC            : 0.8590
PR-AUC             : 0.3565
Balanced Accuracy  : 0.5043
MCC                : 0.0838

Confusion Matrix:
[[114038      6]
 [  4029     35]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9659    0.9999    0.9826    114044
       Fraud     0.8537    0.0086    0.0171      4064

    accuracy                         0.9658    118108
   macro avg     0.9098    0.5043    0.4998    118108
weighted avg     0.9620    0.9658    0.9494    118108
LightGBM - Remove C + M + id + V - Original

Features: 37
Accuracy           : 0.8633
Precision          : 0.1583
Recall             : 0.6887
F1 Score           : 0.2575
ROC-AUC            : 0.8734
PR-AUC             : 0.3395
Balanced Accuracy  : 0.7791
MCC                : 0.2852

Confusion Matrix:
[[99163 14881]
 [ 1265  2799]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9874    0.8695    0.9247    114044
       Fraud     0.1583    0.6887    0.2575      4064

    accuracy                         0.8633    118108
   macro avg     0.5729    0.7791    0.5911    118108
weighted avg     0.9589    0.8633    0.9018    118108
XGBoost - Remove C + M + id + V - Original

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


===== Remove C + M + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + M + id + V - SMOTE

Features: 37
Accuracy           : 0.9687
Precision          : 0.7111
Recall             : 0.1508
F1 Score           : 0.2489
ROC-AUC            : 0.8444
PR-AUC             : 0.3477
Balanced Accuracy  : 0.5743
MCC                : 0.3183

Confusion Matrix:
[[113795    249]
 [  3451    613]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9706    0.9978    0.9840    114044
       Fraud     0.7111    0.1508    0.2489      4064

    accuracy                         0.9687    118108
   macro avg     0.8409    0.5743    0.6164    118108
weighted avg     0.9616    0.9687    0.9587    118108
LightGBM - Remove C + M + id + V - SMOTE

Features: 37
Accuracy           : 0.9643
Precision          : 0.4678
Recall             : 0.2719
F1 Score           : 0.3439
ROC-AUC            : 0.8475
PR-AUC             : 0.3198
Balanced Accuracy  : 0.6304
MCC                : 0.3397

Confusion Matrix:
[[112787   1257]
 [  2959   1105]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9744    0.9890    0.9817    114044
       Fraud     0.4678    0.2719    0.3439      4064

    accuracy                         0.9643    118108
   macro avg     0.7211    0.6304    0.6628    118108
weighted avg     0.9570    0.9643    0.9597    118108
XGBoost - Remove C + M + id + V - SMOTE

Features: 37
Accuracy           : 0.9647
Precision          : 0.4777
Recall             : 0.2709
F1 Score           : 0.3457
ROC-AUC            : 0.8461
PR-AUC             : 0.3192
Balanced Accuracy  : 0.6302
MCC                : 0.3431

Confusion Matrix:
[[112840   1204]
 [  2963   1101]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9744    0.9894    0.9819    114044
       Fraud     0.4777    0.2709    0.3457      4064

    accuracy                         0.9647    118108
   macro avg     0.7260    0.6302    0.6638    118108
weighted avg     0.9573    0.9647    0.9600    118108


===== Remove C + M + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + M + id + V - Undersampling

Features: 37
Accuracy           : 0.8660
Precision          : 0.1585
Recall             : 0.6713
F1 Score           : 0.2564
ROC-AUC            : 0.8600
PR-AUC             : 0.3156
Balanced Accuracy  : 0.7721
MCC                : 0.2811

Confusion Matrix:
[[99558 14486]
 [ 1336  2728]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9868    0.8730    0.9264    114044
       Fraud     0.1585    0.6713    0.2564      4064

    accuracy                         0.8660    118108
   macro avg     0.5726    0.7721    0.5914    118108
weighted avg     0.9583    0.8660    0.9033    118108
LightGBM - Remove C + M + id + V - Undersampling

Features: 37
Accuracy           : 0.8375
Precision          : 0.1408
Recall             : 0.7296
F1 Score           : 0.2361
ROC-AUC            : 0.8715
PR-AUC             : 0.3348
Balanced Accuracy  : 0.7855
MCC                : 0.2719

Confusion Matrix:
[[95956 18088]
 [ 1099  2965]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9887    0.8414    0.9091    114044
       Fraud     0.1408    0.7296    0.2361      4064

    accuracy                         0.8375    118108
   macro avg     0.5648    0.7855    0.5726    118108
weighted avg     0.9595    0.8375    0.8860    118108
XGBoost - Remove C + M + id + V - Undersampling

Features: 37
Accuracy           : 0.8275
Precision          : 0.1331
Recall             : 0.7281
F1 Score           : 0.2251
ROC-AUC            : 0.8697
PR-AUC             : 0.3330
Balanced Accuracy  : 0.7796
MCC                : 0.2608

Confusion Matrix:
[[94776 19268]
 [ 1105  2959]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9885    0.8310    0.9030    114044
       Fraud     0.1331    0.7281    0.2251      4064

    accuracy                         0.8275    118108
   macro avg     0.5608    0.7796    0.5640    118108
weighted avg     0.9590    0.8275    0.8796    118108


===== Remove C + M + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + M + id + V - SMOTE + Undersampling

Features: 37
Accuracy           : 0.9681
Precision          : 0.5898
Recall             : 0.2384
F1 Score           : 0.3396
ROC-AUC            : 0.8518
PR-AUC             : 0.3513
Balanced Accuracy  : 0.6163
MCC                : 0.3619

Confusion Matrix:
[[113370    674]
 [  3095    969]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9734    0.9941    0.9836    114044
       Fraud     0.5898    0.2384    0.3396      4064

    accuracy                         0.9681    118108
   macro avg     0.7816    0.6163    0.6616    118108
weighted avg     0.9602    0.9681    0.9615    118108
LightGBM - Remove C + M + id + V - SMOTE + Undersampling

Features: 37
Accuracy           : 0.9478
Precision          : 0.3155
Recall             : 0.4434
F1 Score           : 0.3687
ROC-AUC            : 0.8660
PR-AUC             : 0.3472
Balanced Accuracy  : 0.7046
MCC                : 0.3476

Confusion Matrix:
[[110135   3909]
 [  2262   1802]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9799    0.9657    0.9727    114044
       Fraud     0.3155    0.4434    0.3687      4064

    accuracy                         0.9478    118108
   macro avg     0.6477    0.7046    0.6707    118108
weighted avg     0.9570    0.9478    0.9520    118108
XGBoost - Remove C + M + id + V - SMOTE + Undersampling

Features: 37
Accuracy           : 0.9517
Precision          : 0.3376
Recall             : 0.4195
F1 Score           : 0.3741
ROC-AUC            : 0.8638
PR-AUC             : 0.3413
Balanced Accuracy  : 0.6951
MCC                : 0.3515

Confusion Matrix:
[[110698   3346]
 [  2359   1705]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9791    0.9707    0.9749    114044
       Fraud     0.3376    0.4195    0.3741      4064

    accuracy                         0.9517    118108
   macro avg     0.6583    0.6951    0.6745    118108
weighted avg     0.9571    0.9517    0.9542    118108


===== Remove D + M + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove D + M + id + V - Original

Features: 29
Accuracy           : 0.9727
Precision          : 0.8886
Recall             : 0.2355
F1 Score           : 0.3723
ROC-AUC            : 0.8933
PR-AUC             : 0.5610
Balanced Accuracy  : 0.6172
MCC                : 0.4495

Confusion Matrix:
[[113924    120]
 [  3107    957]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9735    0.9989    0.9860    114044
       Fraud     0.8886    0.2355    0.3723      4064

    accuracy                         0.9727    118108
   macro avg     0.9310    0.6172    0.6792    118108
weighted avg     0.9705    0.9727    0.9649    118108
LightGBM - Remove D + M + id + V - Original

Features: 29
Accuracy           : 0.8809
Precision          : 0.1815
Recall             : 0.7010
F1 Score           : 0.2883
ROC-AUC            : 0.8871
PR-AUC             : 0.4706
Balanced Accuracy  : 0.7942
MCC                : 0.3159

Confusion Matrix:
[[101195  12849]
 [  1215   2849]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9881    0.8873    0.9350    114044
       Fraud     0.1815    0.7010    0.2883      4064

    accuracy                         0.8809    118108
   macro avg     0.5848    0.7942    0.6117    118108
weighted avg     0.9604    0.8809    0.9128    118108
XGBoost - Remove D + M + id + V - Original

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


===== Remove D + M + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove D + M + id + V - SMOTE

Features: 29
Accuracy           : 0.9756
Precision          : 0.7998
Recall             : 0.3883
F1 Score           : 0.5228
ROC-AUC            : 0.8868
PR-AUC             : 0.5256
Balanced Accuracy  : 0.6924
MCC                : 0.5473

Confusion Matrix:
[[113649    395]
 [  2486   1578]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9786    0.9965    0.9875    114044
       Fraud     0.7998    0.3883    0.5228      4064

    accuracy                         0.9756    118108
   macro avg     0.8892    0.6924    0.7551    118108
weighted avg     0.9724    0.9756    0.9715    118108
LightGBM - Remove D + M + id + V - SMOTE

Features: 29
Accuracy           : 0.9706
Precision          : 0.6188
Recall             : 0.3755
F1 Score           : 0.4674
ROC-AUC            : 0.8703
PR-AUC             : 0.4610
Balanced Accuracy  : 0.6836
MCC                : 0.4682

Confusion Matrix:
[[113104    940]
 [  2538   1526]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9781    0.9918    0.9849    114044
       Fraud     0.6188    0.3755    0.4674      4064

    accuracy                         0.9706    118108
   macro avg     0.7984    0.6836    0.7261    118108
weighted avg     0.9657    0.9706    0.9671    118108
XGBoost - Remove D + M + id + V - SMOTE

Features: 29
Accuracy           : 0.9708
Precision          : 0.6326
Recall             : 0.3605
F1 Score           : 0.4592
ROC-AUC            : 0.8630
PR-AUC             : 0.4421
Balanced Accuracy  : 0.6765
MCC                : 0.4641

Confusion Matrix:
[[113193    851]
 [  2599   1465]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9776    0.9925    0.9850    114044
       Fraud     0.6326    0.3605    0.4592      4064

    accuracy                         0.9708    118108
   macro avg     0.8051    0.6765    0.7221    118108
weighted avg     0.9657    0.9708    0.9669    118108


===== Remove D + M + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove D + M + id + V - Undersampling

Features: 29
Accuracy           : 0.8944
Precision          : 0.2033
Recall             : 0.7092
F1 Score           : 0.3160
ROC-AUC            : 0.8972
PR-AUC             : 0.4601
Balanced Accuracy  : 0.8051
MCC                : 0.3422

Confusion Matrix:
[[102749  11295]
 [  1182   2882]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9886    0.9010    0.9428    114044
       Fraud     0.2033    0.7092    0.3160      4064

    accuracy                         0.8944    118108
   macro avg     0.5960    0.8051    0.6294    118108
weighted avg     0.9616    0.8944    0.9212    118108
LightGBM - Remove D + M + id + V - Undersampling

Features: 29
Accuracy           : 0.8678
Precision          : 0.1656
Recall             : 0.7037
F1 Score           : 0.2681
ROC-AUC            : 0.8821
PR-AUC             : 0.4512
Balanced Accuracy  : 0.7887
MCC                : 0.2979

Confusion Matrix:
[[99636 14408]
 [ 1204  2860]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9881    0.8737    0.9273    114044
       Fraud     0.1656    0.7037    0.2681      4064

    accuracy                         0.8678    118108
   macro avg     0.5768    0.7887    0.5977    118108
weighted avg     0.9598    0.8678    0.9047    118108
XGBoost - Remove D + M + id + V - Undersampling

Features: 29
Accuracy           : 0.8797
Precision          : 0.1804
Recall             : 0.7042
F1 Score           : 0.2872
ROC-AUC            : 0.8848
PR-AUC             : 0.4517
Balanced Accuracy  : 0.7951
MCC                : 0.3155

Confusion Matrix:
[[101038  13006]
 [  1202   2862]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9882    0.8860    0.9343    114044
       Fraud     0.1804    0.7042    0.2872      4064

    accuracy                         0.8797    118108
   macro avg     0.5843    0.7951    0.6107    118108
weighted avg     0.9604    0.8797    0.9120    118108


===== Remove D + M + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove D + M + id + V - SMOTE + Undersampling

Features: 29
Accuracy           : 0.9737
Precision          : 0.6820
Recall             : 0.4407
F1 Score           : 0.5354
ROC-AUC            : 0.8950
PR-AUC             : 0.5162
Balanced Accuracy  : 0.7167
MCC                : 0.5358

Confusion Matrix:
[[113209    835]
 [  2273   1791]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9803    0.9927    0.9865    114044
       Fraud     0.6820    0.4407    0.5354      4064

    accuracy                         0.9737    118108
   macro avg     0.8312    0.7167    0.7609    118108
weighted avg     0.9701    0.9737    0.9709    118108
LightGBM - Remove D + M + id + V - SMOTE + Undersampling

Features: 29
Accuracy           : 0.9576
Precision          : 0.4076
Recall             : 0.5138
F1 Score           : 0.4546
ROC-AUC            : 0.8846
PR-AUC             : 0.4803
Balanced Accuracy  : 0.7436
MCC                : 0.4359

Confusion Matrix:
[[111009   3035]
 [  1976   2088]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9825    0.9734    0.9779    114044
       Fraud     0.4076    0.5138    0.4546      4064

    accuracy                         0.9576    118108
   macro avg     0.6950    0.7436    0.7162    118108
weighted avg     0.9627    0.9576    0.9599    118108
XGBoost - Remove D + M + id + V - SMOTE + Undersampling

Features: 29
Accuracy           : 0.9610
Precision          : 0.4389
Recall             : 0.4783
F1 Score           : 0.4578
ROC-AUC            : 0.8783
PR-AUC             : 0.4678
Balanced Accuracy  : 0.7283
MCC                : 0.4380

Confusion Matrix:
[[111559   2485]
 [  2120   1944]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9814    0.9782    0.9798    114044
       Fraud     0.4389    0.4783    0.4578      4064

    accuracy                         0.9610    118108
   macro avg     0.7101    0.7283    0.7188    118108
weighted avg     0.9627    0.9610    0.9618    118108


===== Remove C + D + M + id + V - Original =====
Train samples: 472,432 | Fraud rate: 0.0351


RF - Remove C + D + M + id + V - Original

Features: 15
Accuracy           : 0.9674
Precision          : 0.8263
Recall             : 0.0679
F1 Score           : 0.1255
ROC-AUC            : 0.8163
PR-AUC             : 0.2962
Balanced Accuracy  : 0.5337
MCC                : 0.2314

Confusion Matrix:
[[113986     58]
 [  3788    276]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9678    0.9995    0.9834    114044
       Fraud     0.8263    0.0679    0.1255      4064

    accuracy                         0.9674    118108
   macro avg     0.8971    0.5337    0.5545    118108
weighted avg     0.9630    0.9674    0.9539    118108
LightGBM - Remove C + D + M + id + V - Original

Features: 15
Accuracy           : 0.8582
Precision          : 0.1392
Recall             : 0.6021
F1 Score           : 0.2262
ROC-AUC            : 0.8197
PR-AUC             : 0.2118
Balanced Accuracy  : 0.7347
MCC                : 0.2404

Confusion Matrix:
[[98916 15128]
 [ 1617  2447]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9839    0.8673    0.9220    114044
       Fraud     0.1392    0.6021    0.2262      4064

    accuracy                         0.8582    118108
   macro avg     0.5616    0.7347    0.5741    118108
weighted avg     0.9549    0.8582    0.8980    118108
XGBoost - Remove C + D + M + id + V - Original

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


===== Remove C + D + M + id + V - SMOTE =====
Train samples: 911,666 | Fraud rate: 0.5000


RF - Remove C + D + M + id + V - SMOTE

Features: 15
Accuracy           : 0.9638
Precision          : 0.4366
Recall             : 0.1804
F1 Score           : 0.2553
ROC-AUC            : 0.7979
PR-AUC             : 0.2348
Balanced Accuracy  : 0.5860
MCC                : 0.2649

Confusion Matrix:
[[113098    946]
 [  3331    733]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9714    0.9917    0.9814    114044
       Fraud     0.4366    0.1804    0.2553      4064

    accuracy                         0.9638    118108
   macro avg     0.7040    0.5860    0.6184    118108
weighted avg     0.9530    0.9638    0.9565    118108
LightGBM - Remove C + D + M + id + V - SMOTE

Features: 15
Accuracy           : 0.9435
Precision          : 0.2074
Recall             : 0.2279
F1 Score           : 0.2171
ROC-AUC            : 0.7812
PR-AUC             : 0.1621
Balanced Accuracy  : 0.5984
MCC                : 0.1881

Confusion Matrix:
[[110505   3539]
 [  3138    926]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9724    0.9690    0.9707    114044
       Fraud     0.2074    0.2279    0.2171      4064

    accuracy                         0.9435    118108
   macro avg     0.5899    0.5984    0.5939    118108
weighted avg     0.9461    0.9435    0.9447    118108
XGBoost - Remove C + D + M + id + V - SMOTE

Features: 15
Accuracy           : 0.9563
Precision          : 0.3027
Recall             : 0.2069
F1 Score           : 0.2458
ROC-AUC            : 0.7801
PR-AUC             : 0.1747
Balanced Accuracy  : 0.5950
MCC                : 0.2285

Confusion Matrix:
[[112107   1937]
 [  3223    841]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9721    0.9830    0.9775    114044
       Fraud     0.3027    0.2069    0.2458      4064

    accuracy                         0.9563    118108
   macro avg     0.6374    0.5950    0.6117    118108
weighted avg     0.9490    0.9563    0.9523    118108


===== Remove C + D + M + id + V - Undersampling =====
Train samples: 33,198 | Fraud rate: 0.5000


RF - Remove C + D + M + id + V - Undersampling

Features: 15
Accuracy           : 0.8671
Precision          : 0.1456
Recall             : 0.5881
F1 Score           : 0.2334
ROC-AUC            : 0.8254
PR-AUC             : 0.2211
Balanced Accuracy  : 0.7325
MCC                : 0.2450

Confusion Matrix:
[[100016  14028]
 [  1674   2390]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9835    0.8770    0.9272    114044
       Fraud     0.1456    0.5881    0.2334      4064

    accuracy                         0.8671    118108
   macro avg     0.5646    0.7325    0.5803    118108
weighted avg     0.9547    0.8671    0.9033    118108
LightGBM - Remove C + D + M + id + V - Undersampling

Features: 15
Accuracy           : 0.8299
Precision          : 0.1239
Recall             : 0.6499
F1 Score           : 0.2082
ROC-AUC            : 0.8202
PR-AUC             : 0.2106
Balanced Accuracy  : 0.7431
MCC                : 0.2304

Confusion Matrix:
[[95374 18670]
 [ 1423  2641]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9853    0.8363    0.9047    114044
       Fraud     0.1239    0.6499    0.2082      4064

    accuracy                         0.8299    118108
   macro avg     0.5546    0.7431    0.5564    118108
weighted avg     0.9557    0.8299    0.8807    118108
XGBoost - Remove C + D + M + id + V - Undersampling

Features: 15
Accuracy           : 0.8331
Precision          : 0.1207
Recall             : 0.6127
F1 Score           : 0.2017
ROC-AUC            : 0.8043
PR-AUC             : 0.1838
Balanced Accuracy  : 0.7268
MCC                : 0.2178

Confusion Matrix:
[[95908 18136]
 [ 1574  2490]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9839    0.8410    0.9068    114044
       Fraud     0.1207    0.6127    0.2017      4064

    accuracy                         0.8331    118108
   macro avg     0.5523    0.7268    0.5543    118108
weighted avg     0.9542    0.8331    0.8826    118108


===== Remove C + D + M + id + V - SMOTE + Undersampling =====
Train samples: 248,985 | Fraud rate: 0.3333


RF - Remove C + D + M + id + V - SMOTE + Undersampling

Features: 15
Accuracy           : 0.9616
Precision          : 0.3995
Recall             : 0.2333
F1 Score           : 0.2945
ROC-AUC            : 0.8191
PR-AUC             : 0.2543
Balanced Accuracy  : 0.6104
MCC                : 0.2868

Confusion Matrix:
[[112619   1425]
 [  3116    948]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9731    0.9875    0.9802    114044
       Fraud     0.3995    0.2333    0.2945      4064

    accuracy                         0.9616    118108
   macro avg     0.6863    0.6104    0.6374    118108
weighted avg     0.9533    0.9616    0.9566    118108
LightGBM - Remove C + D + M + id + V - SMOTE + Undersampling

Features: 15
Accuracy           : 0.9352
Precision          : 0.2109
Recall             : 0.3219
F1 Score           : 0.2548
ROC-AUC            : 0.7994
PR-AUC             : 0.1917
Balanced Accuracy  : 0.6395
MCC                : 0.2279

Confusion Matrix:
[[109150   4894]
 [  2756   1308]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9754    0.9571    0.9661    114044
       Fraud     0.2109    0.3219    0.2548      4064

    accuracy                         0.9352    118108
   macro avg     0.5931    0.6395    0.6105    118108
weighted avg     0.9491    0.9352    0.9417    118108
XGBoost - Remove C + D + M + id + V - SMOTE + Undersampling

Features: 15
Accuracy           : 0.9485
Precision          : 0.2731
Recall             : 0.2995
F1 Score           : 0.2857
ROC-AUC            : 0.8001
PR-AUC             : 0.1955
Balanced Accuracy  : 0.6355
MCC                : 0.2593

Confusion Matrix:
[[110805   3239]
 [  2847   1217]]

Classification Report:
              precision    recall  f1-score   support

  Legitimate     0.9749    0.9716    0.9733    114044
       Fraud     0.2731    0.2995    0.2857      4064

    accuracy                         0.9485    118108
   macro avg     0.6240    0.6355    0.6295    118108
weighted avg     0.9508    0.9485    0.9496    118108

