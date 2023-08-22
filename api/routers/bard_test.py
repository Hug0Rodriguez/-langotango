from bardapi import Bard

token = 'aAjFqLgNexhO3Bs-1S8dKNoDG3wU3JDwXM3GI0ES7k6uhdMp_K4XOfWsURvbnei7tTpXTA.'
bard = Bard(token=token)
bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
