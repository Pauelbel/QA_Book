""" 
Скрипт для перебора урлов сайта
"""
from tornado import ioloop, httpclient, gen


URL          = 'https://example.com/'
PAYLOAD_FILE = 'payload/urls.txt'

dirs = open(PAYLOAD_FILE).read().splitlines()

urls_data = []
generetor = [urls_data.append(f'{URL}{dirs}') for dirs in dirs]

def main(urls):

    @gen.coroutine
    def fetch_and_handle():
        httpclient.AsyncHTTPClient.configure(None, defaults=dict(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'))
        http_client = httpclient.AsyncHTTPClient()
        waiter = gen.WaitIterator(*[http_client.fetch(url, raise_error=False, method='HEAD') for url in urls])
        results = []
        
        response_no_200 = 0 
        erorr_in_response = 0
        status_200_in_response = 0
        # Дождаться завершения работ
        while not waiter.done():
            
            try:
                response = yield waiter.next()
            except httpclient.HTTPError as e:
                response_no_200 += 1
                #print(f'Возвращенный HTTP-ответ, отличный от 200: {e} - {response.request.url}')
                continue
            except Exception as e:
                erorr_in_response +=1
                #print(f'Произошла непредвиденная ошибка при запросе: {e} - {response.request.url}')
                continue
            else:
                if response.code == 200:
                    print(f'[{response.code}] URL \'{response.request.url}\'')
                    results.append(response)
                else:
                    status_200_in_response += 1
            
            # UP = "\x1B[6A"
            # CLR = "\x1B[0K"
            # print("\n\n")
            # sys.stdout.write(f"{UP}Oтвет != 200: [{response_no_200}]{CLR}\nОшибка при запросе: [{erorr_in_response}]{CLR}\nОтвет == 200: [{status_200_in_response}]{CLR}\n")

            # sys.stdout.write('\r' + ' ' * 50 + '\r'),
            # sys.stdout.write(f"URL [{response.code}] --> {response.request.url}")
            # sys.stdout.flush()

        return results

    loop = ioloop.IOLoop.current()
    web_pages = loop.run_sync(fetch_and_handle)
    return web_pages



if __name__ == '__main__':
    responses = main(urls_data)