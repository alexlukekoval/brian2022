"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir


class AlsBoto:
    def __init__(self):
        self.file = str(os.getcwd()) + '/brians_response.mp3'

    # def say(self, input_text):
    #     self.make_file(input_text, play_file=True)

    def make_file(self, input_text: object):
        """ note use pygame to play the file"""
        output = self.file
        session = Session(profile_name="default")
        polly = session.client("polly")

        inputted_text = input_text

        ssml_text = f'''
        <speak>
        {inputted_text} 
        <break time="0.5s"/> 
        </speak>
        '''

        '''
        <emphasis level="strong">Kitty.</emphasis>
        <emphasis level="reduced">Kitty.</emphasis>
        <emphasis level="moderate">Kitty.</emphasis>
        </speak>
        '''

        try:
            # Request speech synthesis
            response = polly.synthesize_speech(Text=ssml_text, OutputFormat="mp3",
                                               VoiceId="Brian", TextType='ssml')
        except (BotoCoreError, ClientError) as error:
            # The service returned an error, exit gracefully
            print(error)
            sys.exit(-1)

        # Access the audio stream from the response
        if "AudioStream" in response:
            # Note: Closing the stream is important because the service throttles on the
            # number of parallel connections. Here we are using contextlib.closing to
            # ensure the close method of the stream object will be called automatically
            # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), "speech.mp3")
                output = self.file
                print(output)
                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

        else:
            # The response didn't contain audio data, exit gracefully
            print("Could not stream audio")
            sys.exit(-1)


