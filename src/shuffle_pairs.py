f_read = open('asian_image_pairs_test.txt')
lines = f_read.readlines()
f_read.close()

num_pairs = len(lines)
num_folds = 10
num_same_diff_pairs = num_pairs // 2
num_same_diff_pairs_per_fold = num_same_diff_pairs // num_folds
SAME_FLAG = 0
DIFF_FLAG = 1

f_write = open('asian_image_pairs_test_10_folds.txt', 'w')
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