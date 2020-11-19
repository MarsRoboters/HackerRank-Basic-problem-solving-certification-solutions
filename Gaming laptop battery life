def getBattery(events):
    
    
    remainingCharge = 50
    
    for i in events:
        
        if i >= 0:
            if remainingCharge > 100:
                remainingCharge = 100
            else:
                remainingCharge += i
                if remainingCharge > 100:
                    remainingCharge = 100
        
        else:
            if remainingCharge < 0:
                break
            else:
                remainingCharge += i
    return remainingCharge
            

if __name__ == "__main__":
    
    events = [3,-10, 60, 10]
    result = getBattery(events)
    print(result)
    
