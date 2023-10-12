#!/usr/bin/env python3

import openai
import configparser
import sys
import os
import time

# Load configuration
config = configparser.ConfigParser()
config.read('creds.ini')
api_key = config['OPENAI']['API_KEY']

# Initialize OpenAI API
openai.api_key = api_key

def query_openai(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: chat <query>")
        sys.exit(1)
    
    user_query = sys.argv[1]
    response = query_openai(user_query)
    print(response)
