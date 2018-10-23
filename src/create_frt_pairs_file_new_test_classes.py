import os
import random
import numpy as np

data_dir = '/ditmemay/raid/fti/liemhd/cropped_face'
test_class_indices = np.array([50431, 28035, 81210, 56942, 28917, 83819, 53915, 58086, 17646, 44884], dtype=np.int32)
second_test_class_indices = np.array([50431, 28035, 81210, 56942, 28917, 83819, 53915, 58086, 17646, 44884, 33852, 22055, 48008], dtype=np.int32)
total_classes = np.array(os.listdir(os.path.expanduser(data_dir)))
classes = total_classes[test_class_indices].tolist()
second_classes = total_classes[second_test_class_indices].tolist()
print(classes)
print(second_classes)
num_classes = len(classes)
num_second_classes = len(second_classes)
print('type(num_classes):', type(num_classes))
print('num_classes:', num_classes)
random.seed(3796)
num_folds = 10
num_test_pairs = 6000
num_same_diff_pairs_per_fold = num_test_pairs / num_folds / 2
index_tuple_list = []

f_test_pairs = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/asian_image_pairs_test.txt'), 'w')
f_test_indices = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/asian_index_pairs_test.txt'), 'w')
for class_index in range(num_classes):
    files = os.listdir(os.path.join(data_dir, classes[class_index]))
    num_files = len(files)
    for first_file_index in range(num_files):
        for second_file_index in range(num_files):
            if second_file_index == first_file_index:
                continue
            pair_index_tuple = (class_index, first_file_index, class_index, second_file_index)
            reversed_pair_index_tuple = (class_index, second_file_index, class_index, first_file_index)
            if pair_index_tuple in index_tuple_list or reversed_pair_index_tuple in index_tuple_list:
                continue
            index_tuple_list.append(pair_index_tuple)
            index_tuple_list.append(reversed_pair_index_tuple)
            f_test_pairs.write(classes[class_index] + '\t' + files[first_file_index] + '\t' + classes[class_index] + '\t' + files[second_file_index] + '\n')
            for idx in pair_index_tuple:
                f_test_indices.write(str(idx) + ' ')
            f_test_indices.write('\n')
            for idx in reversed_pair_index_tuple:
                f_test_indices.write(str(idx) + ' ')
            f_test_indices.write('\n')
for first_class_index in range(num_classes):
    for second_class_index in range(num_second_classes):
        if first_class_index == second_class_index:
            continue
        first_files = os.listdir(os.path.join(data_dir, classes[first_class_index]))
        num_first_files = len(first_files)
        second_files = os.listdir(os.path.join(data_dir, second_classes[second_class_index]))
        num_second_files = len(second_files)
        for first_file_index in range(num_first_files):
            second_file_index = random.randint(0, num_second_files - 1)
            pair_index_tuple = (first_class_index, first_file_index, second_class_index, second_file_index)
            reversed_pair_index_tuple = (second_class_index, second_file_index, first_class_index, first_file_index)
            if pair_index_tuple in index_tuple_list or reversed_pair_index_tuple in index_tuple_list:
                second_file_index = random.randint(0, num_second_files - 1)
                pair_index_tuple = (first_class_index, first_file_index, second_class_index, second_file_index)
                reversed_pair_index_tuple = (second_class_index, second_file_index, first_class_index, first_file_index)
            index_tuple_list.append(pair_index_tuple)
            index_tuple_list.append(reversed_pair_index_tuple)
            f_test_pairs.write(classes[first_class_index] + '\t' + files[first_file_index] + '\t' + second_classes[second_class_index] + '\t' + files[second_file_index] + '\n')
            for idx in pair_index_tuple:
                f_test_indices.write(str(idx) + ' ')
            f_test_indices.write('\n')
            for idx in reversed_pair_index_tuple:
                f_test_indices.write(str(idx) + ' ')
            f_test_indices.write('\n')
f_test_pairs.close()
f_test_indices.close()

f_read = open('asian_image_pairs_test.txt')
lines = f_read.readlines()
f_read.close()

num_pairs = len(lines)
num_folds = 10
num_same_diff_pairs = num_pairs // 2
num_same_diff_pairs_per_fold = num_same_diff_pairs // num_folds
SAME_FLAG = 0
DIFF_FLAG = 1

f_write = open('asian_image_pairs_test.txt', 'w')
for fold_index in range(num_folds):
    flag = SAME_FLAG
    start_same_index = flag * num_same_diff_pairs + fold_index * num_same_diff_pairs_per_fold
    end_same_index = flag * num_same_diff_pairs + fold_index * num_same_diff_pairs_per_fold + num_same_diff_pairs_per_fold
    for pair_index in range(start_same_index, end_same_index):
        f_write.write(lines[pair_index])
    flag = DIFF_FLAG
    start_diff_index = flag * num_same_diff_pairs + fold_index * num_same_diff_pairs_per_fold
    end_diff_index = flag * num_same_diff_pairs + fold_index * num_same_diff_pairs_per_fold + num_same_diff_pairs_per_fold
    for pair_index in range(start_diff_index, end_diff_index):
        f_write.write(lines[pair_index])
        print(pair_index)
f_write.close()
