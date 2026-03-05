def divide(a:float, b:float):
    if b ==0 :
        raise ValueError("Can't divide by 0")
    else:
        return (a/b)
    
if __name__ == "__main__":
    print(divide(1, 2))