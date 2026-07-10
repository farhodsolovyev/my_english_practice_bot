"""Тексты для аудирования по уровням CEFR (A1–C1), по ~30 на уровень.
Автогенерация (LLM) с выборочной проверкой. Поля: title, content(EN), translation(RU), level."""

TEXTS = [
  {
    "id": 1,
    "title": "About Me",
    "content": "Hello! My name is Anna. I am ten years old. I am a girl. I am a pupil. I live in a big city. I like music and books. I am happy. This is me.",
    "translation": "Привет! Меня зовут Анна. Мне десять лет. Я девочка. Я ученица. Я живу в большом городе. Я люблю музыку и книги. Я счастлива. Это я.",
    "level": "A1"
  },
  {
    "id": 2,
    "title": "My Colours",
    "content": "I like colours. My hat is red. My bag is blue. My shoes are black. My cat is white. My book is green. The sun is yellow. I have a big box of pens. I am happy.",
    "translation": "Я люблю цвета. Моя шапка красная. Моя сумка синяя. Мои ботинки чёрные. Мой кот белый. Моя книга зелёная. Солнце жёлтое. У меня есть большая коробка ручек. Я счастлива.",
    "level": "A1"
  },
  {
    "id": 3,
    "title": "My Family",
    "content": "This is my family. I have a mother and a father. I have one brother. His name is Max. My mother is a doctor. My father is a teacher. We live in a house. I love my family.",
    "translation": "Это моя семья. У меня есть мама и папа. У меня есть один брат. Его зовут Макс. Моя мама врач. Мой папа учитель. Мы живём в доме. Я люблю свою семью.",
    "level": "A1"
  },
  {
    "id": 4,
    "title": "My Cat",
    "content": "I have a cat. Her name is Kitty. She is small and white. She has big green eyes. She likes milk and fish. She sleeps on my bed. She plays with a ball. I love my cat.",
    "translation": "У меня есть кошка. Её зовут Китти. Она маленькая и белая. У неё большие зелёные глаза. Она любит молоко и рыбу. Она спит на моей кровати. Она играет с мячиком. Я люблю свою кошку.",
    "level": "A1"
  },
  {
    "id": 5,
    "title": "My Home",
    "content": "I live in a small house. My house has four rooms. We have a kitchen and a big room. My room is small. It has a bed and a table. I have many books. I like my home.",
    "translation": "Я живу в маленьком доме. В моём доме четыре комнаты. У нас есть кухня и большая комната. Моя комната маленькая. В ней есть кровать и стол. У меня много книг. Мне нравится мой дом.",
    "level": "A1"
  },
  {
    "id": 6,
    "title": "The Weather",
    "content": "Today is a good day. The sun is hot. The sky is blue. I see white clouds. It is not cold. It is warm. I go to the park. I play with my friends. I am very happy.",
    "translation": "Сегодня хороший день. Солнце горячее. Небо голубое. Я вижу белые облака. Не холодно. Тепло. Я иду в парк. Я играю с друзьями. Я очень счастлив.",
    "level": "A1"
  },
  {
    "id": 7,
    "title": "My Breakfast",
    "content": "I eat breakfast in the morning. I have bread and butter. I eat an egg. I drink milk. My mother makes tea. I like apples. I eat one apple. Breakfast is good. Now I go to school.",
    "translation": "Я завтракаю утром. У меня есть хлеб с маслом. Я ем яйцо. Я пью молоко. Моя мама делает чай. Я люблю яблоки. Я ем одно яблоко. Завтрак вкусный. Теперь я иду в школу.",
    "level": "A1"
  },
  {
    "id": 8,
    "title": "My Dog",
    "content": "I have a dog. His name is Rex. He is big and brown. He has long ears. He likes to run and play. He eats meat. He sleeps near the door. Rex is my best friend. I love him.",
    "translation": "У меня есть собака. Её зовут Рекс. Он большой и коричневый. У него длинные уши. Он любит бегать и играть. Он ест мясо. Он спит у двери. Рекс мой лучший друг. Я люблю его.",
    "level": "A1"
  },
  {
    "id": 9,
    "title": "My Room",
    "content": "This is my room. It is not big. My bed is by the window. I have a small table and a chair. My books are on the table. My red bag is on the floor. I like my room very much.",
    "translation": "Это моя комната. Она не большая. Моя кровать у окна. У меня есть маленький стол и стул. Мои книги на столе. Моя красная сумка на полу. Мне очень нравится моя комната.",
    "level": "A1"
  },
  {
    "id": 10,
    "title": "Animals On A Farm",
    "content": "I like animals. On the farm I see a cow. The cow is big. I see a horse and a pig. I see many hens. The hens are small. The dog runs fast. I like the farm animals.",
    "translation": "Я люблю животных. На ферме я вижу корову. Корова большая. Я вижу лошадь и свинью. Я вижу много кур. Куры маленькие. Собака бегает быстро. Мне нравятся животные на ферме.",
    "level": "A1"
  },
  {
    "id": 11,
    "title": "My Lunch",
    "content": "I eat lunch at school. I have soup and rice. I eat some chicken. I like vegetables too. I drink water. My friend has fish. We eat together. The food is good. After lunch we play in the yard.",
    "translation": "Я обедаю в школе. У меня есть суп и рис. Я ем немного курицы. Я тоже люблю овощи. Я пью воду. У моего друга есть рыба. Мы едим вместе. Еда вкусная. После обеда мы играем во дворе.",
    "level": "A1"
  },
  {
    "id": 12,
    "title": "My Day",
    "content": "I get up at seven. I wash my face and eat breakfast. Then I go to school. I study English and maths. I come home at three. I do my homework. In the evening I read a book. Then I sleep.",
    "translation": "Я встаю в семь. Я умываюсь и завтракаю. Потом я иду в школу. Я изучаю английский и математику. Я прихожу домой в три. Я делаю уроки. Вечером я читаю книгу. Потом я сплю.",
    "level": "A1"
  },
  {
    "id": 13,
    "title": "Seasons And Weather",
    "content": "There are four seasons. In summer it is hot and sunny. In winter it is cold. Snow is white. In autumn it rains. Leaves are red and yellow. In spring flowers grow. I like spring the most.",
    "translation": "Есть четыре времени года. Летом жарко и солнечно. Зимой холодно. Снег белый. Осенью идёт дождь. Листья красные и жёлтые. Весной растут цветы. Больше всего я люблю весну.",
    "level": "A1"
  },
  {
    "id": 14,
    "title": "My Grandparents",
    "content": "I have kind grandparents. My grandmother lives in a village. She has a garden with red apples. My grandfather has a big grey cat. They have hens and a cow. I visit them in summer. I love my grandparents.",
    "translation": "У меня добрые бабушка и дедушка. Моя бабушка живёт в деревне. У неё есть сад с красными яблоками. У моего дедушки большой серый кот. У них есть куры и корова. Я навещаю их летом. Я люблю своих бабушку и дедушку.",
    "level": "A1"
  },
  {
    "id": 15,
    "title": "Things In My Bag",
    "content": "This is my school bag. It is blue and green. In my bag I have books and pens. I have a red pencil and a ruler. I have a small notebook. My lunch is here too. My bag is heavy but I like it.",
    "translation": "Это мой школьный рюкзак. Он синий с зелёным. В рюкзаке у меня есть книги и ручки. У меня есть красный карандаш и линейка. У меня есть маленькая тетрадь. Мой обед тоже здесь. Мой рюкзак тяжёлый, но он мне нравится.",
    "level": "A1"
  },
  {
    "id": 16,
    "title": "My Friends",
    "content": "I have two friends. Their names are Tom and Anna. We play together every day. Tom likes games. Anna likes music. They are very kind. We laugh a lot. I like my friends. They are the best.",
    "translation": "У меня есть два друга. Их зовут Том и Анна. Мы играем вместе каждый день. Том любит игры. Анна любит музыку. Они очень добрые. Мы много смеёмся. Я люблю своих друзей. Они самые лучшие.",
    "level": "A1"
  },
  {
    "id": 17,
    "title": "At School",
    "content": "I go to school every day. My school is big. I have many friends here. We read books and write. Our teacher is nice. I like math and art. School starts at eight. I like my school very much.",
    "translation": "Я хожу в школу каждый день. Моя школа большая. У меня здесь много друзей. Мы читаем книги и пишем. Наша учительница добрая. Мне нравятся математика и рисование. Школа начинается в восемь. Мне очень нравится моя школа.",
    "level": "A1"
  },
  {
    "id": 18,
    "title": "My Hobby",
    "content": "I like to draw. It is my hobby. I draw cats, cars and trees. I have many colours. I draw every evening. My mom likes my pictures. Drawing makes me happy. I want to be an artist.",
    "translation": "Я люблю рисовать. Это моё хобби. Я рисую котов, машины и деревья. У меня много красок. Я рисую каждый вечер. Моей маме нравятся мои рисунки. Рисование делает меня счастливым. Я хочу стать художником.",
    "level": "A1"
  },
  {
    "id": 19,
    "title": "I Play Football",
    "content": "I love football. I play it every week. I play with my friends in the park. We run and kick the ball. Football is fun. My team is good. We win many games. I am happy when I play.",
    "translation": "Я люблю футбол. Я играю в него каждую неделю. Я играю с друзьями в парке. Мы бегаем и пинаем мяч. Футбол весёлый. Моя команда хорошая. Мы выигрываем много игр. Я счастлив, когда играю.",
    "level": "A1"
  },
  {
    "id": 20,
    "title": "My Clothes",
    "content": "I have many clothes. I like my blue shirt. I wear jeans and shoes. In winter I wear a warm coat. In summer I wear a T-shirt. My cap is red. I like nice clothes. They are comfortable.",
    "translation": "У меня много одежды. Мне нравится моя синяя рубашка. Я ношу джинсы и ботинки. Зимой я ношу тёплое пальто. Летом я ношу футболку. Моя кепка красная. Мне нравится красивая одежда. Она удобная.",
    "level": "A1"
  },
  {
    "id": 21,
    "title": "Board Games",
    "content": "My family likes games. We play board games on Sunday. I like chess and cards. My sister likes puzzles. We sit at the table together. Sometimes I win. Sometimes I lose. Games are fun. We laugh and talk.",
    "translation": "Моя семья любит игры. Мы играем в настольные игры по воскресеньям. Мне нравятся шахматы и карты. Моей сестре нравятся пазлы. Мы сидим за столом вместе. Иногда я выигрываю. Иногда я проигрываю. Игры весёлые. Мы смеёмся и разговариваем.",
    "level": "A1"
  },
  {
    "id": 22,
    "title": "The Shop",
    "content": "There is a shop near my home. I go there with my mom. We buy bread, milk and fruit. The shop is small but nice. The woman there is kind. We pay money. Then we go home. I like this shop.",
    "translation": "Рядом с моим домом есть магазин. Я хожу туда с мамой. Мы покупаем хлеб, молоко и фрукты. Магазин маленький, но хороший. Женщина там добрая. Мы платим деньги. Потом мы идём домой. Мне нравится этот магазин.",
    "level": "A1"
  },
  {
    "id": 23,
    "title": "I Ride a Bike",
    "content": "I have a new bike. It is green. I ride it every day. I ride in the park with my friend. We go fast. The bike is fun. I like fresh air. Riding a bike is my favourite thing.",
    "translation": "У меня есть новый велосипед. Он зелёный. Я катаюсь на нём каждый день. Я катаюсь в парке с другом. Мы едем быстро. Велосипед весёлый. Мне нравится свежий воздух. Катание на велосипеде — моё любимое занятие.",
    "level": "A1"
  },
  {
    "id": 24,
    "title": "The Bus",
    "content": "I go to school by bus. The bus is yellow. It comes at seven. I wait at the bus stop. Many people are on the bus. I sit near the window. I look at the city. The bus is not slow.",
    "translation": "Я езжу в школу на автобусе. Автобус жёлтый. Он приходит в семь. Я жду на остановке. В автобусе много людей. Я сижу у окна. Я смотрю на город. Автобус не медленный.",
    "level": "A1"
  },
  {
    "id": 25,
    "title": "My City",
    "content": "I live in a big city. The city has many streets and shops. There is a park and a museum. Many cars go on the roads. People walk fast. I like my city. It is busy but nice. I feel happy here.",
    "translation": "Я живу в большом городе. В городе много улиц и магазинов. Есть парк и музей. По дорогам едет много машин. Люди ходят быстро. Мне нравится мой город. Он суетливый, но хороший. Я чувствую себя счастливым здесь.",
    "level": "A1"
  },
  {
    "id": 26,
    "title": "Summer Holidays",
    "content": "I like summer. In summer we have holidays. We do not go to school. The sun is warm. I swim in the river. I play outside all day. I eat ice cream. Summer is my favourite time of the year.",
    "translation": "Я люблю лето. Летом у нас каникулы. Мы не ходим в школу. Солнце тёплое. Я плаваю в реке. Я играю на улице весь день. Я ем мороженое. Лето — моё любимое время года.",
    "level": "A1"
  },
  {
    "id": 27,
    "title": "The New Year",
    "content": "The New Year is my favourite holiday. It is in winter. We have a big tree at home. I give presents to my family. We eat a lot and sing songs. My friends come to my house. We are all happy.",
    "translation": "Новый год — мой любимый праздник. Он зимой. У нас дома большая ёлка. Я дарю подарки своей семье. Мы много едим и поём песни. Мои друзья приходят ко мне домой. Мы все счастливы.",
    "level": "A1"
  },
  {
    "id": 28,
    "title": "In the Library",
    "content": "I like the library. It is in my school. There are many books there. I read stories about animals and cars. The library is quiet. I sit and read for one hour. I take books home. Reading is good for me.",
    "translation": "Мне нравится библиотека. Она в моей школе. Там много книг. Я читаю истории о животных и машинах. В библиотеке тихо. Я сижу и читаю один час. Я беру книги домой. Чтение полезно для меня.",
    "level": "A1"
  },
  {
    "id": 29,
    "title": "Four Seasons",
    "content": "There are four seasons. In spring flowers grow. In summer it is hot and sunny. In autumn leaves fall down. In winter it is cold and white. I like every season. Each season is different and beautiful. Nature is amazing.",
    "translation": "Есть четыре времени года. Весной растут цветы. Летом жарко и солнечно. Осенью падают листья. Зимой холодно и бело. Мне нравится каждое время года. Каждый сезон разный и красивый. Природа удивительна.",
    "level": "A1"
  },
  {
    "id": 30,
    "title": "Sports Day",
    "content": "Today is sports day at school. All students go to the field. We run, jump and play games. My friend runs very fast. I jump high. The teachers watch us. We get medals. Sports day is exciting. I feel strong and happy.",
    "translation": "Сегодня в школе день спорта. Все ученики идут на поле. Мы бегаем, прыгаем и играем в игры. Мой друг бегает очень быстро. Я прыгаю высоко. Учителя смотрят на нас. Мы получаем медали. День спорта захватывающий. Я чувствую себя сильным и счастливым.",
    "level": "A1"
  },
  {
    "id": 31,
    "title": "My Morning",
    "content": "I get up at seven o'clock every day. First, I wash my face and brush my teeth. Then I eat breakfast. I like bread, eggs and tea. After breakfast, I put on my coat and go to work. I walk to the bus stop. The bus comes at eight. I am never late.",
    "translation": "Я встаю в семь часов каждый день. Сначала я умываю лицо и чищу зубы. Потом я завтракаю. Я люблю хлеб, яйца и чай. После завтрака я надеваю пальто и иду на работу. Я иду пешком до автобусной остановки. Автобус приходит в восемь. Я никогда не опаздываю.",
    "level": "A2"
  },
  {
    "id": 32,
    "title": "After School",
    "content": "My son comes home from school at three. He is often hungry. First, he eats lunch in the kitchen. Then he does his homework. It is not always easy. At five o'clock, he plays football with his friends. In the evening, we watch TV together. He goes to bed at nine.",
    "translation": "Мой сын приходит домой из школы в три. Он часто голодный. Сначала он обедает на кухне. Потом он делает домашнюю работу. Это не всегда легко. В пять часов он играет в футбол с друзьями. Вечером мы вместе смотрим телевизор. Он ложится спать в девять.",
    "level": "A2"
  },
  {
    "id": 33,
    "title": "At the Shop",
    "content": "On Saturday, I go to the small shop near my house. I need milk, bread and some fruit. The apples are cheap today, so I buy six. The bread costs two dollars. I pay with money from my bag. The shop woman is kind. She gives me a bag. Then I walk home slowly.",
    "translation": "В субботу я иду в маленький магазин рядом с моим домом. Мне нужно молоко, хлеб и немного фруктов. Яблоки сегодня дешёвые, поэтому я покупаю шесть. Хлеб стоит два доллара. Я плачу деньгами из моей сумки. Продавщица добрая. Она даёт мне пакет. Потом я медленно иду домой.",
    "level": "A2"
  },
  {
    "id": 34,
    "title": "My Favourite Food",
    "content": "I love pizza very much. My mother makes it on Fridays. She uses cheese, tomatoes and mushrooms. The kitchen smells very good. My little sister helps her. We all sit at the table and eat together. I always want more! After dinner, we have ice cream. Friday is my favourite day of the week.",
    "translation": "Я очень люблю пиццу. Моя мама готовит её по пятницам. Она использует сыр, помидоры и грибы. На кухне очень вкусно пахнет. Моя младшая сестра ей помогает. Мы все садимся за стол и едим вместе. Мне всегда хочется ещё! После ужина мы едим мороженое. Пятница — мой любимый день недели.",
    "level": "A2"
  },
  {
    "id": 35,
    "title": "The Doctor",
    "content": "Yesterday I felt very bad. My head hurt and I was hot. My mother took me to the doctor. The doctor looked at my throat and my ears. He said, \"You have a cold. Stay in bed and drink hot tea.\" I took some medicine. Today I feel much better. Now I can go to school again.",
    "translation": "Вчера я чувствовал себя очень плохо. У меня болела голова, и мне было жарко. Мама отвела меня к врачу. Врач осмотрел моё горло и уши. Он сказал: «У тебя простуда. Оставайся в постели и пей горячий чай». Я принял лекарство. Сегодня я чувствую себя намного лучше. Теперь я снова могу идти в школу.",
    "level": "A2"
  },
  {
    "id": 36,
    "title": "New Shoes",
    "content": "Last week I wanted new shoes. I went to a big shop in the city with my friend. There were many shoes there. I tried black ones and brown ones. The brown shoes were too small. The black shoes were perfect. They cost forty dollars. I paid and put them on. My old shoes went in the bag.",
    "translation": "На прошлой неделе мне понадобились новые туфли. Я пошёл в большой магазин в городе с другом. Там было много обуви. Я примерил чёрные и коричневые. Коричневые туфли были слишком маленькими. Чёрные туфли были идеальными. Они стоили сорок долларов. Я заплатил и надел их. Мои старые туфли отправились в пакет.",
    "level": "A2"
  },
  {
    "id": 37,
    "title": "My Weekend",
    "content": "Last weekend was great. On Saturday morning, I cleaned my room and washed the car. In the afternoon, I met my friends in the park. We played games and ate sandwiches. On Sunday, I visited my grandmother. She made a big cake for me. We talked for hours. I went home late and slept very well.",
    "translation": "Прошлые выходные были замечательными. В субботу утром я убрал свою комнату и помыл машину. Днём я встретился с друзьями в парке. Мы играли в игры и ели бутерброды. В воскресенье я навестил бабушку. Она испекла для меня большой торт. Мы разговаривали часами. Я вернулся домой поздно и очень хорошо спал.",
    "level": "A2"
  },
  {
    "id": 38,
    "title": "At the Café",
    "content": "On Sunday, my sister and I went to a small café in town. We sat by the window. A waiter came and gave us the menu. I ordered a coffee and a piece of cake. My sister had tea and a sandwich. The food was very good. We talked and laughed for an hour. Then we paid and left.",
    "translation": "В воскресенье мы с сестрой пошли в маленькое кафе в городе. Мы сели у окна. Официант подошёл и дал нам меню. Я заказал кофе и кусок торта. Моя сестра взяла чай и бутерброд. Еда была очень вкусной. Мы разговаривали и смеялись целый час. Потом мы заплатили и ушли.",
    "level": "A2"
  },
  {
    "id": 39,
    "title": "A Rainy Day",
    "content": "Last Monday it rained all day. I could not go outside. In the morning, I stayed at home and read a book. Then I made hot soup for lunch. My brother watched a film with me in the afternoon. We drank tea and ate biscuits. In the evening, the rain stopped. Tomorrow we will go for a walk.",
    "translation": "В прошлый понедельник весь день шёл дождь. Я не мог выйти на улицу. Утром я остался дома и читал книгу. Потом я приготовил горячий суп на обед. Днём мой брат смотрел со мной фильм. Мы пили чай и ели печенье. Вечером дождь прекратился. Завтра мы пойдём на прогулку.",
    "level": "A2"
  },
  {
    "id": 40,
    "title": "Going to the Beach",
    "content": "Every summer my family goes to the beach. We take a big car and drive for three hours. My father brings food and water. When we arrive, my brother and I run to the sea. The water is warm. We swim and build sand castles. My mother reads under an umbrella. In the evening, we are tired but happy.",
    "translation": "Каждое лето моя семья ездит на пляж. Мы берём большую машину и едем три часа. Мой папа берёт еду и воду. Когда мы приезжаем, мы с братом бежим к морю. Вода тёплая. Мы плаваем и строим замки из песка. Моя мама читает под зонтом. Вечером мы уставшие, но счастливые.",
    "level": "A2"
  },
  {
    "id": 41,
    "title": "My Birthday Money",
    "content": "For my birthday, my parents gave me some money. I was very happy. I thought about it for a week. I wanted a new bicycle, but it was too expensive. In the end, I bought some books and a football. I also saved ten dollars in my box. Next month I will buy a nice game with it.",
    "translation": "На день рождения родители подарили мне немного денег. Я был очень счастлив. Я думал об этом целую неделю. Я хотел новый велосипед, но он был слишком дорогой. В итоге я купил несколько книг и футбольный мяч. Ещё я отложил десять долларов в мою коробку. В следующем месяце я куплю на них хорошую игру.",
    "level": "A2"
  },
  {
    "id": 42,
    "title": "The Train Trip",
    "content": "Last month we took a train to another city. We got up early and went to the station. The train was fast and clean. I looked out of the window at the green fields and small houses. We ate our lunch on the train. After two hours, we arrived. My aunt was there. She was very happy to see us.",
    "translation": "В прошлом месяце мы поехали на поезде в другой город. Мы встали рано и пошли на вокзал. Поезд был быстрый и чистый. Я смотрел в окно на зелёные поля и маленькие дома. Мы пообедали в поезде. Через два часа мы приехали. Моя тётя была там. Она была очень рада нас видеть.",
    "level": "A2"
  },
  {
    "id": 43,
    "title": "Keeping Healthy",
    "content": "I want to be healthy, so I do many things. Every morning I run in the park for twenty minutes. I eat a lot of fruit and vegetables. I do not eat much sugar. I drink water, not cola. I go to bed early and sleep eight hours. On the weekend, I swim or ride my bike. I feel strong and happy.",
    "translation": "Я хочу быть здоровым, поэтому я делаю много всего. Каждое утро я бегаю в парке двадцать минут. Я ем много фруктов и овощей. Я не ем много сахара. Я пью воду, а не колу. Я рано ложусь спать и сплю восемь часов. По выходным я плаваю или катаюсь на велосипеде. Я чувствую себя сильным и счастливым.",
    "level": "A2"
  },
  {
    "id": 44,
    "title": "Our Summer Holiday",
    "content": "Last summer we went on holiday to Italy. We stayed in a small hotel near the sea for one week. Every day we visited old towns and took many photos. The food was amazing, and we ate pasta and pizza. One day we climbed a big hill. The view was beautiful. Next year we will visit Spain instead.",
    "translation": "Прошлым летом мы ездили в отпуск в Италию. Мы жили в маленьком отеле у моря одну неделю. Каждый день мы посещали старые города и делали много фотографий. Еда была потрясающей, и мы ели пасту и пиццу. Однажды мы поднялись на большой холм. Вид был красивый. В следующем году мы вместо этого поедем в Испанию.",
    "level": "A2"
  },
  {
    "id": 45,
    "title": "A Busy Day",
    "content": "Yesterday was a very busy day. In the morning, I went shopping and bought food for the week. Then I cooked lunch for my family. In the afternoon, I took my dog to the doctor because his leg hurt. Later, I paid some bills at the bank. In the evening, I was very tired, so I went to bed early.",
    "translation": "Вчера был очень напряжённый день. Утром я пошёл за покупками и купил еду на неделю. Потом я приготовил обед для моей семьи. Днём я отвёл свою собаку к врачу, потому что у неё болела лапа. Позже я оплатил несколько счетов в банке. Вечером я очень устал, поэтому лёг спать рано.",
    "level": "A2"
  },
  {
    "id": 46,
    "title": "My Best Friend",
    "content": "I have a best friend. Her name is Anna. We met at school five years ago. Anna is kind and funny. We like the same music and films. Every Saturday we meet in the park. We talk and laugh a lot. Last week we watched a film together. Next Sunday we will go to the cinema. I am very happy to have her.",
    "translation": "У меня есть лучшая подруга. Её зовут Анна. Мы познакомились в школе пять лет назад. Анна добрая и весёлая. Нам нравится одинаковая музыка и фильмы. Каждую субботу мы встречаемся в парке. Мы много разговариваем и смеёмся. На прошлой неделе мы вместе посмотрели фильм. В следующее воскресенье мы пойдём в кино. Я очень рада, что она у меня есть.",
    "level": "A2"
  },
  {
    "id": 47,
    "title": "My Phone",
    "content": "I have a new phone. It is black and small. I use it every day. I call my mother and text my friends. On my phone I take photos and play games. Sometimes I read the news. Yesterday my phone was very slow. My brother helped me. Now it works well. I like my phone very much. It is a good helper.",
    "translation": "У меня есть новый телефон. Он чёрный и маленький. Я пользуюсь им каждый день. Я звоню маме и пишу друзьям. На телефоне я делаю фотографии и играю в игры. Иногда я читаю новости. Вчера мой телефон был очень медленным. Мой брат помог мне. Теперь он работает хорошо. Мне очень нравится мой телефон. Он хороший помощник.",
    "level": "A2"
  },
  {
    "id": 48,
    "title": "A Rainy Day",
    "content": "Today the weather is bad. It is cold and grey. It rains all day. I stay at home with my cat. I drink hot tea and read a book. My mother makes soup for lunch. Outside the streets are wet. Yesterday the sun was warm and bright. Tomorrow the weather will be better. I hope the sun will come back soon.",
    "translation": "Сегодня плохая погода. Холодно и серо. Дождь идёт весь день. Я остаюсь дома с моим котом. Я пью горячий чай и читаю книгу. Мама готовит суп на обед. На улице мокрые дороги. Вчера солнце было тёплым и ярким. Завтра погода будет лучше. Я надеюсь, что солнце скоро вернётся.",
    "level": "A2"
  },
  {
    "id": 49,
    "title": "My Hobby",
    "content": "My hobby is drawing. I love it very much. I draw animals, flowers and people. I have many pencils and paper. Every evening I draw for one hour. It makes me calm and happy. Last year I drew a big picture of the sea. My teacher liked it a lot. Next month I will show my pictures at school. Art is my favourite thing.",
    "translation": "Моё хобби — рисование. Я очень его люблю. Я рисую животных, цветы и людей. У меня много карандашей и бумаги. Каждый вечер я рисую один час. Это делает меня спокойным и счастливым. В прошлом году я нарисовал большую картину моря. Моему учителю она очень понравилась. В следующем месяце я покажу свои картины в школе. Искусство — моё любимое занятие.",
    "level": "A2"
  },
  {
    "id": 50,
    "title": "At School",
    "content": "I am a student. My school is big and old. I go there every morning. My favourite subject is English. I also like maths and art. My teachers are kind and clever. At lunch I eat with my friends. Yesterday we had a test in history. It was not easy. Tomorrow we will start a new book. I like my school very much.",
    "translation": "Я ученик. Моя школа большая и старая. Я хожу туда каждое утро. Мой любимый предмет — английский. Мне также нравятся математика и рисование. Мои учителя добрые и умные. На обеде я ем с друзьями. Вчера у нас была контрольная по истории. Она была нелёгкой. Завтра мы начнём новую книгу. Мне очень нравится моя школа.",
    "level": "A2"
  },
  {
    "id": 51,
    "title": "My Father's Job",
    "content": "My father is a doctor. He works in a big hospital. He helps sick people every day. He starts work early in the morning. Sometimes he works at night too. My father likes his job very much. Last week he helped an old man. The man was very thankful. When I grow up, I will be a doctor too. I am proud of my father.",
    "translation": "Мой папа — врач. Он работает в большой больнице. Он помогает больным людям каждый день. Он начинает работу рано утром. Иногда он работает и ночью. Мой папа очень любит свою работу. На прошлой неделе он помог пожилому мужчине. Мужчина был очень благодарен. Когда я вырасту, я тоже стану врачом. Я горжусь своим папой.",
    "level": "A2"
  },
  {
    "id": 52,
    "title": "Winter Fun",
    "content": "Winter is my favourite season. It is cold and white. Snow falls on the trees and houses. I wear a warm coat, a hat and gloves. My friends and I play in the snow. We make a big snowman with a carrot nose. Last winter we went skiing in the mountains. It was great fun. Next winter I want to try ice skating too.",
    "translation": "Зима — моё любимое время года. Она холодная и белая. Снег падает на деревья и дома. Я надеваю тёплое пальто, шапку и перчатки. Мы с друзьями играем в снегу. Мы лепим большого снеговика с носом из морковки. Прошлой зимой мы ездили кататься на лыжах в горы. Это было очень весело. Следующей зимой я хочу попробовать и кататься на коньках.",
    "level": "A2"
  },
  {
    "id": 53,
    "title": "My Birthday Party",
    "content": "Last week I had a birthday party. I was twelve years old. My friends came to my house. My mother made a big chocolate cake. We ate pizza and drank juice. We played games and danced. My best friend gave me a nice book. I was very happy all day. It was the best party. Next year I want a party in the park.",
    "translation": "На прошлой неделе у меня был день рождения. Мне исполнилось двенадцать лет. Мои друзья пришли ко мне домой. Мама сделала большой шоколадный торт. Мы ели пиццу и пили сок. Мы играли в игры и танцевали. Мой лучший друг подарил мне хорошую книгу. Я был очень счастлив весь день. Это была лучшая вечеринка. В следующем году я хочу вечеринку в парке.",
    "level": "A2"
  },
  {
    "id": 54,
    "title": "Playing Football",
    "content": "My favourite hobby is football. I play it every weekend with my friends. We have a small team of ten boys. I play in the middle of the field. Football is fast and fun. Last Sunday we had a big match. We won three to one. I was very happy. Our coach was proud of us. Next month we will play against another school.",
    "translation": "Моё любимое хобби — футбол. Я играю в него каждые выходные с друзьями. У нас маленькая команда из десяти мальчиков. Я играю в середине поля. Футбол быстрый и весёлый. В прошлое воскресенье у нас был большой матч. Мы выиграли три — один. Я был очень счастлив. Наш тренер гордился нами. В следующем месяце мы сыграем против другой школы.",
    "level": "A2"
  },
  {
    "id": 55,
    "title": "Learning Online",
    "content": "These days I study English online. I use my computer and a special app. Every evening I watch short videos and do exercises. The app has many games with new words. It is easy and fun to use. Last month I learned a hundred new words. My teacher was happy with me. Soon I will speak with a real teacher on video. Technology helps me learn.",
    "translation": "В эти дни я учу английский онлайн. Я использую компьютер и специальное приложение. Каждый вечер я смотрю короткие видео и делаю упражнения. В приложении много игр с новыми словами. Им легко и весело пользоваться. В прошлом месяце я выучил сто новых слов. Мой учитель был доволен мной. Скоро я буду говорить с настоящим учителем по видео. Технологии помогают мне учиться.",
    "level": "A2"
  },
  {
    "id": 56,
    "title": "A Day at Work",
    "content": "My mother is a teacher. She works at a small school in our town. She teaches young children to read and write. She loves her job because she loves kids. Yesterday she had a busy day. Her class made a big painting together. The children were happy and loud. In the evening she was tired but glad. Tomorrow she will read them a new story.",
    "translation": "Моя мама — учительница. Она работает в маленькой школе в нашем городе. Она учит маленьких детей читать и писать. Она любит свою работу, потому что любит детей. Вчера у неё был напряжённый день. Её класс вместе сделал большую картину. Дети были счастливы и шумны. Вечером она устала, но была рада. Завтра она прочитает им новую историю.",
    "level": "A2"
  },
  {
    "id": 57,
    "title": "The New Season",
    "content": "Spring is here at last. The cold winter is over now. The days are longer and warmer. Green leaves grow on the trees again. Birds come back and sing every morning. Flowers open in the gardens and parks. Last week I planted red flowers with my grandmother. We watered them together. Soon they will be big and beautiful. I really love spring days.",
    "translation": "Весна наконец пришла. Холодная зима теперь закончилась. Дни стали длиннее и теплее. Зелёные листья снова растут на деревьях. Птицы возвращаются и поют каждое утро. Цветы открываются в садах и парках. На прошлой неделе я посадил красные цветы с бабушкой. Мы поливали их вместе. Скоро они станут большими и красивыми. Я очень люблю весенние дни.",
    "level": "A2"
  },
  {
    "id": 58,
    "title": "My Dream Job",
    "content": "When I finish school, I want to be a pilot. I love planes and the sky. A pilot flies to many countries and meets new people. It is a hard but exciting job. Last summer I went on a plane for the first time. The pilot said hello to us. From that day I knew my dream. I will study hard and work for it.",
    "translation": "Когда я закончу школу, я хочу стать пилотом. Я люблю самолёты и небо. Пилот летает во многие страны и встречает новых людей. Это трудная, но захватывающая работа. Прошлым летом я впервые полетел на самолёте. Пилот поздоровался с нами. С того дня я узнал свою мечту. Я буду усердно учиться и работать ради неё.",
    "level": "A2"
  },
  {
    "id": 59,
    "title": "A Family Celebration",
    "content": "Last Saturday our family had a big celebration. It was my grandmother's seventieth birthday. All our relatives came to her house. My aunt cooked a lot of tasty food. We gave grandmother flowers and a warm scarf. She was very happy and cried a little. After dinner we sang songs and looked at old photos. It was a special day. We will always remember it.",
    "translation": "В прошлую субботу у нашей семьи был большой праздник. Это был семидесятый день рождения моей бабушки. Все наши родственники пришли к ней домой. Моя тётя приготовила много вкусной еды. Мы подарили бабушке цветы и тёплый шарф. Она была очень счастлива и немного плакала. После ужина мы пели песни и смотрели старые фотографии. Это был особенный день. Мы всегда будем его помнить.",
    "level": "A2"
  },
  {
    "id": 60,
    "title": "Technology at Home",
    "content": "Today technology is a big part of our life. In our home we have a computer, a TV and two phones. My father works on his laptop every evening. My sister watches videos on her tablet. We use the internet to find information and talk to family far away. Last year my grandmother learned to use a phone. Now she calls us often. It helps us stay close.",
    "translation": "Сегодня технологии — большая часть нашей жизни. В нашем доме есть компьютер, телевизор и два телефона. Мой папа работает на ноутбуке каждый вечер. Моя сестра смотрит видео на планшете. Мы используем интернет, чтобы находить информацию и разговаривать с далёкой семьёй. В прошлом году моя бабушка научилась пользоваться телефоном. Теперь она часто нам звонит. Это помогает нам оставаться близкими.",
    "level": "A2"
  },
  {
    "id": 61,
    "title": "My First Job",
    "content": "When I was eighteen, I got my first job in a small coffee shop. At first, I felt nervous because I had never worked with customers before. However, after a few weeks, I started to enjoy it. My colleagues were friendly and they helped me a lot. I learned how to make coffee and how to talk to different people. In my opinion, a first job teaches you many important things about life. Even though the work was hard, I am really glad that I did it.",
    "translation": "Когда мне было восемнадцать, я устроился на свою первую работу в маленькой кофейне. Сначала я нервничал, потому что никогда раньше не работал с клиентами. Однако через несколько недель мне стало это нравиться. Мои коллеги были дружелюбными, и они мне очень помогали. Я научился варить кофе и разговаривать с разными людьми. По моему мнению, первая работа учит тебя многим важным вещам о жизни. Хотя работа была тяжёлой, я действительно рад, что сделал это.",
    "level": "B1"
  },
  {
    "id": 62,
    "title": "A Trip To The Sea",
    "content": "Last summer, my family and I travelled to the sea for two weeks. We stayed in a small hotel near the beach. Every morning, we swam in the warm water and then we ate breakfast together. In the afternoon, we walked along the coast and took many photos. I think travelling is one of the best ways to relax and forget your problems. Although the trip was quite expensive, it was worth every penny. I hope we will go back to the same place next year.",
    "translation": "Прошлым летом мы с семьёй поехали на море на две недели. Мы остановились в маленьком отеле недалеко от пляжа. Каждое утро мы плавали в тёплой воде, а потом вместе завтракали. Днём мы гуляли вдоль побережья и делали много фотографий. Я думаю, что путешествия — один из лучших способов расслабиться и забыть о своих проблемах. Хотя поездка была довольно дорогой, она стоила каждой копейки. Надеюсь, в следующем году мы вернёмся в то же самое место.",
    "level": "B1"
  },
  {
    "id": 63,
    "title": "Living In The City",
    "content": "I have lived in a big city for almost ten years, and I really like it. There is always something to do, such as visiting museums, meeting friends, or going to concerts. Public transport is fast, so I can get anywhere quickly. However, the city can also be noisy and crowded, especially in the morning. Sometimes I dream about a quiet place with fresh air. Still, I believe that city life gives you more chances to study and work. For now, I am happy to stay here.",
    "translation": "Я живу в большом городе почти десять лет, и мне это очень нравится. Всегда есть чем заняться, например, сходить в музеи, встретиться с друзьями или пойти на концерты. Общественный транспорт быстрый, поэтому я могу быстро добраться куда угодно. Однако город также может быть шумным и переполненным, особенно по утрам. Иногда я мечтаю о тихом месте со свежим воздухом. Всё же я считаю, что городская жизнь даёт больше возможностей учиться и работать. Пока что я рад оставаться здесь.",
    "level": "B1"
  },
  {
    "id": 64,
    "title": "Learning A New Language",
    "content": "Two years ago, I decided to learn Spanish because I wanted to travel to Spain. In the beginning, it was really difficult, and I made a lot of mistakes. However, I practised every day and watched short videos online. Little by little, I began to understand more words. Now I can have simple conversations with native speakers. In my opinion, learning a language takes time and patience, but it is worth the effort. When you speak another language, you can meet new people and understand a different culture.",
    "translation": "Два года назад я решил учить испанский, потому что хотел поехать в Испанию. Сначала это было действительно трудно, и я делал много ошибок. Однако я занимался каждый день и смотрел короткие видео в интернете. Мало-помалу я начал понимать больше слов. Теперь я могу вести простые разговоры с носителями языка. По моему мнению, изучение языка требует времени и терпения, но оно стоит усилий. Когда ты говоришь на другом языке, ты можешь знакомиться с новыми людьми и понимать другую культуру.",
    "level": "B1"
  },
  {
    "id": 65,
    "title": "The Old Village",
    "content": "My grandparents live in a small village in the countryside, and I often visit them in summer. The village is very peaceful, and you can hear birds singing everywhere. There are green fields, a small river, and only one shop. Life there is much slower than in the city. At first, I found it boring, but now I really enjoy the calm. I think the countryside is a wonderful place to rest and think. Whenever I feel tired of city life, I go there to relax with my family.",
    "translation": "Мои бабушка и дедушка живут в маленькой деревне в сельской местности, и я часто навещаю их летом. Деревня очень спокойная, и повсюду слышно, как поют птицы. Там есть зелёные поля, маленькая река и всего один магазин. Жизнь там гораздо медленнее, чем в городе. Сначала мне было скучно, но теперь мне очень нравится спокойствие. Я думаю, что сельская местность — чудесное место, чтобы отдохнуть и подумать. Когда я устаю от городской жизни, я еду туда, чтобы расслабиться с семьёй.",
    "level": "B1"
  },
  {
    "id": 66,
    "title": "Saving Our Planet",
    "content": "These days, many people are worried about the environment, and I understand why. We produce too much rubbish, and a lot of it ends up in the ocean. However, I believe that small actions can make a big difference. For example, I have started to recycle plastic and use a reusable bottle. I also walk or ride my bike instead of driving. Of course, one person cannot save the planet alone. But if everybody does something small, together we can protect nature for future generations.",
    "translation": "В наши дни многие люди беспокоятся об окружающей среде, и я понимаю почему. Мы производим слишком много мусора, и большая часть его оказывается в океане. Однако я считаю, что маленькие поступки могут иметь большое значение. Например, я начал перерабатывать пластик и использовать многоразовую бутылку. Я также хожу пешком или езжу на велосипеде вместо машины. Конечно, один человек не может спасти планету в одиночку. Но если каждый сделает что-то маленькое, вместе мы сможем защитить природу для будущих поколений.",
    "level": "B1"
  },
  {
    "id": 67,
    "title": "A Difficult Exam",
    "content": "Last month, I had to take a very difficult exam at university. I studied hard for three weeks and often stayed up late. During the exam, I felt so nervous that I almost forgot everything. Luckily, once I read the first question, I started to feel more confident. When the results came out, I was surprised because I had passed with a good mark. I think this experience taught me that hard work usually pays off. Now I am not so afraid of exams anymore, and I trust myself more.",
    "translation": "В прошлом месяце мне пришлось сдавать очень трудный экзамен в университете. Я усердно готовился три недели и часто засиживался допоздна. Во время экзамена я так нервничал, что чуть не забыл всё. К счастью, как только я прочитал первый вопрос, я начал чувствовать себя увереннее. Когда вышли результаты, я был удивлён, потому что сдал с хорошей оценкой. Я думаю, что этот опыт научил меня, что упорный труд обычно окупается. Теперь я больше не так боюсь экзаменов и больше доверяю себе.",
    "level": "B1"
  },
  {
    "id": 68,
    "title": "Getting Lost Abroad",
    "content": "During my trip to Italy, I got lost in a big city called Rome. I had a map, but I could not understand it at all. At first, I felt scared because I did not speak the language. Then I decided to ask a kind old woman for help. Although she spoke only Italian, she showed me the way with her hands. In the end, I found my hotel safely. Looking back, I think getting lost was actually a good experience, because it taught me not to give up.",
    "translation": "Во время моей поездки в Италию я заблудился в большом городе под названием Рим. У меня была карта, но я совсем не мог в ней разобраться. Сначала я испугался, потому что не говорил на этом языке. Затем я решил попросить помощи у доброй пожилой женщины. Хотя она говорила только по-итальянски, она показала мне дорогу руками. В конце концов я благополучно нашёл свой отель. Оглядываясь назад, я думаю, что потеряться было на самом деле хорошим опытом, потому что это научило меня не сдаваться.",
    "level": "B1"
  },
  {
    "id": 69,
    "title": "Why I Love Reading",
    "content": "Ever since I was a child, I have loved reading books. When I open a good story, I feel like I am travelling to another world. Books have taught me about history, other countries, and different ways of thinking. Although some people prefer films, I believe that reading is better for your imagination. It also helps you to concentrate and relax at the same time. These days, many young people spend hours on their phones instead. In my opinion, they are missing one of the greatest pleasures in life.",
    "translation": "С самого детства я люблю читать книги. Когда я открываю хорошую историю, мне кажется, что я путешествую в другой мир. Книги научили меня истории, другим странам и разным способам мышления. Хотя некоторые люди предпочитают фильмы, я считаю, что чтение лучше для воображения. Оно также помогает тебе сосредоточиться и расслабиться одновременно. В наши дни многие молодые люди вместо этого часами сидят в телефонах. По моему мнению, они упускают одно из величайших удовольствий в жизни.",
    "level": "B1"
  },
  {
    "id": 70,
    "title": "Moving To The Countryside",
    "content": "A few years ago, my family made a big decision and moved from the city to the countryside. At first, I was not happy because I missed my friends and the busy streets. However, over time, I began to appreciate the fresh air and the beautiful views. Now I can grow my own vegetables and enjoy the quiet evenings. Of course, there are fewer shops and the internet is slower. Even so, I honestly believe that our life is healthier and more peaceful than before. I would not go back.",
    "translation": "Несколько лет назад моя семья приняла важное решение и переехала из города в сельскую местность. Сначала я был недоволен, потому что скучал по друзьям и оживлённым улицам. Однако со временем я начал ценить свежий воздух и красивые виды. Теперь я могу выращивать собственные овощи и наслаждаться тихими вечерами. Конечно, здесь меньше магазинов, и интернет медленнее. Тем не менее, я честно считаю, что наша жизнь стала здоровее и спокойнее, чем раньше. Я бы не вернулся назад.",
    "level": "B1"
  },
  {
    "id": 71,
    "title": "An Unforgettable Adventure",
    "content": "Two summers ago, I went hiking in the mountains with a group of friends. We had planned everything carefully, but the weather suddenly changed. It began to rain heavily, and the path became dangerous. Although we were tired and cold, we helped each other and kept walking. Finally, we reached a small hut where we could rest. That night, we laughed about our adventure while drinking hot tea. Looking back, I realise that difficult moments often bring people closer together. It was, without doubt, an experience I will never forget.",
    "translation": "Два лета назад я отправился в поход в горы с группой друзей. Мы всё тщательно спланировали, но погода внезапно изменилась. Начался сильный дождь, и тропа стала опасной. Хотя мы устали и замёрзли, мы помогали друг другу и продолжали идти. Наконец мы добрались до маленькой хижины, где смогли отдохнуть. В ту ночь мы смеялись над нашим приключением, попивая горячий чай. Оглядываясь назад, я понимаю, что трудные моменты часто сближают людей. Это был, без сомнения, опыт, который я никогда не забуду.",
    "level": "B1"
  },
  {
    "id": 72,
    "title": "Studying Online",
    "content": "Since the pandemic, more and more students have started studying online, and I have mixed feelings about it. On one hand, online lessons are very convenient because you can learn from home and save time. On the other hand, it is easy to lose your concentration when nobody is watching you. Personally, I find that I learn better in a real classroom with a teacher and classmates. However, I admit that online courses give people who live far away a great opportunity. In the future, I think both ways will exist together.",
    "translation": "После пандемии всё больше студентов начали учиться онлайн, и у меня смешанные чувства по этому поводу. С одной стороны, онлайн-уроки очень удобны, потому что можно учиться из дома и экономить время. С другой стороны, легко потерять концентрацию, когда за тобой никто не наблюдает. Лично я замечаю, что лучше учусь в настоящем классе с учителем и одноклассниками. Однако я признаю, что онлайн-курсы дают людям, живущим далеко, отличную возможность. В будущем, я думаю, оба способа будут существовать вместе.",
    "level": "B1"
  },
  {
    "id": 73,
    "title": "The Power Of Nature",
    "content": "Whenever I feel stressed, I go for a long walk in the forest near my home. As soon as I step under the tall trees, I feel calmer and my mind becomes clear. Scientists say that spending time in nature is good for both our body and our mind, and I completely agree. Unfortunately, many forests are being cut down every year, which really worries me. I strongly believe that we must protect these green spaces. After all, without nature, our lives would be much poorer and much lonelier.",
    "translation": "Всякий раз, когда я чувствую стресс, я иду на долгую прогулку в лес рядом с домом. Как только я ступаю под высокие деревья, я чувствую себя спокойнее, и мой разум проясняется. Учёные говорят, что время, проведённое на природе, полезно и для тела, и для разума, и я полностью согласен. К сожалению, каждый год вырубается много лесов, что меня по-настоящему беспокоит. Я твёрдо убеждён, что мы должны защищать эти зелёные пространства. В конце концов, без природы наша жизнь была бы гораздо беднее и гораздо одиночнее.",
    "level": "B1"
  },
  {
    "id": 74,
    "title": "A Lesson I Learned",
    "content": "When I was younger, I used to think that success was only about money and fame. However, an important event completely changed my point of view. My best friend became seriously ill, and during that time I understood what truly matters in life. While I was helping him recover, I realised that health, family, and kindness are far more valuable than any career. Since then, I have tried to spend more time with the people I love. In my honest opinion, this is the most important lesson I have ever learned.",
    "translation": "Когда я был моложе, я думал, что успех — это только деньги и слава. Однако одно важное событие полностью изменило мою точку зрения. Мой лучший друг серьёзно заболел, и в то время я понял, что действительно важно в жизни. Пока я помогал ему поправиться, я осознал, что здоровье, семья и доброта гораздо ценнее любой карьеры. С тех пор я стараюсь проводить больше времени с людьми, которых люблю. По моему честному мнению, это самый важный урок, который я когда-либо усвоил.",
    "level": "B1"
  },
  {
    "id": 75,
    "title": "Should We Travel More",
    "content": "Many people say that travelling is one of the best things you can do in life, and I mostly agree with them. When you visit other countries, you learn about new cultures, taste different food, and see the world from another angle. On the other hand, some argue that flying too often harms the environment, and this is a fair point. Personally, I try to travel responsibly by taking trains whenever possible. Although travelling can be expensive and tiring, I am convinced that the memories and lessons it gives us last a lifetime.",
    "translation": "Многие люди говорят, что путешествия — одна из лучших вещей, которые можно сделать в жизни, и я в основном с ними согласен. Когда ты посещаешь другие страны, ты узнаёшь о новых культурах, пробуешь разную еду и видишь мир под другим углом. С другой стороны, некоторые утверждают, что слишком частые полёты вредят окружающей среде, и это справедливое замечание. Лично я стараюсь путешествовать ответственно, выбирая поезда, когда это возможно. Хотя путешествия могут быть дорогими и утомительными, я убеждён, что воспоминания и уроки, которые они нам дают, остаются на всю жизнь.",
    "level": "B1"
  },
  {
    "id": 76,
    "title": "My Morning Phone",
    "content": "Every morning, my phone wakes me up with a soft song. After that, I check the weather and read a few messages from my friends. I think smartphones are really useful because they help me plan my day. However, sometimes I spend too much time looking at the screen. So, last week I decided to leave my phone in another room during breakfast. Now I feel calmer, and I can talk more with my family. Technology is great, but we must use it carefully.",
    "translation": "Каждое утро мой телефон будит меня тихой песней. После этого я проверяю погоду и читаю несколько сообщений от друзей. Я думаю, что смартфоны действительно полезны, потому что они помогают мне планировать мой день. Однако иногда я провожу слишком много времени, глядя в экран. Поэтому на прошлой неделе я решил оставлять телефон в другой комнате во время завтрака. Теперь я чувствую себя спокойнее и могу больше разговаривать со своей семьёй. Технологии — это здорово, но мы должны использовать их аккуратно.",
    "level": "B1"
  },
  {
    "id": 77,
    "title": "Drinking More Water",
    "content": "I used to drink a lot of sweet drinks, and I often felt tired. A few months ago, my doctor told me to drink more water instead. At first, it was difficult because water seemed boring. But now I always carry a bottle with me, and I feel much better. In my opinion, small changes can improve your health a lot. I also try to sleep eight hours every night. Because of these habits, I have more energy for work and sport.",
    "translation": "Раньше я пил много сладких напитков и часто чувствовал усталость. Несколько месяцев назад врач посоветовал мне вместо этого пить больше воды. Сначала это было трудно, потому что вода казалась скучной. Но теперь я всегда ношу с собой бутылку и чувствую себя намного лучше. По моему мнению, небольшие изменения могут сильно улучшить ваше здоровье. Я также стараюсь спать восемь часов каждую ночь. Благодаря этим привычкам у меня больше энергии для работы и спорта.",
    "level": "B1"
  },
  {
    "id": 78,
    "title": "My First Job",
    "content": "Last summer, I got my first real job in a small café. On my first day, I was very nervous because I didn't know anyone. However, my colleagues were friendly, and they showed me everything. I learned how to make coffee and how to talk to customers politely. Although the work was tiring, I enjoyed it a lot. I think a first job teaches you many important skills. Now I feel more confident, and I understand the value of hard work and teamwork.",
    "translation": "Прошлым летом я получил свою первую настоящую работу в маленьком кафе. В первый день я очень нервничал, потому что никого не знал. Однако мои коллеги были дружелюбными, и они показали мне всё. Я научился готовить кофе и вежливо разговаривать с посетителями. Хотя работа была утомительной, мне она очень понравилась. Я думаю, что первая работа учит вас многим важным навыкам. Теперь я чувствую себя увереннее и понимаю ценность упорного труда и командной работы.",
    "level": "B1"
  },
  {
    "id": 79,
    "title": "A Family Tradition",
    "content": "In my family, we have a special tradition every Sunday. We all meet at my grandmother's house and cook a big lunch together. While the food is cooking, we talk about our week and share funny stories. I really enjoy these days because they bring us closer. In the past, I didn't understand why this tradition was important. But now I know that spending time with family is precious. When I have my own children, I want to continue this beautiful custom too.",
    "translation": "В моей семье есть особая традиция каждое воскресенье. Мы все собираемся в доме моей бабушки и вместе готовим большой обед. Пока еда готовится, мы говорим о нашей неделе и делимся смешными историями. Мне очень нравятся эти дни, потому что они сближают нас. Раньше я не понимал, почему эта традиция важна. Но теперь я знаю, что проводить время с семьёй — это ценно. Когда у меня будут собственные дети, я тоже хочу продолжить этот прекрасный обычай.",
    "level": "B1"
  },
  {
    "id": 80,
    "title": "Running in the Park",
    "content": "Three times a week, I go running in the park near my house. When I started last year, I could only run for five minutes without stopping. Now I can run for half an hour, and I feel proud of myself. Running helps me relax after a busy day at work. Moreover, I have met several nice people who also run there. I believe sport is not only good for your body but also for your mind. I hope I will run a real race next spring.",
    "translation": "Три раза в неделю я бегаю в парке рядом с моим домом. Когда я начал в прошлом году, я мог бегать только пять минут без остановки. Теперь я могу бегать полчаса и горжусь собой. Бег помогает мне расслабиться после напряжённого рабочего дня. Более того, я познакомился с несколькими приятными людьми, которые тоже там бегают. Я считаю, что спорт полезен не только для тела, но и для ума. Я надеюсь, что следующей весной пробегу настоящий забег.",
    "level": "B1"
  },
  {
    "id": 81,
    "title": "Learning to Cook",
    "content": "For most of my life, I never cooked at home and always bought ready meals. However, this year I decided to learn how to cook healthy food. I started with simple recipes, such as soups and salads, and watched videos online. At the beginning, I made many mistakes and burned the rice twice. But step by step, I got better. Now cooking is one of my favourite hobbies, and my friends love my dishes. In my opinion, cooking your own food is cheaper and much healthier.",
    "translation": "Большую часть жизни я никогда не готовил дома и всегда покупал готовую еду. Однако в этом году я решил научиться готовить здоровую пищу. Я начал с простых рецептов, таких как супы и салаты, и смотрел видео в интернете. В начале я делал много ошибок и дважды сжёг рис. Но шаг за шагом я становился лучше. Теперь готовка — одно из моих любимых увлечений, и мои друзья обожают мои блюда. По моему мнению, готовить еду самому дешевле и намного полезнее.",
    "level": "B1"
  },
  {
    "id": 82,
    "title": "Working From Home",
    "content": "Since last year, I have been working from home three days a week. In the beginning, I thought it would be difficult to stay focused. Surprisingly, I actually work better because the office is often too noisy. On the other hand, I sometimes miss talking to my colleagues face to face. To solve this, we have short video calls every morning. I think working from home gives people more freedom and saves a lot of travel time. However, it is important to keep a good balance between work and rest.",
    "translation": "С прошлого года я работаю из дома три дня в неделю. Вначале я думал, что будет трудно сохранять концентрацию. Как ни удивительно, я на самом деле работаю лучше, потому что в офисе часто слишком шумно. С другой стороны, мне иногда не хватает общения с коллегами лицом к лицу. Чтобы решить это, мы делаем короткие видеозвонки каждое утро. Я думаю, что работа из дома даёт людям больше свободы и экономит много времени на дорогу. Однако важно сохранять хороший баланс между работой и отдыхом.",
    "level": "B1"
  },
  {
    "id": 83,
    "title": "My Music Collection",
    "content": "I have loved music since I was a small child. When I was young, my father played old records, and I listened to them for hours. These days, I mostly use apps to discover new songs from around the world. Still, I have kept some of my father's records because they remind me of happy times. In my free time, I am learning to play the guitar, although it is not easy. I believe that music brings people together, no matter where they come from or what language they speak.",
    "translation": "Я люблю музыку с самого детства. Когда я был маленьким, мой отец играл старые пластинки, и я слушал их часами. В наши дни я в основном использую приложения, чтобы открывать новые песни со всего мира. Тем не менее я сохранил некоторые пластинки моего отца, потому что они напоминают мне о счастливых временах. В свободное время я учусь играть на гитаре, хотя это непросто. Я верю, что музыка объединяет людей, независимо от того, откуда они и на каком языке говорят.",
    "level": "B1"
  },
  {
    "id": 84,
    "title": "Smart Home Devices",
    "content": "Last month, my brother installed several smart devices in his flat. Now he can turn on the lights, play music, and check the temperature just by speaking. At first, I thought these gadgets were unnecessary, but after I tried them, I changed my mind. They can really make daily life easier, especially for older people. Nevertheless, I worry a little about privacy, because these devices are always listening. In my view, technology should help us, but we should also protect our personal information carefully and stay in control.",
    "translation": "В прошлом месяце мой брат установил несколько умных устройств в своей квартире. Теперь он может включать свет, играть музыку и проверять температуру, просто говоря. Сначала я думал, что эти гаджеты не нужны, но, попробовав их, я изменил своё мнение. Они действительно могут сделать повседневную жизнь легче, особенно для пожилых людей. Тем не менее я немного беспокоюсь о конфиденциальности, потому что эти устройства всегда слушают. На мой взгляд, технологии должны помогать нам, но мы также должны тщательно защищать свою личную информацию и оставаться под контролем.",
    "level": "B1"
  },
  {
    "id": 85,
    "title": "Choosing a Career",
    "content": "When I was at school, everybody asked me what job I wanted to do in the future. Honestly, I had no idea, and this worried me a lot. After finishing my studies, I tried different things, from teaching to selling products in a shop. Thanks to these experiences, I finally discovered that I love working with computers. If I had chosen too quickly, I might have missed my real passion. My advice is simple: do not rush your decision, and be open to trying new opportunities whenever they appear.",
    "translation": "Когда я учился в школе, все спрашивали меня, какую работу я хочу в будущем. Честно говоря, я понятия не имел, и это меня очень беспокоило. Закончив учёбу, я пробовал разные вещи — от преподавания до продажи товаров в магазине. Благодаря этому опыту я наконец обнаружил, что люблю работать с компьютерами. Если бы я выбрал слишком быстро, я мог бы упустить своё настоящее увлечение. Мой совет прост: не торопитесь с решением и будьте открыты к новым возможностям, когда бы они ни появлялись.",
    "level": "B1"
  },
  {
    "id": 86,
    "title": "Festivals in My Country",
    "content": "My country is famous for its colourful festivals, which take place throughout the year. During these celebrations, people wear traditional clothes, prepare special food, and dance in the streets. My favourite festival happens in spring, when we welcome the new season with music and light. Although some old customs are slowly disappearing, many young people are trying to keep them alive. I feel proud when I see families teaching these traditions to their children. In my opinion, festivals are an important part of who we are as a nation.",
    "translation": "Моя страна знаменита своими яркими фестивалями, которые проходят в течение всего года. Во время этих праздников люди надевают традиционную одежду, готовят особую еду и танцуют на улицах. Мой любимый фестиваль проходит весной, когда мы встречаем новый сезон музыкой и светом. Хотя некоторые старые обычаи постепенно исчезают, многие молодые люди стараются сохранить их живыми. Я чувствую гордость, когда вижу, как семьи учат этим традициям своих детей. По моему мнению, фестивали — важная часть того, кто мы есть как нация.",
    "level": "B1"
  },
  {
    "id": 87,
    "title": "Sleep and Health",
    "content": "For many years, I did not think that sleep was very important. I often stayed up late, watching films or scrolling on my phone until midnight. As a result, I felt tired and could not concentrate at work. Recently, I read an article which explained how good sleep affects our health and mood. Since then, I have created a proper evening routine, and I always turn off screens an hour before bed. If I keep doing this, I am sure my energy and memory will continue to improve.",
    "translation": "В течение многих лет я не думал, что сон очень важен. Я часто засиживался допоздна, смотря фильмы или листая телефон до полуночи. В результате я чувствовал усталость и не мог сосредоточиться на работе. Недавно я прочитал статью, которая объясняла, как хороший сон влияет на наше здоровье и настроение. С тех пор я создал правильный вечерний распорядок и всегда выключаю экраны за час до сна. Если я буду продолжать так делать, я уверен, что моя энергия и память будут улучшаться и дальше.",
    "level": "B1"
  },
  {
    "id": 88,
    "title": "My Dream Business",
    "content": "For as long as I can remember, I have dreamed of opening my own small bookshop. I imagine a cosy place where people can read quietly, drink coffee, and discover interesting authors. Of course, I know that starting a business is not easy and requires careful planning. That is why I am currently saving money and studying how successful shops attract customers. If everything goes well, I would like to open my shop within five years. Even if it feels risky, I believe that following your dreams is always worth the effort.",
    "translation": "Сколько себя помню, я мечтал открыть свой собственный маленький книжный магазин. Я представляю уютное место, где люди могут спокойно читать, пить кофе и открывать для себя интересных авторов. Конечно, я знаю, что начать бизнес непросто и требует тщательного планирования. Именно поэтому я сейчас откладываю деньги и изучаю, как успешные магазины привлекают клиентов. Если всё пойдёт хорошо, я хотел бы открыть свой магазин в течение пяти лет. Даже если это кажется рискованным, я верю, что следовать своим мечтам всегда стоит усилий.",
    "level": "B1"
  },
  {
    "id": 89,
    "title": "Team Sports and Friendship",
    "content": "When I joined a local basketball team two years ago, I was mainly interested in getting fit. However, I soon realised that team sports offer much more than exercise. During difficult matches, we learned to trust each other and stay calm under pressure. Even when we lost, we supported our teammates instead of blaming them. Because of this, some of my closest friendships started on that court. Looking back, I understand that sport taught me patience, respect, and how to work together toward a common goal.",
    "translation": "Когда я присоединился к местной баскетбольной команде два года назад, меня в основном интересовало то, чтобы привести себя в форму. Однако вскоре я понял, что командные виды спорта дают гораздо больше, чем просто физическую нагрузку. Во время трудных матчей мы учились доверять друг другу и сохранять спокойствие под давлением. Даже когда мы проигрывали, мы поддерживали товарищей по команде, а не обвиняли их. Благодаря этому некоторые из моих самых близких дружеских отношений начались на той площадке. Оглядываясь назад, я понимаю, что спорт научил меня терпению, уважению и умению работать вместе ради общей цели.",
    "level": "B1"
  },
  {
    "id": 90,
    "title": "Technology and Old Traditions",
    "content": "It is interesting how technology is changing the way we keep our traditions alive. In the past, recipes and stories were only passed down by word of mouth from older relatives. Nowadays, families record videos, share photographs online, and even create digital albums that anyone can see. While some people worry that these customs might lose their meaning, I think technology can actually protect them. If we use these tools wisely, future generations will still be able to enjoy and understand the culture their grandparents once loved so deeply.",
    "translation": "Интересно, как технологии меняют то, как мы сохраняем наши традиции. Раньше рецепты и истории передавались только из уст в уста от старших родственников. В наши дни семьи записывают видео, делятся фотографиями в интернете и даже создают цифровые альбомы, которые может увидеть каждый. Хотя некоторые люди беспокоятся, что эти обычаи могут потерять свой смысл, я думаю, что технологии на самом деле могут их защитить. Если мы будем использовать эти инструменты мудро, будущие поколения всё ещё смогут наслаждаться и понимать культуру, которую их бабушки и дедушки когда-то так глубоко любили.",
    "level": "B1"
  },
  {
    "id": 91,
    "title": "Screens Everywhere We Look",
    "content": "These days, it is hard to imagine life without smartphones. We carry them in our pockets and check them dozens of times a day, sometimes without even thinking about it. While technology has made communication faster and more convenient, many people feel that we have become too dependent on our devices. Instead of talking face to face, we send messages; instead of remembering facts, we simply look them up. Of course, there are clear benefits, but there is also a downside. Spending hours staring at a screen can make us feel tired and disconnected from the people around us. Perhaps the challenge for our generation is learning to use technology wisely, rather than letting it control our daily lives.",
    "translation": "В наши дни трудно представить жизнь без смартфонов. Мы носим их в карманах и проверяем десятки раз в день, иногда даже не задумываясь об этом. Хотя технологии сделали общение быстрее и удобнее, многие люди чувствуют, что мы стали слишком зависимы от своих устройств. Вместо того чтобы разговаривать лицом к лицу, мы отправляем сообщения; вместо того чтобы запоминать факты, мы просто ищем их. Конечно, есть очевидные преимущества, но есть и обратная сторона. Часы, проведённые за экраном, могут вызывать усталость и чувство оторванности от окружающих людей. Возможно, задача для нашего поколения — научиться использовать технологии разумно, а не позволять им управлять нашей повседневной жизнью.",
    "level": "B2"
  },
  {
    "id": 92,
    "title": "Working From Home",
    "content": "Since the pandemic, working from home has become far more common than it used to be. For many employees, this change has been a breath of fresh air. They no longer have to spend hours stuck in traffic, and they can organise their day more flexibly. On the other hand, remote work is not without its problems. Some people find it difficult to switch off at the end of the day, and the line between work and private life can easily become blurred. What is more, working alone at home can feel isolating over time. In the long run, many companies are moving towards a hybrid model, allowing staff to enjoy the best of both worlds while staying connected with their colleagues.",
    "translation": "Со времён пандемии удалённая работа стала гораздо более распространённой, чем раньше. Для многих сотрудников это изменение стало глотком свежего воздуха. Им больше не нужно часами стоять в пробках, и они могут более гибко планировать свой день. С другой стороны, удалённая работа не лишена своих проблем. Некоторым людям трудно отключиться в конце дня, и граница между работой и личной жизнью легко размывается. Более того, работа в одиночестве дома со временем может вызывать чувство изоляции. В долгосрочной перспективе многие компании переходят к гибридной модели, позволяя сотрудникам наслаждаться лучшим из обоих миров, оставаясь при этом на связи с коллегами.",
    "level": "B2"
  },
  {
    "id": 93,
    "title": "Small Changes, Big Difference",
    "content": "When people think about protecting the environment, they often imagine huge, dramatic actions. In reality, small changes in our daily habits can add up to a big difference. Turning off the lights when we leave a room, using public transport instead of driving, and cutting down on plastic are simple steps that almost anyone can take. Of course, individual efforts alone will not solve the climate crisis, but they do send a powerful message. When enough people start caring, governments and companies are forced to take notice. It is easy to feel that one person cannot make a difference, yet history shows that lasting change usually begins with ordinary people deciding that the way things are is no longer good enough.",
    "translation": "Когда люди думают о защите окружающей среды, они часто представляют себе огромные, впечатляющие действия. На самом деле небольшие изменения в наших повседневных привычках могут в сумме дать большую разницу. Выключать свет, покидая комнату, пользоваться общественным транспортом вместо автомобиля и сокращать использование пластика — это простые шаги, которые может сделать почти каждый. Конечно, одни лишь усилия отдельных людей не решат климатический кризис, но они посылают мощный сигнал. Когда достаточно людей начинают проявлять заботу, правительства и компании вынуждены обращать на это внимание. Легко почувствовать, что один человек не может ничего изменить, однако история показывает, что прочные перемены обычно начинаются с того, что обычные люди решают: так, как есть, больше недостаточно хорошо.",
    "level": "B2"
  },
  {
    "id": 94,
    "title": "Travelling With an Open Mind",
    "content": "Travelling is about far more than simply seeing famous landmarks and taking photographs. When we visit another country, we are given the chance to step into a completely different way of life. The food may seem strange at first, the customs unfamiliar, and the language impossible to understand. Yet it is exactly these differences that make travel so rewarding. By keeping an open mind, we learn to see the world through other people's eyes and to question things we once took for granted. Travellers who spend all their time complaining about how things are done abroad often miss the whole point. In the end, the greatest souvenir we can bring home is a broader understanding of humanity and our own place within it.",
    "translation": "Путешествия — это гораздо больше, чем просто осмотр знаменитых достопримечательностей и фотографирование. Когда мы посещаем другую страну, нам даётся возможность окунуться в совершенно иной образ жизни. Еда поначалу может казаться странной, обычаи — незнакомыми, а язык — непонятным. Однако именно эти различия делают путешествия столь ценными. Сохраняя открытость ума, мы учимся видеть мир глазами других людей и подвергать сомнению то, что когда-то считали само собой разумеющимся. Путешественники, которые всё время жалуются на то, как всё устроено за границей, часто упускают самую суть. В конце концов, лучший сувенир, который мы можем привезти домой, — это более широкое понимание человечества и нашего собственного места в нём.",
    "level": "B2"
  },
  {
    "id": 95,
    "title": "The Art of Saying No",
    "content": "Many of us struggle to say no, even when we are already overwhelmed with commitments. We agree to extra tasks at work, favours for friends, and social events we would rather skip, all because we are afraid of disappointing others. Over time, however, constantly putting everyone else first can leave us exhausted and resentful. Learning to set boundaries is not selfish; it is an essential part of looking after ourselves. Saying no politely but firmly allows us to protect our time and energy for the things that truly matter. It may feel uncomfortable at first, and some people may not like it. Still, those who respect us will understand, and in the long run we will be all the better for it.",
    "translation": "Многим из нас трудно говорить «нет», даже когда мы уже перегружены обязательствами. Мы соглашаемся на дополнительные задачи на работе, на просьбы друзей и на общественные мероприятия, которые предпочли бы пропустить, — и всё потому, что боимся разочаровать других. Однако со временем постоянное стремление ставить всех остальных на первое место может оставить нас измотанными и обиженными. Умение устанавливать границы — это не эгоизм, а важная часть заботы о себе. Умение говорить «нет» вежливо, но твёрдо позволяет нам беречь своё время и энергию для того, что действительно важно. Поначалу это может ощущаться некомфортно, и некоторым людям это может не понравиться. Тем не менее те, кто нас уважает, поймут, и в конечном счёте нам от этого будет только лучше.",
    "level": "B2"
  },
  {
    "id": 96,
    "title": "News in the Digital Age",
    "content": "The way we consume news has changed beyond recognition over the past twenty years. Instead of waiting for the morning newspaper or the evening broadcast, we now receive a constant stream of updates on our phones, day and night. While this gives us instant access to what is happening around the world, it also comes with hidden dangers. Not everything we read online is accurate, and false stories can spread like wildfire before anyone bothers to check the facts. In this environment, being able to tell reliable sources from unreliable ones has become a vital skill. Rather than believing every headline that catches our eye, we should pause, think critically, and consider who is behind the information we are being fed.",
    "translation": "То, как мы потребляем новости, изменилось до неузнаваемости за последние двадцать лет. Вместо того чтобы ждать утреннюю газету или вечерний выпуск, мы теперь получаем непрерывный поток обновлений на свои телефоны днём и ночью. Хотя это даёт нам мгновенный доступ к тому, что происходит в мире, это также несёт скрытые опасности. Не всё, что мы читаем в интернете, достоверно, и ложные истории могут распространяться со скоростью лесного пожара, прежде чем кто-либо потрудится проверить факты. В этих условиях умение отличать надёжные источники от ненадёжных стало жизненно важным навыком. Вместо того чтобы верить каждому заголовку, привлекающему наше внимание, нам следует остановиться, подумать критически и задуматься о том, кто стоит за информацией, которую нам преподносят.",
    "level": "B2"
  },
  {
    "id": 97,
    "title": "Getting Out of Your Comfort Zone",
    "content": "Growth rarely happens when we are comfortable. It is easy to stick to familiar routines, avoid risks, and stay within the boundaries we know well. However, the moments that shape us most are usually the ones that push us out of our comfort zone. Whether it is speaking in public, moving to a new city, or learning a difficult skill, stepping into the unknown can be frightening. Yet each time we face our fears, we discover that we are far more capable than we imagined. Naturally, not every attempt will succeed, and failure is part of the process. What matters is that we keep trying, because a life spent avoiding challenges is, in many ways, a life half lived.",
    "translation": "Рост редко происходит, когда нам комфортно. Легко придерживаться привычного распорядка, избегать рисков и оставаться в хорошо знакомых нам рамках. Однако моменты, которые формируют нас больше всего, — это обычно те, что выталкивают нас из зоны комфорта. Будь то публичное выступление, переезд в новый город или освоение сложного навыка, шаг в неизвестность может пугать. И всё же каждый раз, встречаясь со своими страхами, мы обнаруживаем, что способны на гораздо большее, чем нам казалось. Разумеется, не каждая попытка окажется успешной, и неудача — часть процесса. Важно то, что мы продолжаем пытаться, потому что жизнь, проведённая в избегании трудностей, во многом является жизнью, прожитой наполовину.",
    "level": "B2"
  },
  {
    "id": 98,
    "title": "When Machines Learn to Think",
    "content": "Artificial intelligence, once the stuff of science fiction, has quietly become part of everyday life. It recommends the films we watch, filters our emails, and even helps doctors diagnose diseases. As these systems grow more sophisticated, they promise to make our lives easier in countless ways. Nevertheless, this rapid progress raises difficult questions that society cannot afford to ignore. If machines take over more and more tasks, what will happen to the jobs that people currently rely on? And who should be held responsible when an algorithm makes a serious mistake? There are no easy answers, but one thing is certain: the sooner we start having these conversations, the better prepared we will be for the changes that lie ahead.",
    "translation": "Искусственный интеллект, когда-то бывший материалом научной фантастики, незаметно стал частью повседневной жизни. Он рекомендует нам фильмы для просмотра, фильтрует наши письма и даже помогает врачам диагностировать болезни. По мере того как эти системы становятся всё более совершенными, они обещают облегчить нашу жизнь бесчисленным множеством способов. Тем не менее этот стремительный прогресс поднимает сложные вопросы, которые общество не может позволить себе игнорировать. Если машины будут брать на себя всё больше и больше задач, что станет с рабочими местами, на которые люди сейчас полагаются? И кого следует привлекать к ответственности, когда алгоритм совершает серьёзную ошибку? Простых ответов нет, но одно несомненно: чем раньше мы начнём эти разговоры, тем лучше будем подготовлены к переменам, которые нас ждут.",
    "level": "B2"
  },
  {
    "id": 99,
    "title": "The Race Against Rising Seas",
    "content": "For coastal communities around the world, climate change is not a distant threat but a daily reality. As global temperatures climb, ice sheets melt and sea levels creep steadily upward, swallowing beaches and threatening cities that have stood for centuries. Some low-lying island nations face the very real possibility of disappearing altogether within a few generations. Governments are scrambling to build defences, but such measures are expensive and, in many cases, merely buy time. The uncomfortable truth is that we can no longer prevent all of the damage; the best we can do is slow it down while adapting to a changed world. This is a sobering thought, yet it also underlines just how urgently we need to act before matters spiral out of control.",
    "translation": "Для прибрежных сообществ по всему миру изменение климата — это не отдалённая угроза, а повседневная реальность. По мере роста глобальной температуры ледяные щиты тают, а уровень моря неуклонно поднимается, поглощая пляжи и угрожая городам, которые стоят веками. Некоторые низменные островные государства сталкиваются с вполне реальной вероятностью полностью исчезнуть в течение нескольких поколений. Правительства спешно возводят защитные сооружения, но такие меры дороги и во многих случаях лишь выигрывают время. Неудобная правда в том, что мы уже не можем предотвратить весь ущерб; лучшее, что мы можем сделать, — замедлить его, приспосабливаясь к изменившемуся миру. Это отрезвляющая мысль, но она также подчёркивает, насколько срочно нам нужно действовать, пока ситуация не вышла из-под контроля.",
    "level": "B2"
  },
  {
    "id": 100,
    "title": "Culture Shock and Belonging",
    "content": "Anyone who has lived abroad for an extended period knows that the initial excitement of a new country eventually gives way to a more complicated set of emotions. What begins as fascination can slowly turn into frustration, as everyday tasks that once seemed simple become sources of confusion. This experience, often called culture shock, can leave people feeling homesick and out of place. Yet those who push through this difficult phase frequently come out the other side transformed. They gradually build a sense of belonging in their adopted home, forming friendships and picking up habits they never expected. In doing so, they come to realise that identity is not fixed but flexible, and that it is entirely possible to feel at home in more than one place.",
    "translation": "Каждый, кто прожил за границей длительное время, знает, что первоначальный восторг от новой страны в конце концов уступает место более сложному набору эмоций. То, что начинается как очарование, может постепенно превратиться в раздражение, поскольку повседневные дела, когда-то казавшиеся простыми, становятся источником замешательства. Этот опыт, часто называемый культурным шоком, может вызывать у людей тоску по дому и ощущение неуместности. Однако те, кто преодолевает этот трудный этап, нередко выходят из него преображёнными. Они постепенно обретают чувство принадлежности в своём новом доме, заводят дружбу и перенимают привычки, которых никак не ожидали. Поступая так, они начинают понимать, что идентичность не является чем-то раз и навсегда заданным, а гибка, и что вполне возможно чувствовать себя как дома более чем в одном месте.",
    "level": "B2"
  },
  {
    "id": 101,
    "title": "The Myth of Multitasking",
    "content": "In our fast-paced world, being able to juggle several tasks at once is often seen as a valuable skill. We pride ourselves on answering emails during meetings, checking our phones while cooking dinner, and switching endlessly between apps. However, a growing body of research suggests that multitasking is largely a myth. Rather than doing several things well at the same time, our brains rapidly switch back and forth, and each switch comes at a cost. As a result, we tend to make more mistakes, take longer to finish, and remember less of what we have done. Ironically, the key to genuine productivity may lie in doing the opposite of what we have been taught: focusing on one thing at a time and giving it our full attention.",
    "translation": "В нашем стремительном мире умение жонглировать несколькими задачами одновременно часто считается ценным навыком. Мы гордимся тем, что отвечаем на письма во время совещаний, проверяем телефон, готовя ужин, и бесконечно переключаемся между приложениями. Однако растущий объём исследований показывает, что многозадачность — это по большей части миф. Вместо того чтобы делать несколько дел хорошо одновременно, наш мозг быстро переключается туда-сюда, и каждое переключение обходится нам дорого. В результате мы склонны совершать больше ошибок, дольше заканчивать дело и меньше помнить из того, что сделали. Как ни парадоксально, ключ к подлинной продуктивности может заключаться в том, чтобы делать противоположное тому, чему нас учили: сосредотачиваться на одном деле за раз и уделять ему всё своё внимание.",
    "level": "B2"
  },
  {
    "id": 102,
    "title": "Living in the Public Eye",
    "content": "Social media has blurred the line between public and private in ways previous generations could scarcely have imagined. With a single post, an ordinary person can reach millions of strangers, while celebrities are held accountable for every careless word. On the surface, this newfound visibility seems empowering, giving everyone a platform to share their voice. Beneath that surface, however, lies a more troubling reality. The pressure to present a flawless image can take a heavy toll on mental health, and a moment's mistake can haunt someone for years. What is more, the constant comparison to carefully curated highlight reels leaves many feeling that their own lives fall short. Perhaps we would all do well to remember that what we see online is rarely the whole story.",
    "translation": "Социальные сети размыли границу между публичным и частным способами, которые предыдущие поколения едва ли могли себе представить. Одним постом обычный человек может достучаться до миллионов незнакомцев, тогда как знаменитостей призывают к ответу за каждое неосторожное слово. На первый взгляд эта обретённая заметность кажется дающей силы, предоставляя каждому площадку, чтобы поделиться своим голосом. Однако под этой поверхностью скрывается более тревожная реальность. Давление, связанное с необходимостью представлять безупречный образ, может тяжело сказаться на психическом здоровье, а минутная ошибка может преследовать человека годами. Более того, постоянное сравнение с тщательно отобранными яркими моментами оставляет у многих ощущение, что их собственная жизнь не дотягивает. Возможно, всем нам стоило бы помнить, что то, что мы видим в интернете, редко является полной картиной.",
    "level": "B2"
  },
  {
    "id": 103,
    "title": "The Price of Cheap Flights",
    "content": "The rise of budget airlines has transformed the way we travel, putting far-flung destinations within reach of almost anyone. Weekend trips to foreign cities, once a luxury reserved for the wealthy, are now taken for granted by millions. Yet this convenience carries a hidden price tag that rarely appears on our tickets. Aviation is a significant contributor to carbon emissions, and the sheer volume of flights is putting mounting strain on the planet. Meanwhile, popular destinations groan under the weight of mass tourism, as historic centres are overrun and local residents are priced out of their own neighbourhoods. None of this means we should stop exploring the world, but it does invite us to travel more thoughtfully and to weigh the true cost of our wanderlust.",
    "translation": "Появление бюджетных авиакомпаний изменило то, как мы путешествуем, сделав отдалённые направления доступными почти для каждого. Поездки на выходные в зарубежные города, когда-то бывшие роскошью, доступной лишь состоятельным людям, теперь воспринимаются миллионами как нечто само собой разумеющееся. Однако за этим удобством скрывается цена, которая редко указана в наших билетах. Авиация вносит значительный вклад в выбросы углерода, и само по себе огромное количество рейсов оказывает всё возрастающую нагрузку на планету. Тем временем популярные направления стонут под тяжестью массового туризма: исторические центры переполнены, а местные жители вытесняются из собственных районов из-за роста цен. Ничто из этого не означает, что мы должны перестать исследовать мир, но это побуждает нас путешествовать более осознанно и взвешивать истинную цену нашей тяги к странствиям.",
    "level": "B2"
  },
  {
    "id": 104,
    "title": "Rethinking What Success Means",
    "content": "From an early age, many of us are taught to measure success in fairly narrow terms: a prestigious job, a high salary, and an impressive title. We chase these markers relentlessly, often assuming that once we reach them, contentment will surely follow. Yet countless people who have ticked every box on this conventional checklist report feeling strangely empty, as though something vital were missing. This paradox suggests that we may have been chasing the wrong things all along. Genuine fulfilment, it turns out, tends to spring from sources that money cannot buy: meaningful relationships, a sense of purpose, and the freedom to spend our time as we see fit. Redefining success on our own terms is not a sign of weakness but an act of quiet courage.",
    "translation": "С раннего возраста многих из нас учат измерять успех довольно узкими мерками: престижная работа, высокая зарплата и внушительная должность. Мы неустанно гонимся за этими ориентирами, часто полагая, что, достигнув их, мы непременно обретём удовлетворённость. Однако бесчисленное множество людей, отметивших каждый пункт в этом традиционном списке, признаются, что чувствуют себя странно опустошёнными, словно чего-то важного не хватает. Этот парадокс наводит на мысль, что мы, возможно, всё это время гнались не за тем. Подлинное удовлетворение, как выясняется, обычно проистекает из источников, которые нельзя купить за деньги: значимых отношений, чувства цели и свободы распоряжаться своим временем так, как мы считаем нужным. Переосмыслить успех на собственных условиях — это не признак слабости, а акт тихого мужества.",
    "level": "B2"
  },
  {
    "id": 105,
    "title": "The Attention Economy",
    "content": "We often assume that the apps and websites we use every day are designed simply to help us, but the truth is more calculated than that. In what has come to be known as the attention economy, our time and focus have become the most valuable commodities of all. Countless companies compete fiercely to keep us scrolling, tapping, and coming back for more, because every extra minute we spend translates directly into profit. To this end, their products are meticulously engineered to exploit the very quirks of human psychology, from the thrill of notifications to the fear of missing out. Recognising these mechanisms for what they are is the first step towards reclaiming control. After all, our attention is finite, and how we choose to spend it ultimately shapes the lives we lead.",
    "translation": "Мы часто полагаем, что приложения и сайты, которыми мы пользуемся каждый день, созданы просто для того, чтобы помогать нам, но истина куда более расчётлива. В том, что стало известно как экономика внимания, наше время и сосредоточенность превратились в самый ценный товар из всех. Бесчисленные компании ожесточённо соперничают за то, чтобы удержать нас в бесконечной прокрутке, нажатиях и возвращениях снова и снова, потому что каждая лишняя минута, которую мы тратим, напрямую превращается в прибыль. Ради этого их продукты тщательно спроектированы так, чтобы эксплуатировать сами особенности человеческой психологии — от волнения от уведомлений до страха что-то упустить. Распознать эти механизмы такими, какие они есть, — первый шаг к возвращению контроля. В конце концов, наше внимание ограниченно, и то, как мы решаем его тратить, в итоге определяет ту жизнь, которую мы ведём.",
    "level": "B2"
  },
  {
    "id": 106,
    "title": "Choosing a Career Path",
    "content": "Deciding what to study is one of the hardest choices young people face. Many students feel pressure to pick a subject that leads straight to a well-paid job, while others follow their passion and hope for the best. In reality, the two goals often overlap. Employers today value skills like problem-solving and communication just as much as a specific degree. My advice is simple: don't put all your eggs in one basket. Keep your options open, gain some practical experience through internships, and stay curious about different fields. A career is rarely a straight line. Most people change direction several times, and the skills you build along the way matter far more than the label on your diploma.",
    "translation": "Решение о том, что изучать, — один из самых сложных выборов, с которыми сталкиваются молодые люди. Многие студенты чувствуют давление и выбирают предмет, который ведёт прямо к хорошо оплачиваемой работе, тогда как другие следуют за своей страстью и надеются на лучшее. На самом деле эти две цели часто пересекаются. Работодатели сегодня ценят такие навыки, как решение проблем и общение, не меньше, чем конкретный диплом. Мой совет прост: не кладите все яйца в одну корзину. Держите варианты открытыми, получайте практический опыт через стажировки и сохраняйте любопытство к разным сферам. Карьера редко бывает прямой линией. Большинство людей меняют направление несколько раз, и навыки, которые вы приобретаете по пути, значат гораздо больше, чем надпись на вашем дипломе.",
    "level": "B2"
  },
  {
    "id": 107,
    "title": "The Power of Good Sleep",
    "content": "We often treat sleep as something we can sacrifice when life gets busy, but psychologists warn that this is a false economy. During deep sleep, the brain sorts through the day's events, strengthens memories, and clears away harmful waste. People who regularly cut their rest short tend to struggle with concentration, mood, and even decision-making. What surprises many is that quality matters as much as quantity. Staring at a bright screen late at night can trick the brain into staying alert, making it harder to switch off. Building a calm evening routine, avoiding heavy meals, and keeping regular hours can work wonders. In short, a good night's sleep is not a luxury but the foundation of a healthy mind.",
    "translation": "Мы часто относимся ко сну как к чему-то, чем можно пожертвовать, когда жизнь становится напряжённой, но психологи предупреждают, что это ложная экономия. Во время глубокого сна мозг разбирает события дня, укрепляет воспоминания и удаляет вредные отходы. Люди, которые регулярно урезают свой отдых, обычно испытывают трудности с концентрацией, настроением и даже принятием решений. Многих удивляет, что качество важно не меньше количества. Разглядывание яркого экрана поздно ночью может обмануть мозг, заставив его оставаться бодрым, из-за чего труднее расслабиться. Создание спокойного вечернего распорядка, отказ от тяжёлой пищи и соблюдение режима могут творить чудеса. Короче говоря, хороший ночной сон — это не роскошь, а основа здорового ума.",
    "level": "B2"
  },
  {
    "id": 108,
    "title": "Why Museums Still Matter",
    "content": "In an age when almost any painting can be viewed on a screen, some people ask whether museums still have a purpose. The answer, I believe, is a resounding yes. Standing in front of an original work is a completely different experience from scrolling past a photograph. You notice the texture of the paint, the true scale of the canvas, and the quiet atmosphere of the room. Museums also tell stories, placing objects in context and helping us understand the people who created them. They bring communities together and spark conversations across generations. A screen can show you an image, but it cannot capture the sense of wonder you feel when you meet a masterpiece face to face.",
    "translation": "В эпоху, когда почти любую картину можно посмотреть на экране, некоторые люди задаются вопросом, есть ли у музеев ещё смысл. Ответ, я считаю, — решительное «да». Стоять перед оригинальным произведением — совершенно иной опыт, чем пролистывать фотографию. Вы замечаете фактуру краски, истинный масштаб холста и тихую атмосферу зала. Музеи также рассказывают истории, помещая предметы в контекст и помогая нам понять людей, которые их создали. Они объединяют сообщества и рождают разговоры между поколениями. Экран может показать вам изображение, но он не может передать чувство удивления, которое вы испытываете, встречая шедевр лицом к лицу.",
    "level": "B2"
  },
  {
    "id": 109,
    "title": "The Art of Saving Money",
    "content": "Saving money sounds straightforward, yet millions of people find it almost impossible. The problem is rarely a lack of income; more often, it comes down to habits. Small, everyday purchases add up quietly until, at the end of the month, we wonder where our salary went. Financial experts suggest paying yourself first, which means setting aside a fixed amount the moment you are paid, before you have a chance to spend it. Automating this process removes temptation and turns saving into a routine rather than a struggle. It also helps to distinguish between what we truly need and what we merely want. Over time, these modest choices can grow into a genuine safety net for the future.",
    "translation": "Экономия денег звучит просто, но миллионы людей находят это почти невозможным. Проблема редко заключается в недостатке дохода; чаще всё сводится к привычкам. Маленькие повседневные покупки незаметно накапливаются, пока в конце месяца мы не задаёмся вопросом, куда делась наша зарплата. Финансовые эксперты советуют сначала платить себе, что означает откладывать фиксированную сумму сразу после получения денег, прежде чем у вас появится возможность их потратить. Автоматизация этого процесса убирает соблазн и превращает сбережения в рутину, а не в борьбу. Также полезно различать то, что нам действительно нужно, и то, что мы просто хотим. Со временем эти скромные решения могут вырасти в настоящую подушку безопасности на будущее.",
    "level": "B2"
  },
  {
    "id": 110,
    "title": "The Value of True Friendship",
    "content": "As we grow older, the way we think about friendship tends to change. In our teenage years, we often measure popularity by the number of people we know. Later, we come to realise that a handful of loyal friends is worth far more than a crowd of acquaintances. Real friends are the ones who stand by you when things go wrong, who tell you honest truths even when they are hard to hear, and who celebrate your success without a trace of envy. Such relationships are not built overnight; they require time, trust, and a willingness to give as much as you take. In the end, the quality of our friendships often shapes the quality of our lives.",
    "translation": "По мере взросления то, как мы думаем о дружбе, обычно меняется. В подростковые годы мы часто измеряем популярность количеством людей, которых знаем. Позже мы приходим к пониманию, что горстка верных друзей стоит гораздо больше, чем толпа знакомых. Настоящие друзья — это те, кто остаётся с тобой, когда что-то идёт не так, кто говорит честную правду, даже когда её тяжело слышать, и кто радуется твоему успеху без тени зависти. Такие отношения не строятся за одну ночь; они требуют времени, доверия и готовности отдавать столько же, сколько берёшь. В конце концов, качество нашей дружбы часто определяет качество нашей жизни.",
    "level": "B2"
  },
  {
    "id": 111,
    "title": "How Curiosity Drives Science",
    "content": "Behind every great scientific breakthrough lies a simple question that someone dared to ask. Curiosity, more than intelligence alone, is what pushes researchers to explore the unknown. Many discoveries that changed the world began as experiments with no obvious practical purpose. Scientists studied strange moulds, distant stars, or invisible particles simply because they wanted to understand how things work. Only later did their findings lead to medicines, technologies, and industries that transformed daily life. This is why funding pure research matters, even when the benefits are not immediately clear. Society tends to reward quick results, but the seeds of tomorrow's innovations are often planted by those brave enough to follow their curiosity wherever it leads.",
    "translation": "За каждым великим научным прорывом стоит простой вопрос, который кто-то осмелился задать. Любопытство, больше чем один лишь интеллект, — это то, что подталкивает исследователей изучать неизведанное. Многие открытия, изменившие мир, начинались как эксперименты без очевидной практической цели. Учёные изучали странную плесень, далёкие звёзды или невидимые частицы просто потому, что хотели понять, как всё устроено. Лишь позже их находки привели к лекарствам, технологиям и целым отраслям, которые преобразили повседневную жизнь. Вот почему финансирование фундаментальных исследований важно, даже когда выгода не сразу очевидна. Общество склонно вознаграждать быстрые результаты, но семена завтрашних инноваций часто сажают те, кто достаточно смел, чтобы следовать за своим любопытством, куда бы оно ни вело.",
    "level": "B2"
  },
  {
    "id": 112,
    "title": "The Hidden Cost of Stress",
    "content": "A certain amount of stress can be useful; it sharpens our focus and helps us rise to a challenge. The trouble begins when pressure never lets up. Chronic stress keeps the body in a constant state of alert, flooding it with hormones that were designed for short-term emergencies, not for months on end. Over time, this takes a heavy toll on both physical and mental health, contributing to everything from headaches to heart problems. What makes matters worse is that stressed people often abandon the very habits that would help them, such as exercise and proper rest. Learning to recognise the warning signs early, and to switch off now and then, is not weakness but wisdom.",
    "translation": "Определённое количество стресса может быть полезным; он обостряет наше внимание и помогает нам справиться с трудностью. Проблемы начинаются, когда давление не ослабевает. Хронический стресс держит тело в постоянном состоянии готовности, заливая его гормонами, которые были предназначены для краткосрочных чрезвычайных ситуаций, а не для месяцев подряд. Со временем это тяжело сказывается как на физическом, так и на психическом здоровье, способствуя всему — от головных болей до проблем с сердцем. Что усугубляет положение, так это то, что люди в стрессе часто бросают именно те привычки, которые помогли бы им, такие как физические упражнения и полноценный отдых. Научиться распознавать тревожные сигналы рано и время от времени отключаться — это не слабость, а мудрость.",
    "level": "B2"
  },
  {
    "id": 113,
    "title": "Learning Beyond the Classroom",
    "content": "Formal education gives us a solid foundation, but it would be a mistake to think that learning ends the moment we leave school. In a world that changes at breakneck speed, the ability to keep teaching yourself has become an essential skill. Fortunately, opportunities are everywhere. A short online course, a well-chosen book, or even a thoughtful conversation can open doors that a classroom never could. The key is to stay humble and admit how much you still don't know. People who treat every experience as a chance to grow tend to adapt more easily and seize opportunities that others overlook. Education, in this sense, is less a destination than a lifelong journey that never truly comes to an end.",
    "translation": "Формальное образование даёт нам прочный фундамент, но было бы ошибкой думать, что обучение заканчивается в тот момент, когда мы покидаем школу. В мире, который меняется с головокружительной скоростью, способность продолжать учить себя самому стала важнейшим навыком. К счастью, возможности повсюду. Короткий онлайн-курс, удачно выбранная книга или даже вдумчивый разговор могут открыть двери, которые классу были бы не под силу. Ключ в том, чтобы оставаться скромным и признавать, как много вы ещё не знаете. Люди, которые относятся к каждому опыту как к шансу вырасти, обычно легче адаптируются и хватаются за возможности, которые другие упускают из виду. Образование в этом смысле — не столько пункт назначения, сколько путешествие длиною в жизнь, которое никогда по-настоящему не заканчивается.",
    "level": "B2"
  },
  {
    "id": 114,
    "title": "The Rise of Streaming",
    "content": "Not so long ago, watching a film meant renting a disc or waiting for a fixed time on television. Streaming services have turned that world upside down, putting thousands of titles at our fingertips whenever we please. The convenience is undeniable, yet this revolution comes with mixed consequences. On one hand, talented creators from all over the globe now reach audiences they could never have imagined. On the other, the sheer volume of content can leave viewers paralysed, endlessly scrolling instead of settling on anything to watch. Some critics also worry that the pressure to keep us hooked encourages quantity over quality. Whether this shift ultimately enriches culture or dilutes it is a question we are still learning to answer.",
    "translation": "Не так давно посмотреть фильм означало взять диск напрокат или ждать определённого времени по телевизору. Стриминговые сервисы перевернули этот мир с ног на голову, предоставив тысячи наименований в нашем распоряжении, когда бы мы ни пожелали. Удобство неоспоримо, однако эта революция несёт с собой неоднозначные последствия. С одной стороны, талантливые создатели со всего мира теперь достигают аудитории, о которой они и мечтать не могли. С другой стороны, огромный объём контента может парализовать зрителей, заставляя их бесконечно листать вместо того, чтобы остановиться на чём-то одном. Некоторые критики также опасаются, что стремление удержать нас поощряет количество в ущерб качеству. Обогатит ли этот сдвиг культуру в конечном счёте или размоет её — вопрос, на который мы всё ещё учимся отвечать.",
    "level": "B2"
  },
  {
    "id": 115,
    "title": "Understanding Inflation",
    "content": "Most of us notice inflation without knowing exactly how it works. It simply means that, over time, the same amount of money buys fewer goods and services. A moderate, steady rise in prices is generally considered healthy for an economy, as it encourages people to spend and invest rather than hoard their cash. Problems arise when prices climb too quickly and wages fail to keep pace. Suddenly, families find that their earnings stretch less far, and those on fixed incomes are hit especially hard. Central banks try to keep inflation in check by adjusting interest rates, effectively cooling down an overheated economy. It is a delicate balancing act, and getting it wrong can have painful consequences for ordinary people.",
    "translation": "Большинство из нас замечает инфляцию, не зная точно, как она работает. Она просто означает, что со временем на ту же сумму денег можно купить меньше товаров и услуг. Умеренный, устойчивый рост цен обычно считается здоровым для экономики, поскольку побуждает людей тратить и инвестировать, а не копить наличные. Проблемы возникают, когда цены растут слишком быстро, а зарплаты не поспевают за ними. Внезапно семьи обнаруживают, что их заработка хватает на меньшее, и особенно тяжело приходится тем, кто живёт на фиксированный доход. Центральные банки пытаются держать инфляцию под контролем, регулируя процентные ставки и по сути охлаждая перегретую экономику. Это тонкое балансирование, и ошибка может обернуться болезненными последствиями для обычных людей.",
    "level": "B2"
  },
  {
    "id": 116,
    "title": "When Innovation Meets Ethics",
    "content": "Every new technology arrives with a promise and a warning. Innovations that make our lives easier can, in the wrong hands, cause serious harm, which is why ethics can never be an afterthought. Consider genetic research, which offers hope of curing diseases that have plagued humanity for centuries. The very same knowledge, however, raises unsettling questions about how far we should go in reshaping life itself. History teaches us that scientific capability tends to outrun our ability to regulate it wisely. For this reason, engineers and researchers increasingly work alongside philosophers and lawmakers, weighing not only what we can do but what we ought to do. Progress without reflection is a gamble that future generations may be left to pay for.",
    "translation": "Каждая новая технология приходит с обещанием и с предостережением. Инновации, которые облегчают нашу жизнь, в неправильных руках могут причинить серьёзный вред, вот почему этика никогда не может быть чем-то второстепенным. Возьмём генетические исследования, которые дают надежду на излечение болезней, мучивших человечество веками. Однако то же самое знание поднимает тревожные вопросы о том, как далеко нам следует заходить в переустройстве самой жизни. История учит нас, что научные возможности склонны опережать нашу способность мудро их регулировать. По этой причине инженеры и исследователи всё чаще работают бок о бок с философами и законодателями, взвешивая не только то, что мы можем сделать, но и то, что нам следует делать. Прогресс без размышления — это азартная игра, за которую, возможно, придётся расплачиваться будущим поколениям.",
    "level": "B2"
  },
  {
    "id": 117,
    "title": "The Psychology of First Impressions",
    "content": "It takes only a few seconds for us to form an opinion of someone we have just met, and, remarkably, that snap judgement often proves surprisingly stubborn. Our brains are wired to draw quick conclusions from tiny clues, such as a person's posture, tone of voice, or the firmness of a handshake. While this instinct once helped our ancestors decide whom to trust, it can lead us badly astray in modern life. We may dismiss a nervous candidate who would have made a brilliant employee, or warm to a smooth talker who lets us down. Being aware of these mental shortcuts is the first step toward overcoming them. A little patience, and a willingness to look beyond the surface, can spare us costly mistakes.",
    "translation": "Нам требуется всего несколько секунд, чтобы сформировать мнение о человеке, которого мы только что встретили, и, что примечательно, это мгновенное суждение часто оказывается на удивление стойким. Наш мозг устроен так, чтобы делать быстрые выводы из крошечных подсказок, таких как осанка человека, тон голоса или крепость рукопожатия. Хотя когда-то этот инстинкт помогал нашим предкам решать, кому доверять, в современной жизни он может сильно сбить нас с пути. Мы можем отвергнуть нервничающего кандидата, который стал бы блестящим сотрудником, или проникнуться симпатией к красноречивому болтуну, который нас подведёт. Осознание этих ментальных сокращений — первый шаг к их преодолению. Немного терпения и готовность заглянуть за поверхность могут уберечь нас от дорогостоящих ошибок.",
    "level": "B2"
  },
  {
    "id": 118,
    "title": "The Economics of Happiness",
    "content": "For decades, economists assumed that the wealthier a nation became, the happier its citizens would be. Recent research paints a far more complicated picture. Beyond a certain point, additional income seems to add remarkably little to our sense of wellbeing. Once our basic needs are comfortably met, factors such as strong relationships, meaningful work, and a sense of belonging tend to matter far more than the size of our bank balance. This does not mean money is irrelevant; poverty causes very real suffering. Rather, it suggests that endlessly chasing higher earnings may be a road to nowhere. Perhaps the wisest societies are those that measure their progress not merely by wealth produced, but by the quality of the lives their people actually lead.",
    "translation": "На протяжении десятилетий экономисты полагали, что чем богаче становится нация, тем счастливее будут её граждане. Недавние исследования рисуют куда более сложную картину. За определённой чертой дополнительный доход, похоже, добавляет удивительно мало к нашему ощущению благополучия. Как только наши базовые потребности комфортно удовлетворены, такие факторы, как крепкие отношения, значимая работа и чувство принадлежности, обычно значат гораздо больше, чем размер нашего банковского счёта. Это не означает, что деньги не имеют значения; бедность причиняет вполне реальные страдания. Скорее, это говорит о том, что бесконечная погоня за более высоким заработком может оказаться дорогой в никуда. Возможно, самые мудрые общества — это те, что измеряют свой прогресс не просто произведённым богатством, а качеством жизни, которую на самом деле ведут их люди.",
    "level": "B2"
  },
  {
    "id": 119,
    "title": "The Loneliness Paradox",
    "content": "It seems paradoxical that in an era when we are more connected than ever, so many people report feeling profoundly alone. Part of the explanation lies in the difference between contact and connection. We may exchange messages with dozens of people in a single day, yet rarely have the kind of deep, unhurried conversation that nourishes the soul. Genuine relationships demand vulnerability, the courage to let others see us as we truly are, flaws and all. That prospect can feel daunting, so we retreat into polite small talk and keep others at arm's length. Overcoming loneliness, then, is not simply a matter of meeting more people. It calls for the harder work of lowering our defences and allowing ourselves to be truly known.",
    "translation": "Кажется парадоксальным, что в эпоху, когда мы связаны как никогда прежде, столь многие люди сообщают о чувстве глубокого одиночества. Часть объяснения кроется в различии между контактом и связью. Мы можем обмениваться сообщениями с десятками людей за один день, но редко ведём тот глубокий, неспешный разговор, который питает душу. Подлинные отношения требуют уязвимости, смелости позволить другим увидеть нас такими, какие мы есть на самом деле, со всеми недостатками. Такая перспектива может пугать, поэтому мы прячемся в вежливой светской болтовне и держим других на расстоянии вытянутой руки. Преодоление одиночества, стало быть, — это не просто вопрос знакомства с бо́льшим числом людей. Оно требует более трудной работы — опустить нашу защиту и позволить по-настоящему узнать себя.",
    "level": "B2"
  },
  {
    "id": 120,
    "title": "Art in Times of Crisis",
    "content": "Throughout history, one might expect art to fall silent when societies are gripped by war, poverty, or upheaval. In truth, the opposite is often the case: it is precisely in the darkest hours that art tends to burn brightest. When words fail and hardship threatens to overwhelm us, painting, music, and poetry give voice to feelings that would otherwise remain locked inside. They allow us to process grief, to preserve memory, and to imagine that a better world is still possible. Far from being a mere luxury for comfortable times, art can be a lifeline, binding communities together and reminding us of our shared humanity. That enduring resilience may be the clearest proof that creativity is not an indulgence, but a fundamental human need.",
    "translation": "На протяжении истории можно было бы ожидать, что искусство умолкнет, когда общества охвачены войной, бедностью или потрясениями. На самом деле нередко бывает наоборот: именно в самые тёмные часы искусство обычно горит ярче всего. Когда слов не хватает и невзгоды грозят захлестнуть нас, живопись, музыка и поэзия дают голос чувствам, которые иначе остались бы запертыми внутри. Они позволяют нам переживать горе, сохранять память и представлять, что лучший мир всё ещё возможен. Отнюдь не будучи простой роскошью для благополучных времён, искусство может быть спасательным кругом, связывающим сообщества воедино и напоминающим нам о нашей общей человечности. Эта неувядающая стойкость, возможно, и есть самое ясное доказательство того, что творчество — не потворство своим желаниям, а фундаментальная человеческая потребность.",
    "level": "B2"
  },
  {
    "id": 121,
    "title": "The Convenience of Cities",
    "content": "Urban life offers a remarkable concentration of opportunity, yet its advantages are rarely distributed evenly. In a city, essential services, cultural venues and employment cluster within reach, so that residents can, in principle, satisfy most of their needs without travelling far. This proximity is precisely what makes cities so productive: ideas circulate quickly, talent gathers, and businesses feed off one another. Nevertheless, the same density that generates prosperity also intensifies pressure. Housing becomes scarce and expensive, competition for space sharpens, and those on modest incomes are gradually pushed towards the periphery. As a result, the promise of the city, that anyone might benefit from its abundance, is often qualified by who can afford to remain at its centre. Understanding urban life therefore means recognising a persistent tension: between the openness that draws people in and the inequality that quietly determines who ultimately thrives within its crowded, energetic streets.",
    "translation": "Городская жизнь предлагает поразительную концентрацию возможностей, однако её преимущества редко распределяются равномерно. В городе основные услуги, культурные площадки и рабочие места сосредоточены рядом, так что жители в принципе могут удовлетворить большинство своих потребностей, не путешествуя далеко. Именно эта близость и делает города столь продуктивными: идеи циркулируют быстро, таланты собираются, а предприятия питаются друг от друга. Тем не менее та же плотность, что порождает процветание, также усиливает давление. Жильё становится дефицитным и дорогим, конкуренция за пространство обостряется, а люди со скромными доходами постепенно вытесняются на окраины. В результате обещание города — что каждый может воспользоваться его изобилием — часто оговаривается тем, кто может позволить себе остаться в его центре. Понимать городскую жизнь, следовательно, значит признавать устойчивое напряжение: между открытостью, которая привлекает людей, и неравенством, которое тихо определяет, кто в итоге преуспевает на его переполненных, энергичных улицах.",
    "level": "C1"
  },
  {
    "id": 122,
    "title": "Working From Anywhere",
    "content": "The rise of remote work has quietly redrawn the boundaries between our professional and private lives. Where the office once imposed a clear rhythm, marked by a commute and a fixed departure, many employees now find that the working day expands to fill whatever space is left. Flexibility, so often celebrated, can therefore become a subtle burden: without the physical signal of leaving, some struggle to disengage at all. At the same time, the benefits are genuine and hard to dismiss. Time formerly lost to travel can be reclaimed, and workers gain unprecedented control over where they live. What emerges is not a straightforward improvement but a trade-off, one that each individual must negotiate for themselves. The future of work, in this sense, may depend less on technology than on our collective ability to draw new boundaries deliberately, before the absence of old ones erodes the very freedom that remote arrangements were meant to provide.",
    "translation": "Рост удалённой работы незаметно перечертил границы между нашей профессиональной и частной жизнью. Там, где офис когда-то задавал ясный ритм, отмеченный поездкой на работу и фиксированным уходом, многие сотрудники теперь обнаруживают, что рабочий день расширяется, заполняя любое оставшееся пространство. Гибкость, столь часто прославляемая, может поэтому стать незаметным бременем: без физического сигнала об уходе некоторым вообще трудно отключиться. В то же время выгоды подлинны и от них трудно отмахнуться. Время, ранее терявшееся в дороге, можно вернуть, и работники обретают беспрецедентный контроль над тем, где они живут. То, что возникает, — не однозначное улучшение, а компромисс, который каждый должен согласовывать для себя сам. Будущее труда в этом смысле может зависеть не столько от технологий, сколько от нашей коллективной способности осознанно проводить новые границы, прежде чем отсутствие старых размоет ту самую свободу, которую удалённые схемы должны были предоставить.",
    "level": "C1"
  },
  {
    "id": 123,
    "title": "The Cost of Cheap Goods",
    "content": "Globalisation has made an extraordinary array of products affordable to ordinary consumers, but the low prices we enjoy often conceal a complex web of hidden costs. When manufacturing shifts to wherever labour is cheapest, the true expense is not eliminated so much as displaced, borne by distant workers or absorbed by the environment. A shirt that costs little at the till may have travelled thousands of kilometres, passing through supply chains so tangled that no single party can fully account for its origins. This opacity is not accidental; it allows responsibility to be diffused until it effectively disappears. Consumers, meanwhile, are invited to appreciate the bargain without confronting its consequences. To think critically about globalisation, then, is to look beyond the sticker price and ask who, ultimately, has paid for our convenience, and whether a system that thrives on such deliberate distance can ever be made genuinely accountable to those it quietly relies upon.",
    "translation": "Глобализация сделала необычайное разнообразие товаров доступным для обычных потребителей, но низкие цены, которыми мы наслаждаемся, часто скрывают сложную паутину скрытых издержек. Когда производство перемещается туда, где труд дешевле всего, истинные расходы не столько устраняются, сколько смещаются, ложась на далёких работников или поглощаясь окружающей средой. Рубашка, стоящая на кассе немного, могла проделать тысячи километров, пройдя через цепочки поставок настолько запутанные, что ни одна сторона не может полностью отчитаться за её происхождение. Эта непрозрачность не случайна: она позволяет ответственности рассеиваться, пока та фактически не исчезает. Потребителей же приглашают оценить выгодную покупку, не сталкиваясь с её последствиями. Мыслить критически о глобализации, следовательно, значит смотреть за пределы ценника и спрашивать, кто в конечном счёте заплатил за наше удобство и может ли система, процветающая на такой намеренной дистанции, вообще стать по-настоящему подотчётной тем, на кого она тихо опирается.",
    "level": "C1"
  },
  {
    "id": 124,
    "title": "Small Habits, Large Effects",
    "content": "Discussions of climate change frequently oscillate between two extremes: the sweeping demand for systemic transformation and the quiet insistence on individual responsibility. Each position contains a partial truth, yet each becomes misleading when treated as sufficient on its own. Emphasising personal habits alone risks letting powerful institutions evade scrutiny, as though the fate of the planet rested chiefly on recycling and shorter showers. Conversely, dismissing individual action as trivial can breed a paralysing fatalism, in which nothing anyone does seems to matter. The more honest view acknowledges that these levels are interdependent rather than opposed. Personal choices, aggregated and normalised, shift the cultural expectations that make broader policy politically feasible; and ambitious policy, in turn, reshapes the everyday choices available to citizens. Sustainability, properly understood, is therefore not a matter of choosing between the individual and the collective, but of grasping how each continually conditions and reinforces the other.",
    "translation": "Обсуждения изменения климата часто колеблются между двумя крайностями: масштабным требованием системной трансформации и тихим настаиванием на индивидуальной ответственности. Каждая позиция содержит частичную истину, однако каждая становится обманчивой, когда её считают достаточной саму по себе. Акцент лишь на личных привычках рискует позволить могущественным институтам избежать проверки, как будто судьба планеты зависит в основном от переработки отходов и более коротких душей. И наоборот, отвержение индивидуального действия как несущественного может породить парализующий фатализм, в котором ничто из того, что кто-либо делает, не кажется важным. Более честный взгляд признаёт, что эти уровни взаимозависимы, а не противопоставлены. Личные выборы, суммированные и нормализованные, сдвигают культурные ожидания, которые делают более широкую политику политически осуществимой; а амбициозная политика, в свою очередь, переформирует повседневные выборы, доступные гражданам. Устойчивость, понятая правильно, следовательно, есть не вопрос выбора между индивидуальным и коллективным, а вопрос осознания того, как каждое непрерывно обусловливает и укрепляет другое.",
    "level": "C1"
  },
  {
    "id": 125,
    "title": "Algorithms and Attention",
    "content": "The platforms that mediate much of our information do not present the world neutrally; they curate it according to objectives that are rarely visible to those they serve. An algorithm designed to maximise engagement will inevitably favour whatever holds attention, and what holds attention is not necessarily what informs, edifies or calms. Outrage, novelty and confirmation of existing beliefs tend to perform well, while nuance and complexity are quietly disadvantaged. Over time, this subtle bias can reshape not merely what we see but what we come to expect and desire. The danger lies less in any single distorted story than in the gradual recalibration of our collective appetites. If we consume information chiefly through systems optimised for their own commercial ends, we should not be surprised when public understanding drifts in directions no one intended. Reclaiming agency begins with recognising that the interface is never innocent, and that convenience always carries an editorial hand.",
    "translation": "Платформы, опосредующие большую часть нашей информации, не представляют мир нейтрально; они курируют его в соответствии с целями, которые редко видимы тем, кому они служат. Алгоритм, разработанный для максимизации вовлечённости, неизбежно будет отдавать предпочтение всему, что удерживает внимание, а то, что удерживает внимание, не обязательно то, что информирует, назидает или успокаивает. Возмущение, новизна и подтверждение существующих убеждений, как правило, работают хорошо, тогда как нюанс и сложность тихо оказываются в невыгодном положении. Со временем это тонкое смещение может переформировать не просто то, что мы видим, но и то, чего мы начинаем ожидать и желать. Опасность заключается не столько в какой-либо отдельной искажённой истории, сколько в постепенной перекалибровке наших коллективных аппетитов. Если мы потребляем информацию главным образом через системы, оптимизированные для их собственных коммерческих целей, нам не следует удивляться, когда общественное понимание дрейфует в направлениях, которых никто не замышлял. Возвращение свободы действий начинается с осознания того, что интерфейс никогда не невинен и что удобство всегда несёт редакторскую руку.",
    "level": "C1"
  },
  {
    "id": 126,
    "title": "Machines That Decide",
    "content": "As algorithms increasingly assume decisions once reserved for humans, from approving loans to filtering job applicants, a difficult question arises: who bears responsibility when such a system errs? The appeal of automated judgement lies in its apparent objectivity, its freedom from the fatigue and prejudice to which people are prone. Yet this impartiality is largely illusory, for any model inherits the assumptions of its designers and the biases latent in the data it consumes. A decision may feel neutral precisely because its reasoning is hidden, encoded in weights that no one can readily interpret. When outcomes prove unjust, accountability dissolves into a fog of technical complexity, with each party gesturing towards another. The ethical challenge, therefore, is not merely to build systems that perform well on average, but to ensure that their exercise of power remains contestable, explicable and ultimately answerable to the human communities whose lives they increasingly govern.",
    "translation": "По мере того как алгоритмы всё чаще принимают решения, некогда предназначенные для людей, — от одобрения кредитов до отбора соискателей — возникает трудный вопрос: кто несёт ответственность, когда такая система ошибается? Привлекательность автоматизированного суждения заключается в его кажущейся объективности, его свободе от усталости и предрассудков, которым подвержены люди. Однако эта беспристрастность в значительной мере иллюзорна, ибо любая модель наследует допущения своих создателей и предвзятости, скрытые в данных, которые она поглощает. Решение может казаться нейтральным именно потому, что его рассуждение спрятано, закодировано в весах, которые никто не может легко истолковать. Когда результаты оказываются несправедливыми, подотчётность растворяется в тумане технической сложности, где каждая сторона указывает на другую. Этический вызов, следовательно, состоит не просто в создании систем, которые в среднем работают хорошо, но в обеспечении того, чтобы их осуществление власти оставалось оспоримым, объяснимым и в конечном счёте подотчётным человеческим сообществам, чьими жизнями они всё больше управляют.",
    "level": "C1"
  },
  {
    "id": 127,
    "title": "The Vanishing Middle",
    "content": "Automation has long been expected to displace routine manual labour, but its more consequential effect may be the hollowing out of the occupational middle. Tasks that follow predictable rules, however cognitively demanding, are precisely those most amenable to codification, whereas work at either extreme resists it. At the top, roles demanding judgement, creativity and interpersonal subtlety remain stubbornly human; at the bottom, tasks requiring physical dexterity in unstructured settings prove surprisingly hard to mechanise. The result is a labour market pulled towards its poles, with fewer secure, moderately skilled positions in between. This polarisation carries social as well as economic weight, for it was often these middling jobs that offered stable advancement to those without elite credentials. If the ladder loses its central rungs, mobility itself is imperilled, and the comfortable assumption that technological progress lifts everyone in due course begins to look less like a law than a hopeful and increasingly fragile aspiration.",
    "translation": "От автоматизации давно ожидали вытеснения рутинного физического труда, но её более значимым эффектом может стать выхолащивание профессиональной середины. Задачи, следующие предсказуемым правилам, сколь бы когнитивно требовательными они ни были, — именно те, что легче всего поддаются кодификации, тогда как работа на обоих полюсах ей сопротивляется. Наверху роли, требующие суждения, творчества и межличностной тонкости, остаются упрямо человеческими; внизу задачи, требующие физической ловкости в неструктурированных условиях, оказываются на удивление трудными для механизации. Результатом становится рынок труда, стягиваемый к своим полюсам, с меньшим числом надёжных, умеренно квалифицированных позиций посередине. Эта поляризация несёт как социальный, так и экономический вес, ибо именно эти срединные рабочие места часто предлагали стабильное продвижение тем, у кого не было элитных дипломов. Если лестница теряет свои центральные ступени, под угрозой оказывается сама мобильность, и удобное допущение, что технический прогресс со временем поднимает всех, начинает выглядеть не столько законом, сколько обнадёживающим и всё более хрупким чаянием.",
    "level": "C1"
  },
  {
    "id": 128,
    "title": "News Without Gatekeepers",
    "content": "The dismantling of traditional editorial gatekeeping has been hailed as a democratisation of information, and in certain respects the celebration is warranted. Voices once excluded from the public conversation can now reach audiences directly, unmediated by institutions that were themselves far from neutral. Yet the removal of gatekeepers has not abolished the exercise of power over what circulates; it has merely relocated it. In place of editors, we now have ranking systems, recommendation engines and the diffuse pressures of virality, none of which was designed with the health of public discourse in mind. The old arrangement concentrated authority in identifiable hands that could, at least in principle, be held to account; the new one disperses it into mechanisms that resist scrutiny precisely because they belong to no one in particular. Freedom from gatekeepers, it turns out, is not the same as freedom from being governed, only a change in the character of the governing.",
    "translation": "Демонтаж традиционного редакторского контроля приветствовался как демократизация информации, и в определённых отношениях это торжество оправдано. Голоса, некогда исключённые из публичного разговора, теперь могут достигать аудитории напрямую, не опосредованные институтами, которые сами были далеко не нейтральны. Однако устранение «привратников» не упразднило осуществление власти над тем, что циркулирует; оно лишь переместило её. Вместо редакторов у нас теперь системы ранжирования, рекомендательные движки и рассеянное давление вирусности — ни одно из которых не проектировалось с заботой о здоровье публичного дискурса. Прежнее устройство сосредоточивало власть в опознаваемых руках, которые можно было, по крайней мере в принципе, призвать к ответу; новое рассеивает её в механизмах, сопротивляющихся проверке именно потому, что они не принадлежат никому в частности. Свобода от привратников, как выясняется, не то же самое, что свобода от управления, а лишь перемена в характере управляющего.",
    "level": "C1"
  },
  {
    "id": 129,
    "title": "The Right to Disconnect",
    "content": "In an economy where communication is instantaneous and perpetual, the boundary that once protected leisure has grown alarmingly porous. The mere possibility of being reached, at any hour and from any place, imposes a low but constant demand on attention, an expectation of availability that few employers need articulate because the technology articulates it for them. Some jurisdictions have responded by legislating a formal right to disconnect, obliging firms to respect the limits of the working day. Critics dismiss such measures as unenforceable or paternalistic, yet their symbolic weight should not be underestimated. By naming the problem, the law reasserts a principle that the market, left to itself, steadily erodes: that a worker's time is not infinitely elastic, and that rest is not a privilege grudgingly granted but a condition of any sustainable and genuinely humane arrangement between labour and the enterprises that depend upon it.",
    "translation": "В экономике, где общение мгновенно и непрерывно, граница, некогда защищавшая досуг, стала тревожно проницаемой. Сама возможность быть достигнутым в любой час и из любого места налагает низкую, но постоянную нагрузку на внимание — ожидание доступности, которое немногим работодателям нужно артикулировать, потому что технология артикулирует его за них. Некоторые юрисдикции ответили, законодательно закрепив формальное право на отключение, обязывающее фирмы уважать пределы рабочего дня. Критики отмахиваются от таких мер как неисполнимых или патерналистских, однако их символический вес не следует недооценивать. Называя проблему, закон вновь утверждает принцип, который рынок, предоставленный самому себе, неуклонно размывает: что время работника не бесконечно эластично и что отдых — не привилегия, неохотно даруемая, а условие любого устойчивого и по-настоящему гуманного соглашения между трудом и предприятиями, которые от него зависят.",
    "level": "C1"
  },
  {
    "id": 130,
    "title": "Cities That Breathe",
    "content": "The most ambitious visions of urban sustainability propose not merely to reduce a city's environmental harm but to reconceive the city itself as a living system, one that metabolises resources rather than merely consuming them. In such a vision, waste heat from one process warms another, rainwater is captured rather than flushed away, and green corridors thread through the built environment to cool the air and shelter fragile ecologies. What distinguishes this approach from conventional environmental measures is its insistence on integration: efficiencies are sought not in isolated components but in the relationships between them. The obstacle, however, is rarely technical. Cities are palimpsests of past decisions, layered infrastructures and entrenched interests, none of which yields easily to holistic redesign. To make a city breathe, therefore, is as much a political and institutional undertaking as an engineering one, demanding a patience and coordination that democratic systems, for all their virtues, seldom sustain.",
    "translation": "Самые амбициозные представления о городской устойчивости предлагают не просто уменьшить экологический вред города, но переосмыслить сам город как живую систему — такую, что метаболизирует ресурсы, а не просто их потребляет. В таком видении сбросное тепло от одного процесса согревает другой, дождевая вода улавливается, а не смывается прочь, а зелёные коридоры пронизывают застроенную среду, охлаждая воздух и укрывая хрупкие экосистемы. Что отличает этот подход от обычных природоохранных мер — так это настойчивое требование интеграции: эффективность ищется не в изолированных компонентах, а в отношениях между ними. Препятствие, однако, редко бывает техническим. Города — это палимпсесты прошлых решений, наслоённых инфраструктур и укоренившихся интересов, ни один из которых не поддаётся легко целостному переустройству. Заставить город дышать, следовательно, — это столь же политическое и институциональное предприятие, сколь и инженерное, требующее терпения и координации, которые демократические системы, при всех их достоинствах, редко способны поддерживать.",
    "level": "C1"
  },
  {
    "id": 131,
    "title": "The Illusion of Consensus",
    "content": "Digital networks were once expected to enlarge our exposure to differing views, yet in practice they frequently narrow it, cocooning us within communities of the like-minded. What makes this tendency insidious is not the mere existence of agreement but the illusion of consensus it fosters. When one encounters the same opinions repeatedly, echoed by seemingly independent voices, those opinions acquire an unearned authority; their prevalence within a curated circle is mistaken for their prevalence in the world at large. This distortion has consequences beyond the personal. Movements can overestimate their support, dismiss opposition as marginal, and be genuinely bewildered when reality confounds their expectations. The remedy is not simply to seek out disagreement, though that helps, but to cultivate a certain epistemic humility, an awareness that the vividness with which a view presents itself to us is no reliable measure of how widely, or how justly, it is actually held.",
    "translation": "От цифровых сетей некогда ожидали, что они расширят наше соприкосновение с различными взглядами, однако на практике они нередко его сужают, укутывая нас в сообщества единомышленников. Что делает эту тенденцию коварной — не само существование согласия, а иллюзия консенсуса, которую она порождает. Когда человек снова и снова встречает одни и те же мнения, эхом отражаемые, казалось бы, независимыми голосами, эти мнения обретают незаслуженный авторитет; их распространённость в тщательно отобранном кругу принимается за их распространённость в мире в целом. Это искажение имеет последствия за пределами личного. Движения могут переоценивать свою поддержку, отвергать оппозицию как маргинальную и искренне недоумевать, когда реальность опрокидывает их ожидания. Средство — не просто искать несогласие, хотя это и помогает, а взращивать некоторое эпистемическое смирение, осознание того, что яркость, с которой взгляд предстаёт перед нами, не является надёжной мерой того, насколько широко или насколько справедливо он на самом деле разделяется.",
    "level": "C1"
  },
  {
    "id": 132,
    "title": "Progress and Its Shadow",
    "content": "Every technological advance arrives accompanied by a shadow it seldom acknowledges: the displacement of skills, communities and ways of life rendered suddenly obsolete. We are inclined to narrate progress as pure addition, a steady accumulation of capability, and to overlook the subtractions that accompany it. Yet innovation is rarely neutral in its distribution of gains and losses; it tends to reward those positioned to exploit it while quietly stranding those bound to the arrangements it supersedes. The ethical difficulty is that these losses are frequently invisible in the aggregate statistics by which progress is measured. A rising average conceals the individuals for whom the change was catastrophic. To govern technology wisely, then, requires more than celebrating what it makes possible; it demands a sustained attentiveness to what, and whom, it leaves behind, and a willingness to shoulder collectively the costs that the market, indifferent by design, distributes so unevenly and so silently.",
    "translation": "Каждое технологическое достижение приходит в сопровождении тени, которую оно редко признаёт: вытеснения навыков, сообществ и укладов жизни, внезапно оказавшихся устаревшими. Мы склонны повествовать о прогрессе как о чистом прибавлении, неуклонном накоплении возможностей, и упускать из виду вычитания, которые его сопровождают. Однако инновация редко нейтральна в своём распределении выгод и потерь; она склонна вознаграждать тех, кто расположен её использовать, тихо бросая на мель тех, кто привязан к устройствам, которые она вытесняет. Этическая трудность в том, что эти потери часто невидимы в совокупной статистике, которой измеряется прогресс. Растущее среднее скрывает тех, для кого перемена оказалась катастрофой. Управлять технологией мудро, следовательно, требует большего, чем прославление того, что она делает возможным; это требует непрерывной внимательности к тому, что и кого она оставляет позади, и готовности коллективно нести те издержки, которые рынок, безразличный по своей природе, распределяет столь неравномерно и столь безмолвно.",
    "level": "C1"
  },
  {
    "id": 133,
    "title": "The Tragedy of the Commons",
    "content": "The predicament of climate action is often illuminated by an old parable in which shared pasture is ruined because each herder, acting rationally, adds one more animal, reaping the full benefit while the harm is borne by all. The atmosphere is such a commons, and its degradation follows the same relentless logic: the advantages of emission accrue locally and immediately, while the costs are dispersed across the globe and deferred into the future. No individual actor, whether a person or a nation, has a compelling incentive to restrain itself when restraint merely cedes advantage to others less scrupulous. What the parable reveals is that the failure is structural rather than moral; appeals to conscience, however sincere, cannot reliably overcome incentives arrayed so firmly against cooperation. The escape, if one exists, lies in constructing institutions that alter the calculus itself, binding actors together so that self-interest and collective survival cease to pull in opposite directions.",
    "translation": "Затруднение с борьбой против изменения климата часто освещается старой притчей, в которой общее пастбище разоряется, потому что каждый пастух, действуя рационально, добавляет ещё одно животное, пожиная полную выгоду, тогда как вред несут все. Атмосфера — такое общее достояние, и её деградация следует той же неумолимой логике: преимущества выбросов накапливаются локально и немедленно, тогда как издержки рассеиваются по всему миру и откладываются в будущее. Ни у одного отдельного действующего лица, будь то человек или нация, нет убедительного стимула сдерживать себя, когда сдержанность лишь уступает преимущество другим, менее щепетильным. Что раскрывает притча — так это то, что провал структурен, а не морален; призывы к совести, сколь бы искренними они ни были, не могут надёжно преодолеть стимулы, столь твёрдо выстроенные против сотрудничества. Выход, если он существует, заключается в построении институтов, которые изменяют само исчисление, связывая действующих лиц воедино так, чтобы личный интерес и коллективное выживание перестали тянуть в противоположные стороны.",
    "level": "C1"
  },
  {
    "id": 134,
    "title": "Belonging in the Global City",
    "content": "The global city presents a paradox of intimacy and estrangement. Drawing together people from every corner of the earth, it offers an unprecedented density of encounter, yet the very heterogeneity that makes it vibrant can also render belonging elusive. Where a traditional community derived cohesion from shared history and inherited assumptions, the global city offers no such ready-made bond; solidarity, if it emerges at all, must be constructed rather than inherited. This is demanding work, and its failure is visible in the parallel worlds that so often coexist within a single metropolis, populations occupying the same physical space while inhabiting entirely separate social realities. Yet the possibility latent in such places should not be dismissed. Precisely because nothing is presupposed, the global city becomes a laboratory in which new and more capacious forms of collective identity might be forged, provided its inhabitants can summon the imagination, and the generosity, that the task so plainly requires.",
    "translation": "Глобальный город являет парадокс близости и отчуждения. Стягивая вместе людей из каждого уголка земли, он предлагает беспрецедентную плотность встреч, однако сама разнородность, что делает его живым, может также делать принадлежность ускользающей. Там, где традиционное сообщество черпало сплочённость из общей истории и унаследованных допущений, глобальный город не предлагает такой готовой связи; солидарность, если она вообще возникает, должна быть построена, а не унаследована. Это требовательная работа, и её провал виден в параллельных мирах, столь часто сосуществующих в пределах одного мегаполиса, — в группах населения, занимающих одно и то же физическое пространство, но обитающих в совершенно раздельных социальных реальностях. И всё же возможность, скрытую в таких местах, не следует отвергать. Именно потому, что ничто не предполагается заранее, глобальный город становится лабораторией, в которой могут выковываться новые и более вместительные формы коллективной идентичности — при условии, что его обитатели сумеют призвать воображение и великодушие, которых задача столь очевидно требует.",
    "level": "C1"
  },
  {
    "id": 135,
    "title": "The Ethics of Prediction",
    "content": "As predictive systems grow more sophisticated, they promise to anticipate our behaviour with uncanny accuracy, forecasting what we will buy, whether we will default, even whether we might offend. Yet the very act of prediction, once it informs consequential decisions, threatens to become self-fulfilling in ways that quietly subvert the freedom it purports merely to observe. If a person is denied opportunity on the basis of a forecast, they are not simply being judged by their probable future; they are being nudged towards it, their prospects narrowed by an expectation that then helps to ensure its own confirmation. The deeper ethical worry is not inaccuracy but a peculiar kind of accuracy that manufactures the reality it claims to describe. A society governed increasingly by prediction risks foreclosing the possibility of self-revision, treating individuals as the sum of their statistical antecedents rather than as agents capable of confounding the very models that presume to know them.",
    "translation": "По мере того как прогностические системы становятся всё более изощрёнными, они обещают предвосхищать наше поведение с жутковатой точностью, предсказывая, что мы купим, объявим ли мы дефолт, даже совершим ли мы правонарушение. Однако сам акт предсказания, как только он влияет на значимые решения, грозит стать самосбывающимся способами, которые тихо подрывают ту свободу, которую он якобы всего лишь наблюдает. Если человеку отказывают в возможности на основании прогноза, его не просто судят по его вероятному будущему; его подталкивают к нему, сужая его перспективы ожиданием, которое затем помогает обеспечить собственное подтверждение. Более глубокое этическое беспокойство — не неточность, а своеобразная точность, которая изготавливает ту реальность, которую претендует описывать. Общество, всё больше управляемое предсказанием, рискует закрыть возможность самопересмотра, обращаясь с индивидами как с суммой их статистических предпосылок, а не как с субъектами, способными опровергнуть те самые модели, что берутся их знать.",
    "level": "C1"
  },
  {
    "id": 136,
    "title": "The Comfort of Habits",
    "content": "Psychologists have long observed that much of our daily behaviour operates on autopilot. Habits, once established, allow the brain to conserve energy by automating routine decisions, from the route we take to work to the way we hold a cup. This efficiency, however, comes at a cost. Because habitual actions bypass conscious deliberation, we often persist in behaviours that no longer serve us, simply because breaking them demands sustained attention and effort. Interestingly, research suggests that habits are not erased but overwritten; the old pattern lingers beneath the new one, ready to resurface under stress or fatigue. Understanding this helps explain why change is so difficult and why relapse is common. Rather than relying on willpower alone, behavioural scientists recommend reshaping the environment that triggers unwanted routines. By altering the cues around us, we make desirable actions easier and undesirable ones less accessible, gently steering behaviour without exhausting our limited reserves of self-control.",
    "translation": "Психологи давно заметили, что значительная часть нашего повседневного поведения работает на автопилоте. Привычки, однажды сформировавшись, позволяют мозгу экономить энергию, автоматизируя рутинные решения — от маршрута до работы до того, как мы держим чашку. Однако эта эффективность имеет свою цену. Поскольку привычные действия обходят сознательное обдумывание, мы часто продолжаем поведение, которое уже не служит нам, просто потому что его прекращение требует устойчивого внимания и усилий. Любопытно, что исследования показывают: привычки не стираются, а перезаписываются; старый паттерн сохраняется под новым, готовый вновь проявиться при стрессе или усталости. Понимание этого помогает объяснить, почему перемены даются так трудно и почему рецидивы столь распространены. Вместо того чтобы полагаться лишь на силу воли, специалисты по поведению советуют перестраивать среду, которая запускает нежелательные привычки. Изменяя окружающие нас сигналы, мы делаем желательные действия проще, а нежелательные — менее доступными, мягко направляя поведение и не истощая наши ограниченные запасы самоконтроля.",
    "level": "C1"
  },
  {
    "id": 137,
    "title": "Why We Trust Experts",
    "content": "In an age saturated with information, deciding whom to believe has become a genuine cognitive challenge. We cannot personally verify most of what we accept as true, so we outsource judgement to experts whose authority we take largely on faith. Yet trust in expertise is neither blind nor unconditional. People tend to grant credibility to those who demonstrate consistency, transparency, and a willingness to acknowledge uncertainty. Paradoxically, an expert who admits the limits of their knowledge often appears more trustworthy than one who projects absolute confidence. This reflects an intuitive understanding that genuine competence is rarely dogmatic. Problems arise, however, when expertise is politicised or when competing authorities issue contradictory claims. Confronted with such dissonance, many retreat into scepticism or embrace whichever voice confirms their existing beliefs. Restoring healthy trust therefore requires not only competent experts but also a public equipped to distinguish reasoned argument from mere assertion, a skill that education too often neglects to cultivate.",
    "translation": "В эпоху, насыщенную информацией, решение о том, кому верить, превратилось в настоящую когнитивную задачу. Мы не можем лично проверить большую часть того, что принимаем за истину, поэтому передаём суждение экспертам, чей авторитет во многом принимаем на веру. Однако доверие к экспертному знанию не является ни слепым, ни безусловным. Люди склонны наделять доверием тех, кто демонстрирует последовательность, прозрачность и готовность признавать неопределённость. Парадоксально, но эксперт, признающий пределы своих знаний, часто кажется более надёжным, чем тот, кто излучает абсолютную уверенность. Это отражает интуитивное понимание того, что подлинная компетентность редко бывает догматичной. Проблемы, однако, возникают, когда экспертиза политизируется или когда конкурирующие авторитеты выдвигают противоречивые утверждения. Столкнувшись с таким диссонансом, многие уходят в скептицизм или принимают тот голос, который подтверждает их прежние убеждения. Поэтому восстановление здорового доверия требует не только компетентных экспертов, но и общества, способного отличать обоснованный довод от простого утверждения — навыка, который образование слишком часто не развивает.",
    "level": "C1"
  },
  {
    "id": 138,
    "title": "The Serendipity of Discovery",
    "content": "The popular image of scientific progress as a steady march of deliberate experiment obscures the surprising role of chance. Many landmark discoveries emerged not from careful planning but from accidents that alert minds were prepared to exploit. Penicillin, X-rays, and even the microwave oven owe their existence to observations that a less attentive researcher might have dismissed as errors. Yet to call these breakthroughs mere luck would be misleading. Serendipity favours those who possess the knowledge to recognise significance in the unexpected and the courage to pursue it against prevailing assumptions. What appears accidental is, in truth, the meeting of an anomaly with a mind trained to interpret it. This suggests that fostering discovery depends as much on cultivating curiosity and tolerance for ambiguity as on funding structured research. A laboratory too narrowly focused on predetermined outcomes may inadvertently filter out the very irregularities from which transformative insight so often springs.",
    "translation": "Расхожий образ научного прогресса как размеренного шествия целенаправленных экспериментов затмевает удивительную роль случайности. Многие эпохальные открытия возникли не из тщательного планирования, а из случайностей, которые бдительные умы сумели использовать. Пенициллин, рентгеновские лучи и даже микроволновая печь обязаны своим существованием наблюдениям, которые менее внимательный исследователь мог бы отбросить как ошибки. Однако называть эти прорывы простой удачей было бы неверно. Счастливая случайность благоволит тем, кто обладает знаниями, чтобы распознать значимость в неожиданном, и смелостью, чтобы преследовать её вопреки господствующим представлениям. То, что кажется случайным, на самом деле есть встреча аномалии с умом, обученным её толковать. Это наводит на мысль, что содействие открытиям зависит от воспитания любопытства и терпимости к неоднозначности в той же мере, что и от финансирования структурированных исследований. Лаборатория, чересчур узко сосредоточенная на заранее заданных результатах, может невольно отсеивать те самые отклонения, из которых так часто рождается преобразующее прозрение.",
    "level": "C1"
  },
  {
    "id": 139,
    "title": "The Meaning of Colour",
    "content": "Colour is far more than a physical property of light; it is a language laden with cultural meaning and emotional resonance. Across societies, the same hue can signify opposite ideas: white evokes purity in one tradition and mourning in another. Artists have long exploited this ambiguity, using colour not merely to represent the visible world but to shape how we feel about it. A canvas dominated by cold blues invites contemplation or melancholy, while warm reds provoke urgency and passion. What makes colour so powerful is that its effects operate beneath conscious awareness; we respond emotionally before we can articulate why. Neuroscience has begun to trace these reactions to deep evolutionary associations, yet no purely biological account can capture the layers of learned symbolism a viewer brings. When we stand before a painting, then, we are decoding a message written in two languages at once: one inscribed in our nervous system, the other inherited from our culture.",
    "translation": "Цвет — это гораздо больше, чем физическое свойство света; это язык, насыщенный культурным смыслом и эмоциональным откликом. В разных обществах один и тот же оттенок может обозначать противоположные идеи: белый в одной традиции символизирует чистоту, а в другой — траур. Художники издавна пользовались этой двусмысленностью, применяя цвет не просто для изображения видимого мира, но чтобы формировать наше отношение к нему. Полотно, где преобладает холодная синева, располагает к созерцанию или меланхолии, тогда как тёплые красные тона пробуждают напряжение и страсть. Сила цвета в том, что его воздействие происходит ниже порога осознания; мы реагируем эмоционально прежде, чем можем объяснить почему. Нейронаука начала прослеживать эти реакции до глубоких эволюционных ассоциаций, однако никакое чисто биологическое объяснение не способно охватить пласты усвоенной символики, которые привносит зритель. Стоя перед картиной, мы, таким образом, расшифровываем послание, написанное сразу на двух языках: одном, запечатлённом в нашей нервной системе, и другом, унаследованном от нашей культуры.",
    "level": "C1"
  },
  {
    "id": 140,
    "title": "The Illusion of Choice",
    "content": "Modern consumers pride themselves on the abundance of options available to them, yet behavioural economists question whether this abundance genuinely empowers us. Beyond a certain threshold, an excess of choice tends to paralyse rather than liberate. Faced with dozens of comparable products, shoppers frequently postpone decisions, feel less satisfied with whatever they eventually select, and second-guess themselves afterwards. This phenomenon, sometimes called the paradox of choice, reveals a mismatch between what we believe we want and how our minds actually cope with complexity. Retailers exploit this vulnerability deliberately, arranging options to nudge us toward more profitable purchases while preserving the comforting illusion of autonomy. We imagine ourselves as rational agents weighing alternatives, when in reality much of our decision-making is steered by framing, defaults, and subtle contextual cues. Recognising these forces does not eliminate them, but it may allow us to reclaim a measure of the deliberate judgement we too readily surrender.",
    "translation": "Современные потребители гордятся изобилием доступных им вариантов, однако поведенческие экономисты сомневаются, действительно ли это изобилие расширяет наши возможности. За определённым порогом избыток выбора скорее парализует, чем освобождает. Столкнувшись с десятками сопоставимых товаров, покупатели часто откладывают решения, остаются менее довольны тем, что в итоге выбирают, и впоследствии сомневаются в себе. Это явление, иногда называемое парадоксом выбора, обнажает несоответствие между тем, чего, как нам кажется, мы хотим, и тем, как наш разум на самом деле справляется со сложностью. Розничные продавцы намеренно используют эту уязвимость, располагая варианты так, чтобы подтолкнуть нас к более выгодным для них покупкам, сохраняя при этом утешительную иллюзию самостоятельности. Мы воображаем себя рациональными субъектами, взвешивающими альтернативы, тогда как в действительности значительная часть наших решений направляется формулировкой, настройками по умолчанию и едва заметными подсказками контекста. Осознание этих сил не устраняет их, но может позволить нам вернуть себе долю осознанного суждения, от которого мы слишком легко отказываемся.",
    "level": "C1"
  },
  {
    "id": 141,
    "title": "Rethinking the Classroom",
    "content": "For over a century, the standard classroom has been organised around a single, enduring assumption: that knowledge flows from an authoritative teacher to passive students seated in orderly rows. Reformers increasingly challenge this model as a relic of the industrial age, ill-suited to a world that prizes creativity and adaptability over the mechanical recall of facts. Alternative approaches invert the traditional hierarchy, casting the teacher as a facilitator who guides inquiry rather than dispensing answers. Students, in turn, are encouraged to grapple with open-ended problems, collaborate, and learn from productive failure. Yet such reforms face formidable resistance. They demand smaller classes, extensive teacher training, and assessment methods that resist easy quantification, none of which sit comfortably with budgets or league tables. The deeper obstacle, however, may be cultural: a lingering conviction that rigour means discipline and that learning must be uncomfortable to be worthwhile. Overcoming this inheritance requires reimagining not merely methods but the very purpose of education.",
    "translation": "На протяжении более чем столетия обычный школьный класс строился вокруг одного устойчивого допущения: что знание перетекает от авторитетного учителя к пассивным ученикам, сидящим ровными рядами. Реформаторы всё чаще оспаривают эту модель как пережиток индустриальной эпохи, плохо приспособленный к миру, который ценит творчество и гибкость выше механического воспроизведения фактов. Альтернативные подходы переворачивают традиционную иерархию, отводя учителю роль наставника, который направляет исследование, а не раздаёт готовые ответы. Ученикам же предлагается биться над открытыми задачами, сотрудничать и учиться на плодотворных ошибках. Однако такие реформы наталкиваются на серьёзное сопротивление. Они требуют меньших классов, обширной подготовки учителей и методов оценивания, не поддающихся простому измерению, — а всё это плохо сочетается с бюджетами и рейтинговыми таблицами. Более глубоким препятствием, впрочем, может быть культура: укоренившееся убеждение, что строгость означает дисциплину и что учёба должна быть некомфортной, чтобы быть стоящей. Преодоление этого наследия требует переосмысления не только методов, но и самой цели образования.",
    "level": "C1"
  },
  {
    "id": 142,
    "title": "The Placebo Effect",
    "content": "Few phenomena in medicine are as humbling as the placebo effect, whereby an inert substance produces measurable therapeutic benefits simply because the patient expects it to. Once dismissed as a nuisance to be controlled for in trials, the effect is now recognised as a window into the profound influence of the mind over the body. Expectation, ritual, and the reassuring presence of a caregiver can trigger genuine physiological changes, releasing the body's own analgesics and modulating perceptions of pain. Remarkably, some studies indicate that placebos may retain a degree of potency even when patients know they are receiving them. This challenges the tidy boundary we like to draw between real and imagined healing. It also raises uncomfortable ethical questions about honesty and consent. If belief itself can heal, medicine must reckon with the possibility that the manner in which treatment is delivered may matter as much as its pharmacological content.",
    "translation": "Немногие явления в медицине столь отрезвляющи, как эффект плацебо, при котором инертное вещество приносит измеримую терапевтическую пользу лишь потому, что пациент этого ожидает. Некогда отвергаемый как помеха, которую нужно учитывать в испытаниях, этот эффект теперь признан окном в глубокое влияние разума на тело. Ожидание, ритуал и обнадёживающее присутствие врача способны запускать подлинные физиологические изменения, высвобождая собственные обезболивающие вещества организма и меняя восприятие боли. Поразительно, но некоторые исследования указывают, что плацебо может сохранять определённую действенность, даже когда пациенты знают, что получают именно его. Это ставит под сомнение аккуратную границу, которую мы любим проводить между настоящим и воображаемым исцелением. Это также поднимает неудобные этические вопросы о честности и согласии. Если сама вера способна исцелять, медицина должна считаться с тем, что способ, которым оказывается лечение, может значить не меньше, чем его фармакологическое содержание.",
    "level": "C1"
  },
  {
    "id": 143,
    "title": "The Wisdom of Crowds",
    "content": "Under certain conditions, a large group of ordinary people can collectively arrive at judgements more accurate than those of any individual expert. This counterintuitive principle, dubbed the wisdom of crowds, rests on the observation that independent errors tend to cancel one another out, leaving a surprisingly reliable average. Markets, prediction contests, and even estimates of an ox's weight at a country fair have demonstrated its power. Yet the phenomenon is fragile and easily corrupted. It depends on diversity of opinion, independence of judgement, and a mechanism for aggregating dispersed knowledge. Remove any of these ingredients and the crowd's wisdom curdles into folly. When individuals imitate one another, defer to a dominant voice, or fall prey to shared bias, collective error compounds rather than cancels. The distinction between a wise crowd and a foolish mob thus hinges not on the number of participants but on whether their judgements remain genuinely their own.",
    "translation": "При определённых условиях большая группа обычных людей способна совместно приходить к суждениям более точным, чем суждения любого отдельного эксперта. Этот противоречащий интуиции принцип, названный мудростью толпы, опирается на наблюдение, что независимые ошибки склонны взаимно погашаться, оставляя удивительно надёжное среднее. Рынки, соревнования по прогнозированию и даже оценки веса быка на сельской ярмарке доказали его силу. Однако это явление хрупко и легко разрушается. Оно зависит от разнообразия мнений, независимости суждений и механизма, объединяющего рассеянные знания. Уберите любой из этих ингредиентов — и мудрость толпы обращается в глупость. Когда люди подражают друг другу, уступают доминирующему голосу или поддаются общему предубеждению, коллективная ошибка не гасится, а накапливается. Таким образом, различие между мудрой толпой и безрассудной массой определяется не числом участников, а тем, остаются ли их суждения по-настоящему своими.",
    "level": "C1"
  },
  {
    "id": 144,
    "title": "Art and Its Forgeries",
    "content": "The existence of convincing art forgeries poses a disquieting question: if a copy is indistinguishable from the original, wherein lies the value we ascribe to authenticity? A forgery may delight the eye exactly as its model does, yet the moment its deception is exposed, its worth collapses and admiration turns to contempt. This reaction reveals that our appreciation of art is never purely aesthetic. We prize the singular touch of the artist, the historical thread connecting object to maker, and the narrative of genius that the forgery counterfeits. In effect, we respond not merely to what we see but to what we believe about its origin. Some philosophers argue this reverence for authenticity is irrational, a fetishism of provenance over experience. Others contend that context is inseparable from meaning, that an artwork is a document of a particular human act. Whichever view prevails, the forger's craft exposes how much of beauty resides in the story we tell ourselves.",
    "translation": "Существование убедительных подделок произведений искусства ставит тревожный вопрос: если копия неотличима от оригинала, в чём же заключена ценность, которую мы приписываем подлинности? Подделка может радовать глаз в точности так же, как её образец, но в тот миг, когда её обман раскрывается, её ценность рушится, а восхищение сменяется презрением. Эта реакция обнажает, что наше восприятие искусства никогда не бывает чисто эстетическим. Мы дорожим неповторимым прикосновением художника, исторической нитью, связующей предмет с творцом, и повествованием о гении, которое подделка фальсифицирует. По сути, мы откликаемся не только на то, что видим, но и на то, во что верим относительно происхождения. Некоторые философы утверждают, что это благоговение перед подлинностью иррационально — своего рода фетишизация происхождения в ущерб переживанию. Другие возражают, что контекст неотделим от смысла, что произведение искусства есть свидетельство конкретного человеческого поступка. Какая бы точка зрения ни возобладала, ремесло фальсификатора показывает, сколь многое в красоте кроется в истории, которую мы себе рассказываем.",
    "level": "C1"
  },
  {
    "id": 145,
    "title": "The Hidden Cost of Inequality",
    "content": "Economists once treated inequality largely as a matter of fairness, a moral concern distinct from the hard mechanics of growth. Recent scholarship, however, suggests that extreme disparities of wealth may actively undermine the economies that produce them. When resources concentrate narrowly, aggregate demand can stagnate, since the affluent spend a smaller share of their income than those with less. Social mobility falters as opportunity becomes hereditary, squandering the latent talent of those born without advantage. Perhaps most corrosively, entrenched inequality erodes the trust and shared purpose upon which cooperative societies depend, breeding resentment that can destabilise institutions. None of this implies that perfect equality is desirable or attainable; differential rewards can spur effort and innovation. The argument, rather, is that inequality is not a neutral by-product of prosperity but a variable that, past a certain point, feeds back upon the system, hollowing out the very dynamism it once seemed to reflect.",
    "translation": "Экономисты некогда рассматривали неравенство преимущественно как вопрос справедливости — нравственную заботу, отделённую от суровой механики роста. Однако недавние исследования наводят на мысль, что чрезмерные различия в богатстве могут активно подрывать те самые экономики, что их порождают. Когда ресурсы сосредоточиваются в узких руках, совокупный спрос может застаиваться, поскольку состоятельные тратят меньшую долю своего дохода, чем те, у кого его меньше. Социальная мобильность буксует, когда возможности становятся наследственными, растрачивая скрытый талант тех, кто рождён без преимуществ. Пожалуй, наиболее разрушительно то, что укоренившееся неравенство размывает доверие и общность цели, на которых держатся кооперативные общества, порождая недовольство, способное дестабилизировать институты. Ничто из этого не означает, что совершенное равенство желательно или достижимо; неодинаковые вознаграждения могут подстёгивать усердие и новаторство. Довод, скорее, в том, что неравенство — не нейтральный побочный продукт процветания, а переменная, которая, перейдя определённый порог, воздействует на систему обратной связью, выхолащивая ту самую динамичность, которую прежде, казалось, отражала.",
    "level": "C1"
  },
  {
    "id": 146,
    "title": "The Architecture of Memory",
    "content": "We tend to imagine memory as an archive, a faithful repository from which we retrieve past events intact. Cognitive science paints a far less comforting picture. Every act of recollection is, in fact, an act of reconstruction, in which the brain reassembles fragments and fills the gaps with plausible invention. Because these reconstructions are shaped by our present mood, beliefs, and subsequent experiences, memories subtly mutate each time we revisit them. A vivid, confidently held recollection may bear only a loose resemblance to what actually occurred. This malleability serves adaptive purposes, allowing us to extract general lessons rather than drown in useless detail, yet it carries unsettling implications. Eyewitness testimony, long treated as gold-standard evidence, proves alarmingly prone to distortion. Our sense of a continuous, reliable self rests upon a narrative we perpetually rewrite. To remember, it seems, is not to replay the past but to imaginatively recreate it in the image of the present.",
    "translation": "Мы склонны представлять память как архив — верное хранилище, из которого мы извлекаем прошлые события в неизменном виде. Когнитивная наука рисует куда менее утешительную картину. Всякий акт припоминания на самом деле есть акт реконструкции, в котором мозг вновь собирает фрагменты и заполняет пробелы правдоподобным вымыслом. Поскольку эти реконструкции формируются нашим нынешним настроением, убеждениями и последующим опытом, воспоминания незаметно видоизменяются всякий раз, когда мы к ним возвращаемся. Яркое, уверенно хранимое воспоминание может лишь отдалённо походить на то, что произошло в действительности. Эта пластичность служит приспособительным целям, позволяя нам извлекать общие уроки, а не тонуть в бесполезных подробностях, однако она несёт тревожные последствия. Показания очевидцев, долго считавшиеся эталонным доказательством, оказываются пугающе подвержены искажениям. Наше ощущение непрерывного, надёжного «я» покоится на повествовании, которое мы бесконечно переписываем. Помнить, как выясняется, значит не воспроизводить прошлое, а творчески воссоздавать его по образу настоящего.",
    "level": "C1"
  },
  {
    "id": 147,
    "title": "The Economics of Attention",
    "content": "In economies of abundance, the scarcest resource is often not goods or capital but human attention. When information proliferates without limit, the capacity to attend to it does not expand accordingly; it remains stubbornly finite. This asymmetry has given rise to industries whose fundamental business is the capture and resale of our focus. Every notification, autoplaying video, and infinitely scrolling feed is engineered to colonise a sliver of consciousness that might otherwise wander elsewhere. The transaction is rarely transparent. We imagine we are consuming free content, when in fact our attention is the commodity being harvested and auctioned to advertisers. The consequences extend beyond commerce into the texture of mental life itself. Sustained concentration, the prerequisite for deep thought and meaningful work, grows harder to summon in an environment relentlessly optimised to fragment it. Reclaiming attention, in such a landscape, becomes not merely a matter of productivity but of preserving a certain quality of mind.",
    "translation": "В экономиках изобилия самым дефицитным ресурсом часто оказываются не товары и не капитал, а человеческое внимание. Когда информация разрастается без предела, способность её воспринимать не расширяется соответственно; она остаётся упрямо конечной. Эта асимметрия породила целые отрасли, чей основной бизнес — захват и перепродажа нашего внимания. Каждое уведомление, автоматически запускающееся видео и бесконечно прокручиваемая лента сконструированы так, чтобы колонизировать частицу сознания, которая иначе могла бы блуждать где-то ещё. Эта сделка редко бывает прозрачной. Нам кажется, что мы потребляем бесплатный контент, тогда как на деле именно наше внимание — тот товар, что собирают и продают с аукциона рекламодателям. Последствия выходят за пределы коммерции и проникают в саму ткань умственной жизни. Устойчивую сосредоточенность, необходимую предпосылку глубокого мышления и осмысленного труда, всё труднее вызвать в среде, неустанно оптимизированной под её раздробление. Возвращение внимания в таком ландшафте становится не просто вопросом продуктивности, но сохранения определённого качества ума.",
    "level": "C1"
  },
  {
    "id": 148,
    "title": "The Paradox of Expertise",
    "content": "Expertise is universally esteemed, and rightly so, for it distils years of experience into swift, reliable judgement. Yet the very depth that makes an expert formidable can, under certain conditions, become a subtle liability. Having internalised the established frameworks of a discipline, the seasoned specialist perceives problems through habitual patterns that filter perception with extraordinary efficiency. This is ordinarily a virtue, but it can render the expert curiously blind to anomalies that fall outside familiar categories. Novices, unencumbered by such patterns, occasionally notice what the master overlooks precisely because they lack the schema that would explain it away. History is littered with paradigm shifts resisted most fiercely by the eminent authorities of the day, whose mastery had calcified into orthodoxy. The lesson is not that expertise should be distrusted, but that it must be leavened with a deliberate humility, an openness to the possibility that the deepest knowledge sometimes obscures as much as it reveals.",
    "translation": "Экспертное знание повсеместно почитается, и справедливо, ибо оно перегоняет годы опыта в быстрое, надёжное суждение. Однако та самая глубина, что делает эксперта грозным, при определённых условиях может обернуться незаметной уязвимостью. Усвоив устоявшиеся схемы своей дисциплины, опытный специалист воспринимает задачи сквозь привычные шаблоны, которые фильтруют восприятие с необычайной эффективностью. Обыкновенно это достоинство, но оно способно сделать эксперта на удивление слепым к аномалиям, выпадающим из знакомых категорий. Новички, не обременённые такими шаблонами, порой замечают то, что упускает мастер, именно потому, что у них нет схемы, которая объяснила бы это как несущественное. История усеяна сменами парадигм, которым яростнее всего сопротивлялись выдающиеся авторитеты своего времени, чьё мастерство окостенело в догму. Урок не в том, что экспертизе не следует доверять, а в том, что её нужно сдабривать намеренным смирением — открытостью к возможности, что глубочайшее знание иногда затемняет столько же, сколько раскрывает.",
    "level": "C1"
  },
  {
    "id": 149,
    "title": "The Ethics of Genetic Medicine",
    "content": "The advent of precise gene-editing technologies has thrust medicine into terrain where its traditional ethical compass strains to orient itself. To correct a mutation that condemns a child to lifelong suffering seems an unambiguous good, an extension of medicine's ancient mandate to heal. Yet the same tools that repair disease could, in principle, be turned toward enhancement, the deliberate augmentation of traits deemed desirable rather than the remedy of pathology. The line between therapy and improvement, once assumed to be clear, dissolves under scrutiny; who is to say where the alleviation of disadvantage ends and the pursuit of advantage begins? Compounding the difficulty, edits to reproductive cells would ripple down the generations, imposing irreversible choices upon descendants who cannot consent. Such prospects demand more than technical mastery; they call for a collective deliberation about what constitutes a life worth living and who bears the authority to define it. Science has outpaced the wisdom required to wield it.",
    "translation": "Появление точных технологий редактирования генов ввергло медицину в область, где её традиционный этический компас с трудом находит ориентиры. Исправить мутацию, обрекающую ребёнка на пожизненные страдания, кажется безусловным благом, продолжением древнего призвания медицины исцелять. Однако те же инструменты, что устраняют болезнь, могли бы в принципе быть обращены на усовершенствование — намеренное усиление признаков, считающихся желательными, а не на устранение патологии. Граница между терапией и улучшением, некогда мнившаяся ясной, растворяется при внимательном рассмотрении; кто скажет, где заканчивается смягчение недостатка и начинается погоня за преимуществом? Трудность усугубляется тем, что изменения в репродуктивных клетках отозвались бы во всех последующих поколениях, навязывая необратимый выбор потомкам, которые не могут дать согласия. Такие перспективы требуют большего, чем техническое мастерство; они взывают к коллективному осмыслению того, что составляет жизнь, достойную того, чтобы её прожить, и кто вправе это определять. Наука опередила мудрость, необходимую, чтобы ею владеть.",
    "level": "C1"
  },
  {
    "id": 150,
    "title": "The Tyranny of Metrics",
    "content": "There is a seductive appeal to measurement, a promise that by quantifying performance we render it transparent, comparable, and improvable. This conviction now pervades institutions from hospitals to universities, where funding, prestige, and survival increasingly hinge upon numerical indicators. But the faith invested in metrics conceals a treacherous flaw. Whenever a measure becomes a target, those subject to it learn to optimise the number rather than the underlying quality it was meant to represent. Surgeons may shun difficult cases that would depress their success rates; schools may drill students for tests at the expense of genuine understanding. The metric, initially a proxy for excellence, gradually supplants the very thing it was designed to track, hollowing out substance in favour of appearance. What is measurable is not always what matters, and what matters most, discretion, judgement, care, frequently resists quantification altogether. The remedy is not to abandon measurement but to temper it with the wisdom to know its limits.",
    "translation": "В измерении есть соблазнительная притягательность — обещание, что, оцифровывая деятельность, мы делаем её прозрачной, сопоставимой и поддающейся улучшению. Это убеждение ныне пронизывает учреждения от больниц до университетов, где финансирование, престиж и само выживание всё больше зависят от числовых показателей. Но вера, вложенная в метрики, скрывает коварный изъян. Как только мера становится целью, те, кого она касается, научаются оптимизировать число, а не то базовое качество, которое оно призвано отражать. Хирурги могут избегать трудных случаев, способных понизить их показатели успеха; школы могут натаскивать учеников на тесты в ущерб подлинному пониманию. Метрика, изначально бывшая заменителем совершенства, постепенно вытесняет то самое, что должна была отслеживать, выхолащивая суть в угоду видимости. Измеримое не всегда есть то, что важно, а самое важное — рассудительность, суждение, забота — зачастую вовсе не поддаётся количественной оценке. Средство не в том, чтобы отказаться от измерений, а в том, чтобы умерять их мудростью, позволяющей знать их пределы.",
    "level": "C1"
  }
]
