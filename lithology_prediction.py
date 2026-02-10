# Functions to predict lithology using machine learning algorithms random forest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split

from lithology_prediction_using_machine_learning import visualisation

def train_random_forest(train_csv, test_csv):
    # Read the training and testing CSV files
    train_data = pd.read_csv(train_csv)
    test_data = pd.read_csv(test_csv)

    # Separate features and target variable
    X_train = train_data.drop(columns=['Facies'])
    y_train = train_data['Facies']
    X_test = test_data.drop(columns=['Facies'])
    y_test = test_data['Facies']

    # Train the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    return model, y_test, y_pred

if __name__ == "__main__":
    # Train the Random Forest model and evaluate it
    model, y_test, y_pred = train_random_forest('train_data.csv', 'test_data.csv')  

    visualisation.plot_confusion_matrix(y_test, y_pred)
    visualisation.plot_feature_importance(model, X_train.columns)

def predict_lithology(model, new_data_csv):
    # Read the new data CSV file
    new_data = pd.read_csv(new_data_csv)

    # Predict lithology using the trained model
    predictions = model.predict(new_data)

    return predictions

def save_predictions(predictions, output_csv):
    # Save the predictions to a CSV file
    predictions_df = pd.DataFrame(predictions, columns=['Predicted_Facies'])
    predictions_df.to_csv(output_csv, index=False)
