import os 
file_path = input()
if os.path.exists(file_path) and os.path.isfile(file_path):
    print("YES")
else:
    print("NO")