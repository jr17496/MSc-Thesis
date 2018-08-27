# MSc-Thesis
Motor Imagery implementation using Python 3 

The scripts and scenarios used in the final implementation have been uploaded on github and can be accessed by the following link https://github.com/jr17496/MSc-Thesis. The two scenarios used for data acquisition as well as the LUA script used for stimulus generation can be found in the �Openvibe� folder. The scripts used for classifier training and real time classification can be found in the �Real_time� folder. The Real_time_data_collection_and_classifier_training script is used to train the classifier, while The Real_time_output_prediction script is used to allow real-time classification using the pretrained classifiers from the previously mentioned script. Both of these scripts require the corresponding openvibe scenario to be run in the background. All other scripts found in the Real_time folder as well as the Classification and Laplacian_filter scripts found in the main folder of the project are used by these two main scripts. The script used to allow avatar movement in the virtual environment, along with a script to attempt object colour change can be found in the �VE� folder.The 'VE' folder also contains a executable build of the virtual environment. Scripts and Openvibe scenarios which were implemented but were not used in the final implementation can be found in the 'Dev' folder.