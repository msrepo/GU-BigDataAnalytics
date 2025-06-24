import os
import glob

def load_words_from_file(file_path):
    """
    Load words from a text file and return them as a set.
    """
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
        text = file.read()
        # Normalize text: convert to lowercase and split into words
        words = text.lower().split()
        # Remove punctuation and special characters
        words = [word.strip(".,!?\"'()[]{}") for word in words]
        return set(words)

def load_text_from_file(file_path):
    """
    Load text from a file and return it as a string.
    """
    with open(file_path, "r", encoding='utf-8', errors='ignore') as file:
        return file.read().split(' ')
    
def find_similarity_scores(input_file, directory, use_tf_idf, n_grams):
    """
    Find the file with the most common words compared to the input file.
    """
    # Extract the task name from the input file (e.g., "taska" from "g0pA_taska.txt")
    task_name = os.path.basename(input_file).split("_")[1].split(".")[0].lower()

    print(f"Task name extracted: {task_name}")
    # Ensure the input file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    # Ensure the directory exists
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The directory {directory} does not exist.")
    
    print(f"Input file: {input_file}")
    
    # Load words from the input file
    input_words = load_words_from_file(input_file)

    
    # print n-grams of words not characters
    if n_grams > 1:
        print(f"Generating {n_grams}-grams of words not characters for comparison.")
        input_words = generate_n_gram_wordlevel(n_grams, input_words)
    
        

    print(f"Number of words in input file: {len(input_words)}")
    print(f"Words in input file: {input_words}")

    
    # Find all files with the same task name in the directory
    task_files = glob.glob(os.path.join(directory, f"*_{task_name}.txt"))
    
    # exclude the input file from the task files
    task_files = [file for file in task_files if os.path.basename(file) != os.path.basename(input_file)]

    if not task_files:
        print("No task files found for the specified task name.")
        return None, 0
    print(f"Number of task files found: {len(task_files)}")
    
    
    # Compare similarity score between the input file and each task file
    similarity_scores = {}
    for task_file in task_files:
        J, Dsc = generate_set_similarity_score(input_file, task_file)
        cosine_similarity = generate_vector_similarity_score(input_file, task_file, use_tf_idf=use_tf_idf, n_grams=n_grams)
        
        similarity_scores[task_file] = (J, Dsc, cosine_similarity)

    return similarity_scores

def generate_n_gram_wordlevel(n_grams, input_words):
    n_grams_set = set()
    input_words = list(input_words)  # Convert set to list for n-gram generation
    for i in range(len(input_words) - n_grams + 1):
        n_gram = ' '.join(input_words[i:i+n_grams])
        n_grams_set.add(n_gram)
    input_words = n_grams_set
    return input_words

def generate_set_similarity_score(input_file, task_file):
    """
    Generate a similarity score between the input file and a task file.
    """
    input_words = load_words_from_file(input_file)
    task_words = load_words_from_file(task_file)
    
    common_words = input_words.intersection(task_words)
    common_count = len(common_words)
    
    if not input_words:
        return 0.0  # Avoid division by zero
    
    jaccard_similarity = common_count / (len(input_words) + len(task_words) - common_count)
    dice_coefficient = (2 * common_count) / (len(input_words) + len(task_words))
    
    return jaccard_similarity, dice_coefficient

def generate_vector_similarity_score(input_file, task_file, use_tf_idf, n_grams):
    """
    Generate a vector similarity score between the input file and a task file.
    TF-IDF only implemented for n_grams = 1
    """
    if n_grams > 1:
        input_vector, task_vector = generate_vector_representation(input_file, task_file, n_grams=n_grams)
    else:    
        if use_tf_idf:
            input_vector, task_vector = generate_tf_idf_vector(input_file, task_file)
    
    cosine_similarity = get_cosine_similarity(input_vector, task_vector)
    
    return cosine_similarity


