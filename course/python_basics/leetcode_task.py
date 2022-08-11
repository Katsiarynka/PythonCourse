def defangIPaddr(address: str) -> str:
    # https://leetcode.com/problems/defanging-an-ip-address/submissions/      
    result = ''
    for c in address:
        if c == '.':
            result += '[.]'
        else:
            result += c
    return result

assert defangIPaddr('123.32.234.534') == '123[.]32[.]234[.]534'