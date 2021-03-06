from .models import book

book.objects.create(
    name="ملکه اسیر",
    writer="آلیسون ویر",
    summery="زنی ۳۰ ساله و زیبا به همراه تعداد معدودی محافظ مثل باد به سمت سرزمینی می تازد که فرانسه نامیده می شود. اکنون تاج و تخت دختر کوچکش و ازدواجی نابود شده با لویی ،پادشاه فرانسه، را پشت سر می‌گذارد.  نام این زن دوشس اکتین است و تنها هدفش این است که به دوک نشین قدرتمندش بازگردد و با مردی ازدواج کند که دوستش دارد",
    genre = "تاریخی")
    
book.objects.create(
    name="خائن بی گناه",
    writer="آلیسون ویر",
    summery="این داستان در دوره‌های حساس و سرنوشت ساز اتفاق می افتد. او به عنوان نوه خواهری هنری هشتم و دختر عمه ادوارد چهارم در می یابد که هرگز نمی‌تواند سرنوشتش را تغییر دهد. صداقت هوش و شخصیت قوی او خواننده را از میان مسیر پر پیچ و خم سیاست‌های دوران قدرت تیودور می گذراند.",
    genre = "تاریخی")

book.objects.create(
    name="رثیه شوم",
    writer="مارگارت کمبل بارنز",
    summery="این کتاب داستان شورانگیز دو زن قهرمان را بازگو می کند که گرچه در دو زمان مختلف زندگی می‌کنند اما توسط مشهور ترین معمای قتل تاریخ با یکدیگر پیوند خورده‌اند. لیدی کاترین گری هم اکنون بیشتر از سهم خود طعم شور بختی را چشیده است. خواهر بزرگترش لیدی جین گری به خاطر پذیرش غیرقانونی تاج و تختی که به او تعلق نداشت گردن زده شد و اکنون به خاطر عشقی ممنوعه خشم دخترعمه با صلابت خود را بر انگیخته است. اوضاع دربار خوب نیست و خیلی زود شایعاتی به گوش کاترین می رسد که تمام چیزهایی را که عزیز می داشت به خطر می اندازد.",
    genre = "تاریخی")

book.objects.create(
    name="چشمان همیشه هوشیار",
    writer="جویس کرول اتس",
    summery="این کتاب داستان دختر نوجوانی است که مادرش به طرز مشکوکی ناپدید می شود و بعد از مدت‌ها تلاش متوجه دست داشتن پدرش در این ماجرا می شود. نویسنده از این کتاب بهره می‌برد تا فضای رسانه کشورش را نقد کند.",
    genre = "جنایی")

book.objects.create(
    name="افشاگر",
    writer="جان گریشام",
    summery="وکیلی مرموز از یک قاضی فدرال آمریکا به جرم تبانی با مافیای ساحل غربی آمریکا شکایت می‌کند. هدف او دریافت جایزه‌ای است که بنابر قانون به افشاگران قضات فاسد تعلق می‌گیرد. اما هیچکس گمان نمی کرد این شکایت به نبردی سخت و خطرناک با مافیای آمریکایی بیانجامد و عدع ای بی گناه کشته شوند و آسیب ببینند.",
    genre = "جنایی")

book.objects.create(
    name="در یک جنگل تاریک تاریک",
    writer="روث ور",
    summery="وقتی نورا نویسنده ی خلوت گزین رمان های جنایی از طرف دوستی که سال ها از او بی خبر بوده به مهمانی دوستانه ای در ییلاقات شمال انگلستان دعوت می شود . نورا میلی به شرکت در مهمانی ندارد اما با این حال شرکت می کند. 48 ساعت بعد وقتی در یک بیمارستان به هوش می آید متوجه می شود کسی کشته شده. اما سوالی که مدام در ذهنش ایجاد می شود این است که چه اتفاقی افتاده",
    genre = "جنایی")

book.objects.create(
    name="شهر و ستارگان",
    writer="آرتور سی کلارک",
    summery="یک میلیارد سال بعد اقیانوس های زمین تبخیر شده اند و بشر هم تقریباً از زمین ناپدید شده. ساکنان شهر دیاسپارتصور می‌کنند آخرین انسان‌های کیهان هستند. اما هیچ چیزی از سیاره زمین و دیگر نقاط جهان نمی‌دانند. شهر با دیواری بلند از جهان جدا شده و میلیونها میلیون سال است که کسی شهر را ترک نکرده اما به طرز عجیبی بعد از میلیون ها سال نخستین بچه متولد می شود. آلوین که بی اندازه کنجکاو است از دنیای بیرون شهر بداند به رغم همه مشکلات سفری را آغاز می کند که حقیقت شهر و تاریخ بشر را بیابد.",
    genre = "فانتزی")

