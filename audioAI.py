import os
import pyrec  # 录音函数文件
import wav2pcm  # wav转换pcm 函数文件
import FAQ  # 交互词库函数文件
import pygame
import time
from aip import AipSpeech

# 进入消息循环


# 这里的三个参数,对应在百度语音创建的应用中的三个参数
APP_ID = "15511053"
API_KEY = "iEhU73Iq3ZYfcq03yFPI7hSB"
SECRET_KEY = "e3lGowGRHYtmsM8l9UlCIKeo6HieKzoZ"
# 图灵需要的参数
TULING_KEY = 'bd2c8a71bf9f4e05baa4d8fdb103db47'

def main():
    while True:
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        pyrec.rec("1.wav")  # 录音并生成wav文件,使用方式传入文件名
        pcm_file = wav2pcm.wav_to_pcm("1.wav")  # 将wav文件 转换成pcm文件 返回 pcm的文件名
        # 读取文件 , 得到了PCM文件
        with open(pcm_file, 'rb') as fp:
            file_context = fp.read()
        # 识别本地文件
        res = client.asr(file_context, 'pcm', 16000, {
            'dev_pid': 1536,
        })
        # 从字典里面获取"result"的value 列表中第1个元素,就是识别出来的字符串
        res_str = res.get("result")[0]
        print(res_str)
        #识别出来的内容交给图灵机器人来回答
        Q_str = FAQ.answer(res_str,TULING_KEY)
        # 将转换出来的字符串进行语音合成
        synth_file = "synth.mp3"
        synth_context = client.synthesis(Q_str, "zh", 1, {
            "vol": 6,
            "spd": 2,
            "pit": 3,
            "per": 0
        })
        with open(synth_file, "wb") as f:
            f.write(synth_context)
        # 播放合成语音
        pygame.mixer.init()
        pygame.mixer.music.load(synth_file)
        pygame.mixer.music.play()
        count = 0
        while (count < 9):
           csx = pygame.mixer.music.get_busy()
           if csx == 1:
               time.sleep(5)
               count = count + 1
           else:
               count = 10
        pygame.mixer.music.stop()
        #os.system("/usr/local/Cellar/ffmpeg/4.1_3/bin/ffplay  %s"%(synth_file))
        
if __name__ == '__main__':
    main()