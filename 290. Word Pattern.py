pattern = 'abba'
s ="dog dog dog dog"
dict_ = {}
check = ''
new_s = s.split(" ")
for i in range(len(new_s)):
    dict_[pattern[i]] = new_s[i]
for i in range(len(pattern)):
    check += dict_.get(pattern[i])
    check += " "
print(check[0:-1])
print(check[0:-1] == s)