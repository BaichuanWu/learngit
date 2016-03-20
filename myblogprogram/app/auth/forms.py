#!usr/bin/env python
# coding=utf-8
"""
author:wubaichuan

"""

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, \
    Email, Regexp, EqualTo
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])
    username = StringField('Username',
                           validators=[DataRequired(), Length(1, 64),
                                       Regexp('^[A-Za-z][A-Za-z0-9]*$',
                                              0, 'Usernames must have only\
                                              letters,numbers,dots or underscores')])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('password2',
                                                 'Passwords must match ')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already used!')


class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password',
                             validators=[DataRequired(),
                                         EqualTo('password2',
                                                 'password must math')])
    password2 = PasswordField('Comfirm your password', validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[DataRequired(),
                                             Length(1, 64),
                                             Email()])
    password = PasswordField('New password',
                             validators=[DataRequired(),
                                         EqualTo('password2',
                                                 'password must math')])
    password2 = PasswordField('Comfirm your password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')

    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).first() is None:
    #         raise ValidationError('Unknown email address')
