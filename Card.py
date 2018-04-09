class Card(object):

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    def __repr__(self):
        return "suit:%s value:%s" % (self.__suit, self.__value)

    def get_suit(self):
        return self.__suit

    def get_value(self):
        return self.__value
