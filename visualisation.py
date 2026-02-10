# visualize the results of the machine learning model
import pandas as pd
import matplotlib.pyplot as plt

def plot_facies_distribution(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Plot the distribution of facies labels
    plt.figure(figsize=(10, 6))
    data['Facies'].value_counts().plot(kind='bar')
    plt.title('Distribution of Facies Labels')
    plt.xlabel('Facies')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()

def plot_feature_importance(model, feature_names):
    # Get feature importance from the model
    importance = model.feature_importances_

    # Create a DataFrame for feature importance
    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importance})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    # Plot feature importance
    plt.figure(figsize=(10, 6))
    plt.bar(feature_importance_df['Feature'], feature_importance_df['Importance'])
    plt.title('Feature Importance')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.show()

def plot_confusion_matrix(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    import seaborn as sns

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

def wireline_log_plot(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Plot wireline logs
    plt.figure(figsize=(12, 8))
    for column in data.columns:
        if column not in ['Depth', 'Facies']:
            plt.plot(data['Depth'], data[column], label=column)
    plt.title('Wireline Logs')
    plt.xlabel('Depth')
    plt.ylabel('Log Values')
    plt.legend()
    plt.gca().invert_yaxis()  # Invert y-axis for depth
    plt.show()

def plot_prediction_results(y_true, y_pred):
    # Plot true vs predicted facies labels
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.title('True vs Predicted Facies Labels')
    plt.xlabel('True Facies')
    plt.ylabel('Predicted Facies')
    plt.show()

def plot_wireline_log_with_facies(csv_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Plot wireline logs with facies labels
    plt.figure(figsize=(12, 8))
    for column in data.columns:
        if column not in ['Depth', 'Facies']:
            plt.plot(data['Depth'], data[column], label=column)
    plt.scatter(data['Depth'], data['Facies'], color='red', label='Facies', alpha=0.5)
    plt.title('Wireline Logs with Facies Labels')
    plt.xlabel('Depth')
    plt.ylabel('Log Values / Facies')
    plt.legend()
    plt.gca().invert_yaxis()  # Invert y-axis for depth
    plt.show()

    