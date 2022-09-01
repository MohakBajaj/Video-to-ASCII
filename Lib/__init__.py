from modules import *

class VideoToASCII:
    def __init__(self, video_file_path, ascii_zip=False, cols=150, zip_file_name_for_player=None, FPS=30):
        self.video_file_path = video_file_path
        self.ascii_zip = ascii_zip
        self.cols = cols
        self.zip_file_name_for_player = zip_file_name_for_player
        if self.zip_file_name_for_player is not None:
            self.zipped = True
        self.FPS = FPS

    def v2a(self):
        # Extracting the frames from video
        ToFrames(self.video_file_path)
        # Converting the frames to ASCII
        FramesToASCII(self.ascii_zip, self.cols).convert_frames_to_ascii()
        # Playing the ASCII frames
        Player(self.zip_file_name_for_player, self.FPS, self.zipped).play()

if __name__ == "__main__":
    VideoToASCII(r".\resources\example_video_1.mp4", ascii_zip=True, cols=175, zip_file_name_for_player="ascii_frames.asciipack", FPS=30).v2a()