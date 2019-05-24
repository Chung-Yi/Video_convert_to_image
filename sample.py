import glob
import os

from shutil import copyfile
from random import shuffle


def make_bucket(image_list, bucket_size=100):
    for i in range(0, len(image_list), bucket_size):
        yield image_list[i:i + bucket_size]


def main():
    image_files = list(glob.iglob('gen/**/*.png', recursive=True))
    shuffle(image_files)
    buckets = list(make_bucket(image_files, 100))
    for i, bucket in enumerate(buckets):
        os.mkdir("buckets/index" + str(i))
        os.mkdir("buckets/index" + str(i) + "/frames")
        os.mkdir("buckets/index" + str(i) + "/labels")
        for image_path in bucket:
            basename = os.path.basename(image_path)
            copyfile(image_path,
                     "buckets/index" + str(i) + "/frames/" + basename)


if __name__ == '__main__':
    main()