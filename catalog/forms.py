from django.forms import Form, CharField, IntegerField


class FilterForm(Form):
    search = CharField(required=False)


class VoteForm(Form):
    score = IntegerField(
        required=True, label="score", min_value=0, max_value=10
    )
