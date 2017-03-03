import sys, os, django, json, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ginthusiasm_project.settings')
django.setup()
random.seed(8765)

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ginthusiasm.models import Article, Distillery, Gin, TasteTag, Review, UserProfile, Wishlist

def populate_article():
    print("Populating articles...")
    user = User.objects.get(username="Catherine")
    userprofile = user.userprofile

    articles = [
    {
        "title" : "January Gin of the Month",
        "shortDesc" : "This is the short description",
        "content" : "Lorem ipsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea. Latine aperiri ea mea, eu tota viris essent mei, feugait delicata gloriatur sit in. Ad putent graeco sea. Minimum urbanitas intellegam in vim. An vidit inimicus nam. An vis habeo aperiam. Et ius veri sententiae liberavisse. Tritani epicurei explicari vis id. Ei pro malis utamur complectitur. Case dolore laboramus in has, ea has meliore suscipiantur. Eum ne ignota labitur adipisci, id has iusto oporteat. Ei probo delicatissimi qui, libris concludaturque mel id, mea an fierent repudiandae. At per iusto invenire.  Cum ea aliquip eripuit corrumpit. Vel fugit nulla urbanitas id. In facer malorum copiosae mea, dicit deterruisset eu has. Invenire consetetur at pri. Has cu placerat reprimique concludaturque, ne ipsum elitr vim, qui ad vide simul ubique. Suas noster et quo, pri te noster eruditi, et pri assueverit voluptatibus. Ex eam facete scripta moderatius. No pri tantas conceptam, soleat consequat dissentias eam ne. Illud veritus in vis, nibh appareat phaedrum at mel. Pri cu brute interesset, has id summo menandri praesent, ignota graeci ad sea. Quo te semper alterum. Ut usu hinc solum, dicant salutatus laboramus pro eu. Graece semper vel cu. Ea sint mandamus concludaturque est, sit mandamus inimicus liberavisse ea, porro scripta adipisci ex nec. Tota mutat fugit sea ei, ei alii saperet moderatius est. Est odio brute eu, expetenda scribentur instructior mea te. Ea vel reque dolor aliquam. Nam cu utinam everti oblique. Ex sed vide sale. Ne nec veri iusto recusabo, nam quando primis postea ex, sit ne posse iracundia elaboraret. Nonumy dolorum elaboraret ex vix, cu patrioque comprehensam mel. Congue prodesset pro cu, cu cum iudicabit cotidieque. Cum eu sanctus scripserit. Atqui eripuit atomorum pri at, et has harum omnes. Nam ei idque delicatissimi. Has possit copiosae volutpat eu, est diam latine adolescens cu, qui no odio liber putant. Ex cum soleat iisque erroribus, ad clita graece aliquip eam. No consul argumentum efficiendi eam, labitur sententiae id eam. Dolorem maluisset eos an. Facilisi democritum conclusionemque ea pri, habeo ubique percipit mel at, quo dicant euripidis ei. Prima salutandi at his, qui ei bonorum utroque sententiae, sit eu fierent qualisque expetendis. Brute maiorum ne ius. No veri evertitur qui, nusquam oportere id eam, has id ullum paulo denique. Vocent lobortis eloquentiam ei pro, agam dicant disputando id mel. Prima putent definiebas at eum. Cu est sale patrioque, sea soleat dicunt cu. Graeco recusabo expetendis in vis.",
        "date" : '2017-02-17',
        "slug" : "january-gin-of-the-month",
        "author" :userprofile,
        "image" : "articles/jan_gin.jpg",
        "month": True,
    },
    {
        "title" : "Test Article",
        "shortDesc" : "Some more short desciption",
        "content" : "This is the content",
        "date" : '2017-01-03',
        "slug" : "test-article",
        "author" : userprofile,
        "image" : "articles/jan_gin.jpg",
        "month": False,
    },
    {
        "title" : "Another article",
        "shortDesc" : "Lorem ipsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea.",
        "content" : "Lorem ipsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea. Latine aperiri ea mea, eu tota viris essent mei, feugait delicata gloriatur sit in. Ad putent graeco sea. Minimum urbanitas intellegam in vim. An vidit inimicus nam. An vis habeo aperiam. Et ius veri sententiae liberavisse. Tritani epicurei explicari vis id. Ei pro malis utamur complectitur. Case dolore laboramus in has, ea has meliore suscipiantur. Eum ne ignota labitur adipisci, id has iusto oporteat. Ei probo delicatissimi qui, libris concludaturque mel id, mea an fierent repudiandae. At per iusto invenire.  Cum ea aliquip eripuit corrumpit. Vel fugit nulla urbanitas id. In facer malorum copiosae mea, dicit deterruisset eu has. Invenire consetetur at pri. Has cu placerat reprimique concludaturque, ne ipsum elitr vim, qui ad vide simul ubique. Suas noster et quo, pri te noster eruditi, et pri assueverit voluptatibus. Ex eam facete scripta moderatius. No pri tantas conceptam, soleat consequat dissentias eam ne. Illud veritus in vis, nibh appareat phaedrum at mel. Pri cu brute interesset, has id summo menandri praesent, ignota graeci ad sea. Quo te semper alterum. Ut usu hinc solum, dicant salutatus laboramus pro eu. Graece semper vel cu. Ea sint mandamus concludaturque est, sit mandamus inimicus liberavisse ea, porro scripta adipisci ex nec. Tota mutat fugit sea ei, ei alii saperet moderatius est. Est odio brute eu, expetenda scribentur instructior mea te. Ea vel reque dolor aliquam. Nam cu utinam everti oblique. Ex sed vide sale. Ne nec veri iusto recusabo, nam quando primis postea ex, sit ne posse iracundia elaboraret. Nonumy dolorum elaboraret ex vix, cu patrioque comprehensam mel. Congue prodesset pro cu, cu cum iudicabit cotidieque. Cum eu sanctus scripserit. Atqui eripuit atomorum pri at, et has harum omnes. Nam ei idque delicatissimi. Has possit copiosae volutpat eu, est diam latine adolescens cu, qui no odio liber putant. Ex cum soleat iisque erroribus, ad clita graece aliquip eam. No consul argumentum efficiendi eam, labitur sententiae id eam. Dolorem maluisset eos an. Facilisi democritum conclusionemque ea pri, habeo ubique percipit mel at, quo dicant euripidis ei. Prima salutandi at his, qui ei bonorum utroque sententiae, sit eu fierent qualisque expetendis. Brute maiorum ne ius. No veri evertitur qui, nusquam oportere id eam, has id ullum paulo denique. Vocent lobortis eloquentiam ei pro, agam dicant disputando id mel. Prima putent definiebas at eum. Cu est sale patrioque, sea soleat dicunt cu. Graeco recusabo expetendis in vis.",
        "date" : '2016-05-21',
        "slug" : "another-article",
        "author" :userprofile,
        "image" : "articles/jan_gin.jpg",
        "month": False,
    },
    {

        "title" : "A final article",
        "shortDesc" : "Lorem ipssdfsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea.",
        "content" : "Lorem ipsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea. Latine aperiri ea mea, eu tota viris essent mei, feugait delicata gloriatur sit in. Ad putent graeco sea. Minimum urbanitas intellegam in vim. An vidit inimicus nam. An vis habeo aperiam. Et ius veri sententiae liberavisse. Tritani epicurei explicari vis id. Ei pro malis utamur complectitur. Case dolore laboramus in has, ea has meliore suscipiantur. Eum ne ignota labitur adipisci, id has iusto oporteat. Ei probo delicatissimi qui, libris concludaturque mel id, mea an fierent repudiandae. At per iusto invenire.  Cum ea aliquip eripuit corrumpit. Vel fugit nulla urbanitas id. In facer malorum copiosae mea, dicit deterruisset eu has. Invenire consetetur at pri. Has cu placerat reprimique concludaturque, ne ipsum elitr vim, qui ad vide simul ubique. Suas noster et quo, pri te noster eruditi, et pri assueverit voluptatibus. Ex eam facete scripta moderatius. No pri tantas conceptam, soleat consequat dissentias eam ne. Illud veritus in vis, nibh appareat phaedrum at mel. Pri cu brute interesset, has id summo menandri praesent, ignota graeci ad sea. Quo te semper alterum. Ut usu hinc solum, dicant salutatus laboramus pro eu. Graece semper vel cu. Ea sint mandamus concludaturque est, sit mandamus inimicus liberavisse ea, porro scripta adipisci ex nec. Tota mutat fugit sea ei, ei alii saperet moderatius est. Est odio brute eu, expetenda scribentur instructior mea te. Ea vel reque dolor aliquam. Nam cu utinam everti oblique. Ex sed vide sale. Ne nec veri iusto recusabo, nam quando primis postea ex, sit ne posse iracundia elaboraret. Nonumy dolorum elaboraret ex vix, cu patrioque comprehensam mel. Congue prodesset pro cu, cu cum iudicabit cotidieque. Cum eu sanctus scripserit. Atqui eripuit atomorum pri at, et has harum omnes. Nam ei idque delicatissimi. Has possit copiosae volutpat eu, est diam latine adolescens cu, qui no odio liber putant. Ex cum soleat iisque erroribus, ad clita graece aliquip eam. No consul argumentum efficiendi eam, labitur sententiae id eam. Dolorem maluisset eos an. Facilisi democritum conclusionemque ea pri, habeo ubique percipit mel at, quo dicant euripidis ei. Prima salutandi at his, qui ei bonorum utroque sententiae, sit eu fierent qualisque expetendis. Brute maiorum ne ius. No veri evertitur qui, nusquam oportere id eam, has id ullum paulo denique. Vocent lobortis eloquentiam ei pro, agam dicant disputando id mel. Prima putent definiebas at eum. Cu est sale patrioque, sea soleat dicunt cu. Graeco recusabo expetendis in vis.",
        "date" : '2016-12-01',
        "slug" : "a-final-article",
        "author" :userprofile,
        "image" : "articles/jan_gin.jpg",
        "month": False,

    }
    ]

    for data in articles:
        article_results = []
        try:
            article_results = Article.objects.get(title=data['title'])
        except Article.DoesNotExist:
            pass

        if not article_results:
            article = Article()
            article.title = data['title']
            article.shortDesc = data['shortDesc']
            article.content = data['content']
            article.date = data['date']
            article.slug = data['slug']
            article.author = data['author']
            article.image = data['image']
            article.month = data['month']
            article.save()

def populate_distillery():
    print("Populating distilleries...")
    distilleries = [
        {
            "name" : "Edinburgh Gin",
            "address" : "1A Rutland Place, Edinburgh, EH1 2AD",
            "phone" : "01316 562810",
            "email" : "info@edinburghgindistillery.com",
            "long_description" : "Nestled beneath the West End of Edinburgh, you'll find something of a hidden wonderland - the Edinburgh Gin Distillery. Steeped in history and creation, we invite you to disappear down the rabbit hole and indulge yourself in the mystery of the beautiful botanical libations we call gin.",
            "image" : "distilleries/Edinburgh-Gin.jpg",
            "lat" : 55.949982,
            "long" : -3.208180,
        },
        {
            "name": "Eden Mill",
            "address": "Main Street, Guardbridge, St Andrews, KY16 0UU",
            "phone": "01334 834038",
            "email" : "hello@edenmill.com",
            "long_description": "Eden Mill Scottish craft gin. Traditionally made by hand in Scotland using copper pot stills. Our distilling talent comes from the deeply rooted understanding of whisky and a real drive to innovate.",
            "image": "distilleries/Eden-Mill.jpg",
            "lat": 56.363755,
            "long": -2.892163,
        }
    ]

    for data in distilleries:
        distillery_results = []
        try:
            distillery_results = Distillery.objects.get(name=data['name'])
        except Distillery.DoesNotExist:
            pass

        if not distillery_results:
            distillery = Distillery()
            distillery.name = data['name']
            distillery.address = data['address']
            distillery.phone = data['phone']
            distillery.email = data['email']
            distillery.long_description = data['long_description']
            distillery.image = data['image']
            distillery.lat = data['lat']
            distillery.long = data['long']

            distillery.save()

