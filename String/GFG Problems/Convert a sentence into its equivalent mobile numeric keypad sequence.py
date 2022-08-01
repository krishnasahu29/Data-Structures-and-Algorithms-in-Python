# https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/

# Python3 implementation to convert
# a sentence into its equivalent
# mobile numeric keypad sequence

# Function which computes the
# sequence
def printSequence(arr, inp):
    # length of input string
    n = len(inp)
    output = ""

    for i in range(n):

        # checking for space
        if inp[i] == ' ':
            output = output + "0"
        else:
            # calculating index for each
            # character
            position = ord(inp[i]) - ord('A')
            output = output + arr[position]
    # output sequence
    return output


if __name__ == '__main__':

    # Driver code
    string = ["2", "22", "222",
              "3", "33", "333",
              "4", "44", "444",
              "5", "55", "555",
              "6", "66", "666",
              "7", "77", "777", "7777",
              "8", "88", "888",
              "9", "99", "999", "9999"]

    inp = "GEEKSFORGEEKS"
    print(printSequence(string, inp))
