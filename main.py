logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program!")

moreBidders = True
bidders = {}


def highestBidder(biddingRecord):
    highestBid = 0
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")


while moreBidders:
    bidderName = input("What is your name? ")
    bidderBid = int(input("What is your bid? $"))
    bidders[bidderName] = bidderBid
    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if otherBidders == 'no':
        print(f"The winner is {max(bidders, key=bidders.get)} with a bid of ${max(bidders.values())}")  #This line would allow me to remove/delete the entire function.
        moreBidders = False
        highestBidder(bidders)  #Finds the winner by calling the function
    else:
        print ('\n' * 25)

