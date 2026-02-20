import re

with open('jam2.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
match = re.search(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
if match:
    with open('script.jsx', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
    print("Extracted successfully.")
else:
    print("Could not find script tag.")
