from openai import OpenAI

OPENAI_API_KEY = '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'
client = OpenAI(api_key=OPENAI_API_KEY)
from github import Github

# Set your keys

GITHUB_TOKEN = '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'
REPO_NAME = 'indra-deepika/clash-of-clans'
FILE_PATH = '/src/building.py'  # Path to the file in the repository


def detect_design_smells(code):
    response = client.completions.create(
    model="babbage-002",  # Use the appropriate model name here
    prompt="Detect design smells in this code:\n\n{code}",  # Your input prompt for the model
    temperature=0.5,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)   

    return response.choices[0].text.strip()

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
contents = repo.get_contents(FILE_PATH)
code = contents.decoded_content.decode()

design_smells = detect_design_smells(code)
print("Design Smells Detected:", design_smells)
