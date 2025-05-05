import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

# Step 1: Load the dataset
url = "Train.csv"
df = pd.read_csv(url)

# Selecting features and target
FEATURES = ["Warehouse_block", "Mode_of_Shipment", "Customer_care_calls", "Customer_rating","Cost_of_the_Product","Prior_purchases","Product_importance","Gender","Discount_offered","Weight_in_gms"]
TARGET = "Reached_on_time"

# Step 2: Preprocess the data
imputer = SimpleImputer(strategy='most_frequent')
data_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Check for missing values
#print(data.isnull().sum())

# Encode all object (categorical) columns
for column in data_imputed.columns:
    if data_imputed[column].dtype == 'object':
        data_imputed[column] = LabelEncoder().fit_transform(data_imputed[column])   

# # Step 3: Split the dataset into features and target variable
X = data_imputed[FEATURES]
y = data_imputed[TARGET]

# Step 4: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Step 5: Train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 6: Make predictions
#y_pred = model.predict(X_test)

# Step 7: Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model, "delivery_predictor.pkl")

def load_model():
    """Loads the trained model."""
    return joblib.load("delivery_predictor.pkl")

def predict_delivery(input_data: dict):
    """Takes JSON input and predicts delivery."""
    model = load_model()
    df_input = pd.DataFrame([input_data])

    # encode categorical fields as done during training
    label_encoders = {
        'Warehouse_block': {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4},
        'Mode_of_Shipment': {'Flight': 0, 'Road': 1, 'Ship': 2},
        'Product_importance': {'low': 1, 'medium': 2, 'high': 0},  # match training order
        'Gender': {'F': 0, 'M': 1}
    }

    for col, mapping in label_encoders.items():
        df_input[col] = df_input[col].map(mapping)

    prediction = model.predict(df_input)
    return int(prediction[0])
