##View with Coin Class!

import CoinClass as c

### = 2/10
# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = c.Coin()
    your_coin = c.Coin()
    """
    # this creates an instance called 'my_coin' of the class 'Coin()'
    # Goes looking for the __init__ method

    # Display the side of the coin that is facing up.
    print("This side is up:", my_coin.get_sideup())

    # It's going to be heads!
    # notice you do not have to supply the argument/parameter
    

    # Toss the coin.
    print("I am going to toss the coin ten times:")
    for count in range(10):
        my_coin.toss()

        ##This line of code is a way a user could cheat if they had access to the class attributees!
        ##However, our __sideup definition in Coin Class prevents that from happening! :)
        my_coin.sideup = "Heads"

        # Display the side of the coin that is facing up.
        print("This side is up:", my_coin.get_sideup())
        """
    ###Receive the object as an argument and pass that object to a method
    def show_coin_status(coin_obj):
        print(coin_obj.get_sideup())

    def flip(coin_obj):
        coin_obj.toss()

    show_coin_status(my_coin)
    flip(my_coin)
    show_coin_status(my_coin)

    show_coin_status(your_coin)
    flip(your_coin)
    show_coin_status(your_coin)


# Call the main function.

main()
