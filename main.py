import argparse
import Lib

argParser = argparse.ArgumentParser(description='Video to Ascii Video Converter/Player')
argParser.add_argument('-v video_file_path', type=str, help='Path to the video file',required=True)
argParser.add_argument('-a ascii_zip', type=bool, help='Whether to zip the ascii frames or not')
argParser.add_argument('-c cols', type=int, help='Number of columns in the ascii frames')
argParser.add_argument('-z zip_file_name_for_player', type=str, help='Name of the zip file for the player')
argParser.add_argument('-f FPS', type=int, help='FPS of the ascii video')
argParser.add_argument('-m more' , type=bool, help='If you want to input more options', required=True)
args = argParser.parse_args()

Video = args.video_file_path
ascii_zip = args.ascii_zip
cols = args.cols
zip_file_name_for_player = args.zip_file_name_for_player
FPS = args.FPS
more = args.more

if more:
    Lib.VideoToASCII(Video, ascii_zip, cols, zip_file_name_for_player, FPS).v2a()
else:
    Lib.VideoToASCII(Video).v2a()
