
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the data (replace 'user_behavior_data.csv' with your actual file path)
data = pd.read_csv('user_behavior_data.csv')

# Data preprocessing
data['click_rate'] = data['clicks'] / data['impressions']
data['time_spent_per_session'] = data['total_time_spent'] / data['sessions']

# Split the data into training and testing sets
X = data[['click_rate', 'time_spent_per_session', 'sessions']]
y = data['ad_clicked']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model (Logistic Regression as an example)
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print results
print(f"Model Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)

# Save the model for deployment (using joblib)
import joblib
joblib.dump(model, 'ads_recommendation_model.pkl')
