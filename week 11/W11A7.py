try : 
    tuoi = int(input())
    if tuoi >= 0 : 
        print(2025 - tuoi) 
    else : 
        raise ValueError
except ValueError: 
    print("Tuoi khong hop le.")