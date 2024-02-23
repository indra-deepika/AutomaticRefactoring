from github import Github, GithubException
import os
import sys
from constants import OPENAI_API_KEY , GITHUB_TOKEN , REPO_NAME , FILE_PATH
# Configuration

OUTPUT_FILE_PATH = sys.argv[1]  # The output file path from the command line argument

# Initialize GitHub client
g = Github(os.getenv('GITHUB_TOKEN'))

def create_pull_request(repo_name, file_path, output_file_path):
    try:
        # Load the repository
        repo = g.get_repo(repo_name)

        # Read the refactored code from the output file
        with open(output_file_path, 'r') as file:
            refactored_code = file.read()

        # Create a new branch from the default branch
        default_branch = repo.get_branch(repo.default_branch)
        print(default_branch)
        new_branch_name = "refactoring-branch"
        ref = f"refs/heads/{new_branch_name}"
        repo.create_git_ref(ref, default_branch.commit.sha)

        # Commit the changes to the new branch
        commit_message = "Apply refactoring"
        contents = repo.get_contents(file_path, ref=repo.default_branch)
        repo.update_file(contents.path, commit_message, refactored_code, contents.sha, branch=new_branch_name)

#         # Create a pull request
#         pr_title = "Refactor code using automated tool"
#         pr_body = "This pull request applies refactoring changes to improve code quality."
#         pr = repo.create_pull(title=pr_title, body=pr_body, head=new_branch_name, base=repo.default_branch)
#         print(f"Pull Request created: {pr.html_url}")

    except GithubException as e:
        print(f"An error occurred: {e.status}")
        print(e.data)
        print(e.headers)

# Run the function with the provided arguments
create_pull_request(REPO_NAME, FILE_PATH, OUTPUT_FILE_PATH)
