import os
import zipfile
import pathlib
import tqdm
import PIL
import ascii_magic

class FramesToASCII:
    def __init__(self, zipping=False, cols=150):
        self.cols = cols
        self.zipping = zipping
        self.reading_dir = pathlib.Path("./video_frames")
        self.writing_dir = pathlib.Path("./ascii_frames")
        self.zip_file_output = pathlib.Path("./output_zipped_files") / "ascii_frames.asciipack"
        if not self.writing_dir.exists():
            self.writing_dir.mkdir()
        if self.zipping:
            if not self.zip_file_output.parent.exists():
                self.zip_file_output.parent.mkdir()
        if os.listdir(self.reading_dir):
            if len(os.listdir(self.reading_dir)) > 1:
                self.empty_frames()
        
    def empty_frames(self):
        print("\nDeleting the Pre-Existing frames\n")
        list_files = os.listdir(self.writing_dir)
        list_files.remove("README.md")
        for i in tqdm.tqdm(list_files, ncols=100, ascii=True, unit=' frames', unit_scale=True, colour='green'):
            os.remove(os.path.join(self.writing_dir, i))

    def zip_files(self):
        print("\nZipping the ASCII Frames\n")
        with zipfile.ZipFile(self.zip_file_output, "w") as zip_file:
            for file in tqdm.tqdm(self.writing_dir.iterdir(), ncols=100, ascii=True, unit=' frames', unit_scale=True, colour='green'):
                zip_file.write(file, arcname=file.name)
        
    def convert_frames_to_ascii(self):
        print("\nConverting the Frames to ASCII\n")
        frame_list = os.listdir(self.reading_dir)
        frame_list.remove("README.md")
        frame_list = list(map(lambda x: os.path.join(self.reading_dir, x), frame_list))
        count = 0
        for i in tqdm.tqdm(frame_list, ncols=100, ascii=True, unit=' frames', unit_scale=True, colour='green'):
            image = PIL.Image.open(i)
            ascii_image = ascii_magic.from_image(image, columns=self.cols)
            with open(os.path.join(self.writing_dir, f"{count}.txt"), "w") as file:
                file.write(ascii_image)
            count += 1
        if self.zipping:
            self.zip_files()

if __name__ == "__main__":
    FramesToASCII(zipping=True, cols=175).convert_frames_to_ascii()