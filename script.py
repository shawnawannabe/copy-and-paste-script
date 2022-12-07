with open("input.txt","r") as input_file:
    input_data = input_file.readlines()
    input_list = []
    for i, line in enumerate(input_data):
        line = line.replace(",", ".")
        line = line.replace("\n", "")
        if "<" in line:
            line = "0"
        input_list.append(line)

with open('copyfrom.txt','r') as f:
    data = f.readlines()

with open('result.txt','w') as f:
    li = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    for i, line in enumerate(data):
        fields = line.split(",")
        fields[1] = input_list[i]
       
        data[i] = '{},{},{},{},\n'.format(fields[0],fields[1],fields[2],fields[3])

   
    data = ''.join(data)
    strToReplace   = ','
    replacementStr = ''
    # Reverse the substring that need to be replaced
    strToReplaceReversed   = strToReplace[::-1]
    # Reverse the replacement substring
    replacementStrReversed = replacementStr[::-1]
    # Replace last occurrences of substring 'is' in string with 'XX'
    data = data[::-1].replace(strToReplaceReversed, replacementStrReversed, 1)[::-1]
    f.write(data)


#Thank you for your e-maill. I am currently out of office with no access to my e-mail. I'll be back on Monday, 10 October 2022. For more information, please have a look into my calendar.  Kind regards,