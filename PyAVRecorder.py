#Python 3.7.7 is using
#System: Win 10
from threading import Thread
import cv2, numpy, os, sys
import pyaudio, wave, time
import moviepy.editor as mpe

sec = 5     #Video lengh in seconds

def videoRecorder():
    web_cam = cv2.VideoCapture(0)
    fourcc_codec = cv2.VideoWriter_fourcc(*'DIVX')
    resolution = (640, 480)
    fps = 15
    out = cv2.VideoWriter('PyWebVideo.avi', fourcc_codec, fps, resolution)

    while(web_cam.isOpened()):
        ret, frame = web_cam.read()
        cv2.imshow('PyWebCam', frame)
        out.write(frame)
        if cv2.waitKey(1) == 27 or ret == False:
            break

    web_cam.release()
    out.release()
    cv2.destroyAllWindows()


def audioRecorder():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = sec
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK)
    
    print("sound recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
            
    stream.stop_stream()
    stream.close()
    p.terminate()
        
    print("sound recording is finished!")

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def avRecorder():
        th_1, th_2 = Thread(target = audioRecorder), Thread(target = videoRecorder)
        th_1.start(), th_2.start()
        th_1.join(), th_2.join()
        video_file = mpe.VideoFileClip(str(os.getcwd()) + '\PyWebVideo.avi')
        video_file.write_videofile(str(os.getcwd()) + '\ResultVideo.avi', audio = str(os.getcwd()) + '\output.wav', codec = 'libvpx')


def main():
    #videoRecorder()
    #audioRecorder()
    avRecorder()
    
if __name__ == '__main__':
    main()

