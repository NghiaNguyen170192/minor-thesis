
RF - Baseline
Features: 437
Accuracy           : 0.9723
Precision          : 0.8778
Recall             : 0.2281
F1 Score           : 0.3621
ROC-AUC            : 0.9012
PR-AUC             : 0.5306
Balanced Accuracy  : 0.6135
MCC                : 0.4395
Confusion Matrix:
[[113915    129]
 [  3137    927]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9732    0.9989    0.9859    114044
       Fraud     0.8778    0.2281    0.3621      4064
    accuracy                         0.9723    118108
   macro avg     0.9255    0.6135    0.6740    118108
weighted avg     0.9699    0.9723    0.9644    118108

RF - Feature Engineering
Features: 439
Accuracy           : 0.9725
Precision          : 0.8857
Recall             : 0.2308
F1 Score           : 0.3662
ROC-AUC            : 0.9050
PR-AUC             : 0.5366
Balanced Accuracy  : 0.6149
MCC                : 0.4443
Confusion Matrix:
[[113923    121]
 [  3126    938]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9733    0.9989    0.9859    114044
       Fraud     0.8857    0.2308    0.3662      4064
    accuracy                         0.9725    118108
   macro avg     0.9295    0.6149    0.6761    118108
weighted avg     0.9703    0.9725    0.9646    118108

RF - Remove C
Features: 423
Accuracy           : 0.9715
Precision          : 0.8816
Recall             : 0.1978
F1 Score           : 0.3232
ROC-AUC            : 0.8902
PR-AUC             : 0.4894
Balanced Accuracy  : 0.5984
MCC                : 0.4100
Confusion Matrix:
[[113936    108]
 [  3260    804]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9722    0.9991    0.9854    114044
       Fraud     0.8816    0.1978    0.3232      4064
    accuracy                         0.9715    118108
   macro avg     0.9269    0.5984    0.6543    118108
weighted avg     0.9691    0.9715    0.9626    118108

RF - Remove D
Features: 415
Accuracy           : 0.9728
Precision          : 0.8799
Recall             : 0.2434
F1 Score           : 0.3813
ROC-AUC            : 0.8998
PR-AUC             : 0.5273
Balanced Accuracy  : 0.6211
MCC                : 0.4547
Confusion Matrix:
[[113909    135]
 [  3075    989]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9737    0.9988    0.9861    114044
       Fraud     0.8799    0.2434    0.3813      4064
    accuracy                         0.9728    118108
   macro avg     0.9268    0.6211    0.6837    118108
weighted avg     0.9705    0.9728    0.9653    118108

RF - Remove M
Features: 428
Accuracy           : 0.9725
Precision          : 0.8772
Recall             : 0.2320
F1 Score           : 0.3670
ROC-AUC            : 0.8989
PR-AUC             : 0.5274
Balanced Accuracy  : 0.6154
MCC                : 0.4431
Confusion Matrix:
[[113912    132]
 [  3121    943]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9733    0.9988    0.9859    114044
       Fraud     0.8772    0.2320    0.3670      4064
    accuracy                         0.9725    118108
   macro avg     0.9253    0.6154    0.6765    118108
weighted avg     0.9700    0.9725    0.9646    118108

RF - Remove id
Features: 399
Accuracy           : 0.9727
Precision          : 0.8835
Recall             : 0.2370
F1 Score           : 0.3737
ROC-AUC            : 0.9029
PR-AUC             : 0.5314
Balanced Accuracy  : 0.6179
MCC                : 0.4496
Confusion Matrix:
[[113917    127]
 [  3101    963]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9735    0.9989    0.9860    114044
       Fraud     0.8835    0.2370    0.3737      4064
    accuracy                         0.9727    118108
   macro avg     0.9285    0.6179    0.6799    118108
weighted avg     0.9704    0.9727    0.9650    118108

RF - Remove V
Features: 98
Accuracy           : 0.9708
Precision          : 0.8974
Recall             : 0.1700
F1 Score           : 0.2859
ROC-AUC            : 0.9125
PR-AUC             : 0.5526
Balanced Accuracy  : 0.5847
MCC                : 0.3835
Confusion Matrix:
[[113965     79]
 [  3373    691]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9713    0.9993    0.9851    114044
       Fraud     0.8974    0.1700    0.2859      4064
    accuracy                         0.9708    118108
   macro avg     0.9343    0.5847    0.6355    118108
weighted avg     0.9687    0.9708    0.9610    118108

RF - Remove C + D
Features: 401
Accuracy           : 0.9719
Precision          : 0.8761
Recall             : 0.2124
F1 Score           : 0.3418
ROC-AUC            : 0.8851
PR-AUC             : 0.4875
Balanced Accuracy  : 0.6056
MCC                : 0.4235
Confusion Matrix:
[[113922    122]
 [  3201    863]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9727    0.9989    0.9856    114044
       Fraud     0.8761    0.2124    0.3418      4064
    accuracy                         0.9719    118108
   macro avg     0.9244    0.6056    0.6637    118108
weighted avg     0.9693    0.9719    0.9635    118108

RF - Remove C + M
Features: 414
Accuracy           : 0.9715
Precision          : 0.8733
Recall             : 0.2000
F1 Score           : 0.3255
ROC-AUC            : 0.8853
PR-AUC             : 0.4828
Balanced Accuracy  : 0.5995
MCC                : 0.4102
Confusion Matrix:
[[113926    118]
 [  3251    813]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9723    0.9990    0.9854    114044
       Fraud     0.8733    0.2000    0.3255      4064
    accuracy                         0.9715    118108
   macro avg     0.9228    0.5995    0.6555    118108
weighted avg     0.9688    0.9715    0.9627    118108

RF - Remove C + id
Features: 385
Accuracy           : 0.9718
Precision          : 0.8803
Recall             : 0.2082
F1 Score           : 0.3367
ROC-AUC            : 0.8874
PR-AUC             : 0.4868
Balanced Accuracy  : 0.6036
MCC                : 0.4203
Confusion Matrix:
[[113929    115]
 [  3218    846]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9725    0.9990    0.9856    114044
       Fraud     0.8803    0.2082    0.3367      4064
    accuracy                         0.9718    118108
   macro avg     0.9264    0.6036    0.6611    118108
weighted avg     0.9694    0.9718    0.9633    118108

RF - Remove C + V
Features: 84
Accuracy           : 0.9665
Precision          : 0.9286
Recall             : 0.0288
F1 Score           : 0.0558
ROC-AUC            : 0.8838
PR-AUC             : 0.4101
Balanced Accuracy  : 0.5144
MCC                : 0.1603
Confusion Matrix:
[[114035      9]
 [  3947    117]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9665    0.9999    0.9830    114044
       Fraud     0.9286    0.0288    0.0558      4064
    accuracy                         0.9665    118108
   macro avg     0.9476    0.5144    0.5194    118108
weighted avg     0.9652    0.9665    0.9510    118108

RF - Remove D + M
Features: 406
Accuracy           : 0.9728
Precision          : 0.8769
Recall             : 0.2436
F1 Score           : 0.3813
ROC-AUC            : 0.8956
PR-AUC             : 0.5201
Balanced Accuracy  : 0.6212
MCC                : 0.4541
Confusion Matrix:
[[113905    139]
 [  3074    990]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9737    0.9988    0.9861    114044
       Fraud     0.8769    0.2436    0.3813      4064
    accuracy                         0.9728    118108
   macro avg     0.9253    0.6212    0.6837    118108
weighted avg     0.9704    0.9728    0.9653    118108

RF - Remove D + id
Features: 377
Accuracy           : 0.9731
Precision          : 0.8745
Recall             : 0.2554
F1 Score           : 0.3954
ROC-AUC            : 0.8945
PR-AUC             : 0.5197
Balanced Accuracy  : 0.6271
MCC                : 0.4644
Confusion Matrix:
[[113895    149]
 [  3026   1038]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9741    0.9987    0.9863    114044
       Fraud     0.8745    0.2554    0.3954      4064
    accuracy                         0.9731    118108
   macro avg     0.9243    0.6271    0.6908    118108
weighted avg     0.9707    0.9731    0.9659    118108

RF - Remove D + V
Features: 76
Accuracy           : 0.9732
Precision          : 0.9051
Recall             : 0.2466
F1 Score           : 0.3875
ROC-AUC            : 0.9063
PR-AUC             : 0.5708
Balanced Accuracy  : 0.6228
MCC                : 0.4647
Confusion Matrix:
[[113939    105]
 [  3062   1002]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9738    0.9991    0.9863    114044
       Fraud     0.9051    0.2466    0.3875      4064
    accuracy                         0.9732    118108
   macro avg     0.9395    0.6228    0.6869    118108
weighted avg     0.9715    0.9732    0.9657    118108

RF - Remove M + id
Features: 390
Accuracy           : 0.9725
Precision          : 0.8769
Recall             : 0.2330
F1 Score           : 0.3682
ROC-AUC            : 0.8965
PR-AUC             : 0.5257
Balanced Accuracy  : 0.6159
MCC                : 0.4440
Confusion Matrix:
[[113911    133]
 [  3117    947]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9734    0.9988    0.9859    114044
       Fraud     0.8769    0.2330    0.3682      4064
    accuracy                         0.9725    118108
   macro avg     0.9251    0.6159    0.6771    118108
weighted avg     0.9700    0.9725    0.9647    118108

RF - Remove M + V
Features: 89
Accuracy           : 0.9709
Precision          : 0.8932
Recall             : 0.1750
F1 Score           : 0.2926
ROC-AUC            : 0.9037
PR-AUC             : 0.5397
Balanced Accuracy  : 0.5871
MCC                : 0.3881
Confusion Matrix:
[[113959     85]
 [  3353    711]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9714    0.9993    0.9851    114044
       Fraud     0.8932    0.1750    0.2926      4064
    accuracy                         0.9709    118108
   macro avg     0.9323    0.5871    0.6389    118108
weighted avg     0.9687    0.9709    0.9613    118108

RF - Remove id + V
Features: 60
Accuracy           : 0.9710
Precision          : 0.8969
Recall             : 0.1777
F1 Score           : 0.2966
ROC-AUC            : 0.9090
PR-AUC             : 0.5517
Balanced Accuracy  : 0.5885
MCC                : 0.3920
Confusion Matrix:
[[113961     83]
 [  3342    722]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9715    0.9993    0.9852    114044
       Fraud     0.8969    0.1777    0.2966      4064
    accuracy                         0.9710    118108
   macro avg     0.9342    0.5885    0.6409    118108
weighted avg     0.9689    0.9710    0.9615    118108

RF - Remove C + D + M
Features: 392
Accuracy           : 0.9719
Precision          : 0.8725
Recall             : 0.2156
F1 Score           : 0.3457
ROC-AUC            : 0.8803
PR-AUC             : 0.4765
Balanced Accuracy  : 0.6072
MCC                : 0.4257
Confusion Matrix:
[[113916    128]
 [  3188    876]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9728    0.9989    0.9857    114044
       Fraud     0.8725    0.2156    0.3457      4064
    accuracy                         0.9719    118108
   macro avg     0.9226    0.6072    0.6657    118108
weighted avg     0.9693    0.9719    0.9636    118108

RF - Remove C + D + id
Features: 363
Accuracy           : 0.9722
Precision          : 0.8775
Recall             : 0.2239
F1 Score           : 0.3568
ROC-AUC            : 0.8765
PR-AUC             : 0.4736
Balanced Accuracy  : 0.6114
MCC                : 0.4353
Confusion Matrix:
[[113917    127]
 [  3154    910]]
Classification Report:
              precision    recall  f1-score   support
  Legitimate     0.9731    0.9989    0.9858    114044
       Fraud     0.8775    0.2239    0.3568      4064
    accuracy                         0.9722    118108
   macro avg     0.9253    0.6114    0.6713    118108
weighted avg     0.9698    0.9722    0.9642    118108

RF - Remove C + D + V
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

RF - Remove C + M + id
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

RF - Remove C + M + V
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

RF - Remove C + id + V
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

RF - Remove D + M + id
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

RF - Remove D + M + V
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

RF - Remove D + id + V
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

RF - Remove M + id + V
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

RF - Remove C + D + M + id
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

RF - Remove C + D + M + V
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
