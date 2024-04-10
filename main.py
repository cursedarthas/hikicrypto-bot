from classes import CryptoCurrency

Bitcoin = CryptoCurrency('Bitcoin', 'https://cryptorank.io/?ysclid=luo1098dvl570589879')
Price_btc = Bitcoin.getPrice('sc-50f3633f-0 sc-28f598be-1 jXsWTV nZrBG')
Change_btc = Bitcoin.getChangePrice('sc-50f3633f-0 sc-92cddc74-0 glCbMx koiTCg')
Market_Cup_btc = Bitcoin.getMarketCup('sc-67ec7576-0 bwSdbV sc-ebc32dcf-0 bZbfEj')

Ethereum = CryptoCurrency('Ethreum', 'https://cryptorank.io/?ysclid=luo1098dvl570589879')
Price_eth = Ethereum.getPrice('sc-50f3633f-0 sc-458805bb-0 duSxXy jBmRfF sc-77da7dd7-4 fhPlWm')
Change_eth = Ethereum.getChangePrice('sc-50f3633f-0 sc-92cddc74-0 glCbMx iksbwa')
Market_Cup_eth = Ethereum.getMarketCup('sc-67ec7576-0 bwSdbV sc-ebc32dcf-0 bZbfEj')


cryptocurrency = {'Bitcoin' : [Price_btc, Change_btc, Market_Cup_btc], 'Ethereum' : [Price_eth, Change_eth, Market_Cup_eth] }


