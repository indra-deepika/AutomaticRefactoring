import openai
from github import Github

# Set your OpenAI API key directly
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

# Set your GitHub token and repo details
GITHUB_TOKEN = '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'
REPO_NAME = 'indra-deepika/SE_Bonus_Test_Repo'
FILE_PATH = '/books-web/src/main/java/com/sismics/books/rest/resource/UserResource.java'

def detect_design_smells(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I am a highly intelligent question answering bot."},
            {"role": "user", "content": f"Detect design smells in this code:\n\n{code}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
contents = repo.get_contents(FILE_PATH)
code = contents.decoded_content.decode()

design_smells = detect_design_smells(code)
print("Design Smells Detected:", design_smells)
