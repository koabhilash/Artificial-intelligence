import numpy as np

# Node class for Decision Tree
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature        # Index of feature to split on
        self.threshold = threshold    # Threshold value for the feature
        self.left = left              # Left subtree (less than or equal to threshold)
        self.right = right            # Right subtree (greater than threshold)
        self.value = value            # Value if node is a leaf (class label)

# Function to calculate Gini impurity
def calculate_gini(y):
    classes = np.unique(y)
    gini = 0
    total_samples = len(y)
    
    for cls in classes:
        p = np.sum(y == cls) / total_samples
        gini += p * (1 - p)
        
    return gini

# Function to perform split based on a feature and threshold
def perform_split(X, y, feature, threshold):
    left_mask = X[:, feature] <= threshold
    right_mask = ~left_mask
    left_X, left_y = X[left_mask], y[left_mask]
    right_X, right_y = X[right_mask], y[right_mask]
    return left_X, left_y, right_X, right_y

# Function to find best split for a node
def find_best_split(X, y):
    best_gini = float('inf')
    best_feature = None
    best_threshold = None
    
    for feature in range(X.shape[1]):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_X, left_y, right_X, right_y = perform_split(X, y, feature, threshold)
            gini = (len(left_y) * calculate_gini(left_y) + len(right_y) * calculate_gini(right_y)) / len(y)
            if gini < best_gini:
                best_gini = gini
                best_feature = feature
                best_threshold = threshold
                
    return best_feature, best_threshold

# Function to build the Decision Tree
def build_tree(X, y, depth=0, max_depth=None):
    if depth == max_depth or len(np.unique(y)) == 1:
        # Create leaf node
        return Node(value=np.argmax(np.bincount(y)))
    
    feature, threshold = find_best_split(X, y)
    if feature is None:
        return Node(value=np.argmax(np.bincount(y)))
    
    left_X, left_y, right_X, right_y = perform_split(X, y, feature, threshold)
    left_subtree = build_tree(left_X, left_y, depth + 1, max_depth)
    right_subtree = build_tree(right_X, right_y, depth + 1, max_depth)
    
    return Node(feature=feature, threshold=threshold, left=left_subtree, right=right_subtree)

# Function to predict using the Decision Tree
def predict(tree, X):
    if tree.value is not None:
        return tree.value
    
    if X[tree.feature] <= tree.threshold:
        return predict(tree.left, X)
    else:
        return predict(tree.right, X)

# Function to calculate accuracy
def calculate_accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

# Example usage
if __name__ == "__main__":
    # Example dataset
    X = np.array([[2.5, 3],
                  [1, 1],
                  [4, 2],
                  [3, 4],
                  [2, 2],
                  [2, 3],
                  [3, 1],
                  [4, 4]])
    y = np.array([1, 0, 1, 0, 1, 1, 0, 0])

    # Build the Decision Tree
    tree = build_tree(X, y, max_depth=3)
    
    # Example prediction
    sample = np.array([3, 3.5])  # Example input for prediction
    prediction = predict(tree, sample)
    print(f"Prediction for {sample}: Class {prediction}")
