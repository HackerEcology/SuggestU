SuggestU
========

A Generic Suggestion Engine for 'all things online'.

* Coming soon..

![SuggestU](https://raw.githubusercontent.com/HackerEcology/SuggestU/master/docs/suggestu.png)

## Installation Steps

- First, Refer to /HackerEcology/qrator for dependencies and initial requirements.

- Install devel packs:
  - On Fedora/RHEL: ```# yum install libxslt-devel python-devel```
    - On Ubuntu: ```# apt-get install libxml2-dev libxslt1-dev python-dev```

- Install pip and virtualenv ```# yum/apt-get install python-pip; pip install virtualenv```

- Go to project root and run:

  ```# virtualenv venv```

  - Append these lines to ```./venv/bin/activate```:

    ```
    export HE_USER='arco'
    export HE_PASS='1234'
    export HE_DB='jugad'
    export DJANGO_SECRET='#@$#%^refdsdgUDRDFhy45766*DGGR&^REfSDG'
    ```

  - Note: Change your secret key here, to a long random set of characters.
    
  - Then from project root, run: ```# sourve venv/bin/activate```


- Install requirements: ```$ pip install -r requirements.txt```

- Go to ```<project root>/suggestu/``` and run:
  ```./manage.py syncdb``` (say no to auth system question for now)

- Then from the same directory, run: ```./manage.py runserver```
