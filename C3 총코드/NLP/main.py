#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# coding: utf-8

import speech as stt
#from store import STT
import os
import pygame
import time

credential_path=r"/home/piai/STT/stt-first-371011-b05925abc00c.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=credential_path

text=stt.STT_main()
cmd_list1=["포리야","코리야","우리야","우리아","코리아","프리야","보리아","콜이야","솔이야","소리야","토리야","보리야","소리 야","불이야","포리아","꼴이야","오리야"]

if text in cmd_list1:
    command1="포리야"

audio1=command1+".mp3"
pygame.mixer.init()
pygame.mixer.music.load(audio1)
pygame.mixer.music.play()

time.sleep(2)
text=stt.STT_main()
cmd_list2=["일구역","1구역","일 구역","1 구역으로가 줘","일 구역으로가 줘","일구 역으로가 줘","1구역 가 줘","1구 역으로가 줘","1구역으로가 줘","1구역으로 가줘","1구역으로 가줄래","일 구역으로 가줘","1구역으로 가자","일부 약으로가 줘","1부 역으로가 줘","일 구역으로가 줘"]
cmd_list3=["이구역","이 구역","2구역","2구역 가 줘","2구 역으로가 줘","이고 역으로가 줘","이거 역으로가 줘","2구역으로가 줘","2구역으로가 줘","2구역으로 가줘","2구역으로 가줄래","이 구역으로 가줘","2구역으로 가자"]
cmd_list4=["삼구역","3구역","삼 구역","3 구역","3구역 가 줘","3구 역으로가 줘","삼구 역으로 가자","3 구역으로 가자","3부 역으로 가자","3구역으로가 줘","3구역으로 가줘","3구역으로 가줄래","삼 구역으로 가줘","3구역으로 가자"]
cmd_list5=["사구역","4구역","사 구역","4 구역","4구역으로 가져","4구역으로가 줘","4 구역으로 가죠","4구역으로 가자",'사고 역으로가 줘',"4구 역으로가 줘","4구역으로가 줘","4구역으로 가줘","4구역으로 가줄래","사 구역으로 가줘","4구역으로 가자"]

if text in cmd_list2:
    command2="1구역"
elif text in cmd_list3:
    command2="2구역"
elif text in cmd_list4:
    command2="3구역"
elif text in cmd_list5:
    command2="4구역"

audio2=command2+".mp3"
pygame.mixer.init()
pygame.mixer.music.load(audio2)
pygame.mixer.music.play()

