from urllib.parse import parse_qs
from db.connect import DBManager
from handlers.post_list import post_list
from units.http import response


def delete_post(request):
    request = request.decode()  # 🔥 SHU QATORNI QO‘SH

    body = request.split("\r\n\r\n")[-1]
    post_id = body.split("=")[-1]

    with DBManager() as cur:
        cur.execute("DELETE FROM postings WHERE id = %s", (post_id,))

    return post_list()