def print_lines(message):
  print("Message is :"+message)
  
  
def printHello():
    print("Hello all")
    
    
def bookMetroTicket(source,destination):
    # actual code to book ticket
    return 90

    
print_lines("Hello")
printHello()

result = bookMetroTicket("Howrah","Bangalore")
print("Ticket price is :"+str(result))