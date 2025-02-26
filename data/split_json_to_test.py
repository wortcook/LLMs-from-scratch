import json
import random
import os

def split_json(file_path):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract header and data array

    source_lang = data.get('source_language', {})
    target_lang = data.get('target_language', {})
    data_array = data.get('data', [])
    
    # Shuffle the data array
    random.shuffle(data_array)
    
    # Split the data array into training and testing sets
    split_index = int(0.8 * len(data_array))
    training_data = data_array[:split_index]
    testing_data = data_array[split_index:]
    
    # Create the training and testing JSON objects
    training_json = {'source_language': source_lang, 'target_lang':target_lang, 'data': training_data}
    testing_json  = {'source_language': source_lang, 'target_lang':target_lang, 'data': testing_data}
    
    # Generate the output file names
    base_name, ext = os.path.splitext(file_path)
    training_file = f"{base_name}_training{ext}"
    testing_file = f"{base_name}_test{ext}"
    
    # Write the training JSON to a file
    with open(training_file, 'w') as file:
        json.dump(training_json, file, indent=4)
    
    # Write the testing JSON to a file
    with open(testing_file, 'w') as file:
        json.dump(testing_json, file, indent=4)

# Example usage
if __name__ == "__main__":
    split_json('./deu.json')
    split_json('./fra.json')
    split_json('./spa.json')
