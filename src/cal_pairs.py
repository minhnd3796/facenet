import os
import math

def nCr(n, r):
  return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def cal_same_pairs(data_dir):
  total_num_same_pairs = 0
  classes = os.listdir(data_dir)
  for class_ in classes:
    print(class_)
    class_path = os.path.join(data_dir, class_)
    num_files = len(class_path)
    num_same_pairs_per_cls = nCr(num_files, 2)
    total_num_same_pairs += num_same_pairs_per_cls
  return total_num_same_pairs

def cal_diff_pairs(data_dir):
  total_diff_pairs = 0
  total_files = 0
  classes = os.listdir(data_dir)
  for class_ in classes:
    class_path = os.path.join(data_dir, class_)
    num_files = len(class_path)
    total_files += num_files
  for class_ in classes:
    print(class_)
    class_path = os.path.join(data_dir, class_)
    num_files = len(class_path)
    num_diff_pairs_per_cls = num_files * (total_files - num_files)
    total_diff_pairs += num_diff_pairs_per_cls
  return total_diff_pairs // 2

if __name__ == '__main__':
  data_dir = '/ditmemay/raid/fti/vision.minhnd/datasets/frt/cropped_face'
  num_same = cal_same_pairs(data_dir)
  num_diff = cal_diff_pairs(data_dir)
  print("SAME:", num_same)
  print("DIFF:", num_diff)
  print("TOTAL:", num_same + num_diff)