def populate_gin():
    print("Populating gins...")
    print("    Populating gin taste tags...")
    #tags = ["Juniper", "Sugar Kelp", "Coriander", "Angelica Root", "Orris Root", "Cubebs", "Bitter Orange Peel", "Licorice", "Cassia Bark"]

    #for tag_name in tags:
        #tag, created = TasteTag.objects.get_or_create(name = tag_name)

        #if created:
            #tag.name = tag_name
            #tag.save()

    print("    Populating gins...")

    gins = []
    with open('gin_data.json') as f:
        gins = json.load(f)

    """gins = [
        {
            "name" : "Isle of Harris Gin",
            "price" : "35.00",
            "short_description" : "Our new gin captures the elemental nature of the Isle of Harris, rewarding the drinker with maritime pleasures. The unique inclusion of local, hand-harvested Sugar kelp speaks of our island's deep connections to the sea while working with eight other carefully chosen botanicals.",
            "long_description" : "Test long description",
            "abv" : "45.0",
            "taste_tags" : ["Sugar Kelp", "Juniper", "Coriander", "Angelica Root", "Orris Root", "Cubebs", "Bitter Orange Peel", "Licorice", "Cassia Bark"],
            "image" : "gins/Harris-Gin.jpg",
            "distillery" : ""
        },
        {
            "name" : "Eden Mill Love Gin",
            "price" : "30.00",
            "short_description" : "The famous light blush Pink Gin from Eden Mill brings together an outstanding blend of local botanicals and exotic fruits. Our pink gin is a pale colour when poured and when diluted, sweet vanilla and floral notes are brought out. Show your appreciation of a great pink gin and spread the word about Love Gin.",
            "long_description" : "Test long description",
            "abv" : "42.0",
            "taste_tags" : ["Juniper", "Rose Petals", "Hibiscus", "Strawberry", "Raspberry", "Vanilla", "Apples", "Pears", "Pink Grapefruit", "Rose Water"],
            "image" : "gins/Eden-Mill-Love-Gin.jpg",
            "distillery" : "Eden Mill"
        },
        {
            "name" : "The Botanist Islay Dry Gin",
            "price" : "35.00",
            "short_description" : "The Botanist Gin is a progressive exploration of the botanical heritage of our Isle of Islay. 22 hand-foraged local botanicals delicately augment nine berries, barks, seeds and peels during an achingly slow distillation. This first and only Islay Dry Gin is a rare expression of the heart and soul of our remote Scottish island home.",
            "long_description" : "Test long description",
            "abv" : "46.0",
            "taste_tags" : ["Menthol", "Apple Mint", "Spring Woodlands", "Juniper", "Coriander", "Aniseed", "Lemon Peel", "Orange Peel", "Thistle Honey", "Gorse Coconut", "Wild Mint"],
            "image" : "gins/The-Botanist-Gin.jpg",
            "distillery" : ""
        }
    ]"""

    for data in gins:
        gin, created = Gin.objects.get_or_create(name = data['name'])

        if created:
            gin.price = data['price']
            gin.short_description = data['short_description']
            gin.long_description = data['long_description']
            gin.abv = data['abv']

            # add tags to gins
            tags = data['taste_tags'].split(', ')
            for tag_name in tags:
                if not tag_name=="":
                    tag_name = tag_name.title()
                    tag, tag_created = TasteTag.objects.get_or_create(name = tag_name)

                    if tag_created:
                        tag.name = tag_name
                        tag.save()

                    gin.taste_tags.add(TasteTag.objects.get(name = tag))

            gin.image = data['image']

            # associate distillery with gin
            if data['distillery'] == "":
                gin.distillery = None
            else:
                gin.distillery = Distillery.objects.get(name = data['distillery'])

            gin.save()

    #remake indexes
    print ("        Remaking indexes...")
    os.system('python manage.py rebuild_index')

