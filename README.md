# Small ChatGPT CLI Application for Raspberry Pi

A lightweight command-line interface to interact with OpenAI's GPT models, optimized for Raspberry Pi Zero and similar hardware.

## Installation
### 1. Prerequisites

Ensure you have Python and Pip installed. If not, run:

  `sudo apt-get update`
  `sudo apt-get upgrade`
  `sudo apt-get install python3 python3-pip`

### 2. Clone the Repository

Clone this repository to your Raspberry Pi:

  `git clone https://github.com/your-github-username/chatgpt-app.git`
  `cd chatgpt-app`

Replace your-github-username with your actual GitHub username.

### 3. Install Dependencies

Install the required Python libraries:

  `pip3 install openai configparser`

### 4 . Make the Script Executable

  `chmod +x chat`

### 5. Global Access

To make the script accessible from anywhere in the CLI, move it to a directory in your PATH:

  `sudo mv chat /usr/local/bin/`

## Usage:

From anywhere in the CLI, run:

  `chat "Your query here"`

For example:

  `chat "What is the capital of France?"`

Optional: Create an Alias

If you named your script something other than chat, but you want to use the chat command, add an alias:

  `echo "alias chat='/path/to/your/script'" >> ~/.bashrc`
  `source ~/.bashrc`

Replace /path/to/your/script with the actual path to your script.
