from .models import Vote, Book, User, Author
from .management.commands.populate import Command
from django.test import TestCase
from decimal import Decimal

from random import randrange

class VoteTests(TestCase):
    """Test that populate  has been saved data properly
       require files XXXX.pkl stored in the same directory that manage.py"""

    def setUp(self):
        self.authorDict = {
            "first_name": 'Paco',
            "last_name": 'Picapiedra',
        }
        self.bookDict = {
            "isbn": '1234567890123',
            "title": 'title_1',
            "price": Decimal(23.32),
            "path_to_cover_image": 'kk.jpg',
            "number_copies_stock": -23,
        }
        self.userDict = {
            "username": 'pmarmol',
            "password": 'troncomovil',
            "first_name": 'Pablo',
            "last_name": 'Marmol',
            "email": 'p.marmol@cantera.com',
        }
    
    def create_check(self, dictionary, ObjectClass):
        """ create an object of the class 'ObjectClass'
        using the dictionary. Then,
        check that all key-values in the
        dictionary are attributes in the object.
        return created object of class Object
        """
        # check that str function exists
        self.assertTrue(ObjectClass.__str__ is not object.__str__)
        # create object
        item = ObjectClass.objects.create(**dictionary)
        for key, value in dictionary.items():
            self.assertEqual(getattr(item, key), value)
        # execute __str__() so all the code in models.py is checked
        item.__str__()
        return item

    def test01_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        voteDict = {    "book": book,
                        "user": user,
                        "score": randrange(11)
                        }
        v1 = self.create_check(voteDict, Vote)
        self.assertEqual(user.pk, v1.user.pk)
        self.assertEqual(book.pk, v1.book.pk)

    def test02_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        voteDict = {    "book": book,
                        "user": user,
                        "score": 11
                        }
        v1=None
        try:
            v1 = self.create_check(voteDict, Vote)
        except:
            self.assertEqual(v1, None)
    
    def test03_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        voteDict = {    "book": book,
                        "user": user,
                        "score": -1
                        }
        v1=None
        try:
            v1 = self.create_check(voteDict, Vote)
        except:
            self.assertEqual(v1, None)

    def test04_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        voteDict = {    "book": book,
                        "user": user,
                        "score": randrange(11)
                        }
        v1 = self.create_check(voteDict, Vote)
        self.assertLessEqual(v1.score, 10)
        self.assertGreaterEqual(v1.score, 0)

    def test05_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        voteDict = {    "book": book,
                        "user": user,
                        "score": randrange(11)
                        }
        v1 = self.create_check(voteDict, Vote)

        userDict2 = {
            "username": 'Andiamo',
            "password": 'troncomovil',
            "first_name": 'Pablo',
            "last_name": 'Marmol',
            "email": 'p.marmol@cantera.com',
        }
        user2 = self.create_check(userDict2, User)

        voteDict2 = {    "book": book,
                        "user": user2,
                        "score": randrange(11)
                        }
        v2 = self.create_check(voteDict2, Vote)

        self.assertEqual(book.score, (v1.score+v2.score)/2)

        userDict3 = {
            "username": 'Pepe',
            "password": 'troncomovil',
            "first_name": 'Pablo',
            "last_name": 'Marmol',
            "email": 'p.marmol@cantera.com',
        }
        user3 = self.create_check(userDict3, User)

        voteDict3 = {    "book": book,
                        "user": user3,
                        "score": randrange(11)
                        }
        v3 = self.create_check(voteDict3, Vote)

        self.assertEqual(book.score, (v1.score+v2.score+v3.score)/3)

    def test06_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        
        self.assertEqual(book.score, None)

    def test07_vote(self):
        user = self.create_check(self.userDict, User)
        book = self.create_check(self.bookDict, Book)
        voteDict = {    "book": book,
                        "user": user,
                        "score": randrange(11)
                        }
        v1 = self.create_check(voteDict, Vote)


        voteDict2 = {    "book": book,
                        "user": user,
                        "score": randrange(11)
                        }
        v2 = self.create_check(voteDict2, Vote)

        self.assertEqual(book.score, v2.score)
