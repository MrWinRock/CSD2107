import tensorflow as tf
from tensorflow.keras import layers, models

# Create a simple neural network model
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(input_size,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(output_size, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model (X_train and y_train are assumed to be your training data)
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Make predictions
predictions = model.predict(X_test)
