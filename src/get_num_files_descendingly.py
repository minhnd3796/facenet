import os
import numpy as np
import sys
import math

def nCr(r, n):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

if __name__ == '__main__':
    dataset_dir = sys.argv[1]
    classes = os.listdir(dataset_dir)
    num_classes = len(classes)
    num_files = np.zeros(num_classes, dtype=np.int32)
    
    for i in range(num_classes):
        files = os.listdir(os.path.join(dataset_dir, classes[i]))
        num_files[i] = len(files)
    
    num_files_indices = np.flip(np.argsort(num_files))
    
    offset = int(sys.argv[2])
    num_selected_classes = int(sys.argv[3])
    selected_num_files = num_files[num_files_indices][offset:offset + num_selected_classes].tolist()
    print('selected_num_files:', selected_num_files)
    # print(num_files_indices[offset:offset + 20])
    unique_selected_num_files = np.unique(np.array(selected_num_files)).tolist()
    print("unique_selected_num_files:", unique_selected_num_files)
    count_dict = {}
    for unique_num_files in unique_selected_num_files:
        count_dict[unique_num_files] = selected_num_files.count(unique_num_files)
    print(count_dict)
    num_same_pairs = 0
    for key in count_dict.keys():
        num_same_pairs += count_dict[key] * nCr(2, key)
    print('num_same_pairs:', num_same_pairs)
    selected_class_indices = num_files_indices[offset:offset + num_selected_classes]
    print('selected_class_indices:', selected_class_indices)
