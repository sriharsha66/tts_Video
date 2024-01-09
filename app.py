# # # load all the functions
# # from voice_cloning.generation import *
# # from .encoder import inference as encoder


# # # provide a reference sound file, speech text and clone the voice
# # sound_path = "/home/sriharsha/vc/record.wav" # support most of the sound formats
# # speech_text = "Please use this package carefully"

# # generated_wav = speech_generator(
# #     voice_type = "western", # supports "indian" & "western"
# #     sound_path = sound_path, 
# #     speech_text=  speech_text
# #     )

# # ## Play and save the sound with noise-reduction capabilities

# # # play the generated sound
# # play_sound(generated_wav)

# # # save the file
# # save_sound(generated_wav, filename="voice output", noise_reduction=True) # enable noise reduction


# # load all the functions
# # from encoder import inference as encoder

# from voice_cloning.generation import play_library_sound, speech_generator, play_sound, save_sound

# # Play the speaker sound to get an idea of available voices
# play_library_sound(voice_type="indian", gender="male", speaker_id="speaker-1")

# # Set the desired text for voice cloning
# speech_text = "Please use this package carefully"

# # Generate a synthetic voice with your own recorded voice
# generated_wav = speech_generator(
#     voice_type="indian", 
#     gender="male", 
#     speaker_id="2",  # Replace with your actual speaker ID
#     speech_text=speech_text
# )

# # Play the generated sound
# play_sound(generated_wav)

# # Save the generated sound with noise reduction
# save_sound(generated_wav, filename="cloned_voice", noise_reduction=True)
from gtts import gTTS
tts = gTTS('hello mee harsha')
tts.save('hello.mp3')