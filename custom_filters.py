from aiogram.filters import BaseFilter
from aiogram.types import Message


class TagMaker(BaseFilter):

    async def __call__(self, message: Message):
        send_lst = message.text.split()
        goal_dict = {}
        if len(send_lst) > 1:
            goal_dict['tag'] = send_lst[1]
        if len(send_lst) > 2:
            goal_dict['count'] = send_lst[2]

        return goal_dict