"""
3) Python Script to Simulate Simple Attention Weights
This script illustrates how attention weights are computed simply using dot-products and softmax, simulating a core idea behind Transformers.
"""

import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=-1, keepdims=True)

# Simulate some 'query', 'key' vectors for three words in a sequence
queries = np.array([[1, 0], [0, 1], [1, 1]])  # shape: (3, 2)
keys = np.array([[1, 0], [0, 1], [1, 1]])     # shape: (3, 2)

# Compute raw attention scores (dot product between queries and keys)
scores = np.dot(queries, keys.T)  # shape: (3, 3)

# Convert scores to attention weights using softmax
attention_weights = softmax(scores)

print("Raw Attention Scores:\n", scores)
print("\nAttention Weights (softmax applied):\n", attention_weights)
