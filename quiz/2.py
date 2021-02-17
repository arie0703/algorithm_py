def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in chars:
        #charがlookupのkeyにある場合
        if char in lookup.keys():
            stack.append(lookup[char])
        #charがlookupのvalueにある場合（閉じカッコ）
        if char in lookup.values():
            #stackが空なのに閉じカッコが出るのはおかしいのでfalse
            if not stack:
                return False
            #popするものと異なる場合もfalse
            # if char in stack:
            #     stack.pop()
            # else:
            #     return False
            #これを一行に↓
            if char != stack.pop():
                return False
        
        
    #最後にstackに何かしら残ってたらアウト
    if stack:
        return False
        
    return True


j = "{'key1': 'value1', 'key2' : [1, 2, 3], 'key3': (1,2,3)}"
i = "[]"
print(validate_format(j))