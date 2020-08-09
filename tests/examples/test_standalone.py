import pytest
from tartiflette_request_context_hooks.examples.standalone import\
    StandaloneRequestContextHooks
from tartiflette_request_context_hooks.exceptions import\
    RequestDataNotStoredException


class TestStandaloneRequestContextHooks:
    def test_standalone_example_init(self):
        service = StandaloneRequestContextHooks()

    @pytest.mark.asyncio
    async def test_standalone_example_call_data_not_set(self):
        service = StandaloneRequestContextHooks()
        service.request = {'fake': 'data'}
        with pytest.raises(RequestDataNotStoredException):
            await service()

    @pytest.mark.asyncio
    async def test_standalone_example_call_data_set(self):
        service = StandaloneRequestContextHooks()
        service.request = {'fake': 'data'}
        async with service:
            pass
        assert await service() == 'foo'


