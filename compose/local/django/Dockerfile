FROM python:3.9

ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=$HOME/web

RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/uploads

ENV CHROMEDRIVER_VERSION 2.19
ENV CHROMEDRIVER_DIR /usr/bin/chromedriver
RUN mkdir $CHROMEDRIVER_DIR
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
ENV PATH $CHROMEDRIVER_DIR:$PATH

ADD back/requirements/base.txt $APP_HOME
ADD back/requirements/local.txt $APP_HOME

RUN pip install -U pip
RUN pip install -r $APP_HOME/local.txt

ADD ./back $APP_HOME
WORKDIR $APP_HOME


CMD ["bash"]