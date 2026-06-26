import os
import sqlite3
import sounddevice as sd
from scipy.io.wavfile import write
import whisper

# =====================================
# FFmpeg Path
# =====================================
ffmpeg_path = r"C:\Users\SNEHA MONDAL\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ.get("PATH", "")

# =====================================
# Project Directory
# =====================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

question_audio_path = os.path.join(BASE_DIR, "question.wav")
answer_audio_path = os.path.join(BASE_DIR, "answer.wav")
db_path = os.path.join(BASE_DIR, "conversation.db")

# =====================================
# Audio Settings
# =====================================
fs = 44100
question_duration = 15
answer_duration = 60

# =====================================
# Record Question
# =====================================
print("\nRecording Question (15 seconds)...")

question_audio = sd.rec(
    int(question_duration * fs),
    samplerate=fs,
    channels=1
)

sd.wait()

write(question_audio_path, fs, question_audio)

print("Question recording completed!")

# =====================================
# Record Answer
# =====================================
print("\nRecording Answer (60 seconds)...")

answer_audio = sd.rec(
    int(answer_duration * fs),
    samplerate=fs,
    channels=1
)

sd.wait()

write(answer_audio_path, fs, answer_audio)

print("Answer recording completed!")

# =====================================
# Load Whisper
# =====================================
print("\nLoading Whisper Model...")

model = whisper.load_model("base")

# =====================================
# Speech To Text
# =====================================
print("\nConverting Question...")

question = model.transcribe(question_audio_path)["text"]

print("Converting Answer...")

answer = model.transcribe(answer_audio_path)["text"]

# =====================================
# Print Result
# =====================================
print("\n" + "=" * 50)
print("QUESTION")
print("-" * 50)
print(question)

print("\n" + "=" * 50)
print("ANSWER")
print("-" * 50)
print(answer)
print("=" * 50)

# =====================================
# Database
# =====================================
print("\nDatabase Path:")
print(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

cursor.execute(
    """
    INSERT INTO conversations(question, answer)
    VALUES (?, ?)
    """,
    (question, answer)
)

conn.commit()

# =====================================
# Verify Data
# =====================================
cursor.execute("SELECT * FROM conversations")

print("\nDatabase Records:\n")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

print("\nConversation Saved Successfully!")
print("Project Completed Successfully!")