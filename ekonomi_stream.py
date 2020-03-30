import tweepy
import csv
import sys

# Fill the API Key
consumer_key = "RCSAqyk9HSlhb2gLgxR2W92iL"
consumer_secret = "68gX0fBZyOCmgEun0ia5tEfS3zyoStz2E12gpTbk1NlYZH9tJC"
access_token = "1242416699317477376-hrPhHXPhQoPDDhjscChNLsrFH2DNVv"
access_token_secret = "ha2VVykrZw5Jo4wlVPNotExJlIxT3A25kNG60G3g9Fvn9"

# Auth.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api


def cek_wil(tup):
    list_wilayah = ['aceh',
                    'simeulue',
                    'aceh singkil',
                    'aceh selatan',
                    'aceh tenggara',
                    'aceh timur',
                    'aceh tengah',
                    'aceh barat',
                    'aceh besar',
                    'pidie',
                    'bireuen',
                    'aceh utara',
                    'aceh barat daya',
                    'gayo lues',
                    'aceh tamiang',
                    'nagan raya',
                    'aceh jaya',
                    'bener meriah',
                    'pidie jaya',
                    'kota banda aceh',
                    'kota sabang',
                    'kota langsa',
                    'kota lhokseumawe',
                    'kota subulussalam',
                    'sumatera utara',
                    'nias',
                    'mandailing natal',
                    'tapanuli selatan',
                    'tapanuli tengah',
                    'tapanuli utara',
                    'toba samosir',
                    'labuhan batu',
                    'asahan',
                    'simalungun',
                    'dairi',
                    'karo',
                    'deli serdang',
                    'langkat',
                    'nias selatan',
                    'humbang hasundutan',
                    'pakpak bharat',
                    'samosir',
                    'serdang bedagai',
                    'batu bara',
                    'padang lawas utara',
                    'padang lawas',
                    'labuhan batu selatan',
                    'labuhan batu utara',
                    'nias utara',
                    'nias barat',
                    'kota sibolga',
                    'kota tanjung balai',
                    'kota pematang siantar',
                    'kota tebing tinggi',
                    'kota medan',
                    'kota binjai',
                    'kota padangsidimpuan',
                    'kota gunungsitoli',
                    'sumatera barat',
                    'kepulauan mentawai',
                    'pesisir selatan',
                    'solok',
                    'sijunjung',
                    'tanah datar',
                    'padang pariaman',
                    'agam',
                    'lima puluh kota',
                    'pasaman',
                    'solok selatan',
                    'dharmasraya',
                    'pasaman barat',
                    'kota padang',
                    'kota solok',
                    'kota sawah lunto',
                    'kota padang panjang',
                    'kota bukittinggi',
                    'kota payakumbuh',
                    'kota pariaman',
                    'riau',
                    'kuantan singingi',
                    'indragiri hulu',
                    'indragiri hilir',
                    'pelalawan',
                    'siak',
                    'kampar',
                    'rokan hulu',
                    'bengkalis',
                    'rokan hilir',
                    'kepulauan meranti',
                    'kota pekanbaru',
                    'kota dumai',
                    'jambi',
                    'kerinci',
                    'merangin',
                    'sarolangun',
                    'batang hari',
                    'muaro jambi',
                    'tanjung jabung timur',
                    'tanjung jabung barat',
                    'tebo',
                    'bungo',
                    'kota jambi',
                    'kota sungai penuh',
                    'sumatera selatan',
                    'ogan komering ulu',
                    'ogan komering ilir',
                    'muara enim',
                    'lahat',
                    'musi rawas',
                    'musi banyuasin',
                    'banyu asin',
                    'ogan komering ulu selatan',
                    'ogan komering ulu timur',
                    'ogan ilir',
                    'empat lawang',
                    'penukal abab lematang ilir',
                    'musi rawas utara',
                    'kota palembang',
                    'kota prabumulih',
                    'kota pagar alam',
                    'kota lubuklinggau',
                    'bengkulu',
                    'bengkulu selatan',
                    'rejang lebong',
                    'bengkulu utara',
                    'kaur',
                    'seluma',
                    'mukomuko',
                    'lebong',
                    'kepahiang',
                    'bengkulu tengah',
                    'kota bengkulu',
                    'lampung',
                    'lampung barat',
                    'tanggamus',
                    'lampung selatan',
                    'lampung timur',
                    'lampung tengah',
                    'lampung utara',
                    'way kanan',
                    'tulangbawang',
                    'pesawaran',
                    'pringsewu',
                    'mesuji',
                    'tulang bawang barat',
                    'pesisir barat',
                    'kota bandar lampung',
                    'kota metro',
                    'kep. bangka belitung',
                    'bangka',
                    'belitung',
                    'bangka barat',
                    'bangka tengah',
                    'bangka selatan',
                    'belitung timur',
                    'kota pangkal pinang',
                    'kepulauan riau',
                    'karimun',
                    'bintan',
                    'natuna',
                    'lingga',
                    'kepulauan anambas',
                    'kota batam',
                    'kota tanjung pinang',
                    'dki jakarta',
                    'kepulauan seribu',
                    'kota jakarta selatan',
                    'kota jakarta timur',
                    'kota jakarta pusat',
                    'kota jakarta barat',
                    'kota jakarta utara',
                    'jawa barat',
                    'bogor',
                    'sukabumi',
                    'cianjur',
                    'bandung',
                    'garut',
                    'tasikmalaya',
                    'ciamis',
                    'kuningan',
                    'cirebon',
                    'majalengka',
                    'sumedang',
                    'indramayu',
                    'subang',
                    'purwakarta',
                    'karawang',
                    'bekasi',
                    'bandung barat',
                    'pangandaran',
                    'kota bogor',
                    'kota sukabumi',
                    'kota bandung',
                    'kota cirebon',
                    'kota bekasi',
                    'kota depok',
                    'kota cimahi',
                    'kota tasikmalaya',
                    'kota banjar',
                    'jawa tengah',
                    'cilacap',
                    'banyumas',
                    'purbalingga',
                    'banjarnegara',
                    'kebumen',
                    'purworejo',
                    'wonosobo',
                    'magelang',
                    'boyolali',
                    'klaten',
                    'sukoharjo',
                    'wonogiri',
                    'karanganyar',
                    'sragen',
                    'grobogan',
                    'blora',
                    'rembang',
                    'pati',
                    'kudus',
                    'jepara',
                    'demak',
                    'semarang',
                    'temanggung',
                    'kendal',
                    'batang',
                    'pekalongan',
                    'pemalang',
                    'tegal',
                    'brebes',
                    'kota magelang',
                    'kota surakarta',
                    'kota salatiga',
                    'kota semarang',
                    'kota pekalongan',
                    'kota tegal',
                    'd i yogyakarta',
                    'kulon progo',
                    'bantul',
                    'gunung kidul',
                    'sleman',
                    'kota yogyakarta',
                    'jawa timur',
                    'pacitan',
                    'ponorogo',
                    'trenggalek',
                    'tulungagung',
                    'blitar',
                    'kediri',
                    'malang',
                    'lumajang',
                    'jember',
                    'banyuwangi',
                    'bondowoso',
                    'situbondo',
                    'probolinggo',
                    'pasuruan',
                    'sidoarjo',
                    'mojokerto',
                    'jombang',
                    'nganjuk',
                    'madiun',
                    'magetan',
                    'ngawi',
                    'bojonegoro',
                    'tuban',
                    'lamongan',
                    'gresik',
                    'bangkalan',
                    'sampang',
                    'pamekasan',
                    'sumenep',
                    'kota kediri',
                    'kota blitar',
                    'kota malang',
                    'kota probolinggo',
                    'kota pasuruan',
                    'kota mojokerto',
                    'kota madiun',
                    'kota surabaya',
                    'kota batu',
                    'banten',
                    'pandeglang',
                    'lebak',
                    'tangerang',
                    'serang',
                    'kota tangerang',
                    'kota cilegon',
                    'kota serang',
                    'kota tangerang selatan',
                    'bali',
                    'jembrana',
                    'tabanan',
                    'badung',
                    'gianyar',
                    'klungkung',
                    'bangli',
                    'karang asem',
                    'buleleng',
                    'kota denpasar',
                    'nusa tenggara barat',
                    'lombok barat',
                    'lombok tengah',
                    'lombok timur',
                    'sumbawa',
                    'dompu',
                    'bima',
                    'sumbawa barat',
                    'lombok utara',
                    'kota mataram',
                    'kota bima',
                    'nusa tenggara timur',
                    'sumba barat',
                    'sumba timur',
                    'kupang',
                    'timor tengah selatan',
                    'timor tengah utara',
                    'belu',
                    'alor',
                    'lembata',
                    'flores timur',
                    'sikka',
                    'ende',
                    'ngada',
                    'manggarai',
                    'rote ndao',
                    'manggarai barat',
                    'sumba tengah',
                    'sumba barat daya',
                    'nagekeo',
                    'manggarai timur',
                    'sabu raijua',
                    'malaka',
                    'kota kupang',
                    'kalimantan barat',
                    'sambas',
                    'bengkayang',
                    'landak',
                    'pontianak',
                    'sanggau',
                    'ketapang',
                    'sintang',
                    'kapuas hulu',
                    'sekadau',
                    'melawi',
                    'kayong utara',
                    'kubu raya',
                    'kota pontianak',
                    'kota singkawang',
                    'kalimantan tengah',
                    'kotawaringin barat',
                    'kotawaringin timur',
                    'kapuas',
                    'barito selatan',
                    'barito utara',
                    'sukamara',
                    'lamandau',
                    'seruyan',
                    'katingan',
                    'pulang pisau',
                    'gunung mas',
                    'barito timur',
                    'murung raya',
                    'kota palangka raya',
                    'kalimantan selatan',
                    'tanah laut',
                    'kota baru',
                    'banjar',
                    'barito kuala',
                    'tapin',
                    'hulu sungai selatan',
                    'hulu sungai tengah',
                    'hulu sungai utara',
                    'tabalong',
                    'tanah bumbu',
                    'balangan',
                    'kota banjarmasin',
                    'kota banjar baru',
                    'kalimantan timur',
                    'paser',
                    'kutai barat',
                    'kutai kartanegara',
                    'kutai timur',
                    'berau',
                    'penajam paser utara',
                    'mahakam hulu',
                    'kota balikpapan',
                    'kota samarinda',
                    'kota bontang',
                    'kalimantan utara',
                    'malinau',
                    'bulungan',
                    'tana tidung',
                    'nunukan',
                    'kota tarakan',
                    'sulawesi utara',
                    'bolaang mongondow',
                    'minahasa',
                    'kepulauan sangihe',
                    'kepulauan talaud',
                    'minahasa selatan',
                    'minahasa utara',
                    'bolaang mongondow utara',
                    'siau tagulandang biaro',
                    'minahasa tenggara',
                    'bolaang mongondow selatan',
                    'bolaang mongondow timur',
                    'kota manado',
                    'kota bitung',
                    'kota tomohon',
                    'kota kotamobagu',
                    'sulawesi tengah',
                    'banggai kepulauan',
                    'banggai',
                    'morowali',
                    'poso',
                    'donggala',
                    'toli-toli',
                    'buol',
                    'parigi moutong',
                    'tojo una-una',
                    'sigi',
                    'banggai laut',
                    'morowali utara',
                    'kota palu',
                    'sulawesi selatan',
                    'kepulauan selayar',
                    'bulukumba',
                    'bantaeng',
                    'jeneponto',
                    'takalar',
                    'gowa',
                    'sinjai',
                    'maros',
                    'pangkajene dan kepulauan',
                    'barru',
                    'bone',
                    'soppeng',
                    'wajo',
                    'sidenreng rappang',
                    'pinrang',
                    'enrekang',
                    'luwu',
                    'tana toraja',
                    'luwu utara',
                    'luwu timur',
                    'toraja utara',
                    'kota makassar',
                    'kota parepare',
                    'kota palopo',
                    'sulawesi tenggara',
                    'buton',
                    'muna',
                    'konawe',
                    'kolaka',
                    'konawe selatan',
                    'bombana',
                    'wakatobi',
                    'kolaka utara',
                    'buton utara',
                    'konawe utara',
                    'kolaka timur',
                    'konawe kepulauan',
                    'muna barat',
                    'buton tengah',
                    'buton selatan',
                    'kota kendari',
                    'kota baubau',
                    'gorontalo',
                    'boalemo',
                    'gorontalo',
                    'pohuwato',
                    'bone bolango',
                    'gorontalo utara',
                    'kota gorontalo',
                    'sulawesi barat',
                    'majene',
                    'polewali mandar',
                    'mamasa',
                    'mamuju',
                    'mamuju utara',
                    'mamuju tengah',
                    'maluku',
                    'maluku tenggara barat',
                    'maluku tenggara',
                    'maluku tengah',
                    'buru',
                    'kepulauan aru',
                    'seram bagian barat',
                    'seram bagian timur',
                    'maluku barat daya',
                    'buru selatan',
                    'kota ambon',
                    'kota tual',
                    'maluku utara',
                    'halmahera barat',
                    'halmahera tengah',
                    'kepulauan sula',
                    'halmahera selatan',
                    'halmahera utara',
                    'halmahera timur',
                    'pulau morotai',
                    'pulau taliabu',
                    'kota ternate',
                    'kota tidore kepulauan',
                    'papua barat',
                    'fakfak',
                    'kaimana',
                    'teluk wondama',
                    'teluk bintuni',
                    'manokwari',
                    'sorong selatan',
                    'sorong',
                    'raja ampat',
                    'tambrauw',
                    'maybrat',
                    'manokwari selatan',
                    'pegunungan arfak',
                    'kota sorong',
                    'papua',
                    'merauke',
                    'jayawijaya',
                    'jayapura',
                    'nabire',
                    'kepulauan yapen',
                    'biak numfor',
                    'paniai',
                    'puncak jaya',
                    'mimika',
                    'boven digoel',
                    'mappi',
                    'asmat',
                    'yahukimo',
                    'pegunungan bintang',
                    'tolikara',
                    'sarmi',
                    'keerom',
                    'waropen',
                    'supiori',
                    'mamberamo raya',
                    'nduga *',
                    'lanny jaya',
                    'mamberamo tengah',
                    'yalimo',
                    'puncak',
                    'dogiyai',
                    'intan jaya',
                    'deiyai',
                    'kota jayapura']
    tf = tup.lower() in ''.join(list_wilayah)
    return tf


