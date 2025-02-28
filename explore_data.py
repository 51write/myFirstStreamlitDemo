# 第八章/explore_data.py
import pandas as pd
from utils import getCurrentDir

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)
# 读取数据集，并指定字符编码为gbk，防止中文报错
penguin_df = pd.read_csv(getCurrentDir()+'\\'+'penguins-chinese.csv', encoding='gbk')

# 输出数据框的前5行
print(penguin_df.head())
