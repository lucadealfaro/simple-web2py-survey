# coding: utf8

import datetime

db.define_table('question',
    Field('author', db.auth_user, default=auth.user_id),
    Field('creation_date', 'datetime', default=datetime.datetime.utcnow()),
    Field('code', 'string'),
    Field('title', 'string'),
    Field('text', 'text', required=True),
    )

db.define_table('answer',
    Field('author', db.auth_user, default=auth.user_id),
    Field('creation_date', 'datetime', default=datetime.datetime.utcnow()),
    Field('question', db.question),
    Field('text', 'text', required=True),
    )
    
db.define_table('feedback',
    Field('author', db.auth_user, default=auth.user_id),
    Field('creation_date', 'datetime', default=datetime.datetime.utcnow()),
    Field('answer', db.answer),
    Field('text', 'text', required=True),
    )

db.question.author.writable = False
db.answer.author.readable = db.answer.author.writable = False
db.feedback.author.writable = False

db.question.creation_date.writable = False
db.answer.creation_date.writable = False
db.feedback.creation_date.writable = False

professor = "Luca"