def generate_vector_representation(input_file, task_file, n_grams):
    """
    Generate vector representations for the input file and task file.
    """
    input_words = load_text_from_file(input_file)
    task_words = load_text_from_file(task_file)
    
    # Create a set of unique words from both files
    if n_grams  == 1:
        unique_words = set(input_words) | set(task_words)
    else:
        # Generate n-grams of words not characters
        print(f"Generating {n_grams}-grams of words not characters for comparison.")
        input_n_gram_words = generate_n_gram_wordlevel(n_grams, input_words)
        task_n_gram_words = generate_n_gram_wordlevel(n_grams, task_words)
        unique_words = set(input_words) | set(task_words) | set(input_n_gram_words) | set(task_n_gram_words)
        print(f"Unique words after n-gram generation: {unique_words}")
        
    # Create vectors for both files
    input_vector = [input_words.count(word) for word in unique_words]
    task_vector = [task_words.count(word) for word in unique_words]
        
    
    return input_vector, task_vector

def generate_tf_idf_vector(input_file, task_file):
    """
    Generate TF-IDF vectors for the input file and task file.
    do not use sklearn, use a custom implementation
    """
    from collections import Counter
    import math
    
    input_words = load_text_from_file(input_file)
    task_words = load_text_from_file(task_file)
    
    # Create a set of unique words from both files
    unique_words = set(input_words) | set(task_words)
    
    # Count word frequencies
    input_word_count = Counter(input_words)
    task_word_count = Counter(task_words)
    
    # Calculate TF for each word in both files
    input_tf = {word: count / len(input_words) for word, count in input_word_count.items()}
    task_tf = {word: count / len(task_words) for word, count in task_word_count.items()}
    
    # Calculate IDF for each word across both files
    idf = {}
    total_files = 2  # We have two files: input and task
    for word in unique_words:
        containing_files = sum(1 for file in [input_word_count, task_word_count] if word in file)
        idf[word] = math.log(total_files / (1 + containing_files))  # Add 1 to avoid division by zero
    
    # Calculate TF-IDF vectors
    input_vector = [input_tf.get(word, 0) * idf[word] for word in unique_words]
    task_vector = [task_tf.get(word, 0) * idf[word] for word in unique_words]
    
    return input_vector, task_vector

def get_cosine_similarity(input_vector, task_vector):
    """
    Calculate the cosine similarity between two vectors.
    """
    if not input_vector or not task_vector:
        return 0.0  # Avoid division by zero
    
    dot_product = sum(i * t for i, t in zip(input_vector, task_vector))
    magnitude_input = sum(i ** 2 for i in input_vector) ** 0.5
    magnitude_task = sum(t ** 2 for t in task_vector) ** 0.5
    
    if magnitude_input == 0 or magnitude_task == 0:
        return 0.0  # Avoid division by zero
    
    return dot_product / (magnitude_input * magnitude_task)


if __name__ == "__main__":
    # Input file and directory containing task files
    input_file = "orig_taska.txt"  # Replace with the path to your input file
    directory = "."  # Replace with the directory containing task files

    # Find the file with the most common words
    similarity_scores = find_similarity_scores(input_file, directory,use_tf_idf=True, n_grams=3)
    
    # print the similarity scores in a readable format in descending order
    if similarity_scores:
        sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1][0], reverse=True)
        print("Similarity scores (Jaccard Index, Dice Coefficient):")
        for task_file, (jaccard_index, dice_coefficient, cosine_similarity) in sorted_scores:
            print(f"{os.path.basename(task_file)}: Jaccard Index = {jaccard_index:.4f} (Cosine Similarity = {cosine_similarity:.4f})")
    else:
        print("No similarity scores found.")    

    # save into csv in a readable format with columns "file_name", "jaccard_index"
    import csv
    # Create the output file name with task name appended
    task_name = os.path.basename(input_file).split('_')[1].split('.')[0]
    output_file = f"similarity_scores_{task_name}.csv"
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file_name", "jaccard_index", "cosine_similarity"])
        for task_file, (jaccard_index, dice_coefficient, cosine_similarity) in sorted_scores:
            writer.writerow([os.path.basename(task_file), f"{jaccard_index:.4f} ", f"{cosine_similarity:.4f}"])
    
    