import sys
import getSources
import getDestinations
import getWarehouses

def main(token):
    getSources.main(token)
    getDestinations.main(token)
    getWarehouses.main(token)

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        token = sys.argv[1]
        main(token)