import re

email = "ilearniexcel@gmail.com"
position_at = email.find('@')
print("Position of '@':", position_at)

dot_com = email[-4:]
print(f"Extracted '.com':", dot_com)

at_index = email.find('@')
dot_index = email.find('.')
gmail_part = email[at_index + 1:dot_index]
print("Extracted 'gmail':", gmail_part)

split_parts = re.split(r"[@.]", email)
print("Split parts:",split_parts) 