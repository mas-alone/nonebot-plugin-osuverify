import re
import asyncio

import httpx
import nonebot
from nonebot import on_request
from nonebot.rule import Rule
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import GroupRequestEvent
from nonebot.adapters.onebot.v11.message import MessageSegment


__plugin_meta__ = PluginMetadata(
    name='osu!入群验证',
    type='application',
    description='osu!账户自动审批入群申请！',
    homepage='https://github.com/mas-alone/nonebot-plugin-sayoroll',
    usage="通过判断用户入群的答案，通过osu! api查询用户名验证入群",
    config={},
    extra={}
)

join_group = on_request(
    priority=1,
    block=True
)

async def check_comment(comment):
    k = nonebot.get_driver().config.dict().get('osu_amd')
    if k:
        verify_api = 'https://osu.ppy.sh/api/get_user?k={}&u={}'.format(k, comment)
        async with httpx.AsyncClient() as client:
            resp = await client.get(verify_api)
            resp = resp.json()
            if len(resp) == 0:
                return False
            else:
                return True
    else:
        return False



@join_group.handle()
async def _grh(bot: Bot, event: GroupRequestEvent):
    if event.sub_type == 'add':
        comment = event.comment.strip()
        comment = re.findall(re.compile('答案：(.*)'), comment)[0].strip()
        if comment != "":
            if await check_comment(comment):
                await event.approve(bot)
                await asyncio.sleep(2)
                await bot.set_group_card(group_id=event.group_id, user_id=event.user_id, card=comment)
                await join_group.finish(MessageSegment.at(event.user_id) + '欢迎加入本群，已将您的群名片改为您的osu!用户名:{}'.format(comment))
            else:
                await event.reject(bot, reason='id: {} 认证错误，请检查您输入的是否为正确的osu!用户名'.format(comment))
        else:
            await event.reject(bot, reason='id: {} 认证错误，请检查您输入的是否为正确的osu!用户名'.format(comment))
    else:
        pass
