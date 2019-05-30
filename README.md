# machine-learning
Gaussian Processes Regression (GPR), [theory, conclusion](https://github.com/suzyi/machine-learning/blob/master/GPR.pdf)

Reservoir Computing, to understand training process see [jujuba's article](http://jujuba.me/articles/reservoir_computing.html). History, papers recommendation, practical coding and demo demenstration see [minds-esnresearch](http://minds.jacobs-university.de/research/esnresearch/).
## Machine Learning Basics
data preprocessing, some tricks

| Date(2019) | |
|---| ----- |
| May 9 | [training-using-batchsize-data.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/training-using-batchsize-data.ipynb) |
| Apr 24 | [kernel density,mean and variance estimation.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebook/pdf-and-expectation-and-variance-estimation.ipynb) |
## Data

**Time Series**
PDE - Partical Differential Equation

ODE - Ordinary Differential Equation

| Date(2019) | System | Generator | Characteristic |
|---| ----- | -------- | ---------- |
| May 13 | Crime data | [CHI and LA crime data](https://data.cityofchicago.org/) | Wang, Bao, et al. "Graph-Based Deep Modeling and Real Time Forecasting of Sparse Spatio-Temporal Data." arXiv preprint arXiv:1804.00684 (2018). |
| May 13 | Weather data | [underground data base](https://www.wunderground.com/) | Wang, Bao, et al. "Graph-Based Deep Modeling and Real Time Forecasting of Sparse Spatio-Temporal Data." arXiv preprint arXiv:1804.00684 (2018). |
| May 13 | climate data | [US Historical Climatology Network](https://cdiac.ess-dive.lbl.gov/ftp/ushcn_daily/) | Yu, Rose, et al. "Long-term forecasting using tensor-train rnns." arXiv preprint arXiv:1711.00073 (2017). |
| May 13 | traffic data | [US LA County highway network](http://pems.dot.ca.gov/) | Yu, Rose, et al. "Long-term forecasting using tensor-train rnns." arXiv preprint arXiv:1711.00073 (2017). |
| May 13 | Iberian Electricity Price | [smartwatt-competition](http://complatt.smartwatt.net/#/public/home) |
| May 13 | CBOE Volatility Index | [yahoo-finance-vix](https://ca.finance.yahoo.com/quote/%5EVIX/history?p=^VIX) |
| May 13 | Tesla | [yahoo-finance-tsla](https://finance.yahoo.com/quote/TSLA/history?p=TSLA) |
| May 7 | kuramoto sivashinsky | [KS.mat](https://github.com/suzyi/Gaussian-process-regression/blob/master/data/KS.mat) | chaos, PDE |
| Apr 16 | Lorenz | [Lorenz.ipynb](https://github.com/suzyi/python/blob/master/notebook/Lorenz.ipynb) | chaos, ODE |

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
