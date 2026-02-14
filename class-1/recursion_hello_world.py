def hello_world(n):
    print('hello world',n)
    if n>1:    
        hello_world(n-1)
    
hello_world(1100)