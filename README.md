# aibeecara-test

# Pipeline Flow

# 1. User's prompt is passed to the Gemini AI

# 2. The LLM's response is fed into Deepgram TTS

# 3. The output of Deepgram TTS is saved in the test.mp3

# Difficulties
This is my first time applying a TTS model, and I was confused when the ouput in postman shows null. 
Although this can be resolved by better API design, due to time constraints, I did not have the time to do this. 

However, after few fixes, result was gained, and I succeeded. You can take a look at the output in the test.mp3 file.

# Fixes
1. I figured that the mistake I made is I forgot to put the test.mp3 for the TTS to write into. 
2. I made a new Gemini API Key instead of using my old one. 