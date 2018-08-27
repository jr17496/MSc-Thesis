from sklearn.metrics import accuracy_score, precision_score,recall_score
import pickle
import random
import numpy as np
from sklearn import svm
def classification(input, targets, sample_percentage,evaluate = False):

    if evaluate == True:
        indexes = random.sample(range(0, len(input)), int(len(input)*0.01*sample_percentage))
        test_input = [input[i] for i in indexes]
        test_target = [targets[i] for i in indexes]
        train_input = np.delete(input,indexes,axis = 0)
        train_targets = np.delete(targets,indexes,axis = 0)
        clf_evaluation = svm.SVC()
        clf_evaluation.fit(train_input, train_targets)
        evaluation_predictions = clf_evaluation.predict(test_input)
        print(accuracy_score(test_target,evaluation_predictions))
        print(precision_score(test_target,evaluation_predictions,average='macro'))
        print(recall_score(test_target, evaluation_predictions, average='macro'))

    clf = svm.SVC()
    clf.fit(input,targets)
    pickle.dump(clf,open('SVM_classifier.pkl','wb'))