from haystack import indexes
from ginthusiasm.models import Distillery, Gin


class GinIndex(indexes.SearchIndex, indexes.Indexable):
    # Template links to gin_text.txt which tells haystack which fields to include
    # in the keyword search
    text = indexes.CharField(document=True, use_template=True)

    # This field is used for autocompleting based on the gin name
    content_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Gin

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class DistilleryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # This field is used for autocompleting based on the gin name
    distillery_auto = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Distillery

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
