# Barbell Motion Tracking with Machine Learning

This project aims to use data science methods to analyse variety of barbell exercises and build a ML model that would recognise these exercises. Utilizing gyroscope and accelerometer data from wrist motion sensors worn by participants during exercises, I perform data cleaning, wrangling, visualization, interpret data and develop a machine learning model.

If you're interested to delve deeper into motion sensors and the applications, as well as the underlying mathematical principles, I highly recommend readint this [Nature article](https://www.nature.com/articles/s41467-020-19424-2), it offers a comprehensive insight into the significance of this research area.

Please note that this is my first machine learning project and GitHub experience. As of May 26th, this project is still in progress, and I am currently in the process of developing the machine learning model. Advice or constructive feedback welcomed! I would appreciate it as I continue learning and refining my skills in the field of Data Science! The project idea taken from [Dave Ebbelaar](https://github.com/daveebbelaar/tracking-barbell-exercises)

Please refer to the project [folder structure](https://github.com/SergejData/barbell-exercise-motion-pattern-recognition/blob/master/references/folder_structure.txt) if you're lost in the folders. This file will be further adjusted to the project.


## Data

The time series [dataset](https://github.com/SergejData/barbell-exercise-motion-pattern-recognition/tree/master/data/raw/MetaMotion) comes from CSV files generated by gyroscope and accelerometer during barbell exercises such as squat, deadlift, bench press, overhead press and barbell row. Exercises were performed at medium and high difficulty levels, 

## Methodology

- [x] **Data Wrangling:** In this step, I process the raw CSV files to remove/solve any inconsistencies and errors, missing values in the dataset. I then transform raw data and map into an interim data. This involves merging all CSV files into a single one, extracting exercise name, participant name and exercise difficulty from the filename.csv, adding these as columns to the data frame. It also involves resampling the resulting time-series data from both the accelerometer and the gyroscope to ensure that the time scale is aligned.

- [x] **Data Visualization:** Using matplotlib and seaborn library, I explore the patterns in the data, check for quiality and outliers. This helps to make fine adjustments to the data and develop the machine learning models.

- [ ] **Machine Learning:** Currently under development. The goal of this step is to use the processed data to develop machine learning models that can classify exercises, count the number of repetitions. I assume I will add some more aims to this part soon!

## Future Work

I plan to continue refining machine learning models and explore additional features that could be extracted from the sensor data. Suggestions are welcomed!