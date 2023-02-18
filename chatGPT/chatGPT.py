import openai
import os
import sys
import argparse
from pathlib import Path
import datetime
import readline


def cli():
    # Set a name for our logfile
    log_name = "chatGPT.log"
    # Detect users home, this is where we will place the chatGPT log of questions and answers
    user_home = Path.home()
    log_file = Path(user_home/log_name)
    log_state = log_file.is_file()
    if log_state:
        pass 
    else:
        with open(f"{user_home}/{log_name}", 'x') as f:
            f.write('ChatGPT Log')
        f.close()

    
    # Define our Logger
    class Logger(object):
        def __init__(self):
            self.terminal = sys.stdout
            self.log = open(f"{user_home}/{log_name}", "a")
       
        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)  
    
        def flush(self):
            pass    
    # Accept question from cmdline
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-q', 
            '--question', 
            help='Provide a question for ChatGPT, ensure your question is quoted'
    )
    args = parser.parse_args()
    question = args.question
    
    # allow for users to also be prompted for their question, if not provided on the cmdline
    if question:
        prompt = question
    else:
        prompt = input("Ask your question: ")
    
    # Set up the OpenAI API client, export your api key in your shell
    # `export OPENAI_API_KEY='XXXXXXXXXXXXXXX'`
    openai.api_key = os.environ['OPENAI_API_KEY']
    
    # Set up the model and prompt
    model_engine = "text-davinci-003"
    
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=3072,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    response = completion.choices[0].text
    # Send our stdout to our logger
    sys.stdout = Logger()
    
    nl = os.linesep
    # Print the date and time
    now = datetime.datetime.now()
    print(f"{nl}{now.strftime('%Y-%m-%d %H:%M:%S')}")
    # Print our question
    print(f"Question: {prompt}{nl}")
    # Print chatGPT response
    print(f"Response: {response}")
    # Add a visual seperator
    sp = "-" * 17
    print(f"{nl} {sp}")

