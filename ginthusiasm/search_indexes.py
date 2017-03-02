from haystack import indexes
from ginthusiasm.models import Gin

class GinIndex(indexes.SearchIndex, indexes.Indexable):
    # Template links to gin_text.txt which tells haystack which fields to include
    # in the keyword search
    text = indexes.CharField(document=True, use_template=True)

    # Add the other filterable fields to the index
    price = indexes.FloatField(model_attr='price')
    average_rating = indexes.FloatField(model_attr='average_rating')
    taste_tags = indexes.MultiValueField()
    #distillery = indexes.CharField(model_attr='distillery', null=True)

    # This field is used for autocompleting based on the gin name
    content_auto = indexes.EdgeNgramField(model_attr='name')

    def prepare_taste_tags(self, obj):
        print [tag for tag in obj.taste_tags.all()]
        return [tag for tag in obj.taste_tags.all()]

    def prepare_distillery(self, obj):
        print obj.distillery
        return obj.distillery

    def get_model(self):
        return Gin

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
