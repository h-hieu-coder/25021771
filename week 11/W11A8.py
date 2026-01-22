try : 
    s = input()
    end_s = s[len(s)-4:]
    if end_s == ".txt" or end_s == ".zip" : 
        print("Doc file thanh cong")
    else : 
        raise ValueError
except ValueError : 
    print("File khong hop le")