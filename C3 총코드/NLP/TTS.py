#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install google


# In[2]:


#!pip install google-cloud-texttospeech


# In[15]:


# -*- coding: utf-8 -*-

#!/usr/bin/env python

# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .
Example usage:
    python quickstart.py
"""
import os

credential_path=r"C:/Users/sinju/Downloads/top-chassis-371917-3d24a7b8ca3f.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=credential_path


def run_quickstart(transfer):
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()


    print("-",transfer,"-","전달받은 파라미터")
    
    #s = transfer ###
    if transfer=='포리야':
        s="무슨 구역으로 이동할까요?"
    elif transfer == '1구역':
        s = "1구역으로 이동하겠습니다."
    elif transfer == '2구역':
        s = "2구역으로 이동하겠습니다."
    elif transfer == '3구역':
        s = "3구역으로 이동하겠습니다."
    elif transfer == '4구역':
        s = "4구역으로 이동하겠습니다."
    else:
        s = "죄송하지만 알아듣지 못했어요."

    print(s)
    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=s)
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # OUTPUT = input("output.mp3")  #apple.mp3

    
    # The response's audio_content is binary.
    with open(s+".mp3", "wb") as out:
        
        # wb : binary 형태를 읽어주는 w는 이미 있는 파일 삭제하고 새로 실행

        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

    return s
    # [END tts_quickstart]
#run_quickstart("4구역")

#"""if __name__ == "__main__":
#    run_quickstart(transfer)
#"""


# In[ ]:





# In[ ]:





# In[ ]:




