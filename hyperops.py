import re


def hyperop(exp: str) -> int:
    """
    This function facilitates higher order repetitive operations (hyperoperations) such as tetration.\n
    'exp' should be a string of the form: an integer a, followed by one or more *'s, followed by an integer b. Whitespace around args is ignored.\n
    E.g. '2***3' or ' 2 *** 3 '\n
    The number of *'s corresponds to the order of the hyperoperation minus 1\n
    E.g. * = multiplication, ** = exponentiation, *** = tetration, ...
    """

    if re.match("^\s*\d+\s*\*+\s*\d+\s*", exp) == None:
        raise Exception("expression was not formatted correctly")
    newStr = "".join(exp.split())
    ind = newStr.index("*")
    n = newStr.count('*')
    a = int(newStr[0:ind])
    b = int(newStr[ind+n:len(newStr)])
    return hyperopHelper(a, b, n)

def hyperopHelper(a, b, n):
    if n == 1:
        return a * b
    if n == 2:
        return a ** b
    ans = a
    for i in range(b-1):
        ans = hyperopHelper(ans, a, n-1)
    return ans

def main():
    print(hyperop("2 * 3"))
    print(hyperop("  2 **3 "))
    print(hyperop("2***3"))
    print(hyperop("2 **** 3"))
    print(hyperop("4 *** 4"))
    print(hyperop("2 ********** 2"))
    print(hyperop("wef wefwe f"))

if __name__ == "__main__":
    main()