import os
import pathlib
import tqdm
import cv2

class ToFrames:
    def __init__(self, filepath=None):
        self.filepath = filepath
        try:
            self.default_output_path = pathlib.Path('./video_frames')
        except:
            os.mkdir('./video_frames')
            self.default_output_path = pathlib.Path('./video_frames')
        if self.filepath is None:
            raise ValueError('No filepath provided')
        cap = cv2.VideoCapture(self.filepath)
        self.toframes(cap)
        cap.release()
        cv2.destroyAllWindows()
        
    def toframes(self, cap):
        if self.filepath is None:
            raise ValueError('No filepath provided')
        else:
            if os.listdir(self.default_output_path):
                if len(os.listdir(self.default_output_path)) > 1:
                    self.empty_frames()
            print("\nExtracting the frames from the video\n")
            count = 0
            bar = tqdm.tqdm(total=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), ncols=100, ascii=True, unit=' frames', unit_scale=True, colour='green')
            while True:
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite(os.path.join(self.default_output_path, str(count) + '.jpg'), frame)
                    count += 1
                    bar.update(1)
                else:
                    break
            return None

    def empty_frames(self):
        print("\nDeleting the Pre-Existing frames\n")
        list_files = os.listdir(self.default_output_path)
        list_files.remove("README.md")
        for i in tqdm.tqdm(list_files, ncols=100, ascii=True, unit=' frames', unit_scale=True, colour='green'):
            os.remove(os.path.join(self.default_output_path, i))

    def __del__(self):
        print("\nAll the Video Frames are being Extracted\n")

if __name__ == "__main__":
    ToFrames(r".\resources\example_video.mp4")