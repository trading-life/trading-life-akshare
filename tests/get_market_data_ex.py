from xtquant import xtdata
res = xtdata.get_sector_list()
print(res)
res = xtdata.get_stock_list_in_sector('上证A股')
print(res)
res = xtdata.get_stock_list_in_sector('深证A股')
print(res)
res = xtdata.get_stock_list_in_sector('京市A股')
print(res)
res = xtdata.get_stock_list_in_sector('沪深A股')
print(res)
