#Covalyzer
## MOTIVATION
I strongly believe in the Blue Collar Strategy from Alan Ellman and his Blue Collar Investors. It is a 100% safe way of getting high yields in the current low-interest environment without the need for taking risks. 
The only hook is: you MUST have your emotions under control. 
So I am a very emotional guy as I experienced :-(. And I am a softwareengineer. And I need some more money :-) 
So there you can see now the reason why this project was born. When it is finished, it helps to coordinate and even automizing the different involved activities belonging to this BCI strategy.

## MAIN OBJECTIVES
- Auto- and Optimizing the "Blue Collar Strategy" from Alan Ellman. 
- Make your Profits plannable. 
- Exclude risks from trading.

### Introduction
Alan Ellman has laid out an excellent strategy/Policy over the last decades on covered call or cash secured put positions. This comprises scanning the market, entering positions after a well defined screening process, maintaining the open Buywrites and - most important - executing the right exitstrategy.

The only drawback is the toolsupport. The only support his company gives are some excel sheets which you have to fill-in and maintain manually. This gets more and more complicated whenever your positionsgrow. Managing earningcalls, ex-dividend dates, option expriry-dates and especially rollover-activity you cannot handle anymore seriously with excel if you have more than 10 positions.
But all of this can be automized. Especially searching the perfect option for a specific position in regards to ITM/ATM/OTM by considering expiry and all other timeline issues, calculatin gthe profit and and and this all can be done in a much better way with the help of a machine.

The mainproblem I experienced with the strategy is, that you loose the overview very soon if you try to track your positions manually. Especially mixing up optionprofits with the current P/L of the underlying stockprice brings in a huge mess. And if you are trading on margin it even becomes much worse: you have to take into account the interest rate you pay on your margin loan and consider carefully if taking a margin loan would be worth it. Loads of issues to consider when running a covered call strategy.

This program here should separate the accumulated optionprofits from the stockpositions. The stockpositions are observed only in the background. The main task of this program is to track AND visualize your past, your current AND your future profits so that the Blue Collar Strategy is better plannable !

### Functionality
For accomplishing the objectives explained above you need tables, graphs and automatisms. A robot first must gets fed with the right input, then the robot has to run. I must get the current prices, it has to process these, afterwards runs the BCI rules over it, gets all the dates for the important events for expiry/earningcalls/dividends and at the end visualizes the whole results of theses processes to the accountholder. Everytime all possible and plannable contraints must be taken into account.
Be aware this is all pure old classic mechanisms ! No artificial intelligence involved.

1) Create Watchlists to watch profitable Buy-Write positions.
 - Possibly take the weekly Stock Report from BCI as a basis for this with all included informations about earningcalls, dividends, open interests, weekly/monthly option availability, etcetc...
 - Query and analyse optionchains for good candidates from the Blue Collar Weekly Stockreport regarding maximisation of the monthly return
 - Propose the best option to buy, taking into account the general current attitude regarding the stockmarkettrend
 - ITM/ATM and OTM options literally have to be taken into account
 - Watchout for diversification ! Never more than 10% in one industry / Hold at least 10 positions.
 - Include ETFs as well !
 - Calculate upside potentials and downside protections in realtime

2) Draw timeline containing for each CC-position:
 - earnings call for the associated position
 - dividend ex-date for the position
 - expiry of the underlying option 
 - when the position was invoked
 - would be nice to have one MAIN-Timeline where all "milestones" are put on, maybe along with the foreseeable profit during that time
 
3) Monitor the Portfolio open positions
 - Separate accumulated profits from your calls from a potential decrease of stockprices. SHOW THE PROFITS (past/current/future) !!!
 - Visualize the big advantage of trading covered call vs. stock trading whereever possible.
 - WARN if a stockprice drops too fast 
   But do NOT warn if the entire market drops with this speed, as this will recover sooner or later.
 - WARN if an earningcall is coming up soon
 - Survey the BCI strategies: has the underlying optionprice already reached 20% or 10% of the initial price ?
 - In which phase of the 4 week period are we ?
 
4) Draw graphs
 - Visualization is everything. So this is an important part of the entire project:
 - Visualize th optionprofits of account over the next weeks on the basis of the actual portfolio, taking into account dividends and rollovers and transaction fees. 
 - Meltdown of timevalue of the options
 - Maybe some nice 3D charts drawing x=days left until expitry / y=strikeprice (with the current price marked) / z=timevalue
 
5) Automization of the trading-interface. 
- I have a lot of experience with is the Trading-API of Interactive Brokers. This will be it.