book.objects.create(
    name="مجموعه دزد جادوگر",
    writer="سارا پرینیز",
    summery="کتاب روایتگر ماجراهای پسرکی به نام کان و فراز و نشیب های زندگی او در مسیر تبدیل شدن از یک دزد به جادوگر است. کان در این مسیر با چالش‌های فراوانی روبرو است. شهر جادویی ولمت پر از جادوگرانی است که کان را به عنوان جادوگر به رسمیت نمی شناسند و همین سبب رخ دادن حوادث تلخ و شیرین بسیار برای او می شود.",
    genre = "فانتزی")

book.objects.create(
    name="ملکه سرخ",
    writer="ویکتوریا اویارد",
    summery="این کتاب داستانی را روایت می کند که بر اساس رنگ خون مردم به دو قسمت تقسیم شده اند. سرخ برای مردم معمولی و نقره‌ای برای مردم برتر که توانایی های خارق العاده ای دارند. مر دزد خیابانی ای که هرچه بتواند می دزدد تا به خانواده اش کمک کند، سعی می‌کند بهترین دوستش را از سربازگیری و رفتن به ارتش نجات بدهد. این ماموریت باعث می شود او در نهایت به قصر راه پیدا کند و در آنجا جلوی پادشاه و دیگر اعضای شورا قدرت های خاصی از خود بروز دهد. قدرت هایی که مناسب یک سرخ نیستند.",
    genre = "فانتزی")

book.objects.create(
    name="مجموعه کتاب‌های تلماسه",
    writer="فرانک هربت",
    summery="بعد از دوره تاریخی «جهاد بزرگ باتلری» تولید ربات‌ها و کامپیوترها رونق یافت. همین عامل باعث شد، مردم مجبور شوند توانایی‌های جسمی و ذهنی خود را پرورش دهند. آن‌ها برای این کار از ماده‌ای بنام ملانژ استفاده می‌کنند که قدرت ذهنی انسان را افزایش و پیش‌بینی‌های دقیقی انجام میدهد. ملانژ، ماده‌ای کمیاب است که از ماسه‌های منطقه آراکیس ساخته می‌شوند و افرادی که برای استخراج آن به آراکیس اعزام می‌شوند، مجبورند با آب و هوای وحشتناک آن مقابله کنند. داستان اصلی تلماسه، درباره جنگ میان ۳ خاندان برای تصاحب سیاره‌ آراکیس است.",
    genre = "علمی تخیلی")

book.objects.create(
    name="مریخی",
    writer="اندی وییر",
    summery="مارک واتنی از خدمه ی دومین گروه فضانوردان ناسا است که بر سطح مریخ فرود آمده اند. به دلیل طوفان شدید در مریخ گروه در نهایت عجله مریخ را ترک می کرده و در این بین مارک را به دلیل آسیت دیدگی شدید و تصور مردنش رها کرده و می روند. اما مارک زنده است و مجبور است چهار سال تا آمدن گروه بعدی صبر کند، با توجه به اینکه کمتر از یکسال جیره غذایی دارد و هیچ ارتباط مخابراتی هم با زمین ندارد.",
    genre = "علمی تخیلی")

book.objects.create(
    name="پیک نیک در جاده",
    writer="آر کادی بوریس استروگانسکی",
    summery="این کتاب روایتگر داستان مشهور بازدید بیگانگان از زمین است با این تفاوت که این بار بین انسان ها و بیگانگان دیداری صورت نمی گیرد. نه تنها انسان‌ها بیگانگان مذکور را ندیده‌اند بلکه طبق شواهد موجود آنها نیز متوجه حضور انسان ها نشده یا اصلاً به حضور شان اهمیت نداده اند. تنهانتیجه ی این بازدید به وجود آمدن ۶ ناحیه روی کره زمین است. این نواحی پر از پدیده ها، اشیا و فناوری های بیگانه هستند که حتی بهترین دانشمندان نیز قادر به توضیح دادن شان نیستند ولی برای بسیاری از آنها کاربرد عملی پیدا کرده و مدعی هستند که آنچه بیگانگان از خود روی زمین به جا گذاشته اند می تواند مسیر پیشرفت تاریخ بشریت را برای همیشه عوض کند.",
    genre = "علمی تخیلی")











    