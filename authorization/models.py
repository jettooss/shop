from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

user = get_user_model()
name = get_user_model()

