#************************************************************************
# * Name: Stephen Ronkowski                                         CSC 157
# * Date: 8/23/2018                                             LAB 1
# *************************************************************************
# * Statement: Determine owner, selling cost and commission for house sale
# * Specifications:
# * Input  - owner
# *        - selling cost
# * Output - owner
# *        - selling cost
# *        - commission
# *************************************************************************


# output descriptive messages
print("This program calculates the cost to sell a home\n" 
                    + "and the commission paid to an individual sales agent.\n")

print("The user is asked for the last name of the seller and the\n" 
                    + "sales price.\n")

# prompt the user for input values

# seller's name
seller = input("Please enter the owner's last name: ")
# price of house
price = input("Please enter the sales price of the home: ")
        
# calculate the cost to sell the house and the commission
# on the sale of the listing and selling agents
cost = 0.06 * float(price)
commission = 0.015 * float(price)

# display the formatted results

# display header line
print('{0: <10}'.format('\nHome Owner'), '{0: >16}'.format('Price of Home'), sep='', end='' )
print('{0: >22}'.format('Seller’s Cost'), '{0: >21}'.format('Agent’s Commission'), sep='' )

# display the correctly formatted seller, price, cost, and commission


#formatting numbers for currency
price = '{0:.2f}'.format(float(price))
cost = '{0:.2f}'.format(float(cost))
commission = '{0:.2f}'.format(float(commission))

#printing numbers with placeholder symbols separating values
print('{0:<10}'.format(seller), '{0:*>16}'.format(price), '{0:*>22}'.format(cost),'{0:*>21}'.format(commission), sep='', end='')


print('\n')
 
