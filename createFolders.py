import os
import argparse

mdates=["20201218",  "20210115", "20210319", "20210416", "20210521", "20210618", "20210917", "20230120"]

argp = argparse.ArgumentParser()
argp.add_argument("symbol", nargs="+")
argp.add_argument(
    "-d", "--debug", action="store_true", help="turn on debug logging"
)
argp.add_argument(
    "-p", "--port", type=int, default=4002, help="local port for TWS connection"
)
argp.add_argument("--size", type=str, default="1 min", help="bar size")
argp.add_argument("--duration", type=str, default="1 D", help="bar duration")
argp.add_argument(
    "-t", "--data-type", type=str, default="MIDPOINT", help="bar data type"
)
argp.add_argument(
    "--base-directory",
    type=str,
    default="C:/importantData/data",
    help="base directory to write bar files",
)
argp.add_argument(
    "--currency", type=str, default="USD", help="currency for symbols"
)
argp.add_argument(
    "--exchange", type=str, default="SMART", help="exchange for symbols"
)
argp.add_argument(
    "--expiry", type=str, default="", help="expiry for options"
)

argp.add_argument(
    "--strike", type=str, default="", help="strike for options"
)

argp.add_argument(
    "--security-type", type=str, default="OPT", help="security type for symbols"
)

argp.add_argument(
    "--max-days", help="Set start date to earliest date", action="store_true",
)
argp.add_argument(
    "--clientid", help="Set client id", action="store_true",
)

args = argp.parse_args()

strikes={}
strikes["OLLI"] = [80,85,90,95,100]
strikes["FIVE"] = [130,135,140,145,150]
strikes["YELP"] = [15,20,25]
strikes["GOOG"] = [1700,1750,1800]
strikes["FB"] = [300]

strikes["RNG"] = [300]
strikes["TTD"] = [900]
strikes["SQ"] = [200]
strikes["EPAM"] = [350]
strikes["QGEN"] = [55]
strikes["HOLX"] = [70,75,80]
strikes["KWEB"] = [75]

strikes["CLGX"] = [75,80]
strikes["ASML"] = [400,450]
strikes["CROX"] = [60,65]
strikes["AMAT"] = [65,70,75]
strikes["IIVI"] = [55,60,65]
strikes["PRIM"] = [15,20,25]

strikes["KRE"] = [45,50,55]
strikes["KBE"] = [30,35,40]
strikes["EWP"] = [20,25,30]

strikes["FORM"] = [35, 38, 40]
strikes["LRCX"] = [400,420,430,450]
strikes["LOW"] = [160]

strikes["NVDA"] = [500,520,525,530,550]
strikes["HTH"] = [22,23,24]
strikes["SIVB"] = [340,345,350]

strikes["TME"]  = [15,16,17,18]
strikes["GMAB"] = [30,35,40,45]
strikes["GRBK"] = [20,22.5,25,30]
strikes["NOW"]  = [505,510,515,520]

strikes["REM"] = [30,31,32]
strikes["EUFN"] = [16,17,18]
strikes["XLI"] = [83,89,90]
strikes["SPYG"] = [52,53,54]

obasedir=r"C:\importantData\data\OPT_MIDPOINT\1_min"
sbasedir=r"C:\importantData\data\STK_MIDPOINT\1_min"

contracts = []
for s in args.symbol:
    # print("sectype:", args.security_type)
    print("mkdir ", os.path.join(sbasedir, s))
    os.makedirs(os.path.join(sbasedir, s), exist_ok=True)
    for md in mdates:
        for k in strikes[s]:
            p = s+md+"C"+str(k)
            print("mkdir "+p)
    # p = make_download_path(args, contract)
            os.makedirs(os.path.join(obasedir,p), exist_ok=True)
