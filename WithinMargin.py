def within_margin_percentage(desired, actual, margin):
    runs = 0
    count = 0

    while runs < len(desired):
     if abs(desired[runs] - actual[runs]) <= margin: 
        count += 1 
     runs += 1

    return count/len(desired)











if __name__ == "__main__":
    print(within_margin_percentage(desired=[10.0, 5.0, 8.0, 3.0, 2.0], actual= [10.3, 5.2, 8.4, 3.0, 1.2], margin=0.5))
