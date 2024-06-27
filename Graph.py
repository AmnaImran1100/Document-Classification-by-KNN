import os
import docx
import networkx as nx
import matplotlib.pyplot as plt

# Function to represent each document as a directed graph
def represent_document_as_graph(preprocessed_text):
    # Initialize a directed graph
    graph = nx.DiGraph()

    # Split the preprocessed text into words
    words = preprocessed_text.split()

    # Add each unique word as a node to the graph
    for word in set(words):
        graph.add_node(word)

    # Iterate through the words to create edges between consecutive words
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        graph.add_edge(current_word, next_word)

    return graph

# Function to read preprocessed text from a .docx file
def read_preprocessed_text(file_path):
    # Initialize an empty string to store text
    text = ""

    # Open the .docx file
    doc = docx.Document(file_path)

    # Extract text from the document
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text


# Folder containing .docx files
folder_path = r'C:\Users\A to Z\Documents\GitHub\Graph_Theory_Project_9296\StemmationProcessedFood'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.docx'):
        file_path = os.path.join(folder_path, filename)

        # Read preprocessed text from the .docx file
        preprocessed_text = read_preprocessed_text(file_path)

        # Represent the document as a directed graph
        graph = represent_document_as_graph(preprocessed_text)

        # Draw the graph
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(graph)  # positions for all nodes
        nx.draw(graph, pos, with_labels=True, arrows=True)
        plt.title(f"Directed Graph - {filename}")
        plt.show()

