import pandas as pd
import matplotlib as mpl
from ydata_profiling import ProfileReport


data = pd.read_parquet('z.parquet')

profile = ProfileReport(df=data)

# import matplotlib.font_manager
# font_list = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
# print([matplotlib.font_manager.FontProperties(fname=font).get_name() for font in font_list])


profile.to_file('z.html')