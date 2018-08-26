from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.metrics import accuracy_score, precision_score,recall_score,classification_report,confusion_matrix
import pickle
import random
import numpy as np

#method parameters:
# the full training set for a metric, targets, sample percentage, a flag to perform evaluation or not, classifier to use and metric
def classification(input, targets, sample_percentage,evaluate = False, classifier = 'SVM', metric_name = 'PLV'):
    if classifier == 'SVM':
        clf_used = svm.SVC()
    elif classifier == 'KNN':
        clf_used = knn(n_neighbors=3)
    elif classifier == 'RFC':
        clf_used = rfc()

    #If the evaluation flag is true a random sample of indexes, the number of samples is calculated as the integer
    #value of the percentage times the lenght of the training set.
    #Two arreys are created, one for testing, while the other for evaluation using the random indexes obtained
    #The target set is split in the same way
    #Accuracy, a classification report (containing the precision, recall, F1 score and support) and confusion matrix are calculated
    #using the true and predicted classes
    if evaluate == True:
        indexes = random.sample(range(0, len(input)), int(len(input)*0.01*sample_percentage))
        test_input = [input[i] for i in indexes]
        test_target = [targets[i] for i in indexes]
        train_input = np.delete(input,indexes,axis = 0)
        train_targets = np.delete(targets,indexes,axis = 0)
        clf_evaluation = clf_used
        clf_evaluation.fit(train_input, train_targets)
        evaluation_predictions = clf_evaluation.predict(test_input)
        print('Accuracy')
        print(accuracy_score(test_target,evaluation_predictions))
        print(classification_report(test_target, evaluation_predictions))
        print('Confusion matrix')
        print(confusion_matrix(test_target, evaluation_predictions))

    #A classifier is trained on the entire training set and serialized to a pickle object

    clf = clf_used
    clf.fit(input,targets)
    pickle.dump(clf,open(classifier+'_classifier'+metric_name+'.pkl','wb'))