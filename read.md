1、创建设备联动的想法
    设备联动的流程为：
        （1）先选择条件，再选择动作
        （2）先选择设备，再选择设备状态
        （3）存在用途的开关类：开关1，开关2，开关3：所以在设备进行用途设备设置的时候，
            将用途开关的名字与联动是开关的名字进行关联，便于联动过后进行设备定位，查看设备的状态
    触发一些设备的方法：
        （1）通过登录dashboard去设置设备的状态来触发设备联动，触发之后再进行设备的状态的查看验证
     设备的状态：
        （1）可以通过设备的文档获取
        （2）先将状态存放在文档中，再进行读取，设置状态

2、对于设备状态的获取：
    （1）单控开关或者用途开关：通过开关按钮相对于屏幕中间的x坐标的大小判断
    （2）其他设备：是否可以获取到H5页面的源码，通过源码中的关键字段来读取状态？？实验中……
    （3）通过接口去获取设备的状态

3、获取嵌入到App中的H5页面的源码
    （1）获取当前页面的context：driver.contexts
        如果存在H5，结果为：['NATIVE_APP', 'WEBVIEW_com.ayla.aylahome']，前面一个为原生的，后面一个为H5的
    （2）切换到H5模式：driver.switch_to.context('WEBVIEW_com.ayla.aylahome')，其中的参数为上一个结果中H5的标签
        注：出现报错：chromedriver版本不匹配
        解决：appium自己会带一个chromedriver，H5自己会有一个匹配的版本
        （1）查看H5的chrome的版本：连接手机，开启dug调试，进入App的H5页面，在chrome浏览器或者是edge浏览器中输入：
            chrome浏览器：chrom://inspect/#devices
            edge浏览器：edge://inspect/#devices
            看：WebView in com.ayla.aylahome (74.0.3729.186) 74.0.3729.186代表anroid手机中的webview版本(相当于chrome浏览器的版本)
            到：http://chromedriver.storage.googleapis.com/index.html 这个地址进行下载对应版本的chromdriver
         （2）修改appium的chromdriver的版本
            前置：替换原本的chromedriver，路径一般为：C:\Users\Administrator\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win
            既是appium desktop的目录
            进行替换后就行
            1、打开appium的服务端
            2、点击advanced
            3、下拉，找到android设置中的：Chromedriver Binary Path 设置
            4、将替换的chromedriver的路径赋值给Chromedriver Binary Path，保存后重启服务
    （3）获取到H5的源码：driver.page_source
    （4）然后根据H5定位的元素进行定位即可像定位web一样定位和操作元素
         