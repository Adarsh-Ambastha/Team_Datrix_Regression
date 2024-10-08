# README

## Project Overview

We are building a machine learning model for **Used Car Price Prediction** specifically for **Maruti Cars in India**. The model is designed to predict the price of used Maruti cars based on 11 key features, such as year, kilometers driven, fuel type, transmission, and more. The dataset was scraped using **Selenium** and **BeautifulSoup** from the **Cars24** website, consisting of around **1,444 rows**.

The project involves multiple regression models, including **Linear Regression**, **Ridge Regression** and **Lasso Regression**, .The models are evaluated using metrics like **Mean Squared Error (MSE)**, **Root Mean Squared Error (RMSE)**, **Mean Absolute Error (MAE)**, and **R² Score** to ensure that the best-performing model is chosen.

## Aim

Our aim is to accurately predict the prices of used Maruti cars using a variety of machine learning algorithms. By tuning different models and evaluating their performance on the dataset, we hope to find the best predictive model.


## Modelling Summary 

- Three machine learning pipelines are defined: Ridge Regression, Lasso Regression, and Linear Regression, each with specific data scaling steps
- Hyperparameter grids are set up for Ridge and Lasso Regression to optimize model performance
- Evaluation metrics include MSE, R², MAE, and RMSE for comprehensive model assessment
- GridSearchCV is used to iterate through models, perform cross-validation, and select the best-performing model based on R² score
- Models are systematically evaluated on training, validation, and test datasets to assess performance and generalization capabilities
- The evaluation process helps in monitoring overfitting, underfitting, and predicting real-world performance

## Running the Program on Your Local Device

### 1. Install the Required Libraries

To run the program, you first need to install all the required Python libraries. These are listed in the `requirements.txt` file.

1. Clone this repository to your local machine:

   ```bash
   git clone "https://github.com/Adarsh-Ambastha/Team_Datrix_Regression"
   ```

2. Navigate to the project directory:

   ```bash
   cd prediction/ml_env
   ```

3. Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

### 2. Download the Dataset

The dataset required for the prediction models is not included in this repository. You need to download the dataset from the main model file, which is stored on Google Drive. 

1. Download the dataset from this [Google Drive link](https://drive.google.com/uc?id=1zF3fYQbAUDE0Jx3lvBHC8GjaK8i9wrno)
2. Save the CSV file on your local device in an accessible location.

### 3. Modify the File Paths

Once you have downloaded the CSV file, you'll need to modify the paths in the code to ensure it points to the correct location of the dataset on your local device.

1. Open the prediction file where the dataset is being loaded using `pandas`.
2. Change the path in all occurrences of `pd.read_csv()` to the path where your CSV file is saved.

For example, modify this:

```python
df = pd.read_csv('path/to/your/data.csv')
```

to:

```python
df = pd.read_csv('your/local/path/to/data.csv')
```

### 4. Run the Program

After modifying the file paths, you can run the program using your preferred IDE or from the command line:

The model will start training and evaluating, and the results will be displayed in the terminal or console.

## Conclusion

By following the steps above, you can easily run the model on your local machine and evaluate its performance using different regression techniques. 

## Results on test set

#### Ridge Regression Performance on Test Set:

-  Root Mean Squared Error: 54643.29
-  Mean Absolute Error: 43557.65
-  R² Score: 0.88

#### Lasso Regression Performance on Test Set:

- Root Mean Squared Error: 54759.61
- Mean Absolute Error: 43634.84
- R² Score: 0.88

#### Linear Regression Performance on Test Set:

- Root Mean Squared Error: 54488.55
- Mean Absolute Error: 43244.49
- R² Score: 0.88



## Team DATRIX Assignment 1 FOML
#### **TEAM MEMBERS**
#### DAIICT M.Sc DS 24-26 
- **PRAGNYA DANDVATE: 202418065 (L)**
- **ADARSH AMBASTH :  202418004**
- **AMAN RAJPUT :     202418003**
- **YASHRAJ SINH :    202418064**

**Note: all the graph used for visualization are plotted using plotly Library, due to dynamic nature of plottly  it is not reflecting on the git , but works properly on local machine or colab**
