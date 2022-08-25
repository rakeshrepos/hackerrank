'''
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=false
'''

if __name__ == '__main__':
    N = int(input())
    values = []

    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            values.insert(int(command[1]),int(command[2]))
        elif command[0] == 'print':
            print(values)
        elif command[0] == 'remove':
            values.remove(int(command[1]))
        elif command[0] == 'append':
            values.append(int(command[1]))
        elif command[0] == 'sort':
            values.sort()
        elif command[0] == 'pop':
            values.pop()
        elif command[0] == 'reverse':
            values.reverse()
        else:
            print('invalid input')

