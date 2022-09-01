import os
import zipfile
import pathlib
import time


class Player:
    def __init__(self, filename=None, FPS=30, zipped=False):
        self.filename=filename
        self.FPS=FPS
        self.default_input_path = pathlib.Path('./output_zipped_files')
        try:
            self.reading_directory = pathlib.Path('./ascii_frames')
        except:
            os.mkdir('./ascii_frames')
            self.reading_directory = pathlib.Path('./ascii_frames')
        if zipped:
            self.unzip_frames()
    
    def unzip_frames(self):
        if self.filename is None:
            raise ValueError('No filename provided')
        else:
            if os.listdir(self.reading_directory):
                if os.listdir(self.default_input_path)[0].endswith('.md'):
                    self.empty_frames()
            print("Extracting")
            with zipfile.ZipFile(self.default_input_path / self.filename, 'r') as zip_ref:
                zip_ref.extractall(self.reading_directory)
        
    def get_frames(self):
        ascii_frames = os.listdir(self.reading_directory)
        ascii_frames.remove("README.md")
        ascii_frames.sort(key=lambda x: int(x.split('.')[0]))
        frames_list = []
        for idx, frame in enumerate(ascii_frames):
            with open(os.path.join(self.reading_directory, frame), 'r') as f:
                frames_list.append(f.read())
        return frames_list
    
    def play(self):
        frames_list = self.get_frames()
        print('Staring to play in 2 seconds...')
        time.sleep(2)
        for frame in frames_list:
            os.system("cls")
            print(frame)
            time.sleep(1/self.FPS)
    
    def empty_frames(self):
        print("Deleting the Pre Existing frames")
        list_files = os.listdir(self.reading_directory)
        list_files.remove("README.md")
        for i in list_files:
            os.remove(os.path.join(self.reading_directory, i))
        
    def __del__(self):
        os.system("cls")
        print("Player Exited")

if __name__ == "__main__":
    Player("ascii_frames.zip", zipped=True).play()
    # Player().play()