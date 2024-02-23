# import openai
# from github import Github
# import re
#
# from constants import OPENAI_API_KEY , GITHUB_TOKEN , REPO_NAME , FILE_PATH
# # # Set your OpenAI API key directly
# # OPENAI_API_KEY = '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'
# openai.api_key = OPENAI_API_KEY
# # # Set your GitHub token and repo details
# # GITHUB_TOKEN = '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'
# # REPO_NAME = 'indra-deepika/SE_Bonus_Test_Repo'
# # FILE_PATH = '/books-web/src/main/java/com/sismics/books/rest/resource/UserResource.java'
#
#
#
# def apply_changes(original_code, changes):
#     # Split the changes into individual functions
#     function_changes = re.split(r'\n(?=\d+\.\s*\*\*\w+)', changes)
#
#     # Iterate over function changes and apply them to the original code
#     for function_change in function_changes:
#         # Extract function name
#         match = re.search(r'\*\*\w+\s*:\s*$', function_change)
#         if match:
#             function_name = match.group().strip('**: ')
#         else:
#             continue
#
#         # Extract function content
#         content_match = re.search(r'```java\n([\s\S]*?)\n```', function_change)
#         if content_match:
#             function_content = content_match.group(1)
#         else:
#             continue
#
#         # Find and replace the original function with the modified content
#         original_code = re.sub(
#             fr'{function_name}\s*\(.*?{{\n([\s\S]*?)\n}}',
#             f'{function_name} {{\n{function_content}\n}}',
#             original_code
#         )
#
#     return original_code
#
#
# # print(apply_changes(original_code, changes)
#
# def refactor_design_smells(code):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
# #         max_tokens = 4096,
#         messages=[
#             {"role": "system", "content": "I am a refactoring bot that gives particular changes that changed in functions or classes"},
#             {"role": "user", "content": f"Give the refactored pieces of code given the design smell is Unutilised Abstraction :\n\n{code}"}
#         ]
#     )
#     return response['choices'][0]['message']['content']
#
#
#
#
#
# # Initialize GitHub client
# g = Github(GITHUB_TOKEN)
# repo = g.get_repo(REPO_NAME)
# contents = repo.get_contents(FILE_PATH)
# code = contents.decoded_content.decode()
#
# print(code)
#
# # refactored_code = refactor_design_smells(code)
# # print("Refactored Code:", refactored_code)
#
# # final_code = apply_changes(code , refactored_code)
# #
# # print(final_code)
#
#
#
#
#
#
#
#
#


print("YAHHHHHHHHHHHHHHOOOOOOOOOOOOOOOOOOO")
