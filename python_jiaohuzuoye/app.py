import pandas as pd
import cufflinks as cf
import plotly as py

# 准备
df = pd.read_csv('fuyang.csv',encoding='utf8')
df1 = pd.read_csv('growth.csv',encoding='utf8')
df2 = pd.read_csv('consume.csv',encoding='utf8')
df3 = pd.read_csv('unemp.csv',encoding='utf8')

cf.set_config_file(offline=True, theme="polar")
py.offline.init_notebook_mode()

# 开始Flask框架处理
from flask import Flask, render_template, request, escape

app = Flask(__name__)


# 总表的下拉菜单 按年份（未定）
# regions_available_loaded_0 = list(df_z.年份.unique())

# 首页
@app.route('/')
@app.route('/entry', methods=['GET'])
def index():
    # 将总表以数据框形式列出
    data_str = df.to_html()
    title = '影响抚养比的因素分析'
    return render_template('entry.html',
                           the_title=title,
                           the_res=data_str
                           )


@app.route('/renkou', methods=['POST'])
def yi_yu_select_1():
    with open("./templates/fuyang1.html", encoding="utf8", mode="r") as f1:
        plot_all_1 = "".join(f1.readlines())
    the_region = request.form["the_region_selected_1"]
    print(the_region)
    title = '影响抚养比的因素分析'
    return render_template('renkou.html',
                           the_plot_all_1=plot_all_1,
                           the_title=title,
                           )


@app.route('/shiye', methods=['POST'])
def yi_yu_select_2():
    with open("./templates/fuyang2.html", encoding="utf8", mode="r") as f2:
        plot_all_2 = "".join(f2.readlines())
    the_region = request.form["the_region_selected_2"]
    print(the_region)
    title = '影响抚养比的因素分析'
    return render_template('shiye.html',
                           the_plot_all_2=plot_all_2,
                           the_title=title, )


@app.route('/beijing', methods=['POST'])
def yi_yu_select_3():
    with open("./templates/fuyang3.html", encoding="utf8", mode="r") as f3:
        plot_all_3 = "".join(f3.readlines())
    the_region = request.form["the_region_selected_3"]
    print(the_region)
    title = '影响抚养比的因素分析'
    return render_template('beijing.html',
                           the_plot_all_3=plot_all_3,
                           the_title=title, )

if __name__ == '__main__':
    app.run()
