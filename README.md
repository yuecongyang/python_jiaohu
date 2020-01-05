<div align="center">
  <h1>Python与交互式数据可视化-技术文档之总结说明</h1>
</div>

### :sun_with_face:**个人信息**：
* 姓名：杨悦聪
* 班级：网新3班
* 学号：181013078  

### :link:**python项目查看**：
* [GitHub_URL](https://github.com/yuecongyang/python_jiaohu)
* [pythonanywhere个人部署URL](http://zerow.pythonanywhere.com)  

### :thought_balloon:项目主要URL及功能如下：  

    /entry 首页 展示三个跳转按钮  

    /renkou 展示抚养比与人口自然增长率的对比分析

    /shiye 展示失业率与抚养比的对比分析

    /beijing 展示北京市居民消费水平与抚养比的对比分析 

### :heavy_check_mark:**数据传递描述**：  

#### HTML档描述：
1.**布局**：用link标签连接到hf.css，奠定基本格式。

2.**图表**：用h1标签充当空格，使图表之间有一定距离，不会太过拥挤。

3.**html与python文档的交互体现**：在html页面设置一个空的图表容器{{ the_res|safe }}，通过后端py文件进行对应可视化函数传输数据给三个html页面一个提交按钮，提交时图表数据会提交到相对应的页面。通过function标签实现页面跳转连接。

#### python档描述：  

1.**主要运用的模块**：pandas、flask、cufflinks、plotly       


2.**具体操作**：  
首先每一个视图函数都要用pandas模块pd.read_csv（）读取每个表对应的csv文件数据，然后用cufflinks和plotly模块清理数据。

用@app.route(路由规则) 的方式绑定可视化视图函数, route() 会告诉告诉 Flask 什么样的URL 能触发我们的函数，就像项目里的@app.route('/entry')。  
用with和open标签连接17级交互图表的html，用title标签定义名称。最后return render_template会根据后面传入的参数，对html进行修改渲染。  

#### webapp动作描述：  

**提交按钮**：项目启动后显示的主页面有三个提交按钮，分别对应的是抚养比与人口自然增长率的对比分析/失业率与抚养比的对比分析/北京市居民消费水平与抚养比的对比分析这三个图表。通过点击可以跳转到相应的图表。  三个页面打开后左上角有一个按钮“首页”，点击可以返回首页。

  
