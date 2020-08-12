import zipfile

name = r'C:\Users\Prajith\Downloads\assignment.zip'
password = 'Twg48wTM'

zip_file = zipfile.ZipFile(name)
wordlist = [] 
chars = [] 
for i in range(1,27):
    chars.append(chr(i+64))
    chars.append(chr(i+96))

for i in range(10):
    chars.append(str(i))

for i in range(len(chars)):
    for j in range(len(chars)):
        wordlist.append(chars[i]+chars[j])
for word in wordlist:
    try:
        val = password + word
        zip_file.extractall(pwd=bytes(val,'utf-8'))
    except:
        continue
    else:
        print('The password is: ',word)
        exit()
print('Password Not Found')