from datasets import load_dataset
re_dataset = load_dataset("json", data_files="/Users/tu_v10/Documents/2023/advances nlp/assign2-main/week6/distributed/assignment2_result/bactrian-vi-data.json")
print(re_dataset['train'][0])