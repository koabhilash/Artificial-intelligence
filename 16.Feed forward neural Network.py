import numpy as np

# Define the activation function (sigmoid in this case)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the activation function (for backpropagation)
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases randomly
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.weights2 = np.random.randn(hidden_size, output_size)
        self.bias2 = np.zeros((1, output_size))
    
    def forward(self, X):
        # Forward propagation through the network
        self.hidden_output = sigmoid(np.dot(X, self.weights1) + self.bias1)
        self.output = sigmoid(np.dot(self.hidden_output, self.weights2) + self.bias2)
        return self.output
    
    def train(self, X, y, epochs):
        # Training the neural network using backpropagation
        for epoch in range(epochs):
            # Forward propagation
            output = self.forward(X)
            
            # Backpropagation
            error = y - output
            delta_output = error * sigmoid_derivative(output)
            
            error_hidden = delta_output.dot(self.weights2.T)
            delta_hidden = error_hidden * sigmoid_derivative(self.hidden_output)
            
            # Updating weights and biases
            self.weights2 += self.hidden_output.T.dot(delta_output)
            self.bias2 += np.sum(delta_output, axis=0, keepdims=True)
            self.weights1 += X.T.dot(delta_hidden)
            self.bias1 += np.sum(delta_hidden, axis=0, keepdims=True)
    
    def predict(self, X):
        # Predicting output for new data
        return self.forward(X)

# Example usage
if __name__ == "__main__":
    # Example dataset (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    
    # Define neural network parameters
    input_size = X.shape[1]
    hidden_size = 4
    output_size = 1
    epochs = 10000
    
    # Create a neural network
    nn = NeuralNetwork(input_size, hidden_size, output_size)
    
    # Train the neural network
    nn.train(X, y, epochs)
    
    # Make predictions
    predictions = nn.predict(X)
    print("Predictions:")
    for i in range(len(X)):
        print(f"Input: {X[i]}, Predicted Output: {predictions[i]}")
