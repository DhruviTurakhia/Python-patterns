for i in range(34,49):
    with open(f'number_pattern/Medium/pattern_{i}.py', 'w') as f:
        data = 'def Pattern_Programs(n):\n\tfor i in range(1,n+1):\n\t\tprint("*"*i)\n\n\nif __name__ == \'__main__\':\n\tPattern_Programs(int(input()))'
        f.write(data)
