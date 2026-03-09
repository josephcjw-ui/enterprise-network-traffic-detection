# 项目总结

## 研究背景
在企业网络环境中，攻击流量识别对于保障系统安全非常重要。本项目尝试设计一个基于规则的流量过滤模型，用于识别常见攻击行为。

## 核心思路
通过分析网络流量统计特征，例如：

- Flow Duration
- Flow IAT Mean
- Packet Length Mean
- Total Fwd Packets
- Total Backward Packets
- SYN Flag Count
- ACK Flag Count

构建规则模型，逐步识别不同攻击类型。

## 模型评估
使用以下指标评估模型性能：

- Accuracy
- Precision
- Recall
- Confusion Matrix

## 商业分析
除了模型准确率，本项目还讨论了：

- 误报（False Positive）对企业业务中断的影响
- 漏报（False Negative）导致的潜在安全损失
- 安全优先与业务体验之间的权衡

## 后续优化方向
- 调整阈值
- 增加更多网络流量特征
- 引入 Random Forest / XGBoost 等机器学习方法
