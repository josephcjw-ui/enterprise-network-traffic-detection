# 企业网络安全流量检测模型设计

## 项目简介
本项目基于 CICIDS-2017 网络流量数据集，设计了一个基于规则的流量过滤模型，用于识别企业网络环境中的异常攻击流量。

该项目重点分析了不同攻击流量的统计特征，并尝试使用可解释的规则模型识别以下攻击类型：

- DoS / DDoS
- PortScan
- BruteForce
- Benign（正常流量）

## 项目目标
- 分析网络流量的关键统计特征
- 设计可解释的规则型攻击检测模型
- 评估模型的 Accuracy、Precision、Recall
- 从企业视角分析误报和漏报带来的商业风险

## 数据集
- Dataset: CICIDS-2017
- Sample Size: 500,000 network flow records
- Features: numerical traffic statistics only

## 技术栈
- Python
- Pandas
- NumPy
- Rule-Based Filtering Model
- Cybersecurity Traffic Analysis

## 项目内容
1. 网络流量特征分析
2. 攻击类型差异比较
3. 规则过滤模型设计
4. 模型性能评估
5. 商业风险与成本收益分析
6. 企业部署思考

## 项目亮点
- 使用可解释规则模型进行流量攻击识别
- 将技术分析与企业商业风险结合
- 兼顾网络安全工程思路与数据分析方法

## 作者
Zicheng Wang
