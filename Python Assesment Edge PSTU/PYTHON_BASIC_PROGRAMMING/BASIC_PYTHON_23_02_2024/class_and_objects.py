fresh = 'I feel Fresh!'
tired = 'I feel Tired!'

class Hours:
    def morning(self):
        print(fresh)
    def evening(self):
        print(tired)

def main():
    how_i_feel = Hours()
    
    how_i_feel.morning()
    how_i_feel.evening()

if __name__ == "__main__":
    main()
