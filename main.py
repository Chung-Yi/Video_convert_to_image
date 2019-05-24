import video_converter
import glob
import traceback
import time

from multiprocessing import Pool


def handle_error(e):
    traceback.print_exception(type(e), e, e.__traceback__)


def process_video_task(file_path):
    converter = video_converter.Converter()
    converter.convert2frame(file_path)


def main():
    start_time = time.time()
    with Pool() as p:
        for file_path in glob.glob('*.mp4'):
            p.apply_async(
                process_video_task,
                args=(file_path, ),
                error_callback=handle_error)

        p.close()
        p.join()
    print('all processes done! cost: %f sec' % (time.time() - start_time))


if __name__ == '__main__':
    main()