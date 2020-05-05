# machine-learning
+ May 5, 2020. Ensemble learning-adaboost, theory, [code-example](https://github.com/suzyi/machine-learning/blob/master/document/adaboost_code.txt)
+ May 3, 2020. Descent method, including gradient descent method and Newton's method, [theory](https://github.com/suzyi/machine-learning/blob/master/document/descent-method.pdf).
+ May 2, 2020. Intro-to-classification, [theory](https://github.com/suzyi/machine-learning/blob/master/document/intro-to-classification.pdf).
+ May 2, 2020. Support Machine Vector, [theory](https://github.com/suzyi/machine-learning/blob/master/document/SVM.pdf).
+ Mar 26, 2020. Logistic Regression, [theory](https://github.com/suzyi/machine-learning/blob/master/document/logistic-reg.pdf).
+ Apr 23, 2019. Gaussian Processes Regression (GPR), [theory, conclusion](https://github.com/suzyi/machine-learning/blob/master/document/GPR.pdf).
+ Reservoir Computing, to understand training process see [jujuba's article](http://jujuba.me/articles/reservoir_computing.html). History, papers recommendation, practical coding and demo demenstration see [minds-esnresearch](http://minds.jacobs-university.de/research/esnresearch/).
## Programming Basics

| Date | codes |
|---| ----- |
| Jul 2, 2019 | [subplot-subplots-curve-surface-colorbar.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/subplot-subplots-curve-surface-colorbar.ipynb) |
| Jul 2, 2019 | [function-class.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/function-class.ipynb) |

## Machine Learning Basics
data preprocessing, some tricks

| Date | codes |
|---| ----- |
| Sep 25, 2019 | [periodic_condition.ipynb](https://github.com/suzyi/machine-learning/blob/master/notebooks/periodic_condition.ipynb) |
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
```
List = [predict_error, enc_steps, dec_steps, latent_dim, num_discard, num_train, num_test, batch_sz, num_iter, time_cost, activate_units, npseed, q, l]
Name = 'predict_error, enc_steps, dec_steps, latent_dim, num_discard,num_train, num_test, batch_sz, num_iter, time_cost, activate_units, npseed, q, l\n'
f = open('KdV-seq2seq-training-process.csv','a')
# f.write(Name)
for i in List:
    f.write('{},'.format(str(i)))
f.write('\n')
f.close()
```
+ Generally, there are two types of parameters. The first kind are those parameters related to the selection of features and labels, like input and output dimension. The second kind are parameters of the model, like width and depth of a neural network. During the process of finding better parameters, adjust the second kind while keeping the first kind fixed is a good strategy.
+ If the training process of Neural Network is completed in just about 3 epochs and the training error drops quickly, like 
<p align="center">
  <img src="http://suzyi.github.io/images/overfitting-training-curve.png", alt="sturcture of a lstm unit", width=500px>
</p>
then in most cases it means your model is too deep or too wide (thus too powerful) and you'd better decrease the width or depth.

## Make Model Reproduceable
### Make Model Built using Tensorflow
No matter GPU is enabled or not, add the following piece of code at the start of your code so that it is reproduceable.
```
import tensorflow as tf
sd = 1
tf.reset_default_graph()
sess = tf.InteractiveSession()
tf.set_random_seed(seed = sd)
```
### Make the Model Built using Keras with Tensorflow as Backend Reproduceable
When you're using Keras with Tensorflow as backend, you'll find it is very hard to make the result reproduceable, especially when GPU is enabled. However, here we still have a solution. First, disable GPU.
```
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = ""
```
Second, seed those libraries which are included in your code, say "tensorflow, numpy, random".
```
import tensorflow as tf
import numpy as np
import random as rn

sd = 1 # Here sd means seed.
np.random.seed(sd)
rn.seed(sd)
os.environ['PYTHONHASHSEED']=str(sd)

from keras import backend as K
config = tf.ConfigProto(intra_op_parallelism_threads=1,inter_op_parallelism_threads=1)
tf.set_random_seed(sd)
sess = tf.Session(graph=tf.get_default_graph(), config=config)
K.set_session(sess)
```
Make sure these two pieces of code are included at the start of your code, then the result will be reproducible.
