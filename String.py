letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''

print(letter.replace("<|Name|>", "Maria").replace("<|Date|>", "15 june 2025"))
