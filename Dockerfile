FROM python:3.10.12-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the app user
RUN mkdir -p /home/appuser

# don't run as root therefore create non-root user
RUN groupadd --gid 1001 appuser && \
    useradd --uid 1001 --gid appuser --home /home/appuser appuser

# install pipenv
RUN pip install pipenv

# create the appropriate directories
ENV HOME=/home/appuser
ENV APP_HOME=/home/appuser/personalwebsite
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

COPY Pipfile Pipfile.lock $APP_HOME

RUN pipenv install --system

# Copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R appuser:appuser $APP_HOME

# change to the app user
USER appuser
