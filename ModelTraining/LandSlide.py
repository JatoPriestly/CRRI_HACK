import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("ModelTraining/dummy_landslide_data.csv")

# Preprocessing
label_encoder = LabelEncoder()
df['Land Cover'] = label_encoder.fit_transform(df['Land Cover'])
df['Soil Type'] = label_encoder.fit_transform(df['Soil Type'])

# Features and target variable
X = df[['Elevation (m)', 'Slope (degrees)', 'Rainfall (mm)', 'Soil Type', 'Land Cover']]
y = df['Landslide Occurrence']

# Standardize the data
scaler = StandardScaler()
X[['Elevation (m)', 'Slope (degrees)', 'Rainfall (mm)']] = scaler.fit_transform(X[['Elevation (m)', 'Slope (degrees)', 'Rainfall (mm)']])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model with class weights for imbalanced classes
rf_classifier = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
rf_classifier.fit(X_train, y_train)

# Save the trained model to a file using joblib
joblib.dump(rf_classifier, 'landslide_model.pkl')  # Save model immediately after training
print("Model saved successfully!")

# Predictions
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Display the classification report with zero_division=0 to avoid precision warnings
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
