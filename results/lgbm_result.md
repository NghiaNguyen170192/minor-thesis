
LightGBM - Baseline
Features: 437
Accuracy           : 0.9007
Precision          : 0.2170
Recall             : 0.7232
F1 Score           : 0.3338
ROC-AUC            : 0.9041
PR-AUC             : 0.5273
Balanced Accuracy  : 0.8151
MCC                : 0.3605
Confusion Matrix:
[[103437  10607]
 [  1125   2939]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9892    0.9070    0.9463    114044
       Fraud     0.2170    0.7232    0.3338      4064
    accuracy                         0.9007    118108
   macro avg     0.6031    0.8151    0.6401    118108
weighted avg     0.9627    0.9007    0.9253    118108

LightGBM - Feature Engineering
Features: 439
Accuracy           : 0.9012
Precision          : 0.2181
Recall             : 0.7239
F1 Score           : 0.3352
ROC-AUC            : 0.9077
PR-AUC             : 0.5215
Balanced Accuracy  : 0.8157
MCC                : 0.3618
Confusion Matrix:
[[103496  10548]
 [  1122   2942]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9893    0.9075    0.9466    114044
       Fraud     0.2181    0.7239    0.3352      4064
    accuracy                         0.9012    118108
   macro avg     0.6037    0.8157    0.6409    118108
weighted avg     0.9627    0.9012    0.9256    118108

LightGBM - Remove C
Features: 423
Accuracy           : 0.8931
Precision          : 0.2020
Recall             : 0.7143
F1 Score           : 0.3150
ROC-AUC            : 0.8978
PR-AUC             : 0.4867
Balanced Accuracy  : 0.8069
MCC                : 0.3422
Confusion Matrix:
[[102577  11467]
 [  1161   2903]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9888    0.8995    0.9420    114044
       Fraud     0.2020    0.7143    0.3150      4064
    accuracy                         0.8931    118108
   macro avg     0.5954    0.8069    0.6285    118108
weighted avg     0.9617    0.8931    0.9204    118108

LightGBM - Remove D
Features: 415
Accuracy           : 0.9016
Precision          : 0.2184
Recall             : 0.7215
F1 Score           : 0.3353
ROC-AUC            : 0.8986
PR-AUC             : 0.5230
Balanced Accuracy  : 0.8147
MCC                : 0.3614
Confusion Matrix:
[[103549  10495]
 [  1132   2932]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9892    0.9080    0.9468    114044
       Fraud     0.2184    0.7215    0.3353      4064
    accuracy                         0.9016    118108
   macro avg     0.6038    0.8147    0.6411    118108
weighted avg     0.9627    0.9016    0.9258    118108

LightGBM - Remove M
Features: 428
Accuracy           : 0.8979
Precision          : 0.2110
Recall             : 0.7175
F1 Score           : 0.3261
ROC-AUC            : 0.9026
PR-AUC             : 0.5176
Balanced Accuracy  : 0.8109
MCC                : 0.3527
Confusion Matrix:
[[103139  10905]
 [  1148   2916]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9890    0.9044    0.9448    114044
       Fraud     0.2110    0.7175    0.3261      4064
    accuracy                         0.8979    118108
   macro avg     0.6000    0.8109    0.6354    118108
weighted avg     0.9622    0.8979    0.9235    118108

LightGBM - Remove id
Features: 399
Accuracy           : 0.8955
Precision          : 0.2075
Recall             : 0.7224
F1 Score           : 0.3224
ROC-AUC            : 0.9053
PR-AUC             : 0.5130
Balanced Accuracy  : 0.8121
MCC                : 0.3503
Confusion Matrix:
[[102831  11213]
 [  1128   2936]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9891    0.9017    0.9434    114044
       Fraud     0.2075    0.7224    0.3224      4064
    accuracy                         0.8955    118108
   macro avg     0.5983    0.8121    0.6329    118108
weighted avg     0.9623    0.8955    0.9220    118108

LightGBM - Remove V
Features: 98
Accuracy           : 0.8935
Precision          : 0.2081
Recall             : 0.7470
F1 Score           : 0.3255
ROC-AUC            : 0.9103
PR-AUC             : 0.5159
Balanced Accuracy  : 0.8229
MCC                : 0.3577
Confusion Matrix:
[[102492  11552]
 [  1028   3036]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9901    0.8987    0.9422    114044
       Fraud     0.2081    0.7470    0.3255      4064
    accuracy                         0.8935    118108
   macro avg     0.5991    0.8229    0.6339    118108
weighted avg     0.9632    0.8935    0.9210    118108

LightGBM - Remove C + D
Features: 401
Accuracy           : 0.8912
Precision          : 0.1978
Recall             : 0.7069
F1 Score           : 0.3091
ROC-AUC            : 0.8863
PR-AUC             : 0.4877
Balanced Accuracy  : 0.8024
MCC                : 0.3356
Confusion Matrix:
[[102389  11655]
 [  1191   2873]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9885    0.8978    0.9410    114044
       Fraud     0.1978    0.7069    0.3091      4064
    accuracy                         0.8912    118108
   macro avg     0.5931    0.8024    0.6250    118108
weighted avg     0.9613    0.8912    0.9192    118108

LightGBM - Remove C + M
Features: 414
Accuracy           : 0.8891
Precision          : 0.1933
Recall             : 0.7005
F1 Score           : 0.3030
ROC-AUC            : 0.8915
PR-AUC             : 0.4741
Balanced Accuracy  : 0.7982
MCC                : 0.3290
Confusion Matrix:
[[102163  11881]
 [  1217   2847]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9882    0.8958    0.9398    114044
       Fraud     0.1933    0.7005    0.3030      4064
    accuracy                         0.8891    118108
   macro avg     0.5908    0.7982    0.6214    118108
weighted avg     0.9609    0.8891    0.9178    118108

LightGBM - Remove C + id
Features: 385
Accuracy           : 0.8889
Precision          : 0.1965
Recall             : 0.7215
F1 Score           : 0.3088
ROC-AUC            : 0.8936
PR-AUC             : 0.4742
Balanced Accuracy  : 0.8082
MCC                : 0.3381
Confusion Matrix:
[[102053  11991]
 [  1132   2932]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9890    0.8949    0.9396    114044
       Fraud     0.1965    0.7215    0.3088      4064
    accuracy                         0.8889    118108
   macro avg     0.5928    0.8082    0.6242    118108
weighted avg     0.9618    0.8889    0.9179    118108

LightGBM - Remove C + V
Features: 84
Accuracy           : 0.8727
Precision          : 0.1722
Recall             : 0.7094
F1 Score           : 0.2771
ROC-AUC            : 0.8839
PR-AUC             : 0.3806
Balanced Accuracy  : 0.7939
MCC                : 0.3072
Confusion Matrix:
[[100184  13860]
 [  1181   2883]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9883    0.8785    0.9302    114044
       Fraud     0.1722    0.7094    0.2771      4064
    accuracy                         0.8727    118108
   macro avg     0.5803    0.7939    0.6036    118108
weighted avg     0.9603    0.8727    0.9077    118108

LightGBM - Remove D + M
Features: 406
Accuracy           : 0.8989
Precision          : 0.2118
Recall             : 0.7121
F1 Score           : 0.3265
ROC-AUC            : 0.8942
PR-AUC             : 0.5101
Balanced Accuracy  : 0.8088
MCC                : 0.3520
Confusion Matrix:
[[103273  10771]
 [  1170   2894]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9888    0.9056    0.9453    114044
       Fraud     0.2118    0.7121    0.3265      4064
    accuracy                         0.8989    118108
   macro avg     0.6003    0.8088    0.6359    118108
weighted avg     0.9621    0.8989    0.9241    118108

LightGBM - Remove D + id
Features: 377
Accuracy           : 0.8989
Precision          : 0.2133
Recall             : 0.7207
F1 Score           : 0.3292
ROC-AUC            : 0.8992
PR-AUC             : 0.5123
Balanced Accuracy  : 0.8130
MCC                : 0.3560
Confusion Matrix:
[[103242  10802]
 [  1135   2929]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9891    0.9053    0.9453    114044
       Fraud     0.2133    0.7207    0.3292      4064
    accuracy                         0.8989    118108
   macro avg     0.6012    0.8130    0.6373    118108
weighted avg     0.9624    0.8989    0.9241    118108

LightGBM - Remove D + V
Features: 76
Accuracy           : 0.8935
Precision          : 0.2045
Recall             : 0.7244
F1 Score           : 0.3189
ROC-AUC            : 0.8986
PR-AUC             : 0.4979
Balanced Accuracy  : 0.8120
MCC                : 0.3476
Confusion Matrix:
[[102591  11453]
 [  1120   2944]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9892    0.8996    0.9423    114044
       Fraud     0.2045    0.7244    0.3189      4064
    accuracy                         0.8935    118108
   macro avg     0.5968    0.8120    0.6306    118108
weighted avg     0.9622    0.8935    0.9208    118108

LightGBM - Remove M + id
Features: 390
Accuracy           : 0.8938
Precision          : 0.2041
Recall             : 0.7192
F1 Score           : 0.3180
ROC-AUC            : 0.9004
PR-AUC             : 0.5055
Balanced Accuracy  : 0.8096
MCC                : 0.3458
Confusion Matrix:
[[102646  11398]
 [  1141   2923]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9890    0.9001    0.9424    114044
       Fraud     0.2041    0.7192    0.3180      4064
    accuracy                         0.8938    118108
   macro avg     0.5966    0.8096    0.6302    118108
weighted avg     0.9620    0.8938    0.9209    118108

LightGBM - Remove M + V
Features: 89
Accuracy           : 0.8905
Precision          : 0.2032
Recall             : 0.7470
F1 Score           : 0.3195
ROC-AUC            : 0.9068
PR-AUC             : 0.5038
Balanced Accuracy  : 0.8213
MCC                : 0.3524
Confusion Matrix:
[[102138  11906]
 [  1028   3036]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9900    0.8956    0.9405    114044
       Fraud     0.2032    0.7470    0.3195      4064
    accuracy                         0.8905    118108
   macro avg     0.5966    0.8213    0.6300    118108
weighted avg     0.9630    0.8905    0.9191    118108

LightGBM - Remove id + V
Features: 60
Accuracy           : 0.8940
Precision          : 0.2104
Recall             : 0.7564
F1 Score           : 0.3292
ROC-AUC            : 0.9122
PR-AUC             : 0.5067
Balanced Accuracy  : 0.8276
MCC                : 0.3628
Confusion Matrix:
[[102509  11535]
 [   990   3074]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9904    0.8989    0.9424    114044
       Fraud     0.2104    0.7564    0.3292      4064
    accuracy                         0.8940    118108
   macro avg     0.6004    0.8276    0.6358    118108
weighted avg     0.9636    0.8940    0.9213    118108

LightGBM - Remove C + D + M
Features: 392
Accuracy           : 0.8920
Precision          : 0.1960
Recall             : 0.6900
F1 Score           : 0.3053
ROC-AUC            : 0.8804
PR-AUC             : 0.4771
Balanced Accuracy  : 0.7946
MCC                : 0.3292
Confusion Matrix:
[[102545  11499]
 [  1260   2804]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9879    0.8992    0.9414    114044
       Fraud     0.1960    0.6900    0.3053      4064
    accuracy                         0.8920    118108
   macro avg     0.5920    0.7946    0.6234    118108
weighted avg     0.9606    0.8920    0.9195    118108

LightGBM - Remove C + D + id
Features: 363
Accuracy           : 0.8884
Precision          : 0.1927
Recall             : 0.7037
F1 Score           : 0.3026
ROC-AUC            : 0.8879
PR-AUC             : 0.4693
Balanced Accuracy  : 0.7993
MCC                : 0.3292
Confusion Matrix:
[[102064  11980]
 [  1204   2860]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9883    0.8950    0.9393    114044
       Fraud     0.1927    0.7037    0.3026      4064
    accuracy                         0.8884    118108
   macro avg     0.5905    0.7993    0.6210    118108
weighted avg     0.9610    0.8884    0.9174    118108

LightGBM - Remove C + D + V
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

LightGBM - Remove C + M + id
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

LightGBM - Remove C + M + V
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

LightGBM - Remove C + id + V
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

LightGBM - Remove D + M + id
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

LightGBM - Remove D + M + V
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

LightGBM - Remove D + id + V
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

LightGBM - Remove M + id + V
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

LightGBM - Remove C + D + M + id
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

LightGBM - Remove C + D + M + V
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

LightGBM - Remove C + D + id + V
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

LightGBM - Remove C + M + id + V
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

LightGBM - Remove D + M + id + V
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

LightGBM - Remove C + D + M + id + V
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
