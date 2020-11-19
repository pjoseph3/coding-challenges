def generate_palindromic_decompositions(s):
    result = []
    helper(s, 0, '', result)

    return result


def helper(s, count, word, result):
    if count == len(s):
        isPalin = True
        string = ''

        print(word)
        for i in range(len(word)):

            if word[i] == '|':
                # print(string)

                isPalin = isPalindrome(string)
                string = ''
            else:
                string += word[i]

            if not isPalin:
                break
        if string != '':
            isPalin = isPalindrome(string)

        if isPalin and word[len(word)-1] != '|':
            print(word)
            result.append(word)

        return

    helper(s, count + 1, word + s[count], result)
    helper(s, count + 1, word + s[count] + '|', result)


def isPalindrome(s):
    for i in range((len(s) // 2) + 1):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True

def main(s):

    print(generate_palindromic_decompositions(s))


if __name__ == '__main__':
    s = "abracadabra"
    main(s)