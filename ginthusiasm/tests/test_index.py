from django.test import TestCase, Client, override_settings


@override_settings(SECURE_SSL_REDIRECT=False)
class IndexTextCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_uses_widget_templates(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, 'ginthusiasm/feature_search_widget.html', "Index uses feature search")
        self.assertTemplateUsed(response, 'ginthusiasm/gin_month_widget.html', "Index uses gin of the month")
        self.assertTemplateUsed(response, 'ginthusiasm/trending_widget.html', "Index uses trending widget")
        self.assertTemplateUsed(response, 'ginthusiasm/collection_highlights_widget.html',
                                "Index uses collection highlights")
