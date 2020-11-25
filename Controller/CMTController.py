import os
import re
import datetime, time

import argparse
from threading import Thread

import Misc.const
import Model
from Misc.globals import globvars
from Model.download import DownloadApp, make_download_path
from Model.resamplecsv import resample

class Controller:
    def __init__(self, model):
        self.model = model
        self.brokerPort = 7497
        self.downloadCounter = 0
        self.autoUpdate = True
        self.args = argparse.Namespace()
        self.args.base_directory = Misc.const.DATADIR
        self.args.data_type = "MIDPOINT"
        self.args.size = "1 min"
        self.args.max_days = None
        self.args.duration = "1 D"
        self.downloadThread = Thread(target=self.updateHistory, daemon=False)
        self.doDownload = False
        self.downloadSelector = Misc.const.BOTH
        self.downloadThread.start()
        globvars.logger.info("***************************")
        globvars.logger.info(__name__)
        attrs = vars(self)
        s="\n"+__name__+":"
        s = '\n'+__name__+':'.join("\n%s: %s" % item for item in attrs.items())
        globvars.logger.info(str(s))
        globvars.logger.info("***************************")
        pass

    def initData(self,v):
        self.view = v

    def getStockData(self, cc):
        return self.model.getHistStockData(cc)

    def switchDownloadState(self):
        #"callback" called when pushing the toolbar button
        if self.doDownload == True:
            self.doDownload = False
            globvars.logger.info("stop downloading data, finishing current download, please wait...")
        else:
            self.doDownload = True
            globvars.logger.info("start downloading data")

    def fullSymbol(self, contract):
        if contract.secType == "OPT":
            ret = contract.symbol + contract.lastTradeDateOrContractMonth + "C" + contract.strike
        else:
            ret = contract.symbol
        return ret

    def updateHistory(self, do_overwrite=False, forced_startdate = "20200501", forced_enddate = "20201017"):
        globvars.logger.info("***********************************************")
        globvars.logger.info("THREAD STARTED")
        globvars.logger.info("***********************************************")
        #this is the main thread target function
        while True:
            if self.doDownload == True:
                globvars.logger.info("Starting Download")
                self.doUpdateHistory(do_overwrite, forced_startdate, forced_enddate)
                globvars.logger.info("Download stopped")
            time.sleep (1)
        return

    def optionExpired(self,optionpatmatch):
        if optionpatmatch:
            (dt, type, ul, expiry_y, expiry_m, expiry_d, strike) = optionpatmatch.groups(0)

            expiry_d = expiry_y + expiry_m + expiry_d

            try:
                expiryday = datetime.datetime.strptime(expiry_d, "%Y%m%d")
            except:
                pass
            daybeforeyesterday = datetime.datetime.now() - datetime.timedelta(2)

            if expiryday < daybeforeyesterday:
                return True
            else:
                return False
        else:
            raise Exception("nomatch in optionpattern")

    def doUpdateHistory(self, do_overwrite=False, forced_startdate = "20200101", forced_enddate = "20201017"):
        while True:
            globvars.logger.info("do update history")
            datetimepattern=""
            latest = {}
            newest = {}
            contracts=[]
            optpat = re.compile(Misc.const.DATADIR + r"\\(...)_(.+)\\1_min\\(\w*)(....)(..)(..)C(.+)$")
            stkpat = re.compile(Misc.const.DATADIR + r"\\(...)_(.+)\\1_min\\(\w*)$")
            barwidth = "1_min"
            self.args.port = self.brokerPort

            self.downloadCounter = 0
            for root, dirs, files in os.walk(Misc.const.DATADIR):

                if "1_min" in root:
                    o = optpat.match(root)
                    s = stkpat.match(root)

                    if o:
                        if self.downloadSelector == Misc.const.STOCKSONLY:
                            continue
                        (dt, type, ul, expiry_y, expiry_m, expiry_d, strike) = o.groups(0)

                        if ul == "DEMO" or ul == "CTLT" or self.optionExpired(o):
                            continue

                        expiry_d = expiry_y + expiry_m + expiry_d

                        ctrct = self.model.brkConnection.make_contract(ul, dt, "USD", "SMART", expiry_d, strike)
                        contracts.append(ctrct)
                        newest[ctrct] = {}
                        newest[ctrct]["c"] = datetime.datetime.strptime("20200501", "%Y%m%d")
                        newest[ctrct]["t"] = type
                        nextname = datetime.datetime.strftime(newest[ctrct]["c"] + datetime.timedelta(1), "%Y%m%d") + ".csv"
                        newest[ctrct]["f"] = os.path.join(root, nextname)

                        # globvars.logger.info(root)
                        for name in files:
                            #option

                            if type != "MIDPOINT":
                                continue

                            if dt not in latest:
                                latest[dt]={}
                            if type not in latest[dt]:
                                latest[dt][type] = {}
                            if barwidth not in latest[dt][type]:
                                latest[dt][type][barwidth] = {}
                            if ul not in latest[dt][type][barwidth]:
                                latest[dt][type][barwidth][ul] = {}
                            if expiry_d not in latest[dt][type][barwidth][ul]:
                                latest[dt][type][barwidth][ul][expiry_d] = {}
                            if strike not in latest[dt][type][barwidth][ul][expiry_d]:
                                latest[dt][type][barwidth][ul][expiry_d][strike] = {}

                            match = re.match(r"^(....)(..)(..)\.csv", name)
                            if match:
                                splyear, splmonth, splday = match.groups(0)

                                if newest[ctrct]["c"] < datetime.datetime.strptime(splyear + splmonth + splday, "%Y%m%d"):
                                    newest[ctrct]["c"] = datetime.datetime.strptime(splyear + splmonth + splday, "%Y%m%d")
                                    nextname = datetime.datetime.strftime(newest[ctrct]["c"] + datetime.timedelta(1),
                                                                          "%Y%m%d") + ".csv"
                                    newest[ctrct]["f"] = os.path.join(root, nextname)
                    elif s:
                        if self.downloadSelector == Misc.const.OPTIONSONLY:
                            continue
                        (dt, type, ul) = s.groups(0)
                        if ul == "DEMO" or ul == "CTLT":
                            continue

                        ctrct = self.model.brkConnection.make_contract(ul, dt, "USD", "SMART")
                        if ul in ["CYBR","FIVE","MNST","AMAT", "BRKS", "PRIM", "IIVI"]:
                            #ambigious symbols without primary Exchange:
                            ctrct.primaryExchange = "NASDAQ"
                        if ul == "KWEB":
                            ctrct.primaryExchange = "ARCA"

                        contracts.append(ctrct)
                        newest[ctrct] = {}
                        newest[ctrct]["c"] = datetime.datetime.strptime("20200501", "%Y%m%d")
                        newest[ctrct]["t"] = type
                        nextname = datetime.datetime.strftime(newest[ctrct]["c"] + datetime.timedelta(1), "%Y%m%d") + ".csv"
                        newest[ctrct]["f"] = os.path.join(root, nextname)

                        for name in files:
                            if dt not in latest:
                                latest[dt]={}
                            if type not in latest[dt]:
                                latest[dt][type] = {}
                            if barwidth not in latest[dt][type]:
                                latest[dt][type][barwidth] = {}
                            if ul not in latest[dt][type][barwidth]:
                                latest[dt][type][barwidth][ul] = {}

                            m = re.match(r"^(....)(..)(..)\.csv", name)
                            if m:
                                y,m,d = m.groups(0)

                                if newest[ctrct]["c"] < datetime.datetime.strptime(y + m + d,"%Y%m%d"):
                                        newest[ctrct]["c"] = datetime.datetime.strptime(y+m+d, "%Y%m%d")
                                        nextname = datetime.datetime.strftime(newest[ctrct]["c"]+datetime.timedelta(1), "%Y%m%d")+".csv"
                                        newest[ctrct]["f"] = os.path.join(root,nextname)
                    else:
                        globvars.logger.info("could not match %s as stock or option",root)

            contractsToDownload=[]
            for ctrct in newest:
                #TODO: check if the last file has the same size as all others, only if this is not the case take newestdate=newest[ctrct]["c"].date() here.
                #maybe overwrite the last file,
                #for now: simply start at next day, even if the day before MIGHT be corrupt (dur to an interruption the last time data was fetched)
                newestdate=newest[ctrct]["c"].date()+datetime.timedelta(1)
                today = datetime.datetime.today().date()
                csvfile = newest[ctrct]["f"]
                if  today > newestdate or do_overwrite == True:
                    # if not os.path.exists(csvfile) or do_overwrite == True:
                    # Posiible datatypes: TRADES, MIDPOINT, BID, ASK, BID_ASK, ADJUSTED_LAST, HISTORICAL_VOLATILITY, OPTION_IMPLIED_VOLATILITY, REBATE_RATE, FEE_RATE, YIELD_BID, YIELD_ASK, YIELD_BID_ASK, YIELD_LAST
                    if do_overwrite == True:
                        startdate = forced_startdate
                        enddate = forced_enddate
                        # datatypes = ["BID", "ASK", "BID_ASK", "MIDPOINT"]
                    else:
                        startdate = datetime.datetime.strftime(newestdate, "%Y%m%d")
                        enddate = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d")
                        # datatypes = [newest[ctrct]["t"]]

                    globvars.logger.info("updating %s", self.fullSymbol(ctrct))

                    contractsToDownload=[]
                    if startdate != enddate:
                        self.args.security_type = ctrct.secType
                        self.args.start_date = datetime.datetime.strptime(startdate, "%Y%m%d")
                        self.args.end_date = datetime.datetime.strptime(enddate, "%Y%m%d")
                        self.args.base_directory = Misc.const.DATADIR

                        if ctrct.secType == "OPT":
                            self.args.expiry = ctrct.lastTradeDateOrContractMonth
                            self.args.strike = ctrct.strike

                    timePassed = self.args.end_date - self.args.start_date
                    if timePassed.days > 0:
                        p = make_download_path(self.args, ctrct)
                        os.makedirs(p, exist_ok=True)
                        contractsToDownload.append(ctrct)
                        if self.doDownload == False:
                            return
                        else:

                            startweekday = self.args.start_date.isoweekday()
                            stopweekday = self.args.end_date.isoweekday()

                            if ((not ( startweekday == Misc.const.ISOWKDAYSATDAY and stopweekday == Misc.const.ISOWKDAYSUNDAY and timePassed.days < 4))
                                and (not ( startweekday == Misc.const.ISOWKDAYSUNDAY and stopweekday == Misc.const.ISOWKDAYMONDAY and timePassed.days < 4))
                                and (not ( startweekday == Misc.const.ISOWKDAYSATDAY and stopweekday == Misc.const.ISOWKDAYMONDAY and timePassed.days < 4))):

                                self.downloadCounter = self.downloadCounter + 1

                                globvars.logger.info(
                                    str(self.downloadCounter)+": retrieving " + ctrct.secType + " data for " + ctrct.symbol + ": " + p + " from " + startdate + " to " + enddate)
                                if len(contractsToDownload) > 0:
                                    downApp = DownloadApp(contractsToDownload, self.args)
                                    downApp.connect("127.0.0.1", self.brokerPort, clientId=10)
                                    dwnret=0
                                    try:
                                        downApp.run()
                                        # globvars.logger.info("downret: %s", str(globvars.downerrorcode["errorcode"]))
                                    except:
                                        #just please do not crash

                                        path = ""
                                        if ctrct.secType == "OPT":
                                            path = os.path.sep.join(
                                                [
                                                    Misc.const.DATADIR,
                                                    ctrct.secType + "_" + "MIDPOINT",
                                                    "1_min",
                                                    ctrct.symbol + ctrct.lastTradeDateOrContractMonth + "C" + ctrct.strike,
                                                ]
                                            )
                                        else:
                                            path = os.path.sep.join(
                                                [
                                                    Misc.const.DATADIR,
                                                    ctrct.secType + "_" + "MIDPOINT",
                                                    "1_min",
                                                    ctrct.symbol
                                                ]
                                            )

                                        # globvars.logger.info("downret exception: %s %s %s: %s", str(globvars.downerrorcode["errorcode"]), ctrct.secType,ctrct.symbol,path)
                                        # if globvars.downerrorcode["errorcode"] == 200:
                                        #     os.rmdir(path)
                                        pass
                                    # resample(False, os.path.basename(p))
                            else:
                                globvars.logger.info("we are on a weekend => no data")

                # globvars.logger.info("%s is already uptodate and no overwrite is set", self.fullSymbol(ctrct))

        return



    def getNumPositions(self):
        return self.model.getNumPositions()

    def connect(self):
        self.model.connectBroker()

    def disconnect(self):
        self.model.disconnectBroker()

    def changeBrokerPort(self, port):
        self.brokerPort = port
        self.model.changeBrokerPort(port)
        globvars.logger.info("Broker Port changed to %s", str(port))

    def toggleAutoUpdate(self):
        if self.autoUpdate == True:
            self.autoUpdate = False
        else:
            self.autoUpdate = True

        self.model.setAutoUpdate(self.autoUpdate)

    def resetAllColumns(self):
        self.view.resetAllColumns()

    def showAllColumns(self):
        l = self.model.columnCount(None)
        self.view.showAllColumns(l)

    def clearSelection(self):
        self.view.clearSelection()
