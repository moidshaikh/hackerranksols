'''
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"'''

def strip_comments(strng, markers):
    final = []
    lines = strng.split('\n')
    for line in lines:
        tmpstring = line
        for marker in markers:
            if marker in line:
                tmpstring = line[:line.find(marker)]
                final.append(tmpstring)
        
    return final[:-1]

strng = 'apples, pears # and bananas\ngrapes\nbananas !apples'

lines = ['apples, pears # and bananas', 'grapes', 'bananas !apples']
# lines = strng.split('\n')
markers = ['#', '!']







res = strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
e_res = 'apples, pears\ngrapes\nbananas'
print(len(res), len(e_res))

# strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
# strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')


# strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas')

# strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
# strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')
