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
        "title" : "Signature Serves",
        "shortDesc" : "<p>&lsquo;Signature serve&rsquo; has become an accepted term. It&rsquo;s now so mainstream an expression that it features on the vast majority of brand websites we&rsquo;ve looked at over the past six months. When did this happen? At what point did a suggestion for how to use a gin become a signature serve? and what&rsquo;s it all about? Moreover, if it&rsquo;s become conventional to talk about the ultimate way to serve a gin, are there entire areas that connoisseurs and barkeeps are forgetting about when judging a brand&rsquo;s recommendations or creating their own?</p> ",
        "content" : "<p>&lsquo;Signature serve&rsquo; has become an accepted term. It&rsquo;s now so mainstream an expression that it features on the vast majority of brand websites we&rsquo;ve looked at over the past six months. When did this happen? At what point did a suggestion for how to use a gin become a signature serve? and what&rsquo;s it all about? Moreover, if it&rsquo;s become conventional to talk about the ultimate way to serve a gin, are there entire areas that connoisseurs and barkeeps are forgetting about when judging a brand&rsquo;s recommendations or creating their own?</p> <p>After all, most forget it&rsquo;s almost never just about flavour&hellip; Signature serves have long been part of marketing strategies. No booze brand intent on building an army of engaged consumers will have forgotten to look into how their spirit might be served. Whether they embrace the exact term or not, all brands will have spent time looking into recipes and cocktails that they could use to inspire others to drink their gin over someone else&rsquo;s.</p><p>Signature serves come in many different forms, from twists on classics to entirely new, outlandishly complex propositions, but they are at their most elemental when encapsulated in a G&amp;T. The Gin and Tonic is by far the most widespread serve people choose to use at home, so this is the area we are going to look into here, as the very best &lsquo;signature G&amp;Ts&rsquo; actually have a lot more behind them than meets the eye.</p><p>When seen from a brand&rsquo;s perspective, a signature serve is a way of shining a spotlight on their USP, as well as a method to accentuate flavour. The suggestion might have a nod back to provenance, it might include a cornerstone botanical or it might just be about sharing a core ethos (for example Chase&rsquo;s continuous push towards cross proliferating all things British). These USP&rsquo;s and messages are in addition to a pairing&rsquo;s ability to showcase the range of flavours within a gin that can be harnessed by partnering certain garnishes/tonics/ways of serving etc.&hellip;</p><p>We find signature serves at their most intriguing in this simple cocktail as they separate the clever from the well equipped. For example, a G&amp;T is fundamentally only ever really three parts (and that&rsquo;s being generous by counting the garnish as a core component). Sure, people get fancy with infusions and a splash of juice here and there, but when it comes to those dreaming up brand suggestions for which tonic/garnish combo to pair with their gin- it is understood that their suggestion has to have universal appeal and needs to work for the adventurous drinker as well as it does the occasional tippler.</p><p>Message, flavour profile, aesthetic and overall impact all have to be wrangled into a compelling proposition whilst only using what are quite basic tools to do so. It&rsquo;s the ultimate challenge and the equivalent to fashionistas taking an haute couture concept all the way down to the Primark shopping floor. Too complicated and no one buys in, too simple and there&rsquo;s not enough impact for people to feel inspired and want to try it out.</p><p>We understand the stance many makers take that it is frustrating &ndash; after months or even years toiling away on a recipe &ndash; to suggest mixing it with something that will entirely change that finely balanced mix, but we&rsquo;re, personally, big fans of signature serves and have a lot of time for the ingenuity brands show when they suggest a way to partner their spirits. It&rsquo;s na&iuml;ve to think that saying &ldquo;just serve it neat&rdquo; or &ldquo;don&rsquo;t add a garnish because it&rsquo;s perfect&rdquo; is as effective as suggesting a combo.</p><p>It&rsquo;s not that most gins need a garnish in a G&amp;T; many don&rsquo;t, but by adding one you tilt the serve towards one direction or another and for many that&rsquo;s a joy in itself. Suggesting how to do this is like someone suggesting how to wear a garment of clothing. Sure, you can dress yourself, but if someone hints at the end vision of how something could be when combined or placed in context, the sense of style and the ethos behind a brand becomes clearer. This is no different for gin (and equally as important).</p><p>So, what&rsquo;s the holy grail of G&amp;T signature serves and why? In our opinion, you&rsquo;d be hard pressed to look past Hendrick&rsquo;s with Fever-Tree and a slice of cucumber as a perfect example. It&rsquo;s certainly the best known, and possibly the most simple, but its in this incredible simplicity that a great deal of factors reside.</p><p>Two of Hendrick&rsquo;s core USP&rsquo;s are their &lsquo;unusual&rsquo; brand stance and their addition of cucumber and rose. Picking a cucumber as a garnish was (at the time) highly unusual, so much so that it was years before even a minority of bars would consider stocking it. We estimate that it took around seven or eight years before the majority of bars that carried the spirit got on board with the garnish, but that in itself wasn&rsquo;t without merit.</p><p>Hendrick&rsquo;s fans believe that they are/were the vanguard of gin drinkers. The use of a cucumber was of utmost importance to their enjoyment of the spirit, so they&rsquo;d take bartenders to task if it wasn&rsquo;t available. In the end it was not the sales teams, brand reps or repeated brand messaging that transcended the pairing into the mass consciousness, but the indignant responses of consumers who would shame barkeeps for not serving it right.</p><p>Incidentally, just imagine what sticking to such a singular message of &ldquo;put a cucumber in your G&amp;T&rdquo; was like for such a long period of time when it wasn&rsquo;t being adopted. It&rsquo;s important to understand just how long and how widely they had to seed the message before it began to stick, as it helps contextualise why it&rsquo;s unlikely that anyone else will be able to replicate the success of their &ldquo;signature serve&rdquo;. It was always &ndash; and still is &ndash; very hard to have such a cemented serve that everyone knows about. Even if a brand had the ambitions to do it in the future the realities of the timeline required to implement it might mean it&rsquo;s out of reach simply because of team turnover and changing landscapes.</p><p>As for the Fever-Tree element&hellip; There may be a few options on the market for premium tonic today, but that&rsquo;s a very recent development. Fever Tree was one of the only premium tonics that were widely available in the UK even as far back as 2010, so it made sense that it was only natural that it was selected as the signature serve. Even if Fever-Tree wasn&rsquo;t the perfect partner for the gin (from a purely flavour driven perspective), it would likely have been chosen as the match for Hendrick&rsquo;s, because to be perceived as premium it had to paired with premium.</p><p>The Hendrick&rsquo;s and Tonic with a sliver of cuc&rsquo; became successful because it managed to straddle the divide between premium and simple so neatly; it is a drink can be made in top end super trendy bars as well as at home in suburban heartlands. It is about flavour, brand position on shelf and appealing to their fan&rsquo;s core beliefs about both themselves and the gin. It combines ease of service with a clearly noticeable point of difference and is deceptively clever. In our opinion it ought to go down as one of the greatest marketing decisions in this new era of Gin&rsquo;s history.</p><p>Many brands want their &ldquo;cucumber&rdquo; equivalent, but few understand that it is never just about flavour or positioning alone. It is about having a perfect compromise of the two translated into a combination that everyone can do.</p><p>No one takes you seriously when you suggest a sliver of carrot with a G&amp;T (the market is just not there yet, no matter how adventurous you think the Spanish are), neither does anyone have the mental capacity to deal with making a candied rose petal for a garnish just to make a G&amp;T look pretty. Especially not on a Monday night when they just want a double as soon as they walk through the door&hellip;</p><p>While these may be the perfect flavour or USP partners (and signature serves for two existing brands) they are unobtainable in their nature and not complete as an idea. They are respectively either too complex to consider chancing it for no real underlying brand reason, or too fiddly to do with no real palpable effect.</p><p>The machine gun approach that some brands have taken with a triple or quadruple garnish of several simple peels / spices is no better. It&rsquo;s a G&amp;T, not a fruit salad&hellip; Therein lies the problem; it is in simplicity that signature serves work best, but it is in this same simplicity that they face being just the same as everyone else. Moreover, when at their most complicated they are easier to explain and link back to the brand and to the gin.</p><p>We&rsquo;d urge newbie owners to keep this bipolar dilemma in mind when creating theirs. We, for one, are grateful that all we have to do is focus on flavour alone. All things considered &ndash; making something work for personal preference is a lot easier than trying to sum up a complex set of factors and translating it into one idea that carries universal appeal.</p><p>We doubt that it will be possible to have another universally accepted pairing in the way that Hendrick&rsquo;s and cucumber have been so synonymously linked. The market has moved on, fractured and become much more promiscuous in the way it is presented. That said, just as it is incredibly hard for a sports brand to create a tag line that permeates across all popular culture, it is not impossible either. New campaigns are launched on a weekly basis and some brands are making good headway staying on message season after season.</p><p>Only time will tell if this will work for brands. While we wait, we&rsquo;re off to make our signature serve&hellip; The signature aspect you ask? That the whole drink disappears before you can even cut the peel.</p>",
        "date" : '2017-01-15',
        "slug" : "signature-serves",
        "author" : userprofile,
        "image" : "articles/jan_gin.jpg",
        "month": False,
    },
    {
        "title" : "Innovation vs Heritage",
        "shortDesc" : "<p>With&nbsp;World Gin Day&nbsp;having been and gone and a swathe of gins been released, we&rsquo;ve once again been left wondering where the ideal balance is between all these progressive flavours and the core heritage of the gin category. So many of this year&rsquo;s releases and official debuts were brilliant additions to the category showing real innovation, yet (as always) a few were, well, just not gin at all&hellip;</p><p>To be a gin, the spirit must taste predominantly of&nbsp;juniper. It&rsquo;s both written in the legislation and a sacrosanct part of the understanding for all those who pick up a bottle with&nbsp;the intoxicating mono-syllable, GIN, written on the label. Gin is first and foremost&nbsp;an ode to&nbsp;juniper&nbsp;and if Champagne is just wine that knows someone, Gin is different to flavoured vodka because it is juniper focused.</p> ",
        "content" : "<p>With&nbsp;World Gin Day&nbsp;having been and gone and a swathe of gins been released, we&rsquo;ve once again been left wondering where the ideal balance is between all these progressive flavours and the core heritage of the gin category. So many of this year&rsquo;s releases and official debuts were brilliant additions to the category showing real innovation, yet (as always) a few were, well, just not gin at all&hellip;</p><p>To be a gin, the spirit must taste predominantly of&nbsp;juniper. It&rsquo;s both written in the legislation and a sacrosanct part of the understanding for all those who pick up a bottle with&nbsp;the intoxicating mono-syllable, GIN, written on the label. Gin is first and foremost&nbsp;an ode to&nbsp;juniper&nbsp;and if Champagne is just wine that knows someone, Gin is different to flavoured vodka because it is juniper focused.</p><p>However, much like the diamond in an engagement ring, even if the star of the show is upfront and centre, there are still many questions. How big is it? How it is held? Is the overall structure is complimented or if it is accentuated by surrounding elements? You can range from traditional to modern, from to intricate and complex, as well as from brash to nuanced and elegant. All of these factors need to be decided and are highly subjective. Gin&rsquo;s diamond is&nbsp;juniper, but other botanicals are all used in the mix to help transform it from a humble berry to an evocative and transformative spirit.</p><p>When it comes to gin, arguments over how far new makers can push the boundary of the category are inevitable. The purists will bemoan the adventurous flavour combinations, while those trailblazing a new gin style will point out that there is no point creating the same thing over and again.</p><p>Whichever side you take, both views&nbsp;are needed and there are some undeniable truths. Firstly, the &ldquo;juniper&nbsp;predominant&rdquo; is so highly subjective it is impossible to police or to enforce. Secondly, without innovation, the category will simply retract and interest will diminish, however, innovation at the expense of heritage&nbsp;will also lead to an inevitable implosion.</p><p>Quality is often used as the key point&nbsp;for those seeking to assuage those at loggerheads to come to a compromise. &ldquo;It&rsquo;s okay so long as what is being made is of a high quality&rdquo; they say. However, quality is a red herring in the long term. It doesn&rsquo;t matter if what is being produced is a great spirit, nor does it matter that there is an audience for it &ndash; if it diminishes and dilutes the overall understanding of what gin is. It might &ldquo;broaden the church&rdquo; now, but how do you then reconcile such a huge array of random flavours, styles and production methods after a&nbsp;few years where an anything goes policy has been in place?</p><p>The other huge red herring is when many of the more &ldquo;adventurous&rdquo; gin makers claim to have more than xx% juniper in their botanical bill. It doesn&rsquo;t matter if the it is made of 90%&nbsp;juniper&nbsp;if the resulting 10% completely overwhelm the flavour. Saying so merely overlooks the fact that regulations don&rsquo;t stipulate&nbsp;juniper&nbsp;content by botanical weight, scale or proportion, but its clear presence in the flavour of the end outcome.</p><p>In the long term, if Gin loses its meaning and no one knows what to expect when buying a bottle,&nbsp;the category will have an identity crisis that will result in many consumers &nbsp;&ndash; new and old &ndash; becoming disenfranchised. &nbsp;Short term thinking may well bring in a new audience, but if anything can be &ldquo;gin&rdquo; you will start having more&nbsp;Unicorn Tear / Anti-ageing Gin-type releases. If this is the case, in the blink of an eye&nbsp;the spirit will lose that most ephemeral of things &ndash; being cool. Needless to say, shortly after that, the new audience that has just been brought in, will be onto the next thing as they continue to search for something with credibility and authenticity instead, leaving&nbsp;the Gin category without an identity or an audience&hellip;</p><p>We agree there is a need for Gin to have &ldquo;entry points&rdquo; with a choice of less&nbsp;juniper&nbsp;heavy liquids on offer. We all need to continue bringing in new customers to the category who will&nbsp;eventually progress to&nbsp;juniper&nbsp;heavy versions as their taste buds develop.&nbsp;Salted caramel marshmallow gin is not a valid tool with which to do that however&hellip;</p><p>More importantly, if Gin becomes akin to&nbsp;flavoured vodka, it will be to the demise of all, progressive&nbsp;and traditionally styled alike. Not just because consumers will no longer understand gin and will become frustrated, not just because it will become gimmick ridden as mentioned above. It will be because all gin makers will have to compete against the flavoured vodka category &ndash; whose pockets are much deeper and whose understanding of how to bring a product to market and find a niche, no matter how demented the idea may sound at first, is much more savvy.</p><p>In pure marketing terms, Gin would do well not to poke that mighty bear and keep growing in a different area, a safe distance away, especially as doing so plays to its core strengths. The authenticity and heritage Gin has, is something that only a few vodka brands could possibly ever rival. Why ditch this massive advantage and opt to play their game instead?</p><p>It is important to remember that progression is important however and to not hinder it. Without it, Gin would still be in the dark ages, hidden behind row after row of Rum or Tequila.&nbsp;Hendrick&rsquo;s&nbsp;did a fantastic job at bringing in a new audience to gin when it launched.&nbsp;Hoxton Gin&nbsp;(although clearly this part was unintentional), has been a fantastic benchmark of what &ldquo;too far&rdquo; looks like.</p><p>But now that there are hundreds of gins on the market, the edge of the category is more populated than ever. There is no longer one or two &ldquo;outliers&rdquo;, there are dozens that challenge the status quo. Many of them show that is possible to do set out a new vision without losing sight of the wider identity, heritage and fundamental ethos &ndash;&nbsp;that of being&nbsp;juniper predominant.&nbsp;Bertha&rsquo;s Revenge&nbsp;and&nbsp;Pothecary Gin&nbsp;were two new gins in the past few months that showcase this exceptionally well. They challenge convention while also ring-fencing gin&rsquo;s flavour heritage.</p><p>Juniper is after all, a complex flavour both capable of being green and resinous, while also being citrusy and sometimes even a touch spicy. Like a prism of glass,&nbsp;juniper&nbsp;can be both&nbsp;singular while&nbsp;also, with just a slight a change of perspective, refract a huge array of different flavours. Its very nature allows it to be accentuated, twisted and contrasted by a vast selection&nbsp;of botanicals even when the sole intention is to boost a specific part of its profile.</p><p>Gin has long been a multi-botanical spirit and trends and &ldquo;new discoveries and ideas&rdquo; have been influencing which botanicals were added into the mix for centuries. It&nbsp;would be much poorer without the addition of all the other botanical elements that&nbsp;support juniper. Moreover, distillers would not have the ability to be as evocative as they are,&nbsp;nor be as equipped&nbsp;to&nbsp;instil a sense of place into their spirit and convey&nbsp;their regionality.</p><p>So where does this leave us? Were the team behind&nbsp;Aviation Gin&nbsp;right to try and define a new sub-category&nbsp;all those years ago? Should there be a new classification for these progressive flavour profiles so that consumers, trade and producers can all understand what is in a bottle? Something along the lines of &nbsp;&ldquo;Contemporary&rdquo; or &ldquo;New Wave&rdquo; perhaps?</p><p>We certainly think so and we&rsquo;re not the only ones to want to see something happen. Having stricter regulations on what exists while also simultaneously opening up a new avenue would not affect the possible creativity distillers want to have in future. It would not limit the category&rsquo;s possible new growth and curtail its ambitions to appeal to a new audience. Yet crucially, it might just offer up some much need protection for both those wanting to make more traditionally styled gins and spare consumers a confusing minefield of mixed messages.</p><p>Incidentally &ndash; our vote is to call it New Wave, although, there clearly needs to be a much wider discussion as to what would be most appropriate term. Currently, &ldquo;contemporary&rdquo; is being used in many tasting competitions, but we feel that it possible to be both contemporary and classically styled at the same time (Dorothy Parker Gin&nbsp;&amp;&nbsp;Hope on Hopkins&nbsp;Gin&nbsp;for example) and in calling it that, too few in the industry would endorse the idea and nothing would happen. &ldquo;New Western&rdquo; suffered this fate as (partly) it applied geography to the debate and for a new term and new protection to be enacted, it needs to be flexible and vague enough to begin with, in order to be moulded into a workable compromise that we all accept.</p><p>It&rsquo;s clear to us, a new sub-genre of gin seems like a good way to keep innovation going while also not compromising the vision for, heritage of or understanding about&nbsp;the existing areas. If Old Tom, Navy,&nbsp;Fruit Cups&nbsp;and Sloe are all accepted then why not a new one? Historically, there were many more styles of gin too (Table Gin and Cream Gin for example), so this wouldn&rsquo;t even set a precedent either. There are talks due to be scheduled and thoughts being gathered by better minds than ours on this very matter &ndash; and we&rsquo;ll keep updating the site to let you know what emerges.</p><p>Until this happens however, we&rsquo;ll just have to keep the faith that those who are creating new gins are going to stay within reach of what exists. We hope that they continue to sympathetically build upon those gone before them and stay true to what has&nbsp;made Gin a spirit that has been loved for generations &ndash; one whose resinous, green, piney core&nbsp;is very much&nbsp;palpable and celebrated.</p>",
        "date" : '2016-05-21',
        "slug" : "innovation-vs-heritage",
        "author" :userprofile,
        "image" : "articles/innovation.jpg",
        "month": False,
    },
    {
        "title" : "A final article",
        "shortDesc" : "Lorem ipssdfsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea.",
        "content" : "Lorem ipsum dolor sit amet, hinc delicata dissentiunt sit te, ei tacimates assueverit pro. Ad oratio alienum mel, at integre laoreet eam. Utamur habemus posidonium no sea. Latine aperiri ea mea, eu tota viris essent mei, feugait delicata gloriatur sit in. Ad putent graeco sea. Minimum urbanitas intellegam in vim. An vidit inimicus nam. An vis habeo aperiam. Et ius veri sententiae liberavisse. Tritani epicurei explicari vis id. Ei pro malis utamur complectitur. Case dolore laboramus in has, ea has meliore suscipiantur. Eum ne ignota labitur adipisci, id has iusto oporteat. Ei probo delicatissimi qui, libris concludaturque mel id, mea an fierent repudiandae. At per iusto invenire.  Cum ea aliquip eripuit corrumpit. Vel fugit nulla urbanitas id. In facer malorum copiosae mea, dicit deterruisset eu has. Invenire consetetur at pri. Has cu placerat reprimique concludaturque, ne ipsum elitr vim, qui ad vide simul ubique. Suas noster et quo, pri te noster eruditi, et pri assueverit voluptatibus. Ex eam facete scripta moderatius. No pri tantas conceptam, soleat consequat dissentias eam ne. Illud veritus in vis, nibh appareat phaedrum at mel. Pri cu brute interesset, has id summo menandri praesent, ignota graeci ad sea. Quo te semper alterum. Ut usu hinc solum, dicant salutatus laboramus pro eu. Graece semper vel cu. Ea sint mandamus concludaturque est, sit mandamus inimicus liberavisse ea, porro scripta adipisci ex nec. Tota mutat fugit sea ei, ei alii saperet moderatius est. Est odio brute eu, expetenda scribentur instructior mea te. Ea vel reque dolor aliquam. Nam cu utinam everti oblique. Ex sed vide sale. Ne nec veri iusto recusabo, nam quando primis postea ex, sit ne posse iracundia elaboraret. Nonumy dolorum elaboraret ex vix, cu patrioque comprehensam mel. Congue prodesset pro cu, cu cum iudicabit cotidieque. Cum eu sanctus scripserit. Atqui eripuit atomorum pri at, et has harum omnes. Nam ei idque delicatissimi. Has possit copiosae volutpat eu, est diam latine adolescens cu, qui no odio liber putant. Ex cum soleat iisque erroribus, ad clita graece aliquip eam. No consul argumentum efficiendi eam, labitur sententiae id eam. Dolorem maluisset eos an. Facilisi democritum conclusionemque ea pri, habeo ubique percipit mel at, quo dicant euripidis ei. Prima salutandi at his, qui ei bonorum utroque sententiae, sit eu fierent qualisque expetendis. Brute maiorum ne ius. No veri evertitur qui, nusquam oportere id eam, has id ullum paulo denique. Vocent lobortis eloquentiam ei pro, agam dicant disputando id mel. Prima putent definiebas at eum. Cu est sale patrioque, sea soleat dicunt cu. Graeco recusabo expetendis in vis.",
        "date" : '2016-12-01',
        "slug" : "final-art",
        "author" :userprofile,
        "image" : "articles/innovation.jpg",
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

    distilleries = []
    with open('distillery_data.json') as f:
        distilleries = json.load(f)

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
            distillery.owner = User.objects.get(username="Charlie").userprofile

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
            print(str(gin) + " created")

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
                "review_type" : UserProfile.EXPERT,
                "date" : '2017-03-01',
                "rating" : 3,
                "content" : "Pudding jelly chocolate cake lollipop cupcake. Candy cotton candy pie sweet lollipop. Souffle cheesecake danish halvah. Muffin brownie powder pastry. Candy sweet roll jujubes jelly. Pie icing icing chupa chups lemon drops bear claw carrot cake muffin chocolate bar. Cheesecake bonbon icing lollipop sweet caramels powder. Powder croissant candy lemon drops. Bonbon brownie marzipan gingerbread candy bear claw powder tart. Donut candy sesame snaps. Halvah cake sweet apple pie. Cake oat cake tiramisu cake. Toffee dragee croissant jelly beans dragee macaroon chocolate cake tootsie roll.",
                "lat" : 51.503351 + (random.random() - 0.5),
                "lng" : -0.119522 + (random.random() - 0.5),
                "user" : user.userprofile,
                "gin" : gins[i],
                "postcode": "G2 2RQ",
            })

    for data in reviews:
        try:
           r = Review.objects.get(user=data['user'], gin=data['gin'])
           print(str(r) + ' already exists!')
        except Review.DoesNotExist:
            r = Review.objects.create(
                user=data['user'],
                gin=data['gin'],
                review_type=data['review_type'],
                date=data['date'],
                rating=data['rating'],
                content=data['content'],
                lat=data['lat'],
                lng=data['lng'],
                postcode= data['postcode'],
            )
            print(str(r) + ' successfully created')

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
        {
            "username": "Charlie",
            "first_name": "Charles",
            "last_name": "Charleston",
            "email": "charlie@doesntexist.com",
            "password": make_password("charlietest"),
            "user_type": UserProfile.DISTILLERY_OWNER
        }
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

        # These should be called in order
        populate_users()
        populate_distillery()
        populate_gin()
        populate_review()
        populate_wishlist()
        populate_article()

        print("Successfully finished populating all models")
    else:
        # populate each model as specified from the command line arguments
        for arg in sys.argv:
            if not arg.endswith('.py') and models[arg]:
                # execute the function in the models dict corresponding to the keyword
                models[arg]()

        print("Successfully finished populating " + ", ".join(sys.argv[1:]))
