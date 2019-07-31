# tensorflow2.0_tutorial

## 1. Install
     * 1. if you already have a conda environment for tensorflow-gpu >= 1.13, then you can just clone this enviroment for using tensorflow-gpu2.0.
      * 1. `conda create --name [name of your new environment] --clone [name of your current environment]`
      * 2. `pip install tensorflow-gpu==2.0.0-beta0`
      * [Trouble shooting]: It will probably raise an error `Cannot uninstall 'wrapt'.` Try the following steps:
        * `pip install -U --ignore-installed wrapt enum34 simplejson netaddr`
        * `pip install tensorflow==2.0.0-beta0 --user`
      * 3. Test GPU usage.
        * `import tensorflow as tf`
        * `tf.__version__`
        * `tf.test.is_gpu_available()`
     * 2. Assuming you do not have cudatoolkit 10 cudnn 7.6.0 build in your environment. Try the following step (not test yet).
      * 1. `conda install cudatoolkit==10.0.130`
      * 2. `conda install cudnn==7.6.0`
