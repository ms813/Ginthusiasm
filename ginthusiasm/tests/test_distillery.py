from django.test import TestCase, Client
from django.urls import reverse

from ginthusiasm.models import Distillery


class TestDistillery(TestCase):
    def setUp(self):
        self.client = Client()

    def add_fake_distillery(self, name='TestDistillery'):
        distillery = Distillery(name=name)
        distillery.lat = 0
        distillery.long = 0
        distillery.save()
        return distillery

    def test_distillery_basic(self):
        response = self.client.get(reverse('distillery_search_results'))

        self.assertTemplateUsed('ginthusiasm/distillery_search_page.html')
        self.assertContains(response, "<div class='distillery-search-results'>")

    def test_distillery_search_widget(self):
        response = self.client.get(reverse('distillery_search_results'))

        self.assertContains(response, '<div class="distillery-search-widget">')
        self.assertContains(response, "<form id='distillery_search_form'")
        self.assertContains(response,
                            "<input id='search-btn' type='submit' name='submit' value='Search'/>")

    def test_distillery_no_distilleries(self):
        response = self.client.get(reverse('distillery_search_results'))

        self.assertTemplateUsed('ginthusiasm/distillery_search_page.html')
        self.assertContains(response, 'No Search Results')

    def test_distillery_widget_redirects_when_single_distillery(self):
        distillery = self.add_fake_distillery()
        response = self.client.get(reverse('distillery_search_results'), follow=True)

        self.assertRedirects(response, '/distillery/{}/'.format(distillery.slug))
        self.assertTemplateUsed('ginthusiasm/distillery_page.html')
        self.assertContains(response, '<div class="distillery-info">')

    def test_distillery_multiple_distilleries(self):
        self.add_fake_distillery()
        self.add_fake_distillery('TestDistillery2')
        response = self.client.get(reverse('distillery_search_results'))

        self.assertTemplateUsed('ginthusiasm/distillery_search_page.html')
        self.assertContains(response, "<div class='distillery-widget'>", count=2)

    def test_distillery_keyword_autocomplete_get_redirects(self):
        response = self.client.get(reverse('distillery_autocomplete'), follow=True)

        self.assertRedirects(response, '/distillery/')
        self.assertTemplateUsed('ginthusiasm/distillery_search_page.html')

    def test_distillery_keyword_autocomplete_post(self):
        self.add_fake_distillery();
        self.add_fake_distillery('TestDistillery2')
        response = self.client.post(reverse('distillery_autocomplete'),
                                    data={'search_text': 'TestDistillery'})

        self.assertContains(response, '<a href="/distillery/testdistillery/" class="ginthusiasm-link">TestDistillery</a>')
        self.assertContains(response, '<a href="/distillery/testdistillery2/" class="ginthusiasm-link">TestDistillery2</a>')
