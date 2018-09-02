from nomad import terms
import re

class Mapping():

    def __init__(self):

        self.values = terms.values()
        self.keys = terms.keys()




    def get_term(self, term):

        # return term
        return True


    def term_in_key(self, key, term):
        if term in key:
            return key
        else:
            return False


    def categories(self, term):

        keys = {}
        # term = substring from key
        print("< Term = " + term + " >")
        # find a key in which the term exists
        for key in self.keys:

            if key.find(term) == -1:
                continue
            else:
                print("[    " + key + ": ")

                value = terms[key]
                #value = keys.__setitem__(key, terms[key])
                print("[         " + str(value) + " ]")



    def key_in_values(self, key):
        print("[ " + key + " ]: ")
        for valueArray in terms.values():
            for i in range(0,len(valueArray)-1):
                if str(key) in valueArray[i] :
                    print(str(valueArray))
                else:
                    continue


                    # else:
                    #
                        #
                        # value = terms[key]
                        # # value = keys.__setitem__(key, terms[key])
                        # print("[         " + str(value) + " ]")
                        #

            if valueArray.count(key) == 0:
                return "This key does not occur in any values ;"
            else:
                # print(valueArray.count(key))
                print("[         " + str(valueArray) + " ]")
                print("                                   ")




    def loophole_discovery(self):

        return True

