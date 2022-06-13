# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data
# (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from catalog.models import (Author, Book, Comment, Vote)
from orders.models import (OrderItem, Order)
from django.contrib.auth.models import User
from faker import Faker
# define STATIC_PATH in settings.py
from bookshop.settings import STATIC_PATH
from PIL import Image, ImageDraw, ImageFont
from django.contrib.auth.hashers import make_password
from random import randrange


FONTDIR = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        self.NUMBERUSERS = 7
        self.NUMBERBOOKS = 7
        self.NUMBERAUTHORS = 6
        self.MAXAUTHORSPERBOOK = 3
        self.NUMBERCOMMENTS = self.NUMBERBOOKS * 5
        self.MAXCOPIESSTOCK = 30
        self.cleanDataBase()   # clean database
        # The faker.Faker() creates and initializes a faker generator,
        self.faker = Faker()
        self.user()
        self.author()
        self.book()
        self.comment()
        self.vote()
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here

    def cleanDataBase(self):
        User.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()
        Comment.objects.all().delete()
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        Vote.objects.all().delete()

    def user(self):

        userD = {}

        userD[1] = {'id': 100,
                    'username': 'pikachu123',
                    'password': 'contraseña123', }
        userD[2] = {'id': 101,
                    'username': 'usuario000',
                    'password': 'contraseña123', }
        userD[3] = {'id': 102,
                    'username': 'puerco43',
                    'password': 'contraseña123', }
        userD[4] = {'id': 103,
                    'username': 'elrubius',
                    'password': 'contraseña123', }
        userD[5] = {'id': 104,
                    'username': 'ibai',
                    'password': 'contraseña123', }
        userD[6] = {'id': 105,
                    'username': 'elxokas',
                    'password': 'contraseña123', }
        userD[7] = {'id': 106,
                    'username': 'elpepe',
                    'password': 'contraseña123', }

        for index, a in enumerate(userD.values()):
            x = User.objects.get_or_create(
                id=a['id'],
                username=a['username'],
                password=make_password(a['password'])
            )[0]
            x.save()

    def author(self):

        authorD = {}

        authorD[1] = {'id': 101,
                      'first_name': 'Mario',
                      'last_name': 'Alonso', }
        authorD[2] = {'id': 102,
                      'first_name': 'Alejandro',
                      'last_name': 'De Los Rios', }
        authorD[3] = {'id': 103,
                      'first_name': 'Thomas',
                      'last_name': 'Shelby', }
        authorD[4] = {'id': 104,
                      'first_name': 'Roberto',
                      'last_name': 'Latorre', }
        authorD[5] = {'id': 105,
                      'first_name': 'Fernando',
                      'last_name': 'Rodríguez', }
        authorD[6] = {'id': 106,
                      'first_name': 'Jose',
                      'last_name': 'García', }

        for index, a in enumerate(authorD.values()):
            x = Author.objects.get_or_create(
                id=a['id'],
                first_name=a['first_name'],
                last_name=a['last_name']
            )[0]
            x.save()

    def cover(self, book):
        """create fake cover image.
           This function creates a very basic cover
           that show (partially),
           the primary key, title and author name"""

        img = Image.new('RGB', (200, 300), color=(73, 109, 137))
        # your font directory may be different
        fnt = ImageFont.truetype(
            self.font,
            28, encoding="unic")
        d = ImageDraw.Draw(img)
        d.text((10, 100), "PK %05d" % book.id, font=fnt, fill=(255, 255, 0))
        d.text((20, 150), book.title[:15], font=fnt, fill=(255, 255, 0))
        d.text((20, 200), "By %s" % str(
            book.author.all()[0])[:15], font=fnt, fill=(255, 255, 0))
        img.save(os.path.join(STATIC_PATH, book.path_to_cover_image))

    def book(self):

        bookD = {}

        bookD[1] = {'id': 101,
                    'isbn': '123456789120',
                    'title': 'Robot',
                    'author': 102,
                    'price': 10,
                    'path_to_cover_image': 'portada1.png',
                    'number_copies_stock': 3,
                    'score': 4}
        bookD[2] = {'id': 102,
                    'isbn': '123456789121',
                    'title': '1984',
                    'author': 102,
                    'price': 12,
                    'path_to_cover_image': 'portada2.png',
                    'number_copies_stock': 8,
                    'score': 10}
        bookD[3] = {'id': 103,
                    'isbn': '123456789122',
                    'title': 'Don Quijote',
                    'author': 101,
                    'price': 8,
                    'path_to_cover_image': 'portada3.png',
                    'number_copies_stock': 10,
                    'score': 8}
        bookD[4] = {'id': 104,
                    'isbn': '123456789123',
                    'title': 'El misterio',
                    'author': 104,
                    'price': 9.99,
                    'path_to_cover_image': 'portada4.png',
                    'number_copies_stock': 1,
                    'score': 3}
        bookD[5] = {'id': 105,
                    'isbn': '123456789124',
                    'title': 'Asesinato',
                    'author': 105,
                    'price': 14,
                    'path_to_cover_image': 'portada5.png',
                    'number_copies_stock': 3,
                    'score': 6}
        bookD[6] = {'id': 106,
                    'isbn': '123456789125',
                    'title': 'Recetas de cocina',
                    'author': 102,
                    'price': 25,
                    'path_to_cover_image': 'portada6.png',
                    'number_copies_stock': 17,
                    'score': 8}
        bookD[7] = {'id': 107,
                    'isbn': '123456789126',
                    'title': 'Harry Potter',
                    'author': 101,
                    'price': 40,
                    'path_to_cover_image': 'portada7.png',
                    'number_copies_stock': 34,
                    'score': 10}

        for index, a in enumerate(bookD.values()):
            authorInst = Author.objects.get(id=int(a['author']))
            x = Book.objects.get_or_create(
                id=a['id'],
                isbn=a['isbn'],
                title=a['title'],
                price=a['price'],
                path_to_cover_image=a['path_to_cover_image'],
                number_copies_stock=a['number_copies_stock'],
            )[0]
            x.save()
            x.author.add(authorInst)
            self.cover(x)
            x.save()

    def comment(self):

        commentD = {}

        commentD[1] = {'id': 101,
                       'book': 101,
                       'user': 100, }
        commentD[2] = {'id': 102,
                       'book': 102,
                       'user': 101, }
        commentD[3] = {'id': 103,
                       'book': 103,
                       'user': 105, }
        commentD[4] = {'id': 104,
                       'book': 104,
                       'user': 102, }
        commentD[5] = {'id': 105,
                       'book': 105,
                       'user': 103, }

        for index, a in enumerate(commentD.values()):
            x = Comment.objects.get_or_create(
                id=a['id'],
                msg=self.faker.text(),
                book=Book.objects.get(id=int(a['book'])),
                user=User.objects.get(id=int(a['user']))
            )[0]
            x.save()

    def vote(self):

        voteD = {}

        for i in range(100):

            voteD[i] = {
                'book': randrange(7)+101,
                'user': randrange(7)+100,
                'score': randrange(11)
            }

        for index, a in enumerate(voteD.values()):
            x = Vote.objects.get_or_create(
                score=a['score'],
                book=Book.objects.get(id=int(a['book'])),
                user=User.objects.get(id=int(a['user']))
            )[0]
            x.save()
