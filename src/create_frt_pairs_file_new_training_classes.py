import os
import random
import numpy as np

data_dir = '/ditmemay/raid/fti/vision.minhnd/datasets/cropped_asian_frt_face_training'
classes = np.array(os.listdir(os.path.expanduser(data_dir)))
num_classes = len(classes)
num_files = np.zeros(num_classes, dtype=np.int32)
for i in range(num_classes):
    files = os.listdir(os.path.join(data_dir, classes[i]))
    num_files[i] = len(files)
num_files_indices = np.argsort(num_files)
classes = classes[num_files_indices].tolist()
print("num_classes:", num_classes)
random.seed(3796)
index_tuple_list = []
num_same_training_pairs = 0

f_training_pairs = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/frt_image_pairs_training.txt'), 'w')
f_training_indices = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/frt_index_pairs_training.txt'), 'w')
for class_index in range(num_classes):
    files = os.listdir(os.path.join(data_dir, classes[class_index]))
    num_files = len(files)
    for first_file_index in range(num_files - 1):
        for second_file_index in range(first_file_index + 1, num_files):
            pair_index_tuple = (class_index, first_file_index, class_index, second_file_index)
            f_training_pairs.write(classes[class_index] + '\t' + files[first_file_index] + '\t' + classes[class_index] + '\t' + files[second_file_index] + '\n')
            for idx in pair_index_tuple:
                f_training_indices.write(str(idx) + ' ')
            f_training_indices.write('\n')
            num_same_training_pairs += 1
            # print(num_same_training_pairs)

num_diff_training_pairs = 0
is_enough = False
for first_class_index in range(num_classes):
    if not is_enough:
        first_files = os.listdir(os.path.join(data_dir, classes[first_class_index]))
        num_first_files = len(first_files)
        for first_file_index in range(num_first_files):
            if not is_enough:
                for second_class_index in range(first_class_index + 1, num_classes):
                    if not is_enough:
                        second_files = os.listdir(os.path.join(data_dir, classes[second_class_index]))
                        num_second_files = len(second_files)
                        for second_file_index in range(num_second_files):
                            if not is_enough:
                                pair_index_tuple = (first_class_index, first_file_index, second_class_index, second_file_index)
                                f_training_pairs.write(classes[first_class_index] + '\t' + files[first_file_index] + '\t' + classes[second_class_index] + '\t' + files[second_file_index] + '\n')
                                for idx in pair_index_tuple:
                                    f_training_indices.write(str(idx) + ' ')
                                f_training_indices.write('\n')
                                num_diff_training_pairs += 1
                                # print(str(num_diff_training_pairs) + '/' + str(num_same_training_pairs))
                                if num_diff_training_pairs == num_same_training_pairs:
                                    is_enough = True

f_training_pairs.close()
f_training_indices.close()
