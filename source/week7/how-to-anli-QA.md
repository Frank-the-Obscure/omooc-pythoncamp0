# 如何推广一个项目-QA by 大妈
---
## 目标-export

- 成员
- 影响力
- 领导力

为了实现目标，我们需要进行：

## 项目描述-process

- 5W1H
- 好不好
  - 能否成功
  - 是否有用
- 行不行
  - 自信
  - 学习能力
  - 对其它人的信任
- 是否有趣
  - 一个抽象但核心的判断标准，也许是一个 package...

作为项目提出人，本着`谁提出，谁执行`的原则，需要进行的准备：

## 优秀项目应具备的准备-input

- [5W1H](http://en.wikipedia.org/wiki/Five_Ws)
  - Who did that?
  - What happened?
  - Where did it take place?
  - When did it take place?
  - Why did that happen?
  - How did it happen?
  - 这些都是有必要明确的

- 项目发起人
  - 能力
  - 完成项目的意愿
  - 计划
  - for me: talk is cheap/诚意口说无凭：要用自己的实际行动表现诚意
    - 如相对完善的项目计划书
    - 相对长的项目工作时间

- Fun
  - 如何得趣？
  - for me: 有时陷入工程化的崇拜，重点放在了如何分解项目进行实现，忽视了乐趣
    - 当然一方面，分解和实现的过程对我而言就是乐趣的一部分，并非无趣
    - 但项目本身的乐趣何在值得考虑。一个有趣的项目一定会吸引更多人的参与

- 重复！！！
  - 诚意要通过行动来体现：重复的行动是最有力的表现
  - 例子是阳老荐书/推广快速写作

- 渠道
  - mailling list
  - wechat
  - GTM
  - gitbook
  - phone
  - cafe
  - weibo
  - twitter
  - ...

否定之否定：

- 这里的项目计划用不断迭代的策略为好，不必试图一次拿出一个完美版。
- 拿出草稿，和大家讨论，迭代升级草稿
- 目标是一个好的项目，而不是证明自己或是什么其它奇怪的目标
  - 避免自己陷入无意义的争吵
  - 不怕拿出漏洞百出的项目计划
  - 乐于接受所有人提出意见：这是迭代的最好机会；一个人的想法总会不全面
  - 把行动用在**真正的目标**之上

---

## QA

1. 开发 app 应该用什么工具?
  - iOS 和 android 都有自己的开发语言, python 并不一定适合
  - 如果没有很长时间投入,建议直接开发手机访问的 web app
  - 手机浏览器已经很强大, web app 用 python 开发就方便很多
2. 开发 website 用什么工具?
  - Django/flask > bottle
  - 前两者大而全, bottle 相对精简
3. 爬虫工具如何选择, Scrapy 如何?
  - Scrapy 是一个大而全的爬虫框架
  - 大而全同时常常意味着学习成本提高
  - 针对自己的实际需求,适当选择为上
  - 后续: 42 分钟以内没有希望整个 demo 运行起来的,证明不适合当下的自己
4. 一休 这种微信记录号如何实现,使用了哪些工具?
  - 可从实现方式思考
  - 一休需要一部在线的 android 手机, root 过后可以直接访问文件
  - 访问微信数据库即可
  - 测试发现微信数据用 sqlite 保存
  - 提取相关内容即可发布
5. 如何模拟鼠标键盘操作
  - 工程上常用专门工具进行模拟测试
  - (我的本意是问,如果无法用网页访问,只好模拟鼠标点击按钮过程,py 有什么相关功能...不过这个提问一点也不艺术,还是问 google 吧...)
6. 后台的选择？需要SAE？
  - 见视频