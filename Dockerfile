FROM python
LABEL maintainer=Edgard_Abarcas email=elav.1995@gmail.com

COPY ./ /app

WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]