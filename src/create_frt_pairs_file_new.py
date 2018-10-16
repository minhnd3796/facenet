import os
import random

data_dir = '/ditmemay/raid/fti/vision.minhnd/datasets/frt/cropped_face'
classes = os.listdir(os.path.expanduser(data_dir))
num_classes = len(classes)
random.seed(3796)
num_folds = 10
num_test_pairs = 6000
num_same_diff_pairs_per_fold = num_test_pairs / num_folds / 2
index_tuple_list = []

f_test_pairs = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/frt_image_pairs_test.txt'), 'w')
f_test_indices = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/frt_index_pairs_test.txt'), 'w')
for fold_index in range(num_folds):
    for i in range(int(num_same_diff_pairs_per_fold)):
        class_index = random.randint(0, num_classes - 1)
        files = os.listdir(os.path.join(data_dir, classes[class_index]))
        num_files = len(files)
        first_file_index = random.randint(0, num_files - 1)
        second_file_index = random.randint(0, num_files - 1)
        while second_file_index == first_file_index:
            second_file_index = random.randint(0, num_files - 1)
        pair_index_tuple = (class_index, first_file_index, class_index, second_file_index)
        while pair_index_tuple in index_tuple_list:
            class_index = random.randint(0, num_classes - 1)
            files = os.listdir(os.path.join(data_dir, classes[class_index]))
            num_files = len(files)
            first_file_index = random.randint(0, num_files - 1)
            second_file_index = random.randint(0, num_files - 1)
            while second_file_index == first_file_index:
                second_file_index = random.randint(0, num_files - 1)
            pair_index_tuple = (class_index, first_file_index, class_index, second_file_index)
        index_tuple_list.append(pair_index_tuple)
        f_test_pairs.write(classes[class_index] + '\t' + files[first_file_index] + '\t' + classes[class_index] + '\t' + files[second_file_index] + '\n')
        for idx in pair_index_tuple:
            f_test_indices.write(str(idx) + ' ')
        f_test_indices.write('\n')
    for i in range(int(num_same_diff_pairs_per_fold)):
        first_class_index = random.randint(0, num_classes - 1)
        second_class_index = random.randint(0, num_classes - 1)
        while second_class_index == first_class_index:
            second_class_index = random.randint(0, num_classes - 1)
        first_files = os.listdir(os.path.join(data_dir, classes[first_class_index]))
        num_first_files = len(first_files)
        first_file_index = random.randint(0, num_first_files - 1)
        second_files = os.listdir(os.path.join(data_dir, classes[second_class_index]))
        num_second_files = len(second_files)
        second_file_index = random.randint(0, num_second_files - 1)
        pair_index_tuple = (first_class_index, first_file_index, class_index, second_file_index)
        while pair_index_tuple in index_tuple_list:
            first_class_index = random.randint(0, num_classes - 1)
            second_class_index = random.randint(0, num_classes - 1)
            while second_class_index == first_class_index:
                second_class_index = random.randint(0, num_classes - 1)
            first_files = os.listdir(os.path.join(data_dir, classes[first_class_index]))
            num_first_files = len(first_files)
            first_file_index = random.randint(0, num_first_files - 1)
            second_files = os.listdir(os.path.join(data_dir, classes[second_class_index]))
            num_second_files = len(second_files)
            second_file_index = random.randint(0, num_second_files - 1)
            pair_index_tuple = (first_class_index, first_file_index, class_index, second_file_index)
        index_tuple_list.append(pair_index_tuple)
        f_test_pairs.write(classes[first_class_index] + '\t' + first_files[first_file_index] + '\t' + classes[second_class_index] + '\t' + second_files[second_file_index] + '\n')
        for idx in pair_index_tuple:
            f_test_indices.write(str(idx) + ' ')
        f_test_indices.write('\n')
f_test_pairs.close()
f_test_indices.close()

num_same_diff_training_pairs = 0

f_training_pairs = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/frt_image_pairs_training.txt'), 'w')
f_training_indices = open(os.path.expanduser('/ditmemay/raid/fti/vision.minhnd/sources/facenet/data/frt_index_pairs_training.txt'), 'w')
for class_index in range(len(classes)):
    files = os.listdir(os.path.join(data_dir, classes[class_index]))
    num_files = len(files)
    for first_file_index in range(num_files):
        for second_file_index in range(num_files):
            if second_file_index == first_file_index:
                continue
            pair_index_tuple = (class_index, first_file_index, class_index, second_file_index)
            if pair_index_tuple in index_tuple_list:
                continue
            f_training_pairs.write(classes[class_index] + '\t' + files[first_file_index] + '\t' + classes[class_index] + '\t' + files[second_file_index] + '\n')
            for idx in pair_index_tuple:
                f_training_indices.write(str(idx) + ' ')
            f_training_indices.write('\n')
            num_same_diff_training_pairs += 1
for training_diff_pair_index in range(num_same_diff_training_pairs): # 139320
    first_class_index = random.randint(0, num_classes - 1)
    second_class_index = random.randint(0, num_classes - 1)
    while second_class_index == first_class_index:
        second_class_index = random.randint(0, num_classes - 1)
    first_files = os.listdir(os.path.join(data_dir, classes[first_class_index]))
    num_first_files = len(first_files)
    first_file_index = random.randint(0, num_first_files - 1)
    second_files = os.listdir(os.path.join(data_dir, classes[second_class_index]))
    num_second_files = len(second_files)
    second_file_index = random.randint(0, num_second_files - 1)
    pair_index_tuple = (first_class_index, first_file_index, class_index, second_file_index)
    while pair_index_tuple in index_tuple_list:
        first_class_index = random.randint(0, num_classes - 1)
        second_class_index = random.randint(0, num_classes - 1)
        while second_class_index == first_class_index:
            second_class_index = random.randint(0, num_classes - 1)
        first_files = os.listdir(os.path.join(data_dir, classes[first_class_index]))
        num_first_files = len(first_files)
        first_file_index = random.randint(0, num_first_files - 1)
        second_files = os.listdir(os.path.join(data_dir, classes[second_class_index]))
        num_second_files = len(second_files)
        second_file_index = random.randint(0, num_second_files - 1)
        pair_index_tuple = (first_class_index, first_file_index, class_index, second_file_index)
    index_tuple_list.append(pair_index_tuple)
    f_training_pairs.write(classes[first_class_index] + '\t' + first_files[first_file_index] + '\t' + classes[second_class_index] + '\t' + second_files[second_file_index] + '\n')
    for idx in pair_index_tuple:
        f_training_indices.write(str(idx) + ' ')
    f_training_indices.write('\n')

f_training_pairs.close()
f_training_indices.close()
