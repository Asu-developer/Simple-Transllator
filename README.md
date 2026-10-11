# 🎙️ Simple Translator

### Python-Based Speech Recognition & Language Translation

A lightweight Python application that captures speech through a microphone, converts it into text, and translates the recognized speech into different languages.

Built to explore **speech recognition, audio processing, and language translation** using Python.

---

## 🚀 Features

- 🎤 **Voice Recording** — Captures audio directly from the microphone.
- 📝 **Speech-to-Text** — Converts spoken words into text using Google Speech Recognition.
- 🌍 **Multi-Language Support** — Recognizes speech in different languages.
- 🔄 **Language Translation** — Translates recognized text into a selected target language.
- 💾 **Audio Recording** — Saves recorded audio as a WAV file.
- ⚡ **Command-Line Interface** — Simple terminal-based interaction.
- 🛡️ **Error Handling** — Handles speech recognition failures, translation errors, and invalid language selections.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| SpeechRecognition | Speech-to-text processing |
| Google Speech Recognition | Speech recognition service |
| googletrans | Language translation |
| sounddevice | Microphone audio recording |
| NumPy | Audio data handling |
| SciPy | WAV file processing |

---

## 🌐 Supported Languages

The application provides the following language options:

| Language | Code |
|---|---|
| 🇬🇧 English | `en` |
| 🇪🇸 Spanish | `es` |
| 🇷🇺 Russian | `ru` |
| 🇵🇹 Portuguese | `pt` |
| 🇮🇩 Indonesian | `id` |
| 🇵🇱 Polish | `pl` |
| 🇮🇹 Italian | `it` |
| 🇹🇷 Turkish | `tr` |

Users can select both the speech recognition language and the target translation language.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Asu-developer/Simple-Transllator.git
cd Simple-Transllator
```

### 2. Install Dependencies

Make sure Python 3.10 or later is installed.

```bash
pip install sounddevice numpy scipy SpeechRecognition googletrans==4.0.0rc1
```

### 3. Run the Application

**Speech Recognition Only**

```bash
python main.py
```

Records speech in Turkish and converts it into text.

**Speech Recognition + Translation**

```bash
python translate.py
```

Allows users to select the spoken language and translate the recognized speech into another language.

> **Note:** An active internet connection and a working microphone are required.

---

## 💻 Usage Example

### Step 1 — Select the Input Language

```text
Which language will you speak?

English       en
Spanish       es
Russian       ru
Portuguese    pt
Indonesian    id
Polish        pl
Italian       it
Turkish       tr

> tr
```

### Step 2 — Record Your Voice

```text
Şimdi konuşun...

Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...

Şunu söylediniz: Merhaba dünya
```

The application records **5 seconds of audio** and processes it using Google Speech Recognition.

### Step 3 — Select the Target Language

```text
Which language should I translate into?

> en
```

### Step 4 — Translation Result

```text
🌍 İngilizce çeviri: Hello world
```

The translated text is displayed directly in the terminal.

> The example above illustrates the workflow. Actual terminal prompts are displayed in Turkish.

---

## 📂 Project Structure

```text
Simple-Transllator/
│
├── main.py          # Speech recognition
├── translate.py     # Speech recognition and translation
├── README.md        # Project documentation
└── LICENSE          # MIT License
```

### File Descriptions

**`main.py`**

A basic speech recognition implementation that:

- Records audio through the microphone.
- Saves the recording as `output.wav`.
- Converts Turkish speech into text.
- Displays the recognized text in the terminal.

**`translate.py`**

An extended implementation that:

- Allows users to select the input language.
- Records and recognizes spoken words.
- Allows users to select the target language.
- Translates recognized text using `googletrans`.
- Displays the translated result.

---

## 🔍 How It Works

```text
        🎤 Microphone
              |
              v
        Audio Recording
              |
              v
          output.wav
              |
              v
      Speech Recognition
              |
              v
        Recognized Text
              |
              v
      Language Selection
              |
              v
       Google Translate
              |
              v
       🌍 Translated Text
```

### Processing Workflow

1. The user selects the language they will speak.
2. The microphone records audio for 5 seconds.
3. The recording is saved as a WAV file.
4. Google Speech Recognition converts the audio into text.
5. The user selects a target language.
6. The translation library processes the recognized text.
7. The translated result is displayed in the terminal.

---

## 📚 What I Learned

This project helped me gain practical experience with:

- Working with microphone input in Python.
- Recording and processing digital audio.
- Understanding speech recognition workflows.
- Integrating external services and libraries.
- Implementing multilingual text translation.
- Handling exceptions and invalid user input.
- Building command-line applications.

---

## 🔮 Future Improvements

Potential improvements include:

- [ ] Graphical user interface (GUI).
- [ ] Real-time speech recognition.
- [ ] Text-to-speech for translated results.
- [ ] Automatic language detection.
- [ ] Adjustable recording duration.
- [ ] Translation history.
- [ ] Improved error handling.
- [ ] Support for additional languages.

---

## ⚠️ Limitations

- Speech recording is currently limited to 5 seconds.
- Speech recognition requires an internet connection.
- Recognition accuracy depends on microphone quality and background noise.
- Translation availability depends on the external translation service.
- The application currently runs through the terminal.

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

**Adnan Selim**

Software Developer

[![GitHub](https://img.shields.io/badge/GitHub-Asu--developer-181717?style=flat&logo=github)](https://github.com/Asu-developer)

---

⭐ If you find this project interesting, consider giving it a star!
