import requests
from bs4 import BeautifulSoup
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(category=InsecureRequestWarning)


urls = [

    'https://service.nalog.ru/inn.do/',
    'http://bankrot.fedresurs.ru/',                                    
    'http://egrul.nalog.ru/',
    'https://гибдд.рф/check/driver/',
    'http://results.audit.gov.ru/',
    'http://sudact.ru/',
    'http://www.cbr.ru/credit/main.asp',                                              
    'https://service.nalog.ru/bi.do',
    'http://services.fms.gov.ru/',                                        
    'http://zakupki.gov.ru/223/dishonest/public/supplier-search.html',
    'http://fedsfm.ru/documents/terrorists-catalog-portal-act',
    'http://www.stroi-baza.ru/forum/index.php?showforum=46',
    'http://судебныерешения.рф/',
    'http://www.centerdolgov.ru/',
    'http://ras.arbitr.ru/',
    'https://rosreestr.ru/wps/portal/cc_information_online',
    'http://www.voditeli.ru/',
    'http://www.gcourts.ru/',
    'http://www.e-disclosure.ru/',
    'http://www.fssprus.ru/',
    'http://rnp.fas.gov.ru/',
    'https://rosreestr.ru/wps/portal/p/cc_present/EGRN_1',
    'http://www.notary.ru/notary/bd.html',
    'http://allchop.ru/',
    'http://enotpoiskun.ru/tools/codedecode/',
    'http://polis.autoins.ru/',
    'http://www.vinformer.su/ident/vin.php?setLng=ru',
    'http://fssprus.ru/',
    'http://fssprus.ru/iss/ip',
    'http://fssprus.ru/iss/ip_search',
    'http://fssprus.ru/iss/suspect_info',
    'http://fssprus.ru/gosreestr_jurlic/',
    'http://opendata.fssprus.ru/',
    'http://sro.gosnadzor.ru/',
    'http://zakupki.gov.ru/epz/dishonestsupplier/quicksearch/search.html',
    'https://rosreestr.ru/wps/portal/online_request',
    'https://rosreestr.ru/wps/portal/p/cc_present/EGRN_1',
    'https://rosreestr.ru/wps/portal/p/cc_ib_portal_services/cc_ib_sro_reestrs',
    'https://rosreestr.ru/wps/portal/cc_ib_opendata',
    'https://pkk5.rosreestr.ru/',
]

for url in urls:

    response = requests.get(url, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        if 'Page Not Found' in soup.text:
            print(f"Страница {url} не найдена")
        else:
            pass
    else:
        print(f"Ссылка {url} не работает")
        print("Код ошибки:", response.status_code)