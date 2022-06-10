from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from .validators import validar_gt_0, validar_lt_10
from django.contrib.auth.models import User


class Author(models.Model):
    """
    Modelo que representa un autor
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    # def get_absolute_url(self):
    #     """
    #     Retorna la url para acceder a una instancia particular de un autor.
    #     """
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Book(models.Model):
    """
    Modelo que representa un libro (pero no un Ejemplar específico).
    """

    isbn = models.CharField(
            'ISBN',
            max_length=13,
            help_text='13 Caracteres <a href='
            '"https://www.isbn-international.org/content/what-isbn"'
            '>ISBN number</a>'
        )

    title = models.CharField(max_length=200)

    author = models.ManyToManyField(
            Author,
            help_text="Seleccione un autor para este libro"
        )

    price = models.DecimalField(
            default=0,
            decimal_places=2,
            max_digits=8,
            validators=[validar_gt_0]
        )

    path_to_cover_image = models.CharField(max_length=200, null=True)

    number_copies_stock = models.IntegerField(
            default=0,
            validators=[validar_gt_0]
        )

    date = models.DateTimeField(default=timezone.now())

    slug = models.SlugField(unique=True, null=True)

    score = models.DecimalField(
            default=None,
            decimal_places=2,
            max_digits=4,
            validators=[validar_gt_0, validar_lt_10],
            null=True
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(
                (self.title, self.date.strftime("%d-%b-%Y-%H-%M-%S"))
            )

        if len(self.votes.all()) > 0:
            num = len(self.votes.all())
            
            media = 0

            for vote in self.votes.all():
                media += vote.score
            self.score = media / num

        super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.title

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('detail', kwargs={'slug': self.slug})

    # def display_genre(self):
    #     """
    #     Creates a string for the Genre.
    #     """
    #     return ', '.join([genre.name for genre in self.genre.all()[:3]])


# class UserProfile(models.Model):

#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


class Comment(models.Model):

    msg = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['date']



    # def get_absolute_url(self):
    #     """
    #     Retorna la url para acceder a una instancia particular de un autor.
    #     """
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s-%s, %s' % (
                self.user.username,
                self.book.title,
                self.date.strftime("%d-%b-%Y (%H:%M:%S)")
            )

class Vote(models.Model):

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0, validators=[validar_gt_0, validar_lt_10])


    class Meta:
        ordering = ['book', 'user', 'score']

    def save(self, *args, **kwargs):

        if self.score < 0 or self.score >10:
            raise ValueError

        try:
            Vote.objects.get(book=self.book, user=self.user).delete()
        except:
            print("No existe voto")

        super(Vote, self).save(*args, **kwargs)
        self.book.save()

    # def get_absolute_url(self):
    #     """
    #     Retorna la url para acceder a una instancia particular de un autor.
    #     """
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s-%s, %s' % (
                self.user.username,
                self.book.title,
                self.score
            )
