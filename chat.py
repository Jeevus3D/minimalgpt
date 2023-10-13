#!/usr/bin/env python3

import openai
import configparser
import sys
import os
import time
import textwrap

# Load configuration
config = configparser.ConfigParser()
config.read('creds.ini')
api_key = config['OPENAI']['API_KEY']

# Initialize OpenAI API
openai.api_key = api_key

def query_openai(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are specifically designed to assist with coding to the best of your abilities."},
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
    
    # Format the response to wrap text at 80 characters width
    formatted_response = textwrap.fill(response, width=80)
    
    print(formatted_response)