import cv2
import os


class Converter:
    def __init__(self):
        self.cap = cv2.VideoCapture()

    def convert2frame(self, video_path):
        file_name = os.path.basename(
            video_path)  # folder/video.mp4 -> video.mp4
        file_name = os.path.splitext(file_name)[0]  # video.mp4 -> video
        self.cap.open(video_path)
        success, image = self.cap.read()
        count = 1
        os.mkdir("gen/" + file_name)
        os.mkdir("gen/" + file_name + "/frames/")
        os.mkdir("gen/" + file_name + "/labels/")
        print('Start write file: ', file_name)

        while success:
            cv2.imwrite(
                "gen/" + file_name + "/frames/" + file_name + "-" +
                str(count).zfill(5) + ".png", image)
            success, image = self.cap.read()
            count += 1
        print('Finish write file: ', file_name)
        self.cap.release()