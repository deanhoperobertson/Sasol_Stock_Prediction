#data
from data_downloader import downloader
from preprocessing import process

#Model
from sklearn_crfsuite import CRF

#Evalulation
from sklearn_crfsuite.metrics import flat_classification_report
from sklearn_crfsuite.metrics import flat_f1_score
from sklearn_crfsuite.metrics import flat_accuracy_score

data = downloader()

X_train, Y_train = process(data)

crf4 = CRF(algorithm='lbfgs',
           max_iterations=20,
           c1=0.1,
           c2=0.2,
           all_possible_transitions=False)

#training model
crf4.fit(X=X_train, y=Y_train)

#generate predictions
pred = crf4.predict(X_train)

#generate report on entire model
report = flat_classification_report(y_pred=pred, y_true=Y_train)
print(report)

acc = flat_accuracy_score(y_pred=pred, y_true=Y_train)
print("Accuracy=%.2f"%(acc*100))
