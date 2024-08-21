import re

# Emails
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@another.com"

# Match email addresses but exclude '@exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Find all emails in the text that match the pattern
emails = re.findall(pattern, text)

# Print emails 
print("Extracted Emails:", emails) 