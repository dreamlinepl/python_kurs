# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 18:46:17 2022

@author: Marcin
"""

import copy


stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.copy(stocks)

stocks[0][1] = 'CRJ'

print(f'stocks: {stocks}')
print(f'stocks_copied: {stocks_copied}')

#%%

stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.deepcopy(stocks)

stocks[0][1] = 'CRJ'

print(f'stocks: {stocks}')
print(f'stocks_copied: {stocks_copied}')