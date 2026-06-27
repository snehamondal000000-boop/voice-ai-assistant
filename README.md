 🎙️ Voice AI Assistant

A powerful, seamless, Python-based AI system that enables fluid **voice-to-voice conversations**. By combining cutting-edge Speech-to-Text (STT), intelligent LLM processing, and lifelike Text-to-Speech (TTS) technologies, this assistant bridges the gap between human speech and machine intelligence.

---

 ✨ Features

*   **Real-time Speech Recognition:** High-accuracy audio transcription converts spoken words into digital text instantly.
*   **Intelligent AI Processing:** Powered by advanced AI models to understand context, intent, and deliver smart, natural responses.
*   **Natural Text-to-Speech:** Synthesizes high-quality, expressive audio responses that sound genuinely human.
*   **Local Session History:** Automatically logs conversations into a structured database (`conversation.db`) for context retention and review.

---

🛠️ System Architecture

The workflow follows a continuous, low-latency loop designed for natural conversation:

text
 🗣️ User Speech  ──>  [ Speech-to-Text ]  ──>  📝 Text Prompt
                                                      │
 🔊 Audio Output <──  [ Text-to-Speech ]  <──  🧠 AI Engine Response
