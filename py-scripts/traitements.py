import pandas as pd
from Meaner import Meaner
import matplotlib.pyplot as plt
import seaborn as sns

def get_missing_values_columns(col):
    null_values_column = []
    for column, count in col.items():
        if count >= 1:
            null_values_column.append(column)
    return null_values_column
            
    

# Input data
df = pd.read_csv('star_classification.csv')


# Display missing vales
print("Checking missing values...\n")
count_missing_values = df.isnull().sum()
missing_values_columns = get_missing_values_columns(count_missing_values)

meaner_instance = Meaner(df)
dict_col_mean_mode = {}

for val in missing_values_columns:
    mean_mode = meaner_instance.get_mean_mode(val)
    dict_col_mean_mode[val] = mean_mode

print(dict_col_mean_mode,"\n")


#Populate missing values with mean or mode

for column, value in dict_col_mean_mode.items():
    df[column].fillna(value, inplace=True)


#Re-check for missing values
print("Validate repopulation\n")
print(df.isnull().sum())

    
    
# Supprimer les doublons
print("Checking duplicates...\n")
if df.drop_duplicates(inplace=True) is None:
    print("No duplicates found\n")
else:
    print("Duplicates found and deleted\n")



#Vizualize data

# Distribution des revenus idéaux
sns.histplot(df['IdealYearlyIncome'])
plt.show()

# # Relations entre différentes variables
sns.pairplot(df)
plt.show()


# Continue for machine learning to predict income
# Assuming the target column is 'IdealYearlyIncome' and features are the rest
X = df.drop(columns='IdealYearlyIncome')
y = df['IdealYearlyIncome']

# Splitting data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Example model training (Random Forest)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")

# Visualize feature importance
importances = model.feature_importances_
features = X.columns
importance_df = pd.DataFrame({'Feature': features, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title('Feature Importance')
plt.show()        



