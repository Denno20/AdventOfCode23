def main():
    sum = 0
    numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
    ]

    with open("values.txt", "r") as f:
        for line in f.readlines():
            digits = {}
            for val in numbers:
                if line.find(str(val)) != -1:
                    for i in findall(line, str(val)):
                        digits[i] = convert_word_to_number(str(val))
        
            sortedDigits = sorted(digits.items(), key=lambda t: t[0])
            calibrationValue = int(str(sortedDigits[0][-1]) + str(sortedDigits[-1][-1]))

            sum += calibrationValue
    
    print(f"The final sum: {sum}")

def get_index(digit):
    return digit.get("index")

#Borrowed this from https://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
def findall(text, sub):
    """Return all indices at which substring occurs in text"""
    return [
        index
        for index in range(len(text) - len(sub) + 1)
        if text[index:].startswith(sub)
    ]


def convert_word_to_number(word):
    match word:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return int(word)

if __name__=="__main__":
    main()