def populate_review():
    print("Populating reviews...")

    users = User.objects.all()
    gins = Gin.objects.all()

    reviews = []
    for user in users:
        review_count = random.randint(0, len(gins))

        for i in range(0, review_count):
            reviews.append({
                "review_type" : Review.EXPERT,
                "date" : '2017-03-01',
                "rating" : 3,
                "summary" : "Cupcake ipsum dolor sit amet. Wafer macaroon biscuit chupa chups candy canes candy chocolate cake chocolate. Chocolate cake chupa chups liquorice lemon drops sweet roll cheesecake jelly pudding. Carrot cake cupcake lemon drops candy canes powder sugar plum wafer marzipan.",
                "content" : "Pudding jelly chocolate cake lollipop cupcake. Candy cotton candy pie sweet lollipop. Souffle cheesecake danish halvah. Muffin brownie powder pastry. Candy sweet roll jujubes jelly. Pie icing icing chupa chups lemon drops bear claw carrot cake muffin chocolate bar. Cheesecake bonbon icing lollipop sweet caramels powder. Powder croissant candy lemon drops. Bonbon brownie marzipan gingerbread candy bear claw powder tart. Donut candy sesame snaps. Halvah cake sweet apple pie. Cake oat cake tiramisu cake. Toffee dragee croissant jelly beans dragee macaroon chocolate cake tootsie roll.",
                "lat" : 51.503351 + (random.random() - 0.5),
                "long" : -0.119522 + (random.random() - 0.5),
                "user" : user.userprofile,
                "gin" : gins[i]
            })

    for data in reviews:
        try:
            r = Review.objects.get(user=data['user'], gin=data['gin'])
            print(str(r) + " already exists!")
        except Review.DoesNotExist:
            r = Review.objects.create(
                user=data['user'],
                gin=data['gin'],
                review_type=data['review_type'],
                date=data['date'],
                rating=data['rating'],
                summary=data['summary'],
                content=data['content'],
                lat=data['lat'],
                long=data['long'],
            )
            print(str(r) + ' successfully created')

    """
    user = User.objects.get(username="Rozz")
    userprofile = user.userprofile
    gin = Gin.objects.get(name="Eden Mill Love Gin")
    reviews_results = []
    try:
        reviews_results = Review.objects.get(date=data['date'])
    except Review.DoesNotExist:
        pass

    if not reviews_results:
        review = Review()
        review.review_type = data['review_type']
        review.date = data['date']
        review.rating = data['rating']
        review.summary = data['summary']
        review.content = data['content']
        review.lat = data['lat']
        review.long = data['long']
        review.user = data['user']
        review.gin = data['gin']

        review.save()
    """

