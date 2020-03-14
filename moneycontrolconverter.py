import csv
import sys
import getopt
from datetime import datetime


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('moneycontrolconverter.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
           print('moneycontrolconverter.py -i <inputfile> -o <outputfile>')
           sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    convert(inputfile, outputfile)
   
def convert(inputfile, outputfile):
    with open(outputfile, 'w', newline='') as csvfile:
        fieldnames = ['BSE/NSE/ISIN Code','Buy Date','Buy Quantity','Buy Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        with open(inputfile, 'r') as file:
            reader = csv.DictReader(file)
            money_ctrl_dict = {}
            for row in reader:
                trade_date = datetime.strptime(row['trade_date'],'%Y-%m-%d')
                money_ctrl_dict['BSE/NSE/ISIN Code']= row['tradingsymbol']
                money_ctrl_dict['Buy Date']= trade_date.strftime('%d-%m-%Y')
                money_ctrl_dict['Buy Quantity']= row['quantity'].split('.')[0]
                money_ctrl_dict['Buy Price']= row['price']
                print(money_ctrl_dict)
                writer.writerow(money_ctrl_dict)

if __name__ == "__main__":
    main(sys.argv[1:])
