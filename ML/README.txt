Here I am trying to do some ML stuff. I am following some tutorials online on how to setup tensorflow in environment etc. 
https://www.youtube.com/watch?v=ujTCoH21GlA&ab_channel=TechWithTim
https://www.youtube.com/watch?v=KVFWKrwcXoc&ab_channel=buckmasterinstitute

So first I installed Anaconda using CLI. Then I created an environment (tensor) where I 'pip install'ed tensorflow and keras.
Then in PyCharm, either you add the new environment as interpreter or you can customize All settings - Python interpreter  - to whichever env you want. 
Now in future if you have to make conda env, just do :
$ conda create -n testenv python=3.9
$ conda activate testenv
$ ...whatever you wanna do - install, run python, make shit etc. etc. ...
$ conda deactivate



