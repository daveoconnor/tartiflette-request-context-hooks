from tartiflette_request_context_hooks import BaseRequestContextHooks


class ConcreteRequestContextHooksNoLabel(BaseRequestContextHooks):
    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


class ConcreteRequestContextHooks(BaseRequestContextHooks):
    label = 'CAExample'

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


class ConcreteWorkingRequestContextHooks(BaseRequestContextHooks):
    label = 'CAWorkingExample'

    async def __aenter__(self):
        await self.store_request_data('foo')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
