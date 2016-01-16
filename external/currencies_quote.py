import urllib3
from utils.utils import convert_str_to_dict


def get_current_quote():
    http = urllib3.PoolManager()
    url = "http://developers.agenciaideias.com.br/cotacoes/json"
    r = http.request('GET', url)
    status = r.status
    str_reponse = r.data.strip()
    dict_reponse = convert_str_to_dict(str_reponse)
    return dict_reponse, status
