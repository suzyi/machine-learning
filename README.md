# machine-learning
Gaussian Processes Regression (GPR), [theory, conclusion](https://github.com/suzyi/machine-learning/blob/master/GPR.pdf)

Reservoir Computing, to understand training process see [jujuba's article](http://jujuba.me/articles/reservoir_computing.html). History, papers recommendation, practical coding and demo demenstration see [minds-esnresearch](http://minds.jacobs-university.de/research/esnresearch/).
## Programming Basics

| Date | codes |
|---| ----- |
| Jul 2, 2019 | [subplot-subplots-curve-surface-colorbar.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/subplot-subplots-curve-surface-colorbar.ipynb) |
| Jul 2, 2019 | [function-class.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/function-class.ipynb) |

## Machine Learning Basics
data preprocessing, some tricks

| Date | codes |
|---| ----- |
| Jun 14, 2019 | [training-using-batchsize-data.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/training-using-batchsize-data.ipynb) |
| Apr 24, 2019 | [kernel density,mean and variance estimation.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/pdf-and-expectation-and-variance-estimation.ipynb) |
## Data

**Time Series**
PDE - Partical Differential Equation

ODE - Ordinary Differential Equation

| Date | Generator | paper |
|---| ----- | ---------- |
| Jul 5, 2019  | [Bilingual Sentence Pairs](http://www.manythings.org/anki/) | |
| Jul 5, 2019  | [wikipedia web page traffic-kaggle](https://www.kaggle.com/c/web-traffic-time-series-forecasting/data) | [1st place solution: seq2seq](https://github.com/Arturus/kaggle-web-traffic) |
| Jun 27, 2019 | [twoSolitonKdV.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/KdV-2-soliton-solution.ipynb) |  |
| May 13, 2019 | [CHI and LA crime data](https://data.cityofchicago.org/) | Graph-Based Deep Modeling and Real Time Forecasting of Sparse Spatio-Temporal Data |
| May 13, 2019 | [underground Weather data](https://www.wunderground.com/) | Graph-Based Deep Modeling and Real Time Forecasting of Sparse Spatio-Temporal Data　|
| May 13, 2019 | [US Historical Climatology Network](https://cdiac.ess-dive.lbl.gov/ftp/ushcn_daily/) | Long-term forecasting using tensor-train rnns|
| May 13, 2019 | [US LA County highway network](http://pems.dot.ca.gov/) | Long-term forecasting using tensor-train rnns |
| May 13, 2019 | [Iberian Electricity Price-smartwatt-competition](http://complatt.smartwatt.net/#/public/home) |
| May 13, 2019 | [yahoo-finance-vix](https://ca.finance.yahoo.com/quote/%5EVIX/history?p=^VIX) |
| May 13, 2019 | [yahoo-finance-tsla](https://finance.yahoo.com/quote/TSLA/history?p=TSLA) |
| May 7, 2019 | [KS.mat](https://github.com/suzyi/Gaussian-process-regression/blob/master/data/KS.mat) | chaos, PDE |
| Apr 16, 2019 | [Lorenz.ipynb](https://github.com/suzyi/python/blob/master/notebook/Lorenz.ipynb) | chaos, ODE |

| Date(2018) | System | Generator | Characteristic |
|---| ----- | -------- | ---------- |
| Apr 16 | Duffing system | [duffing.ipynb](https://github.com/suzyi/python/blob/master/notebook/duffing.ipynb) | ODE |


## Prediction Models and Codes
MISO - Multi-Input Single-Output

SISO - Single-Input Single-Output

| Date(2019) | Model | code |
|---| ----- | ---------- |
|　 | Koopman Theory | to-do |
| May 7 | GAN | |
| May 7 | resnet | |
| May 14 | Embedding theorem | [Embedding theorem for time series analysis](https://github.com/suzyi/Embedding-theorem) | to-do |
|Apr 29 | GPR-parallel, but doesn't reduce training time | [GPR-multiple-CPUs](https://github.com/suzyi/Gaussian-process-regression/tree/master/examples) |
| Apr 16 | RNN | repo: [Recurrent Neural Network](https://github.com/suzyi/recurrent-neural-network) |
| Apr 16 | [Gaussian Processes Regression](https://github.com/suzyi/machine-learning/blob/master/document/GPR.pdf).pdf  | [GPR-1D-demo.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/GPR-1D-demo.ipynb) |

## How to Set/Decide the Parameters of a Neural Network?
If the training process of Neural Network is completed in just about 3 epochs and the training error drops quickly, like 
<p align="center">
  <img src="http://suzyi.github.io/images/overfitting-training-curve.png", alt="sturcture of a lstm unit", width=500px>
</p>
then in most cases it means your model is too deep or too wide (thus too powerful) and you'd better decrease the width or depth.
