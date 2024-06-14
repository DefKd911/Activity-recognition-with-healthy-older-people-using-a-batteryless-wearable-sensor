# Activity-recognition-with-healthy-older-people-using-a-batteryless-wearable-sensors via Machine learning approach

![Overview-of-our-technological-approach-for-falls-prevention-A-patient-wears-our-wearable](https://github.com/DefKd911/Activity-recognition-with-healthy-older-people-using-a-batteryless-wearable-sensor/assets/172142546/c4d634b9-d109-4b67-b458-220b6888e733)

The increasing ageing population around the world, is calling for technological innovations that can improve the lives of elderly people. Real time monitoring their activities is imperative in order to mitigate the detrimental occurrences and dangerous events like falls. Our aim is to develop and test a Machine Learning model, capable to determine the activity performed by the elderly in their everyday environment.


![sensors-16-00546-g001](https://github.com/DefKd911/Activity-recognition-with-healthy-older-people-using-a-batteryless-wearable-sensor/assets/172142546/e25cf70d-29dd-4353-b834-05a4598915f9)


# Data : 
Data for this research was acquired by setting up two fully monitored rooms, equipped with Radio Frequency Identification (RFID) antennas, while subjects who participated in the experiment were wearing a Wearable Wireless Identification and Sensing Platform (W2ISP) tag. The dataset consisted of 14 healthy elders, who would perform four activities namely: sitting on the bed, sitting on a chair, lying in bed and ambulating. Nine independent variables were used, eight of which were obtained by the sensors as raw data vectors and the ninth is the gender. The final data set includes 75,128 records.
![image](https://github.com/DefKd911/Activity-recognition-with-healthy-older-people-using-a-batteryless-wearable-sensor/assets/172142546/5f5e3a23-3ac8-4ca1-bdf4-89d5f5b49cb9)
Most falls of the elderly occur around the bed and the chair area, both in residential houses and clinics. Thus, the developers of the data set, decided that sampling should be done in areas that simulate hospital rooms. These two rooms were framed with RFID antennas. In room 1, 4 reading antennas were used (one at ceiling level and three at the wall), while in rooms 2, 3 antennas were used (two at ceiling level and one at the wall) [38]. The antennas were strategically placed so as to cover the maximum space inside the room. Each subjectwas asked to perform a series of broadly scripted activity routines that were an alternation between activities (1) sitting on bed, (2) lying on bed, (3) sitting on chair and (4) walking from A to B, where A, B are the bed, chair or door [41]. Totally, 10 subjects were recorded for the first room 1, and five for the 2nd. One subject participated in both rooms. 

This dataset is available from the UCI Machine Learning Repository. If you use this dataset, please cite it as follows:
Torres,Roberto, Visvanathan,Renuka, and Ranasinghe,Damith. (2016). Activity recognition with healthy older people using a batteryless wearable sensor. UCI Machine Learning Repository. https://doi.org/10.24432/C5GG6B.
For more details, visit the UCI Machine Learning Repository page: https://archive.ics.uci.edu/dataset/427/activity+recognition+with+healthy+older+people+using+a+batteryless+wearable+sensor

# Features :
![image](https://github.com/DefKd911/Activity-recognition-with-healthy-older-people-using-a-batteryless-wearable-sensor/assets/172142546/683c63aa-1f55-45b4-ae58-ea42ffe8ac46)
# Dataset Pre-Processing 
The dataset provides 60 *.csv files for room 2 and 28 *.csv files for room 2. Each *.csv file includes the eight features from the W2ISP sensor and the RFID reader and the label for each record. Data is handled by removing outliers for model training. 
# MODEL training
A total of 6 classification algorithms have been employed namely:  SVM,KNN,multinomial Logistic Regression,XGboost,Random Forest classifier  
However only the Random Forest ensemble algorithm that achieved the highest performance with accuracy of : 99.086% 


HYPERPARAMETER TUNING : we have chosen the combination of n-fold Cross Validation and Grid Search, this is one of the most 
widely strategies used in ML.

# Model evaluation report & parameters
! yet to be attached 
# application
Given model is deployed via Flask , accesable to local host 
![image](https://github.com/DefKd911/Activity-recognition-with-healthy-older-people-using-a-batteryless-wearable-sensor/assets/172142546/0bfeefcd-3087-4850-8c13-d0ce18f6ce54)


