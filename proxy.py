# coding=utf-8

#

#*experimen

#*Pemilik Script by Dullah

#*Recode SCH-T

import requests, os, shutil

from bs4 import BeautifulSoup as bs

from concurrent.futures import ThreadPoolExecutor

try: shutil.rmtree(

    'get_proxy/__pycache__'

  )

except: pass

proxy_list = []

valid_proxy = []

def prox():

  

    return from_file(

    )

def proxy_checker(prox):

  try:

    global valid_proxy

    if requests.get(

       'http://ip.ml.youngjoygame.com:30220/myip',

          verify=False,

          proxies=prox,

          timeout=7

        ).status_code == 200:

      valid_proxy.append(

        prox

      )

    print(

      end='\r[!] Found (%s) valid proxy'%(

        len(

          valid_proxy

        )

      ),

      flush=True

    )

  except: pass

def from_file():

  print(

    '\n'

  )

  list = input(

    '\033[92m[?] PROXYLIST => '

  )

  if os.path.exists(

    list

  ):

    for data in open(

      list,

      'r',

      encoding='utf-8'

    ).readlines(

      ):

      prox = data.strip(

      ).split(

        ':'

      )

      try:

        if prox[0] and prox[1]:

          proxy_list.append({

            'http': 'http://'+data.strip(),

            'https': 'https://'+data.strip(),

          })

      except: pass

    if len(

      proxy_list

    ) != 0:

      print(

        '[*] Total (%s) proxy' %(

          str(

            len(

              proxy_list

            )

          )

        )

      )

      print(

        '\033[92m[*] looking for proxy valid\033[0m'

      )

      with ThreadPoolExecutor(

        max_workers=200

      ) as thread:

        [

          thread.submit(

            proxy_checker,(

              prox

            )

          ) for prox in proxy_list

        ]

      if len(

        valid_proxy

      ) != 0:

        print(

          '\n'

        )

        return valid_proxy

      else: exit(

        '[!] Maaf tidak ada proxy yang valid silahkan coba lagi :('

      )

    else: exit(

      '[!] Maaf proxy tidak ada :('

    )

  else: exit(

    '\033[96m[!] File tidak ditemukan "{0}"'.format(

      list

    )

  )
