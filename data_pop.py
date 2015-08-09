from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from database_setup import Base, Catalog, CatalogItem, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()

#nitem = Catalog(catagory = "Climbing")
#session.add(nitem)
#session.commit()

#xitem = User(name = 'skis', email = 'skis@skis.com', picture = 'picture.jpg')
#session.add(xitem)
#session.commit()

dogs = session.query(User).all()
for dog in dogs:
    print dog.name
#print items
