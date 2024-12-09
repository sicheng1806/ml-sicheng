#import "style.typ": * 
#show: thmrules
#show: conf.with(
  title: "新能源电厂调度问题笔记",
)

= 问题背景与任务

新能源的电力输出高度可变并且难以控制，导致新能源发电很难整合到现有的电网中。为了促进风力发电厂和太阳能发电厂与传统电网的整合，必需解决由于发电不稳定引起的一系列问题，包括:系统均衡，储量管理和发电量调度问题。 因此需要一定的预测和管理方法帮助发电厂和研究员预测长期和短期下风速和太阳辐射。

1. 分别研究风力发电厂和太阳能发电厂的电力产能的波动模式，并在总发电量发生显著降低或增加时进行预报。
2. 预测给定数据未来1-120s每秒的发电量。 
3. 设计使用备用电机的调度方案，使得电厂在给定概率$r$下稳定。 

== 问题分析

=== 任务1

1. 任务1需要分别识别风力发电厂和太阳能发电厂的总电力厂能的波动模式。
2. 此波动模式需要可以反映出电力的显著变换
3. 波动幅度：$ k = (p - q) / q $
4. 显著增加$E_1$: $ k > t $
5. 显著减少$E_2$: $ k < -t $
6. 参考平均发电量$q$: $ q = 1/T sum_i^T p(i) $
   当$i$时刻前三十分钟的数据都为有效数据时才可行。有效指的是对于太阳辐射这种昼夜交替明显的数据，夜间没有太阳辐射，因此$q$的有效区间为具有太阳辐射半小时之后。而对于风力这种日夜都有的数据，$q$的有效区间在有记录的30分钟后至结束。 
7. 波动幅度是最重要的局部波动特征，如果可以对其进行预测那么就可以完成任务1。 

=== 编程任务1

1. 完成数据接口
2. 完成绘制接口框架
3. 完成数据变换接口框架
4. 计算k值
5. 根据t进行时间分类
6. 对value进行连续小波变换和离散小波变换

==== 要点1: 波动模式的认识和识别

==== 要点2: 模式识别的预报方法

=== 任务2

==== 要点1: 时间序列数据的特点

==== 要点2: 时间序列数据的预测方法

=== 任务3

==== 要点1: 调度问题数学模型的建立

==== 要点2: 调度问题数学模型的解决方法