# ini file untuk nyimpen data stream nya. kalo bisa langsung di drive biar gak ilang
filepath = "ekonomi.csv"


class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        with open(filepath, 'a') as f:
            if status.user.location:

                if (len(status.user.location) > 3) & cek_wil(status.user.location):
                    c_code = ""
                    try:
                        status.place.country_code = str(status.place.country_code)
                        writer = csv.writer(f)
                        writer.writerow([status.created_at, status.user.description, status.user.statuses_count,
                                         status.user.screen_name, status.in_reply_to_screen_name, status.user.verified,
                                         status.text, str(status.entities['hashtags']), status.user.location,
                                         status.user.friends_count, status.user.followers_count, status.retweet_count,
                                         str(status.coordinates), status.place.country_code])
                    except:
                        c_code = 'NULL'
                        writer = csv.writer(f)
                        writer.writerow([status.created_at, status.user.description, status.user.statuses_count,
                                         status.user.screen_name, status.in_reply_to_screen_name, status.user.verified,
                                         status.text, str(status.entities['hashtags']), status.user.location,
                                         status.user.friends_count, status.user.followers_count, status.retweet_count,
                                         str(status.coordinates), c_code])
                        # wai

            else:
                if status.place:
                    if status.place.country_code:
                        if cek_wil(status.place.country_code):
                            writer = csv.writer(f)
                            writer.writerow([status.created_at, status.user.description, status.user.statuses_count,
                                             status.user.screen_name, status.in_reply_to_screen_name,
                                             status.user.verified,
                                             status.text, str(status.entities['hashtags']), status.user.location,
                                             status.user.friends_count, status.user.followers_count,
                                             status.retweet_count, str(status.coordinates), status.place.country_code])

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True  # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')

        return True  # Don't kill the stream


# ini keywordnya
keyword_list = ['ekonomi, inflasi, keuangan,harga, saham']
streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
streamingAPI.filter(track=keyword_list)