def newPassword(string):
    """
    https://app.glider.ai/practice/problem/basic-programming/john-wants-new-password/problem

    John has a password (string str) for his account. He created 2 empty strings - a and b. John wants to generate
    new password using these 3  strings (str, a, b) and following rules:
        1) Extract the first character of password and append a with this character.
        2) Extract the last character of a and append b with this character.
        John wants to get str and a empty and b lexicographically minimal.
        Help John, write a new program to generate new password (string b).

    :param string:
    :return:
    """
    n = len(string)
    right_min = list(string)
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i+1], string[i])

    st = []
    res = ""
    for i in range(n):
        while st and st[-1] <= right_min[i]:
            res += st[-1]
            st.pop()
        st.append(string[i])


    while st:
        res += st[-1]
        st.pop()

    print(res)
newPassword('cab')