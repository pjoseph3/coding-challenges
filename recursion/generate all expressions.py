# Complete the function below.

def generate_all_expressions(s, target):
    results = []
    helper(s[1:], target, s[0], results)
    return results


def helper(s, target, string, results):
    if len(s) == 0:

        first = 0;
        second = 0;

        list1 = []
        list1 = list(string)

        mult = False

        for i in list1:
            if i == "+":
                first += second
                second = 0
                mult = False
            elif i == "*":
                mult = True
            else:
                if mult:
                    second *= int(i)
                else:
                    second = int(i)

        if ((first + second) == target):
            results.append(string)
        return

    helper(s[1:], target, string + "+" + s[0], results)
    helper(s[1:], target, string + "*" + s[0], results)
    helper(s[1:], target, string + s[0], results)
    return results


def main(k):

    print(generate_all_expressions("012",3))


if __name__ == '__main__':
    k = 3
    main(k)