def populate_wishlist():
    print("Populating wishlist...")
    users = UserProfile.objects.all()
    if len(users) == 0:
        populate_users()

    gins = Gin.objects.all()
    if len(gins) == 0:
        populate_gin()

    for user in UserProfile.objects.all():
        wishlist, created = Wishlist.objects.get_or_create(user=user)

        if user.user.username == 'Matt' and created:
            wishlist.gins.add(gins[0])
            wishlist.gins.add(gins[1])
            wishlist.gins.add(gins[2])

def populate_users():
    print("Populating users...")

    users = [
        {
            "username" : "Catherine",
            "first_name" : "Catherine",
            "last_name" : "Daly",
            "email" : "2283461d@student.gla.ac.uk",
            "password" : make_password("catherineadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Robert",
            "first_name" : "Robert",
            "last_name" : "Gilmour",
            "email" : "2022607g@student.gla.ac.uk",
            "password" : make_password("robertadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Matt",
            "first_name" : "Matthew",
            "last_name" : "Smith",
            "email" : "2283142s@student.gla.ac.uk",
            "password" : make_password("mattadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Rozz",
            "first_name" : "Rosalyn",
            "last_name" : "Taylor",
            "email" : "2226947t@student.gla.ac.uk",
            "password" : make_password("rozzadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Alice",
            "first_name" : "Alice",
            "last_name" : "Alison",
            "email" : "12345@doesntexist.com",
            "password" : make_password("alicetest"),
            "user_type" : UserProfile.EXPERT
        },
        {
            "username" : "Bob",
            "first_name" : "Bob",
            "last_name" : "Bobertson",
            "email" : "54321@doesntexist.com",
            "password" : make_password("bobtest"),
            "user_type" : UserProfile.BASIC
        },
    ]

    for data in users:
        user, created = User.objects.get_or_create(username = data['username'])

        if created:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.password = data['password']
            user.is_staff = data['user_type'] == UserProfile.ADMIN
            user.is_superuser = data['user_type'] == UserProfile.ADMIN
            user.save()

            profile = UserProfile(
               user = User.objects.get(username=data['username']),
               user_type = data['user_type'],
            )
            profile.save()

if __name__ == '__main__':

    # dictionary linking each population function to a keyword
    models = {
        'article': populate_article,
        'distillery': populate_distillery,
        'gin': populate_gin,
        'review': populate_review,
        'user': populate_users,
        'wishlist': populate_wishlist
    }

    print("Starting population script...")

    if len(sys.argv) <= 1:
        # if no command line arguments, populate every model
        # note first cmd arg is 'populate_db.py'

        # RT - had to comment out the loop below, and add
        # these functions here to make sure DB was populating in
        # right order
        populate_users()
        populate_distillery()
        populate_gin()
        populate_review()
        populate_wishlist()
        populate_article()

        # for key in models:
        #     models[key]();
        print("Successfully finished populating all models")
    else:
        # populate each model as specified from the command line arguments
        for arg in sys.argv:
            if not arg.endswith('.py') and models[arg]:
                # execute the function in the models dict corresponding to the keyword
                models[arg]()

        print("Successfully finished populating " + ", ".join(sys.argv[1:]))
