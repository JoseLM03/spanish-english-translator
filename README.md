# AI Translation CLI

A command-line translation application built with Python and Ollama that uses the Qwen 3.5 9B language model to translate text from any language into natural, modern U.S. English.

## Features

* Translate text from any language into natural U.S. English
* Preserve the original meaning and tone
* Handle common spelling mistakes and missing accents
* Stream translations in real time as the model generates them
* Run locally using Ollama
* Secure configuration through environment variables
* Basic connection and timeout error handling

## Tech Stack

* Python
* Ollama
* Qwen 3.5 9B
* HTTPX
* python-dotenv

## How It Works

The application follows a simple request and response architecture:

```text
User Input
    ↓
Python CLI
    ↓
Ollama Client
    ↓
Qwen 3.5 9B
    ↓
Translation Stream
    ↓
Terminal Output
```

The user enters text into the command line. Python sends the text and translation instructions to the locally running Qwen model through Ollama. The model generates the translation, which is streamed back to the terminal.

## Requirements

* Python 3.10+
* Ollama
* Qwen 3.5 9B model
* A virtual environment is recommended

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/JoseLM03/spanish-english-translator
cd spanish-english-translator
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install ollama httpx python-dotenv
```

### 4. Install the Qwen model

Make sure Ollama is installed and running, then pull the model:

```bash
ollama pull qwen3.5:9b
```

### 5. Configure the Ollama host

Create a `.env` file in the project root:

```env
OLLAMA_HOST=http://your-ollama-host:11434
```

Replace `your-ollama-host` with the address where your Ollama server is running.

### 6. Run the application

```bash
python translator.py
```

## Usage

Enter text when prompted:

```text
Enter text: Hola, ¿cómo estás?
Hi, how are you?
```

The application supports multiple languages:

```text
Enter text: Bonjour, comment allez-vous aujourd'hui ?
Hello, how are you doing today?
```

It can also handle casual language:

```text
Enter text: bro que haces
Dude, what are you up to?
```

Type `exit` to close the application.

## Configuration

The application reads the Ollama server address from the `.env` file using `python-dotenv`.

The `.env` file is excluded from version control to prevent environment-specific configuration from being committed to the repository.

## Error Handling

The application handles Ollama connection and read timeouts and displays an error message when the model server cannot be reached within the configured timeout period.

## Current Limitations

* The application currently runs through a command-line interface.
* Translation quality depends on the selected language model.
* Highly ambiguous, heavily misspelled, or mixed-language input may produce unexpected interpretations.
* The application currently translates into English only.
* Ollama must be running and accessible for translations to work.

## Future Improvements

Potential future improvements include:

* Web-based interface
* Speech-to-text translation
* Text-to-speech output
* Real-time voice translation
* Automatic language detection
* Support for additional target languages
* Improved translation context handling
* Cloud deployment

## Project Purpose

This project was built as a hands-on introduction to developing applications that integrate large language models. It focuses on understanding the fundamentals of LLM application development, including model communication, prompt design, streaming responses, environment configuration, and basic error handling.

## License

This project is for educational and portfolio purposes.
