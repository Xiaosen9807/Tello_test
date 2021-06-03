#导入表格
#方法一
#%%
import pandas as pd
import xlrd
excel=xlrd.open_workbook('C://Users//Surface//Desktop//经济学查校-荷兰 - 副本.csv')
sh=excel.sheet_by_name('Sheet1')
print(sh)
print(sh.nrows)
print(sh.ncols)
print(sh.cell(0,8).value)
print(sh.row_values(0,5))
print(sh.col_values(0))
ses_list=[]
for i in range(1,sh.ncols):
    print(i)
    ses_list.append(sh.row_values(i))

#%%
table=pd.DataFrame(
    ses_list,
    columns=sh.row_values(0)
    #index=np.aarange(12)
)
print(table)

# %%
#%%
#方法二
import pandas as pd
table=pd.read_excel('C:\\Users\\Surface\\Desktop\\123.csv')
table_df=table.values
print(table,type(table))
table
#这两个参数的默认设置都是False
#pd.set_option('display.unicode.ambiguous_as_wide', True)
#pd.set_option('display.unicode.east_asian_width', True)


# %%
#导入csv
import pandas as pd
table=pd.read_csv(
    'C:\\Users\\Surface\\Desktop\\1234.csv',
    error_bad_lines=False,
    header=None,
    names=['one','two','three','four','five']
)
table_df=table.values
print(table,type(table))

#这两个参数的默认设置都是False
#pd.set_option('display.unicode.ambiguous_as_wide', True)
#pd.set_option('display.unicode.east_asian_width', True)
new_table=table.drop(columns=['one'])   #new_table是一个去掉了column的新DataFrame
print(new_table) 
table.drop(
    columns=['one'],
    inplace=True
    )                    #对自身进行修改
table
#table.to_csv('C:\\Users\\Surface\\Desktop\\5678.csv',index=False)  #写入csv

# %%
