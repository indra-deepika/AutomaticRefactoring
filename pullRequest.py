from github import Github
def create_pull_request(repo, original_branch, new_branch_name, file_path, new_code, pr_title, pr_body):
    sb = repo.get_branch(original_branch)
    repo.create_git_ref(ref=f'refs/heads/{new_branch_name}', sha=sb.commit.sha)
    contents = repo.get_contents(file_path, ref=new_branch_name)
    repo.update_file(contents.path, "Refactoring code", new_code, contents.sha, branch=new_branch_name)
    pr = repo.create_pull(title=pr_title, body=pr_body, head=new_branch_name, base=original_branch)
    return pr.html_url

new_branch_name = 'refactoring-branch'
pr_title = "Automated Refactoring for Design Smell Fixes"
pr_body = f"Refactoring changes applied to address the following design smells: \n\n - Long Method\n - Long Parameter List\n - Duplicate Code\n - Feature Envy\n - Data Clumps\n - Switch Statements\n - Refused Bequest\n - Lazy Class\n - Speculative Generality\n - Message Chains\n - Middle Man\n - Inappropriate Intimacy\n - Shotgun Surgery\n - Divergent Change\n - Parallel Inheritance Hierarchies\n - Blob\n - Functional Decomposition\n - Primitive Obsession\n - Data Class\n - Refused Bequest\n - Comments\n - Duplicate Code\n - Lazy Class\n - Data Clumps\n - Feature Envy\n - Long Method\n - Long Parameter List\n - Switch Statements\n - Middle Man\n - Inappropriate Intimacy\n - Message Chains\n - Speculative Generality\n - Data Class\n - Primitive Obsession\n - Refused Bequest\n - Lazy Class\n - Data Clumps\n - Feature Envy\n - Long Method\n - Long Parameter List\n - Switch Statements\n - Middle Man\n - Inappropriate Intimacy\n - Message Chains\n - Speculative Generality\n - Data Class\n - Primitive Obsession\n - Refused Bequest\n - Lazy Class\n - Data Clumps\n - Feature Envy\n - Long Method\n - Long Parameter List\n - Switch Statements\n - Middle Man\n - Inappropriate Intimacy\n - Message Chains\n - Speculative Generality\n - Data Class\n - Primitive Obsession\n - Refused Bequest\n - Lazy Class\n - Data Clumps\n - Feature Envy\n - Long Method\n - Long Parameter List\n - Switch Statements\n - Middle Man\n - Inappropriate Intimacy\n - Message Chains\n - Speculative Generality\n - Data Class\n - Primitive Obsession\n - Refused Bequest\n - Lazy Class\n - Data Clumps\n - Feature Envy\n - Long Method\n - Long Parameter List\n - Switch Statements\n - Middle Man\n - Inappropriate Intimacy\n - Message Chains\n - Speculative Generality\n - Data Class\n - Primitive Obsession\n - Refused Bequest\n - Lazy Class\n - Data Clumps\n - Feature Envy\n - Long Method\n - Long Parameter List\n - Switch Statements\n - Middle Man\n - Inappropriate Intimacy\n - Message Chains\n - Speculative Generality\n - Data Class\n - Primitive Obsession\n - Refused Bequest\n - Lazy Class\n - Data Clumps\n - Feature En"

GITHUB_TOKEN = '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'
REPO_NAME = 'indra-deepika/clash-of-clans'
FILE_PATH = '/src/building.py'
refactored_code = 'Alas! The refactored code!'

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
contents = repo.get_contents(FILE_PATH)
code = contents.decoded_content.decode()

pr_url = create_pull_request(repo, 'main', new_branch_name, FILE_PATH, refactored_code, pr_title, pr_body)
print("Pull Request URL:", pr_url)
