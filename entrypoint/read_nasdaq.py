from data_fetcher import yf_reader


df = yf_reader.get_nasdaq_100_components("/home/pb/python.codes/pre_factor/datas/nasdaq-100-components.txt")[['Symbol', 'Name']]
yf_reader.save_nasdaq_100_quotes(df, "/home/pb/python.codes/pre_factor/datas/nasdaq-100-quotes")

