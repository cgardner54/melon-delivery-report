
def parselogs(date, path):
    delivery_log = open(path)
    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')


        melon = words[0]
        count = words[1]
        amount = words[2]
        
        print("Day {}: Delivered {} {}s for total of ${}".format(date,
            count, melon, amount))



parselogs(19, "um-deliveries-20140519.txt")
parselogs(20, "um-deliveries-20140520.txt")
parselogs(21, "um-deliveries-20140521.txt")