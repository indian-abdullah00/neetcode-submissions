class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        num_str = len(strs)
        letters = []
        for string in strs:
            letters.append(str(len(string)))
            output = output + string 
        letter_string = ",".join(letters)
        output = str(num_str) +"/" + letter_string + "," + output
        # print(output)
        return output
        

    def decode(self, s: str) -> List[str]:
        output = []
        start = 0
        num_strs = ""
        for letter in s:
            start += 1
            if letter == "/":
                break
            num_strs = num_strs + letter

        print(start,num_strs)
        comma = int(num_strs) 
        count = 0
        letters_string = []
        number = ''

        for j,num in enumerate(s[start:]):
            if count == comma:
                print(count, comma, j)
                break
            if num == ",":
                count += 1
                letters_string.append(int(number))
                number = ''
                continue
            number = number + num 
            
        index = j+start
        for num in letters_string:
            word = s[index:index + num ]
            output.append(word)
            index = index + num
        return output
