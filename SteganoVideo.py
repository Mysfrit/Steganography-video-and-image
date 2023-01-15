import random
import ffmpeg
import moviepy.editor as mp
from os import listdir
from os.path import isfile, join
import os
import SteganoImage as bs


def audioFromVideo(videoPath):
    myclip = mp.VideoFileClip(videoPath)
    myclip.audio.write_audiofile("audio.mp3")


def videoToFrames(videoPath):
    #video to frames
    (
        ffmpeg
        .input(videoPath)
        .filter('fps', fps=25)
        .output(os.path.join(os.getcwd(), 'frame%d.png'),
                start_number=0)
        .overwrite_output()
        .run(quiet=True)
    )
    audioFromVideo(videoPath)


def framesToVideo(outputPath):
    # frame to video
    audioPath = os.path.join(os.getcwd(), "audio.mp3")
    audio = ffmpeg.input(audioPath)
    (
        ffmpeg
            .input(os.path.join(os.getcwd(), 'frame%d.png'), framerate=25, )
            .output(audio, outputPath, vcodec='png')
            .overwrite_output()
            .run(quiet=True)
    )


def encodedVideoToFrames(outputPath):
    # encoded video to frames
    (
        ffmpeg
            .input(outputPath)
            .filter('fps', fps=25)
            .output(os.path.join(os.getcwd(), 'frame%d.png'),
                    start_number=0)
            .overwrite_output()
            .run(quiet=False)
    )


def deleteFrames(pathToFrames):
    onlyfiles = [f for f in listdir(pathToFrames) if isfile(join(pathToFrames, f))]
    for i in onlyfiles:
        if i.__contains__("frame"):
            os.remove(i)



def numOfFrames(pathToFrames):
    count = 0
    onlyfiles = [f for f in listdir(pathToFrames) if isfile(join(pathToFrames, f))]
    for i in onlyfiles:
        if i.__contains__("frame"):
            count += 1
    return count


def videoEncode(inputPath, outputPath, message, pwd):
    print(type(inputPath))
    videoToFrames(inputPath)

    count = numOfFrames(os.getcwd())

    if count < len(message):
        raise OverflowError
    random.seed(pwd)

    bs.encode(os.path.join(os.getcwd(), f"frame0.png"), os.path.join(os.getcwd(), f"frame0.png"), str(len(message)), pwd)

    for i in range(1, len(message)+1):
        char = message[i-1]
        passChar = pwd[i % len(pwd)]
        bs.encode(os.path.join(os.getcwd(), f"frame{i}.png"), os.path.join(os.getcwd(), f"frame{i}.png"), char,
                  passChar)

    framesToVideo(outputPath)
    deleteFrames(os.getcwd())
    os.remove(os.path.join(os.getcwd(), "audio.mp3"))


def videoDecode(inputPath, pwd):
    encodedVideoToFrames(inputPath)
    # decode
    data = ""
    lengthOfMessage = bs.decodeFromImage(os.path.join(os.getcwd(), f"frame0.png"), pwd)
    for i in range(1, int(lengthOfMessage)+1):
        passChar = pwd[i % len(pwd)]
        data += bs.decodeFromImage(os.path.join(os.getcwd(), f"frame{i}.png"), passChar)

    deleteFrames(os.getcwd())
    return data
