FROM python:3

COPY requirements.txt /

COPY src/ /dist/
#ADD config/ /config/ comentado para passar no teste do TravisCI

RUN pip install -r requirements.txt
CMD ["python","/dist/bot.py"]
