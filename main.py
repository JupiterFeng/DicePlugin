from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import random


# 注册插件
@register(name="Dice", description="骰子模拟器", version="0.2", author="jianrenjun")
class MyPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg.startswith(".d"):
            import re
            match = re.match(r"\.d(\d+)(?:r(\d+))?", msg)
            if match:
                sides = int(match.group(1))
                rolls = int(match.group(2)) if match.group(2) else 1
                results = [str(random.randint(1, sides)) for _ in range(rolls)]
                reply = ", ".join(results)
                # # 输出调试信息
                # self.ap.logger.debug(f"Rolling {rolls}d{sides} for {ctx.event.sender_id}: {reply}")

                # 回复消息
                ctx.add_return("reply", [f"{reply}"])

                # 阻止该事件默认行为（向接口获取回复）
                ctx.prevent_default()

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 GroupNormalMessageReceived 的对象
        if msg.startswith(".d"):
            import re
            match = re.match(r"\.d(\d+)(?:r(\d+))?", msg)
            if match:
                sides = int(match.group(1))
                rolls = int(match.group(2)) if match.group(2) else 1
                results = [str(random.randint(1, sides)) for _ in range(rolls)]
                reply = ", ".join(results)
                # # 输出调试信息
                # self.ap.logger.debug(f"Rolling {rolls}d{sides} for {ctx.event.sender_id}: {reply}")

                # 回复消息
                ctx.add_return("reply", [f"{reply}"])

                # 阻止该事件默认行为（向接口获取回复）
                ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
