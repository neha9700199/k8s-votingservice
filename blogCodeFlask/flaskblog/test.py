import os
email = os.environ.get('USER_EMAIL')
ps = os.environ.get('USER_PASS')

print(email,' ', ps)