from github import Github, GithubException
import os
import sys
from constants import OPENAI_API_KEY , GITHUB_TOKEN , REPO_NAME , FILE_PATH
# Configuration

OUTPUT_FILE_PATH = sys.argv[1]  # The output file path from the command line argument

# Initialize GitHub client
g = Github(os.getenv('GITHUB_TOKEN'))

# # Read the refactored code from the output file
# with open(OUTPUT_FILE_PATH, 'r') as file:
#     refactored_code = file.read()
#
# print(refactored_code + " OOPSS ")

try:
    repo = g.get_repo(REPO_NAME)
    main_ref = repo.get_git_ref('heads/main')
    main_sha = main_ref.object.sha
    main_commit = repo.get_git_commit(main_sha)
    main_tree_sha = main_commit.tree.sha

    # Read the refactored code from the output file
    with open(OUTPUT_FILE_PATH, 'r') as file:
        refactored_code = file.read()

    # Create a blob with the refactored code
    blob = repo.create_git_blob(refactored_code, "utf-8")

    # Create a new tree with the modifications
    element = Github.GitTreeElement(FILE_PATH, '100644', 'blob', sha=blob.sha)
    tree = repo.create_git_tree([element], base_tree=main_tree_sha)

    # Create a new commit with the new tree
    commit_message = "Refactor code"
    new_commit = repo.create_git_commit(commit_message, tree, [main_commit])

    # Create a new branch from the new commit
    new_branch_name = "refactoring"
    repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=new_commit.sha)

    # Create a pull request
    pr_title = "Refactor code using automated tool"
    pr_body = "This pull request applies refactoring changes to improve code quality."
    pr = repo.create_pull(title=pr_title, body=pr_body, head=new_branch_name, base="main")
    print(f"Pull Request created: {pr.html_url}")

except GithubException as e:
    print(f"An error occurred   : {e}")
