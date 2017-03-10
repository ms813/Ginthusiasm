from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class TestHeaderFooter(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="jsmith")
        self.user.first_name = "John"
        self.user.last_name = "Smith"
        self.user.email = "test@test.com"
        self.user.password = make_password("jsmith123")

        self.user.save()

        self.client = Client()

    def test_index_uses_large_header(self):
        # check the index uses the large header
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, "ginthusiasm/header_large.html", msg_prefix="Index uses large header")

    def test_about_uses_small_header(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, "ginthusiasm/header_small.html", msg_prefix="About page uses small header")

    def test_header_logo(self):
        # check the large header contains the logo
        self.header_has_logo(self.client.get(reverse('index')))

        # check the small header contains the logo
        self.header_has_logo(self.client.get(reverse('about')))

    def test_header_has_nav_links(self):
        # large header has nav
        self.header_has_nav(self.client.get(reverse('index')))

        # small header has nav
        self.header_has_nav(self.client.get(reverse('about')))

    def test_header_has_search(self):
        # large header has search
        self.header_has_search(self.client.get(reverse('index')))

        # small header has search
        self.header_has_search(self.client.get(reverse('about')))

    def test_header_has_login_link(self):
        # large header has login
        self.header_has_login(self.client.get(reverse('index')))

        # small header has login
        self.header_has_login(self.client.get(reverse('about')))

    def test_header_has_logout(self):
        # large header has logout
        self.header_has_login(self.client.get(reverse('index')))

        # small header has logout
        self.header_has_login(self.client.get(reverse('about')))

    def page_has_footer(self, response):
        # check footer template was used
        self.assertTemplateUsed(response, 'ginthusiasm/footer.html', "Index uses footer template")

    def header_has_logo(self, response):
        self.assertContains(response, 'ginthusiasm-logo.png', msg_prefix="Header contains logo")

    def header_has_nav(self, response):
        # check the header contains the nav links
        self.assertTemplateUsed(response, 'ginthusiasm/header_nav.html', msg_prefix="Header uses nav template")
        self.assertContains(response, '<a href="/"><span>Home</span></a>', msg_prefix="Header contains home link")
        self.assertContains(response, '<a href="/about/"><span>About</span></a>',
                            msg_prefix="Header contains about link")
        self.assertContains(response, '<a href="/collections/"><span>Browse Gins</span></a>',
                            msg_prefix="Header contains browse link")
        self.assertContains(response, '<a href="/gin/"><span>Rate Gins</span></a>',
                            msg_prefix="Header contains rate link")

    def header_has_search(self, response):
        # check the header contains the search widget
        self.assertTemplateUsed(response, "ginthusiasm/header-search.html", "Header uses search_widget")
        self.assertContains(response, 'input id="header-search-field"', msg_prefix="header contains search box")

    def header_has_login(self, response):
        # check user is logged out
        user = auth.get_user(self.client)
        self.assertTrue(user.is_anonymous())

        # check login button
        self.assertContains(response, '<a href="/login/">Log In | Sign Up</a>',
                            msg_prefix="Header contains log in button when no user logged in")

    def header_has_logout(self, response):
        # check user is logged in
        self.client.force_login(self.user)
        user = auth.get_user(self.client)
        self.assertFalse(user.is_anonymous())

        # check about and logout buttons
        self.assertContains(response, '<a href="/my-account/">My Account</a>',
                            msg_prefix="Header contains My Account when user logged in")
        self.assertContains(response, '<a href="/logout/">Log Out</a>',
                            msg_prefix="Header contains Log Out when user logged in")
