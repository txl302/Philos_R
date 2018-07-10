import speech_recognition as sr
from gtts import gTTS
import os

import itertools
import numpy
import time
import serial

def hello():
    tts = gTTS(text='Welcome! and thank you for participating in TAG-Games SIG Blocks.', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def intro():
    tts = gTTS(text='This is a study to test cognitive abilities using tangible games. This project is loosely based on a similar IQ test, but replaces the need for a person to read and record the data in real time.', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def consent():
    tts = gTTS(text='Here is the consent form. You may read it over, but I give a quick summary to get you started. The purpose of this form is to provide you with information that may affect your decision as to whether or not you will participate in this research study. If you decide to participate, this form will also be use to record your consent. If you agree to participate in this study, you will take three types of tests using SIG-Blocks. You may also indicate if you would like to be video recorded. The risks associated in this study are minimal, and are not greater than the risks encountered in everyday life. If you feel uncomfortable at any point, you can choose not to participate or withdraw from the test. Feel free to take your time reading this form.', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def get_ready():
    tts = gTTS(text='Now get ready for the SIG Blocks testing segment. SIG Blocks are blocks that have sensors attached to them. You will use the block to enter your answers for all games. The *top face* will represent the answer you will enter. When taking the tests, please make sure your answer is correct before asking for the next testing item. Make sure that the block is touching all surfaces or is touching other blocks to ensure accuracy. Be careful not to drop, throw, or slam the blocks as these can damage the sensors. Please do not cover the sensors located in the middle of each face while you play. If you ever have trouble answering a test item, please try to answer it to the best of your ability. Make sure each item is complete before moving on to the next one.', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def are_you_ready():
    tts = gTTS(text='Are you ready?', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def shape_matching():
    tts = gTTS(text='the Shape Matching game. You will use 1 block for this test. For this game, place the block on the wood platform, touching the back of the block to back of the wood L. Before each test item, you will hear an audible beep. As the images appear on the screen, please think of the pattern that best fills the blank. Place the block on the board so that it represents the missing piece. The orientation of the block does matter. Once you complete one test, please tell your tester that you are ready for the next item. She or he will take your block and randomize it before the next test. If you have any questions or issues, please let your tester know. Lets begin!', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def memory():
    tts = gTTS(text='the Memory sequence game. You will use one block for each portion of this test. For this game, place the block on the wood platform, touching the back of the block to the wood wall. Before each test item, you will hear an audible beep. A sequence of images will appear. As images appear on the screen, try to memorize the sequence they display. After the second beep, you may use the block to enter your answer. Please do not enter your answer before the second beep.** After this beep, make sure your answer is correct before placing the block on the board. You will do two types of sequence tests - one with the color block, and one with the shape block. Please let your tester know if you are color blind, or have any further questions. Again, make sure you do not enter an answer before the second beep as you must memorize all the colors and/or images that appear.The first portion you will do is the Color Block Sequence Game', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def assembly():
    tts = gTTS(text='the Assembly Game. For this game, you will use 4 blocks for the first section and 9 for the second. When an image appears on the screen, try to match pattern using the 4 or 9 SIG Blocks on the table. When assembling, please push the blocks into the corner or together to assure that all blocks are touching. Say next when you believe your answer is completely correct and are ready for the next item. Before the next item, your tester will take your block and randomize it before the next test. Please let your tester know if you have any questions.', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def thank():
    tts = gTTS(text='Thank you for participating in TAG-Games SIG Blocks! Do not disclose testing results and procedures outside of the testing room. Please let your tester or your organization know if you have any further questions or concerns. Have a nice day and thanks again for participating! And here is your gift card! We will have a focus group next year, so we may call you back if you would like to let us know what you liked, didnt like, and what we could improve for future testing.', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def welcome():
    tts = gTTS(text='Hi, my name is Pheelos, the socially assisting robot created by Distributing Intelligent lab under the direction of Doctor Lee. nice to meet you, and may I have your name?', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

def hug():
    tts = gTTS(text='Can you give me a hug?', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")


if __name__ == '__main__':
    hello()