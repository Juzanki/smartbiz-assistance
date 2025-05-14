from moviepy.editor import VideoFileClip
from gtts import gTTS
import speech_recognition as sr
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)


def extract_audio_from_video(video_path: str, output_format: str = "wav") -> str:
    """
    Extract audio from video and save it in specified format.
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video not found: {video_path}")

    try:
        logging.info(f"🎥 Extracting audio from video: {video_path}")
        clip = VideoFileClip(video_path)
        audio = clip.audio

        output_path = os.path.splitext(video_path)[0] + f".{output_format}"
        audio.write_audiofile(output_path)
        logging.info(f"✅ Audio saved to: {output_path}")
        return output_path
    except Exception as e:
        logging.error(f"❌ Error extracting audio: {e}")
        raise
    finally:
        if 'clip' in locals():
            clip.close()


def transcribe_audio(audio_path: str, lang: str = "sw") -> str:
    """
    Convert audio to text using Google Speech Recognition.
    """
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            logging.info(f"🎧 Listening to audio: {audio_path}")
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language=lang)
        logging.info(f"✅ Transcription successful: {text}")
        return text

    except sr.UnknownValueError:
        logging.warning("🤷 Could not understand audio")
        return "Could not understand audio"

    except sr.RequestError as e:
        logging.error(f"🛑 API Error: {e}")
        return "Speech recognition service unavailable"

    except Exception as e:
        logging.error(f"⚠️ Unexpected transcription error: {e}")
        return "Unexpected error during transcription"


def generate_voice_response(text: str, file_id: str = "response") -> str:
    """
    Convert text into voice using gTTS and return audio file path.
    """
    try:
        tts = gTTS(text=text, lang="sw")
        file_path = f"static/responses/{file_id}.mp3"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        tts.save(file_path)
        logging.info(f"🔊 Voice response saved at {file_path}")
        return file_path
    except Exception as e:
        logging.error(f"❌ Failed to generate voice response: {e}")
        raise
