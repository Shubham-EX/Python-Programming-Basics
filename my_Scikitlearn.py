from sklearn.linear_model import

Linear Regression from sklearn.model_selection import train_test_split from sklearn.metrics import mean_squared_error

# Sample data

X = np.random.rand(100, 1) y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)

# Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model 
model = Linear Regression()

# Train the model 
model.fit(X_train, y_train)

# Make predictions

y_pred model.predict(X_test)

# Evaluate the model

mse = mean_squared_error(y_test, y_pred) print(f'Mean Squared Error: {mse}')